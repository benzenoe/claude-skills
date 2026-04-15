# Quick Start Guide

## Creating a New Document

### Step 1: Choose Document Type

**For Pitch Decks:**
```
"Create a pitch for [ClientName] about [ServiceOffering]"
```

**For Pricing Quotes/Proposals:**
```
"Generate a pricing proposal for [ProjectName] at [ClientCompany]"
```

**For Implementation Workbooks:**
```
"Create a workbook for [TrainingTopic] mastermind session"
```

### Step 2: Core Components (ALWAYS Include)

Every document MUST have these 3 elements:

1. **Light/Dark Mode Toggle** (top-right corner)
2. **PDF Download Button** (bottom-right corner)
3. **PDF Preview Modal** (opens when download button clicked)

### Step 3: Copy Exact Code

**Reference the `components-library.md` file** and copy:

- CSS Variables (theming system)
- Theme toggle HTML + CSS + JavaScript
- PDF button HTML + CSS
- PDF modal HTML + CSS + JavaScript
- Any specific components needed (stat cards, checkboxes, etc.)

### Step 4: Create the File

**File location:**
- Pitches: `/Users/eytan/claude-code/bogen-ai/public/pitches/[client-name]-[topic].html`
- Quotes: `/Users/eytan/claude-code/bogen-ai/public/quotes/[client-name]-proposal.html`
- Workbooks: `/Users/eytan/claude-code/bogen-ai/public/masterminds/[topic]-workbook.html`

### Step 5: Generate PDF

1. Open the HTML file in browser
2. Press **Cmd+P** (Mac) or **Ctrl+P** (Windows)
3. Select "Save as PDF" as destination
4. Save in the SAME directory as HTML file
5. Name it exactly the same (e.g., `topic-workbook.pdf`)

### Step 6: Deploy

```bash
cd /Users/eytan/claude-code/bogen-ai
git add public/[directory]/[filename].html
git add public/[directory]/[filename].pdf
git commit -m "Add [type]: [title]"
git push

# Trigger Vercel deployment
date >> .vercel-deploy-trigger
git add .vercel-deploy-trigger
git commit -m "Trigger deployment"
git push
```

## Example: Create a Workbook

### User Request:
```
"Create a workbook for AI Automation Training"
```

### What Claude Should Do:

1. **Read the component library:**
```
Read: /Users/eytan/.claude/skills/pitches-quotes-workbooks/components-library.md
```

2. **Copy exact components:**
   - CSS variables (light/dark theme)
   - Theme toggle (HTML + CSS + JS)
   - PDF button (HTML + CSS)
   - PDF modal (HTML + CSS + JS)
   - Workbook components (cover, checkboxes, write lines, day cards)

3. **Create the file:**
```
Write: /Users/eytan/claude-code/bogen-ai/public/masterminds/ai-automation-workbook.html
```

4. **Include these sections:**
   - Cover page (with hero image)
   - Table of contents
   - Implementation plan (day-by-day checkboxes)
   - Exercises (write areas, worksheets)
   - Commitment section (signature)

5. **Update all placeholders:**
   - `[unique-key]-theme` → `ai-automation-theme`
   - `[filename].pdf` → `ai-automation-workbook.pdf`
   - Title, dates, Zoom links, etc.

6. **Tell user to generate PDF:**
```
"Open the file and use Cmd+P to save as PDF. Then we'll deploy both files."
```

## Example: Create a Pitch

### User Request:
```
"Create a pitch for Cloud Value Lab partnership proposal"
```

### What Claude Should Do:

1. **Read components library** (same as above)

2. **Copy pitch-specific components:**
   - Hero section with gradient
   - Stat grid for metrics
   - Pricing cards
   - Timeline/milestones table
   - CTA section with email button

3. **Create file:**
```
Write: /Users/eytan/claude-code/bogen-ai/public/pitches/cloud-value-lab-pitch.html
```

4. **Customize content** while keeping exact CSS/JS

5. **Guide PDF generation and deployment**

## Checklist Before Deployment

- [ ] Light/Dark mode toggle works
- [ ] PDF download button is visible (bottom-right)
- [ ] Clicking PDF button opens modal preview
- [ ] Modal Close button works
- [ ] Modal Download button works
- [ ] Escape key closes modal
- [ ] Background click closes modal
- [ ] Print-to-PDF looks correct (Cmd+P test)
- [ ] Mobile responsive design works
- [ ] All links work
- [ ] localStorage persists theme choice

## Common Mistakes to Avoid

❌ **Don't modify** the CSS values from components-library.md
❌ **Don't change** the JavaScript logic for theme/modal
❌ **Don't skip** the PDF modal implementation
❌ **Don't forget** to update the localStorage key (make it unique)
❌ **Don't forget** to update PDF filename in 3 places (iframe src, download link, confirm download)

✅ **Do copy** components exactly as written
✅ **Do test** all features before deploying
✅ **Do generate** the PDF file using browser print
✅ **Do deploy** both HTML and PDF together

## Testing Locally

1. Open HTML file in browser
2. Test theme toggle (should persist on refresh)
3. Click PDF download button
4. Verify modal opens with PDF preview
5. Test all close methods (X button, Escape, background click)
6. Test download button in modal
7. Print to PDF (Cmd+P) and verify layout

## File Naming Convention

**HTML Files:**
- `client-name-service.html` (pitches)
- `client-name-proposal.html` (quotes)
- `topic-workbook.html` (workbooks)

**PDF Files:**
- Same name as HTML but with `.pdf` extension

**localStorage Keys:**
- `[document-name]-theme` (unique per document)

## Brand Colors Reference

**Edmund Bogen (bogen.ai):**
- Primary: `#00a8e1` (cyan)
- Navy: `#1a3e5c`
- Gold: `#ffd93d` (accents)

**Eytan Benzeno (eytan.com):**
- Primary: `#2B6166` (teal)
- Navy: `#0d1620`
- Blue: `#00a8e1`

Use appropriate brand colors in the CSS variables.
