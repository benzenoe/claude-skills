# Pitches, Quotes & Workbooks Generator

**Create professional pitch decks, pricing quotes, and implementation workbooks using the EXACT design system from eytan.com and bogen.ai**

## Core Features (REQUIRED in every document)

✅ **Light/Dark Mode Toggle** - Persists user preference in localStorage
✅ **PDF Creation** - Print-to-PDF optimized with proper page breaks
✅ **PDF Download Preview** - Modal popup with embedded PDF viewer (eytan.com style)
✅ **Responsive Design** - Mobile, tablet, and desktop layouts
✅ **Professional Typography** - Montserrat fonts with proper hierarchy

## Usage

When the user asks to create:
- **Pitches**: "Create a pitch for [client] about [service]"
- **Quotes/Proposals**: "Generate a pricing proposal for [project]"
- **Workbooks**: "Create a workbook for [topic/training]"

**IMPORTANT**: Copy components EXACTLY from `components-library.md` - do not modify CSS, structure, or functionality

## Core Components

### 1. Document Types

**Pitch Deck:**
- Hero section with gradient background
- Value proposition and problem/solution sections
- Case studies or testimonials
- Call-to-action with contact form/email

**Quote/Proposal:**
- Executive summary
- Scope of work breakdown
- Pricing configurator (optional interactive)
- Timeline/milestones
- Terms and acceptance section

**Workbook:**
- Cover page with session details
- Table of contents
- Instructional content sections
- Interactive exercises (checklists, write-ins, calculators)
- Implementation plans
- Commitment/signature section

### 2. Theme System

**CSS Variables:**
```css
:root {
  --primary: #00a8e1;
  --navy: #0d1620;
  --teal: #2B6166;
  --gold: #ffd93d;
  --white: #f0f4f8;
  --bg: #0d1620;
  --text: #f0f4f8;
  --border: rgba(255,255,255,0.08);
}

[data-theme="light"] {
  --bg: #ffffff;
  --text: #1a1a1a;
  --border: rgba(0,0,0,0.1);
  --navy: #1a1a1a;
  --white: #0d1620;
}
```

### 3. Required Features

**Theme Toggle Button:**
- Fixed position (top-right: 20px)
- Shows current theme and toggle switch
- Persists choice in localStorage with unique key

**PDF Download System:**
- Fixed button (bottom-right: 30px)
- Opens modal with embedded PDF preview
- Modal header with Close and Download buttons
- Click outside or press Escape to close

**Print CSS:**
- Letter size pages (@page)
- Hide interactive elements
- Preserve brand colors
- Proper page breaks

## Template Structure

### HTML Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Document Title]</title>
  <style>
    /* CSS Variables for theming */
    /* Typography system */
    /* Layout components */
    /* Theme toggle styles */
    /* PDF modal styles */
    /* Print media queries */
  </style>
</head>
<body data-theme="light">

  <!-- Theme Toggle -->
  <div class="theme-toggle" onclick="toggleTheme()">
    <span class="theme-toggle-label">Light</span>
    <div class="toggle-switch"></div>
    <span class="theme-toggle-label">Dark</span>
  </div>

  <!-- PDF Download Button -->
  <div class="pdf-download">
    <button id="downloadBtn">
      <svg><!-- Download icon --></svg>
      Download PDF
    </button>
  </div>

  <!-- PDF Preview Modal -->
  <div class="pdf-modal-overlay" id="pdfModal">
    <div class="pdf-modal">
      <div class="pdf-modal-header">
        <div class="pdf-modal-title">[Title] — Preview</div>
        <div class="pdf-modal-actions">
          <button class="btn-close-modal" id="closeModal">Close</button>
          <button class="btn-confirm-download" id="confirmDownload">Download PDF</button>
        </div>
      </div>
      <div class="pdf-modal-body">
        <iframe id="pdfFrame"></iframe>
      </div>
    </div>
  </div>

  <!-- Document Content -->
  <main>
    <!-- Content sections here -->
  </main>

  <script>
    // Theme toggle functionality
    // PDF modal functionality
  </script>
</body>
</html>
```

## Component Library

### Workbook Components

**Checkbox Item:**
```html
<div class="checkbox-item">Task description here</div>
```

**Write Line:**
```html
<div class="write-line"></div>
```

**Write Area:**
```html
<div class="write-area"></div>
```

**Signature Section:**
```html
<div class="signature-section">
  <div>
    <label>Signature:</label>
    <div class="sig-line"></div>
  </div>
  <div>
    <label>Date:</label>
    <div class="sig-line"></div>
  </div>
</div>
```

**Stats Grid:**
```html
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-label">Metric Name</div>
    <div class="stat-value">$45.5B</div>
    <div class="stat-desc">Description</div>
  </div>
</div>
```

### Pitch/Quote Components

**Hero Section:**
```html
<section class="hero">
  <h1>Main Headline</h1>
  <p class="subtitle">Supporting tagline</p>
</section>
```

**Pricing Card:**
```html
<div class="pricing-card">
  <div class="plan-name">Starter</div>
  <div class="plan-price">$197<span>/month</span></div>
  <ul class="plan-features">
    <li>Feature 1</li>
    <li>Feature 2</li>
  </ul>
  <button class="cta-button">Get Started</button>
