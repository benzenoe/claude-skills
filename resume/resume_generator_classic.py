#!/usr/bin/env python3
"""
Classic Resume Generator — Eytan Benzeno
Traditional multi-page layout with profile photo header, dark blue/orange-red accents.
Reads content from content_classic.json in the same directory.

Usage:
  python3 resume_generator_classic.py                       # generates EN/FR/PT to website
  python3 resume_generator_classic.py --lang en             # single language
  python3 resume_generator_classic.py --prefix "Google-"    # custom prefix for job apps
  python3 resume_generator_classic.py --outdir /tmp         # custom output directory
"""

import json, argparse, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, KeepTogether
)
from reportlab.platypus.flowables import Image as RLImage
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PIL import Image as PILImage, ImageDraw
import io

SKILL_DIR    = os.path.dirname(os.path.abspath(__file__))
CONTENT_FILE = os.path.join(SKILL_DIR, "content_classic.json")
WEBSITE_DIR  = "/Users/eytan/claude-code/Eytan.com/eytan.com Website/"
PROFILE_IMG  = WEBSITE_DIR + "images/profile.jpg"
EB_LOGO_IMG  = WEBSITE_DIR + "images/eb-logo1.png"

PAGE_W, PAGE_H = A4
L_MARGIN = R_MARGIN = 18 * mm
T_MARGIN = B_MARGIN = 15 * mm
BODY_W = PAGE_W - L_MARGIN - R_MARGIN

DARK_BLUE  = colors.HexColor('#1F3864')
ORANGE_RED = colors.HexColor('#C0392B')
BODY_TEXT  = colors.HexColor('#222222')
GRAY       = colors.HexColor('#555555')
LIGHT_GRAY = colors.HexColor('#DDDDDD')

def style(name, **kw):
    base = dict(fontName='Helvetica', fontSize=10, leading=14,
                textColor=BODY_TEXT, spaceAfter=0, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_SECTION   = style('section',  fontName='Helvetica-Bold', fontSize=13, textColor=DARK_BLUE, spaceBefore=10, spaceAfter=3)
S_JOB_TITLE = style('jobtitle', fontName='Helvetica-Bold', fontSize=10, textColor=ORANGE_RED, spaceBefore=8, spaceAfter=1)
S_COMPANY   = style('company',  fontName='Helvetica',      fontSize=10, textColor=DARK_BLUE, spaceAfter=3)
S_BODY      = style('body',     fontSize=10, leading=14, spaceAfter=2)
S_BULLET    = style('bullet',   fontSize=10, leading=14, leftIndent=12, firstLineIndent=-8, spaceAfter=2)
S_FOOTER    = style('footer',   fontSize=8,  textColor=GRAY, alignment=TA_CENTER)
S_NAME      = style('name',     fontName='Helvetica-Bold', fontSize=22, textColor=DARK_BLUE)
S_TAGLINE   = style('tagline',  fontName='Helvetica-Bold', fontSize=10, textColor=BODY_TEXT)
S_CONTACT   = style('contact',  fontSize=10, leading=15)

def bullet(text):
    return Paragraph(f"• &nbsp; {text}", S_BULLET)

def section_hr():
    return HRFlowable(width="100%", thickness=0.5, color=LIGHT_GRAY, spaceAfter=4, spaceBefore=2)

def make_circular_profile(path, size=45*mm):
    img = PILImage.open(path).convert("RGBA")
    w, h = img.size; side = min(w, h)
    left = (w - side) // 2
    top = max(0, int(h * 0.03)); top = min(top, h - side)
    img = img.crop((left, top, left+side, top+side))
    mask = PILImage.new("L", (side, side), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, side, side), fill=255)
    result = PILImage.new("RGBA", (side, side), (255, 255, 255, 0))
    result.paste(img, mask=mask)
    buf = io.BytesIO(); result.save(buf, format="PNG"); buf.seek(0)
    return RLImage(buf, width=size, height=size)

