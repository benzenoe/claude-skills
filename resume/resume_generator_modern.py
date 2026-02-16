#!/usr/bin/env python3
"""
Modern Executive Resume Generator — Eytan Benzeno
Frame-based two-column layout · Canvas-drawn header & backgrounds
Reads content from content_modern.json in the same directory.

Usage:
  python3 resume_generator_modern.py                        # generates EN/FR/PT to website
  python3 resume_generator_modern.py --lang en              # single language
  python3 resume_generator_modern.py --prefix "Google-"     # custom prefix for job apps
  python3 resume_generator_modern.py --outdir /tmp          # custom output directory
"""

import json, argparse, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, FrameBreak,
    Paragraph, Spacer, HRFlowable,
    Table, TableStyle, KeepTogether, Flowable
)
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage, ImageDraw
import io

SKILL_DIR   = os.path.dirname(os.path.abspath(__file__))
CONTENT_FILE = os.path.join(SKILL_DIR, "content_modern.json")
WEBSITE_DIR  = "/Users/eytan/claude-code/Eytan.com/eytan.com Website/"
PROFILE_IMG  = WEBSITE_DIR + "images/profile.jpg"
EB_LOGO_IMG  = WEBSITE_DIR + "images/eb-logo1.png"
FOOTER_TXT   = ("eytan@benzeno.com   ·   +351 93 999 5889 (PT)   ·   "
                "+1 786 727 0696 (US)   ·   linkedin.com/in/benzeno")

# ─── Page constants ───────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
SIDEBAR_W  = 65 * mm
MAIN_W     = PAGE_W - SIDEBAR_W
INNER_PAD  = 5 * mm
HDR_H      = 32 * mm
FOOTER_H   = 9  * mm

# ─── Brand colours ────────────────────────────────────────────────────────────
C_NAVY     = colors.HexColor('#0B1C3F')
C_NAVY_CTB = colors.HexColor('#0D2250')
C_GOLD     = colors.HexColor('#C9993A')
C_GOLD_LT  = colors.HexColor('#F0D080')
C_WHITE    = colors.white
C_BODY     = colors.HexColor('#1E293B')
C_HILIGHT  = colors.HexColor('#EAF1FF')

# ─── Style factory ────────────────────────────────────────────────────────────
def S(name, **kw):
    d = dict(fontName='Helvetica', fontSize=8.5, leading=12.5,
             textColor=C_BODY, spaceAfter=0, spaceBefore=0, alignment=TA_LEFT)
    d.update(kw)
    return ParagraphStyle(name, **d)

SS_SEC  = S('ss_sec', fontName='Helvetica-Bold', fontSize=8,
            textColor=C_GOLD, leading=11, spaceBefore=6, spaceAfter=2)
SS_BODY = S('ss_body', fontSize=8, textColor=C_WHITE, leading=12)
SS_MUTED= S('ss_muted', fontSize=7.5, textColor=C_GOLD_LT, leading=11)
MS_SEC  = S('ms_sec',  fontName='Helvetica-Bold', fontSize=10,
            textColor=C_NAVY, leading=13, spaceBefore=7, spaceAfter=1)
MS_JOB  = S('ms_job',  fontName='Helvetica-Bold', fontSize=9,
            textColor=C_NAVY, leading=12, spaceBefore=5, spaceAfter=1)
MS_CO   = S('ms_co',   fontName='Helvetica-Oblique', fontSize=8,
            textColor=C_GOLD, leading=11, spaceAfter=1)
MS_BODY = S('ms_body', fontSize=8, textColor=C_BODY, leading=11.5, spaceAfter=1)
MS_BUL  = S('ms_bul',  fontSize=8, textColor=C_BODY, leading=11.5,
            leftIndent=8, firstLineIndent=-7, spaceAfter=1)
MS_TECH = S('ms_tech', fontSize=7.5, textColor=C_BODY, leading=11.5)

# ─── Custom Flowables ─────────────────────────────────────────────────────────
class SectionLine(Flowable):
    def __init__(self, width, color=C_GOLD):
        super().__init__(); self.w = width; self.c = color; self.height = 2
    def draw(self):
        self.canv.setStrokeColor(self.c); self.canv.setLineWidth(1.5)
        self.canv.line(0, 1, self.w * 0.22, 1)

class AchievementBox(Flowable):
    def __init__(self, text, width=36*mm):
        super().__init__(); self.text = text; self.w = width; self.height = 8*mm
    def draw(self):
        c = self.canv
        c.setFillColor(C_HILIGHT); c.setStrokeColor(C_GOLD); c.setLineWidth(0.7)
        c.roundRect(0, 0, self.w, self.height - 0.8*mm, 1.8*mm, fill=1, stroke=1)
        c.setFillColor(C_NAVY); c.setFont('Helvetica-Bold', 7.5)
        c.drawCentredString(self.w / 2, self.height * 0.3, self.text)

