---
name: resume
description: Update, customize, or regenerate Eytan's resume PDFs. Edits content, auto-translates EN→FR/PT, supports modern and classic layouts, and customizes per job application.
---

# Resume PDF Manager — Eytan Benzeno

## Files at a Glance

| File | Purpose |
|------|---------|
| `~/.claude/skills/resume/content_modern.json` | Compact content for modern 1-page design (EN/FR/PT) |
| `~/.claude/skills/resume/content_classic.json` | Detailed content for classic multi-page design (EN/FR/PT) |
| `~/.claude/skills/resume/resume_generator_modern.py` | Modern two-column Frame generator |
| `~/.claude/skills/resume/resume_generator_classic.py` | Classic portrait-style generator |
| Website PDFs (default output) | `/Users/eytan/claude-code/Eytan.com/eytan.com Website/` |

---

## Two Layout Options

### Modern (default for eytan.com)
- **1-page** two-column design: dark navy sidebar + white main column
- Canvas-drawn header: name, EB logo, title bar, contact strip
- Sidebar: circular photo, About Me summary, skill dot bars, language proficiency dots, education, affiliations, interests
- Main column: experience with **achievement callout boxes** (e.g. $3M/summer, 400+ members), tech stack, goals
- Navy footer with gold accent line
- Colors: `#0B1C3F` navy · `#C9993A` gold · white
- Generator: `resume_generator_modern.py` · Content: `content_modern.json`

### Classic
- **Multi-page** traditional layout with wide margins
- Header: large circular profile photo (left) + name/contact/tagline (right)
- EB logo in header and footer
- Sections: Professional Summary, Core Competence, Experience, Education, Tech Stack, Languages, Goals, Affiliations, Interests
- Colors: `#1F3864` dark blue · `#C0392B` orange-red · light gray HR lines
- Generator: `resume_generator_classic.py` · Content: `content_classic.json`

---

## What You Can Ask

### "Update [section] to [new content]"
Edit content and regenerate. You **always update English first**, then auto-translate.

**Steps:**
1. Read the appropriate JSON file (`content_modern.json` and/or `content_classic.json`)
2. Apply the change to the `"en"` section
3. **Translate only the changed text** to French (fr) and Portuguese (pt) — use your own translation ability (you are fluent in EN/FR/PT)
4. Update the `"fr"` and `"pt"` sections in the same JSON file with the translations
5. Run the generator:
   ```bash
   python3 ~/.claude/skills/resume/resume_generator_modern.py
   # and/or
   python3 ~/.claude/skills/resume/resume_generator_classic.py
   ```
6. Ask: "Push to website?"

---

### "Customize for [Company] applying for [Role]"
Creates a **tailored version** without touching the master content files.

**Steps:**
1. Read `content_modern.json` (en section) — the modern layout works best for job applications
2. Tailor these sections for the specific company/role:
   - **Summary** — reframe around the role's key requirements
   - **Goals** — target the specific opportunity
   - **Job bullets** — emphasize most relevant experience (can reorder or rephrase)
   - **Achievement boxes** — keep the strongest numbers for this role
3. Translate the tailored EN content to FR and PT
4. Generate custom-named PDFs to `/tmp/`:
   ```bash
   python3 ~/.claude/skills/resume/resume_generator_modern.py \
     --prefix "CompanyName-" \
     --outdir /tmp
   # Outputs: /tmp/CompanyName-Eytan-Benzeno-Resume.pdf
   #          /tmp/CompanyName-Eytan-Benzeno-Resume-FR.pdf
   #          /tmp/CompanyName-Eytan-Benzeno-Resume-PT.pdf
   ```
5. **Do NOT overwrite the master JSON files or website PDFs** unless explicitly asked

---

### "Regenerate modern layout" / "Regenerate classic layout"
```bash
# Modern only:
python3 ~/.claude/skills/resume/resume_generator_modern.py

# Classic only:
python3 ~/.claude/skills/resume/resume_generator_classic.py

# Single language:
python3 ~/.claude/skills/resume/resume_generator_modern.py --lang en
```

---