def footer_table():
    logo = RLImage(EB_LOGO_IMG, width=18*mm, height=18*mm)
    contact_text = "Eytan Benzeno  |  eytan@benzeno.com  |  +351 93 999 5889 pt  |  +1 786 727 0696 us"
    contact = Paragraph(contact_text, S_FOOTER)
    t = Table([[logo, contact]], colWidths=[22*mm, BODY_W - 22*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('ALIGN',  (1,0),(1,0),  'CENTER'),
        ('LINEABOVE', (0,0),(-1,0), 0.5, LIGHT_GRAY),
        ('TOPPADDING',    (0,0),(-1,-1), 4),
        ('BOTTOMPADDING', (0,0),(-1,-1), 0),
    ]))
    return t

def header_table(d):
    profile = make_circular_profile(PROFILE_IMG)
    logo = RLImage(EB_LOGO_IMG, width=16*mm, height=16*mm)
    name_logo = Table(
        [[Paragraph(d['name'], S_NAME), logo]],
        colWidths=[None, 18*mm]
    )
    name_logo.setStyle(TableStyle([
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('ALIGN',  (1,0),(1,0),  'RIGHT'),
    ]))
    contact_lines = [
        name_logo, Spacer(1, 2*mm),
        Paragraph(f"<b>Email:</b>  eytan@benzeno.com", S_CONTACT),
        Paragraph(f"<b>Phone:</b>  +351 93 999 5889 ({d['portugal']})   |   +1 (786) 727 0696 ({d['usa']})", S_CONTACT),
        Paragraph(f"<b>{d['locations_label']}</b>  {d['locations']}", S_CONTACT),
        Spacer(1, 3*mm),
        Paragraph(d['tagline'], S_TAGLINE),
        Paragraph(d['license1'], S_CONTACT),
        Paragraph(d['license2'], S_CONTACT),
    ]
    t = Table([[profile, contact_lines]], colWidths=[52*mm, BODY_W - 52*mm])
    t.setStyle(TableStyle([
        ('VALIGN',       (0,0),(-1,-1), 'TOP'),
        ('LEFTPADDING',  (1,0),(1,0),   8),
        ('RIGHTPADDING', (0,0),(-1,-1), 0),
        ('TOPPADDING',   (0,0),(-1,-1), 0),
        ('BOTTOMPADDING',(0,0),(-1,-1), 4),
    ]))
    return t

def build_pdf(d, out_path):
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=L_MARGIN, rightMargin=R_MARGIN,
        topMargin=T_MARGIN, bottomMargin=B_MARGIN + 20*mm,
    )
    story = []
    story.append(header_table(d))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph(d['summary_heading'], S_SECTION))
    story.append(section_hr())
    story.append(Paragraph(d['summary'], S_BODY))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['competence_heading'], S_SECTION))
    story.append(section_hr())
    story.append(Paragraph(d['competence'], S_BODY))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['experience_heading'], S_SECTION))
    story.append(section_hr())
    for job in d['jobs']:
        block = [Paragraph(job['title'], S_JOB_TITLE),
                 Paragraph(job['company'], S_COMPANY)
                 ] + [bullet(b) for b in job['bullets']] + [Spacer(1, 2*mm)]
        story.append(KeepTogether(block))
    story.append(Paragraph(d['edu_heading'], S_SECTION))
    story.append(section_hr())
    story.append(Paragraph(f"<b>{d['edu_degree']}</b>  |  {d['edu_school']}", S_BODY))
    story.append(Paragraph(d['edu_details'], S_BODY))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['tech_heading'], S_SECTION))
    story.append(section_hr())
    story.append(Paragraph(d['tech_text'], S_BODY))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['lang_heading'], S_SECTION))
    story.append(section_hr())
    story.append(Paragraph(d['lang_fluent'], S_BODY))
    story.append(Paragraph(d['lang_learning'], S_BODY))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['goals_heading'], S_SECTION))
    story.append(section_hr())
    story.append(Paragraph(d['goals_text'], S_BODY))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['aff_heading'], S_SECTION))
    story.append(section_hr())
    for a in d['affiliations']:
        story.append(bullet(a))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(d['int_heading'], S_SECTION))
    story.append(section_hr())
    for p in d['interests']:
        story.append(Paragraph(p, S_BODY))
        story.append(Spacer(1, 2*mm))

    def add_footer(canvas, doc):
        canvas.saveState()
        ft = footer_table()
        ft.wrap(BODY_W, 30*mm)
        ft.drawOn(canvas, L_MARGIN, B_MARGIN)
        canvas.restoreState()

    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
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