class DotRow(Flowable):
    def __init__(self, filled, total=5, dot_r=1.5*mm, gap=1.0*mm):
        super().__init__()
        self.filled = filled; self.total = total; self.r = dot_r; self.gap = gap
        self.width = total * (2 * dot_r + gap); self.height = 2 * dot_r + 0.5*mm
    def draw(self):
        c = self.canv; x = self.r
        for i in range(self.total):
            if i < self.filled:
                c.setFillColor(C_GOLD); c.setStrokeColor(C_GOLD)
            else:
                c.setFillColor(colors.transparent); c.setStrokeColor(C_GOLD_LT)
            c.setLineWidth(0.5); c.circle(x, self.r, self.r, fill=1, stroke=1)
            x += 2 * self.r + self.gap

# ─── Image helpers ────────────────────────────────────────────────────────────
def make_circular_photo(path, size_px=200):
    img = PILImage.open(path).convert("RGBA")
    w, h = img.size; side = min(w, h)
    left = (w - side) // 2
    top = max(0, int(h * 0.04)); top = min(top, h - side)
    img = img.crop((left, top, left+side, top+side)).resize((size_px, size_px), PILImage.LANCZOS)
    mask = PILImage.new("L", (size_px, size_px), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size_px, size_px), fill=255)
    out = PILImage.new("RGBA", (size_px, size_px), (0, 0, 0, 0))
    out.paste(img, mask=mask)
    buf = io.BytesIO(); out.save(buf, format="PNG"); buf.seek(0)
    return buf

# ─── Section helpers ──────────────────────────────────────────────────────────
def sb_section(title, items):
    return [Paragraph(title, SS_SEC),
            HRFlowable(width="100%", thickness=0.4, color=C_GOLD, spaceAfter=3)] + items

def ms_header(title, width):
    return [Paragraph(title, MS_SEC), SectionLine(width), Spacer(1, 1.5*mm)]

def job_block(job):
    items = [Paragraph(job['title'], MS_JOB), Paragraph(job['co'], MS_CO)]
    if job.get('achieve'):
        row_data = [AchievementBox(a) for a in job['achieve']]
        t = Table([row_data], hAlign='LEFT')
        t.setStyle(TableStyle([
            ('TOPPADDING',    (0,0),(-1,-1), 1), ('BOTTOMPADDING', (0,0),(-1,-1), 3),
            ('LEFTPADDING',   (0,0),(-1,-1), 0), ('RIGHTPADDING',  (0,0),(-1,-1), 4),
        ]))
        items.append(t)
    for b in job['bullets']:
        items.append(Paragraph(f"▸  {b}", MS_BUL))
    items.append(Spacer(1, 1*mm))
    return KeepTogether(items)