</div>
```

**Timeline/Milestones:**
```html
<table class="timeline">
  <tr class="phase-header">
    <td colspan="3">Phase 1: Discovery</td>
  </tr>
  <tr>
    <td>Week 1-2</td>
    <td>Kickoff & Requirements</td>
    <td class="td-amount">$2,500</td>
  </tr>
</table>
```

## Styling Patterns

### Typography Scale
- **Hero**: `clamp(2.5rem, 5vw, 4rem)`
- **H1**: `clamp(1.8rem, 3vw, 2.5rem)`
- **H2**: `clamp(1.4rem, 2.5vw, 2rem)`
- **Body**: `1rem` / `line-height: 1.6`

### Color Usage
- **Primary Actions**: `--primary` (cyan #00a8e1)
- **Headers**: `--navy` (dark) / switches in light mode
- **Accents**: `--gold` for highlights, `--teal` for secondary
- **Borders**: `rgba()` with 0.08-0.1 opacity

### Spacing System
- **Sections**: `5rem` vertical padding
- **Cards**: `1.5rem` internal padding
- **Gaps**: `1rem` (default), `1.5rem` (comfortable), `2rem` (spacious)

## JavaScript Functionality

### Theme Toggle
```javascript
function toggleTheme() {
  const body = document.body;
  const current = body.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  body.setAttribute('data-theme', next);
  localStorage.setItem('[unique-key]-theme', next);
}

// Restore on load
const saved = localStorage.getItem('[unique-key]-theme');
if (saved) document.body.setAttribute('data-theme', saved);
```

### PDF Modal
```javascript
const pdfModal = document.getElementById('pdfModal');
const downloadBtn = document.getElementById('downloadBtn');

downloadBtn.addEventListener('click', () => {
  document.getElementById('pdfFrame').src = '[filename].pdf';
  pdfModal.classList.add('active');
});

document.getElementById('closeModal').addEventListener('click', () => {
  pdfModal.classList.remove('active');
  document.getElementById('pdfFrame').src = '';
});

// Close on background click
pdfModal.addEventListener('click', (e) => {
  if (e.target === pdfModal) {
    pdfModal.classList.remove('active');
  }
});

// Download functionality
document.getElementById('confirmDownload').addEventListener('click', () => {
  const link = document.createElement('a');
  link.href = '[filename].pdf';
  link.download = '[filename].pdf';
  link.click();
});
```

## Print CSS Requirements

```css
@media print {
  .theme-toggle,
  .pdf-download,
  .pdf-modal-overlay {
    display: none !important;
  }

  @page {
    size: letter;
    margin: 0.5in;
  }

  body {
    background: white;
    color: #333;
  }

  .page-break {
    page-break-after: always;
  }

  .no-break {
    page-break-inside: avoid;
  }

  * {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
}
```

## File Naming Convention

- **Pitches**: `[client-name]-[service]-pitch.html`
- **Quotes**: `[client-name]-[service]-proposal.html`
- **Workbooks**: `[topic]-workbook.html`
- **PDFs**: Match HTML filename with `.pdf` extension

## Deployment Steps

1. **Create HTML file** in appropriate directory:
   - Pitches: `public/pitches/`
   - Quotes: `public/quotes/`
   - Workbooks: `public/masterminds/` or `public/workbooks/`

2. **Generate PDF** using browser print-to-PDF:
   - Open HTML file
   - Press Cmd+P / Ctrl+P
   - Select "Save as PDF"
   - Save in same directory

3. **Commit and push**:
   ```bash
   git add [files]
   git commit -m "Add [type]: [title]"
   git push
   ```

4. **Trigger deployment** (if using Vercel):
   ```bash
   date >> .vercel-deploy-trigger
   git add .vercel-deploy-trigger
   git commit -m "Trigger deployment"
   git push
   ```

## Brand Guidelines

### Edmund Bogen Brand
- **Primary**: Cyan (#00a8e1)
- **Secondary**: Navy (#0d1620)
- **Accent**: Gold (#ffd93d)
- **Typography**: Montserrat (headings), System fonts (body)

### Eytan Benzeno Brand
- **Primary**: Teal (#2B6166)
- **Secondary**: Navy (#0d1620)
- **Accent**: Blue (#00a8e1)
- **Typography**: System fonts throughout

## Examples to Reference

1. **Pitch**: https://eytan.com/pitches/david-may.html
2. **Proposal**: https://eytan.com/pitches/ashth-retainer-proposal.html
3. **Strategy Doc**: https://eytan.com/pitches/ashth-local-strategy.html
4. **Workbook (Edmund)**: https://www.bogen.ai/masterminds/ai-phone-agent-workbook.html
5. **Workbook (GitHub Pages)**: https://edmundbogen.github.io/zillow-ai-workbook.html

## Common Customizations

### Interactive Pricing Calculator
Add configurator for quotes with:
- Checkbox selection for add-ons
- Real-time price updates
- Live summary box
- Email CTA with pre-filled subject/body

### Hero Animations
Add pulse dot or gradient animations:
```css
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.05); opacity: 0.8; }
}
```

### Responsive Breakpoints
- **Desktop**: Default (1100px max-width)
- **Tablet**: 900px (2-column → 1-column)
- **Mobile**: 600px (compact spacing, stacked layouts)

---

**Note**: Always test print-to-PDF output before deploying to ensure proper formatting and page breaks.