### "Push to website"
```bash
cd "/Users/eytan/claude-code/Eytan.com/eytan.com Website"
git add Eytan-Benzeno-Resume.pdf Eytan-Benzeno-Resume-FR.pdf Eytan-Benzeno-Resume-PT.pdf
git commit -m "Update resume PDFs"
git push origin main
# GitHub Pages auto-deploys in ~2 minutes at https://eytan.com/resume.html
```

---

## Translation Rules

When translating changed English content to French / Portuguese:
- Keep: company names, product names, URLs, numbers, metrics ($3M, 400+, 1991)
- Translate naturally in professional résumé register (not word-for-word)
- **French key terms:** Présent (Present), Fondateur (Founder), Opérateur (Operator), Courtier (Broker), Gestionnaire (Manager), Compétences (Skills), Formations (Education)
- **Portuguese key terms:** Presente (Present), Fundador (Founder), Operador (Operator), Corretor (Broker), Gestor (Manager), Competências (Skills), Formação (Education)
- Section header keys are already translated in the JSON — only update `"fr"` and `"pt"` sections when a field was changed in `"en"`

---

## Content Schema Reference

### modern JSON structure (per language)
```json
{
  "en": {
    "name": "Eytan Benzeno",
    "title": "Technologist  ·  Operator  ·  Marketer",
    "license": "...",
    "contact": ["line 1", "line 2", "line 3"],
    "summary_h": "About Me",
    "summary": "...",
    "skills_h": "Core Skills",
    "skills": [{"name": "Operations & Strategy", "level": 5}],
    "lang_h": "Languages",
    "langs": [{"name": "English", "level": 5, "note": "Native"}],
    "edu_h": "Education",
    "edu_degree": "BBA – Banking & Finance",
    "edu_school": "Adelphi University · NY · 1991",
    "edu_note": "Dean's List",
    "aff_h": "Affiliations",
    "affs": ["REIGNation Community – Founder", "..."],
    "int_h": "Interests",
    "interests": "Finance · AI · ...",
    "exp_h": "Professional Experience",
    "jobs": [
      {
        "title": "Job Title",
        "co": "Company  ·  Location  ·  Dates",
        "achieve": ["Achievement 1", "Achievement 2"],
        "bullets": ["Bullet 1", "Bullet 2", "Bullet 3"]
      }
    ],
    "tech_h": "Tech Stack",
    "tech": "Tool1  ·  Tool2  ·  ...",
    "goals_h": "Professional Goals",
    "goals": "..."
  }
}
```

### classic JSON structure (per language)
```json
{
  "en": {
    "name": "...",
    "tagline": "...", "license1": "...", "license2": "...",
    "locations_label": "Locations:", "locations": "...",
    "summary_heading": "...", "summary": "...",
    "competence_heading": "...", "competence": "...",
    "experience_heading": "...",
    "jobs": [{"title": "...", "company": "...", "bullets": ["..."]}],
    "edu_heading": "...", "edu_degree": "...", "edu_school": "...", "edu_details": "...",
    "tech_heading": "...", "tech_text": "...",
    "lang_heading": "...", "lang_fluent": "...", "lang_learning": "...",
    "goals_heading": "...", "goals_text": "...",
    "aff_heading": "...", "affiliations": ["..."],
    "int_heading": "...", "interests": ["paragraph 1", "paragraph 2"]
  }
}
```

---

## Do Not Change

- Generator scripts (`*.py`) — only edit JSON content files
- Images: `images/profile.jpg` · `images/eb-logo1.png`
- Colors, fonts, layout structure — these are the brand identity
- The `"out_suffix"` field in each language (`""` for EN, `"-FR"` for FR, `"-PT"` for PT)

---

## Quick Command Summary

| What user says | What to do |
|----------------|-----------|
| "update my summary" | Edit `en.summary` in JSON → translate → regenerate |
| "add a new bullet to SoldHere" | Edit `en.jobs[0].bullets` → translate → regenerate |
| "customize for [Company]" | Tailored copy to `/tmp/`, do not touch master |
| "use modern layout" | Run `resume_generator_modern.py` |
| "use classic layout" | Run `resume_generator_classic.py` |
| "generate all" | Run both generators |
| "push to website" | `git add *.pdf && git commit && git push origin main` |
| "just English" | Add `--lang en` flag |