# ─── PDF Builder ──────────────────────────────────────────────────────────────
def build_pdf(d, out_path):
    photo_buf = make_circular_photo(PROFILE_IMG)
    logo_reader = ImageReader(EB_LOGO_IMG)

    def on_page(canv, doc):
        canv.saveState()
        canv.setFillColor(C_NAVY)
        canv.rect(0, PAGE_H - HDR_H, PAGE_W, HDR_H, fill=1, stroke=0)
        ctb_h = 8 * mm
        canv.setFillColor(C_NAVY_CTB)
        canv.rect(0, PAGE_H - HDR_H, PAGE_W, ctb_h, fill=1, stroke=0)
        canv.setFont('Helvetica', 7.5); canv.setFillColor(C_WHITE)
        canv.drawString(6*mm, PAGE_H - HDR_H + 1.8*mm, '   ·   '.join(d['contact']))
        tbar_y = PAGE_H - HDR_H + ctb_h + 2*mm
        canv.setFont('Helvetica-Bold', 9.5); canv.setFillColor(C_GOLD)
        canv.drawString(6*mm, tbar_y, d['title'])
        canv.setFont('Helvetica', 7.5); canv.setFillColor(C_GOLD_LT)
        lic_w = canv.stringWidth(d['license'], 'Helvetica', 7.5)
        canv.drawString(PAGE_W - lic_w - 5*mm, tbar_y, d['license'])
        canv.setFont('Helvetica-Bold', 21); canv.setFillColor(C_WHITE)
        canv.drawString(6*mm, tbar_y + 7*mm, d['name'])
        logo_sz = 11 * mm
        canv.drawImage(logo_reader, PAGE_W - logo_sz - 4*mm, PAGE_H - logo_sz - 2.5*mm,
                       width=logo_sz, height=logo_sz, mask='auto')
        canv.setFillColor(C_GOLD)
        canv.rect(0, PAGE_H - HDR_H - 1.2, PAGE_W, 1.2, fill=1, stroke=0)
        body_top = PAGE_H - HDR_H - 1.2; body_bot = FOOTER_H
        canv.setFillColor(C_NAVY)
        canv.rect(0, body_bot, SIDEBAR_W, body_top - body_bot, fill=1, stroke=0)
        canv.setStrokeColor(C_GOLD); canv.setLineWidth(1.2)
        canv.line(SIDEBAR_W, body_bot, SIDEBAR_W, body_top)
        canv.setFillColor(C_NAVY)
        canv.rect(0, 0, PAGE_W, FOOTER_H, fill=1, stroke=0)
        canv.setFillColor(C_GOLD)
        canv.rect(0, FOOTER_H, PAGE_W, 0.8, fill=1, stroke=0)
        canv.setFont('Helvetica', 7); canv.setFillColor(C_WHITE)
        canv.drawCentredString(PAGE_W / 2, 3*mm, FOOTER_TXT)
        canv.restoreState()

    body_h = PAGE_H - HDR_H - 1.2 - FOOTER_H
    sidebar_frame = Frame(0, FOOTER_H, SIDEBAR_W, body_h,
        leftPadding=INNER_PAD, rightPadding=INNER_PAD-1,
        topPadding=4*mm, bottomPadding=3*mm, id='sidebar', showBoundary=0)
    main_frame = Frame(SIDEBAR_W, FOOTER_H, MAIN_W, body_h,
        leftPadding=INNER_PAD+2*mm, rightPadding=INNER_PAD,
        topPadding=3*mm, bottomPadding=3*mm, id='main', showBoundary=0)
    template = PageTemplate(id='TwoCol', frames=[sidebar_frame, main_frame], onPage=on_page)
    doc = BaseDocTemplate(out_path, pagesize=A4, pageTemplates=[template],
                          leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)

    # Sidebar
    from reportlab.platypus.flowables import Image as RLImg
    photo_flow = RLImg(photo_buf, width=26*mm, height=26*mm)
    photo_tbl = Table([[photo_flow]], hAlign='CENTER')
    photo_tbl.setStyle(TableStyle([
        ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ]))
    sb = [photo_tbl, Spacer(1, 3*mm)]
    sb += sb_section(d['summary_h'], [Paragraph(d['summary'], SS_BODY)])
    sb.append(Spacer(1, 1*mm))
    skill_rows = []
    for s in d['skills']:
        skill_rows += [Paragraph(s['name'], SS_BODY),
                       DotRow(s['level'], total=5, dot_r=1.4*mm, gap=0.9*mm),
                       Spacer(1, 1.2*mm)]
    sb += sb_section(d['skills_h'], skill_rows)
    sb.append(Spacer(1, 1*mm))
    lang_rows = []; sb_inner_w = SIDEBAR_W - 2 * INNER_PAD
    for l in d['langs']:
        rt = Table([[Paragraph(l['name'], SS_BODY), Paragraph(l['note'], SS_MUTED)]],
                   colWidths=[sb_inner_w*0.52, sb_inner_w*0.48])
        rt.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
                                 ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
        lang_rows += [rt, DotRow(l['level'], total=5, dot_r=1.2*mm, gap=0.8*mm), Spacer(1, 1.5*mm)]
    sb += sb_section(d['lang_h'], lang_rows)
    sb.append(Spacer(1, 1*mm))
    sb += sb_section(d['edu_h'], [
        Paragraph(f"<b>{d['edu_degree']}</b>", SS_BODY),
        Paragraph(d['edu_school'], SS_MUTED),
        Paragraph(d['edu_note'], S('en2', fontSize=7.5, textColor=C_GOLD, leading=11)),
    ])
    sb.append(Spacer(1, 1*mm))
    sb += sb_section(d['aff_h'], [
        Paragraph(f"▸  {a}", S('af', fontSize=7.5, textColor=C_WHITE, leading=11.5,
                               leftIndent=7, firstLineIndent=-7))
        for a in d['affs']
    ])
    sb.append(Spacer(1, 1*mm))
    sb += sb_section(d['int_h'], [Paragraph(d['interests'], SS_MUTED)])

    # Main
    mn = []
    mn += ms_header(d['exp_h'], MAIN_W)
    for job in d['jobs']:
        mn.append(job_block(job))
    mn += ms_header(d['tech_h'], MAIN_W)
    mn.append(Paragraph(d['tech'], MS_TECH))
    mn.append(Spacer(1, 2*mm))
    mn += ms_header(d['goals_h'], MAIN_W)
    mn.append(Paragraph(d['goals'], MS_BODY))

    doc.build(sb + [FrameBreak()] + mn)
    print(f"✓  {out_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang',    default=None, choices=['en','fr','pt'],
                        help='Generate single language (default: all 3)')
    parser.add_argument('--prefix',  default='',   help='Output filename prefix, e.g. "Google-"')
    parser.add_argument('--outdir',  default=WEBSITE_DIR, help='Output directory')
    args = parser.parse_args()

    with open(CONTENT_FILE, encoding='utf-8') as f:
        CONTENT = json.load(f)

    langs = [args.lang] if args.lang else ['en', 'fr', 'pt']
    for lang in langs:
        d = CONTENT[lang]
        suffix = d.get('out_suffix', '')
        fname = f"{args.prefix}Eytan-Benzeno-Resume{suffix}.pdf"
        out_path = os.path.join(args.outdir, fname)
        build_pdf(d, out_path)

    print(f"\nDone! ({len(langs)} PDF{'s' if len(langs)>1 else ''} generated)")
