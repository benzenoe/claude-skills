# Pitches, Quotes & Workbooks Skill

Professional document generator with light/dark modes and PDF preview capabilities.

## Skill Structure

```
pitches-quotes-workbooks/
├── skill.md                    # Main skill description
├── README.md                   # This file
├── QUICK-START.md             # Step-by-step guide
├── components-library.md       # Exact CSS/HTML/JS to copy
└── templates/
    └── pitch-template.html     # Basic template example
```

## What This Skill Does

Creates professional HTML documents with:

1. **Light/Dark Mode** - Toggle persists in localStorage
2. **PDF Download** - Floating button bottom-right
3. **PDF Preview Modal** - Embedded viewer before download
4. **Print-Optimized** - Perfect PDF generation via browser print
5. **Responsive Design** - Works on all devices

## When to Use This Skill

User requests:
- "Create a pitch for..."
- "Generate a proposal for..."
- "Make a workbook for..."
- "Design a quote for..."

## Quick Reference

### Required Components (Every Document)

1. **CSS Variables** for theming
2. **Theme Toggle** (top-right, fixed)
3. **PDF Button** (bottom-right, fixed)
4. **PDF Modal** (preview overlay)
5. **Print CSS** (@media print)
6. **JavaScript** (theme + modal logic)

### File Locations

- **Pitches**: `bogen-ai/public/pitches/`
- **Quotes**: `bogen-ai/public/quotes/`
- **Workbooks**: `bogen-ai/public/masterminds/`

### Reference Examples

1. **Workbook**: https://www.bogen.ai/masterminds/ai-phone-agent-workbook.html
2. **Pitch**: https://eytan.com/pitches/david-may.html
3. **Proposal**: https://eytan.com/pitches/ashth-retainer-proposal.html
4. **Strategy**: https://eytan.com/pitches/ashth-local-strategy.html
5. **GitHub Workbook**: https://edmundbogen.github.io/zillow-ai-workbook.html

## Workflow

1. **Create HTML** - Copy components from `components-library.md`
2. **Test Features** - Theme toggle, PDF button, modal
3. **Generate PDF** - Browser print (Cmd+P → Save as PDF)
4. **Deploy Both** - Commit HTML + PDF, push, trigger Vercel

## Component Library Highlights

### Theme System
- CSS variables for light/dark colors
- Toggle switch with animation
- localStorage persistence

### PDF System
- Download button (floating)
- Preview modal (full-screen overlay)
- iframe PDF viewer
- Close: X button, Escape key, background click

### Workbook Components
- Cover page
- Checkbox items
- Write lines/areas
- Stat cards
- Signature section
- Implementation plan (day cards)

### Pitch/Quote Components
- Hero section
- Pricing cards
- Timeline tables
- CTA buttons
- Stat grids

## Brand Guidelines

**Edmund Bogen:**
- Cyan `#00a8e1`
- Navy `#1a3e5c`
- Montserrat font

**Eytan Benzeno:**
- Teal `#2B6166`
- Navy `#0d1620`
- System fonts

## Important Rules

### ✅ DO:
- Copy components EXACTLY from `components-library.md`
- Test all features before deploying
- Generate PDF using browser print
- Deploy HTML + PDF together
- Use unique localStorage keys

### ❌ DON'T:
- Modify CSS values
- Change JavaScript logic
- Skip PDF modal implementation
- Forget to update PDF filename references
- Deploy without testing

## Testing Checklist

- [ ] Theme toggle works and persists
- [ ] PDF button visible and clickable
- [ ] Modal opens with PDF preview
- [ ] All close methods work
- [ ] Download button downloads PDF
- [ ] Print-to-PDF looks correct
- [ ] Mobile layout works
- [ ] All links functional

## Deployment Commands

```bash
# Add files
git add public/[directory]/[filename].html
git add public/[directory]/[filename].pdf

# Commit
git commit -m "Add [type]: [title]"
git push

# Trigger deployment
date >> .vercel-deploy-trigger
git add .vercel-deploy-trigger
git commit -m "Trigger deployment"
git push
```

## Support Files

- **skill.md** - Full documentation
- **QUICK-START.md** - Step-by-step tutorial
- **components-library.md** - Code reference (copy from here)
- **templates/** - Example files

## Key Features Detail

### Light/Dark Mode
- User preference saved in localStorage
- Smooth color transitions
- All components theme-aware
- Print always uses light theme

### PDF Preview
- Modal overlay (90vh height)
- Embedded iframe viewer
- Close, Download buttons
- Keyboard shortcuts (Escape)
- Background click to dismiss

### Print Optimization
- Letter size pages
- Proper margins
- Page breaks controlled
- Colors preserved
- Interactive elements hidden
- Footer pagination

## Usage Example

```
User: "Create a workbook for Real Estate AI Training"

Claude:
1. Read components-library.md
2. Copy exact theme toggle, PDF button, PDF modal
3. Copy workbook components (cover, checkboxes, etc.)
4. Create: public/masterminds/real-estate-ai-workbook.html
5. Replace placeholders with actual content
6. Test features
7. Guide user to generate PDF
8. Deploy both files
```

## Version History

- **v1.0** - Initial skill creation (2026-04-15)
  - Light/dark mode toggle
  - PDF preview modal
  - Component library
  - Templates and guides

## Contact

For updates or improvements to this skill:
- Edmund Bogen: https://www.bogen.ai
- Eytan Benzeno: https://eytan.com
