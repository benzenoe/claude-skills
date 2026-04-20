---
name: pitches-quotes-workbooks
description: Create professional pitch decks, pricing quotes, and implementation workbooks using the eytan.com and bogen.ai design system with light/dark mode toggle, PDF preview modal, and print-optimized layouts.
---

# Pitches, Quotes & Workbooks Generator

**Create professional pitch decks, pricing quotes, and implementation workbooks using the EXACT design system from eytan.com and bogen.ai**

## Core Features (REQUIRED in every document)

✅ **Light/Dark Mode Toggle** - Persists user preference in localStorage
✅ **PDF Creation** - Automated generation with Puppeteer + proper headers/footers
✅ **PDF Download Preview** - Modal popup with embedded PDF viewer (eytan.com style)
✅ **Responsive Design** - Mobile, tablet, and desktop layouts
✅ **Professional Typography** - Montserrat fonts with proper hierarchy
✅ **Brand Logos** - Correct logo usage for PDFs and favicons

## Usage

When the user asks to create:
- **Pitches**: "Create a pitch for [client] about [service]"
- **Quotes/Proposals**: "Generate a pricing proposal for [project]"
- **Workbooks**: "Create a workbook for [topic/training]"

**IMPORTANT**: Copy components EXACTLY from this guide - do not modify CSS, structure, or functionality

## File Structure

```
project/
├── public/
│   ├── pitches/          # Pitch decks
│   ├── proposals/        # Proposals and quotes
│   ├── masterminds/      # Workbooks
│   └── images/
│       ├── eb-logo-old.png      # Dark navy logo for PDF headers/footers
│       └── eb-logo-dark.png     # Circuit design logo for favicon
├── generate-[name]-pdf.js        # PDF generation script (root)
└── .vercel-deploy-trigger        # For deployment
```

## Logo Setup (CRITICAL)

### Favicon (Browser Tab Icon)
```html
<link rel="icon" type="image/png" href="../images/eb-logo-dark.png">
<link rel="shortcut icon" type="image/png" href="../images/eb-logo-dark.png">
```
- Use `eb-logo-dark.png` - Navy blue circular badge with circuit design
- Better visibility in browser tabs
- Matches Bogen.ai brand identity

### PDF Headers/Footers
- Use `eb-logo-old.png` - Dark navy text logo
- Must be converted to base64 data URL for embedding
- Visible on white backgrounds in PDFs

## PDF Generation System

### Reusable PDF Generator Script

Create `generate-[proposal-name]-pdf.js` in project root:

```javascript
#!/usr/bin/env node
/**
 * Generate professional PDF with proper headers/footers
 * - Cover page: NO headers/footers (full page)
 * - All other pages: Headers and footers with logo, company info, and page numbers
 * - Uses base64 encoded logo to avoid broken images
 */

const puppeteer = require('puppeteer');
const { PDFDocument } = require('pdf-lib');
const fs = require('fs').promises;
const fsSync = require('fs');
const path = require('path');

async function generatePDF() {
  console.log('✓ Step 1: Preparing logo...');

  // Read and convert logo to base64 (dark version for visibility)
  const logoPath = path.resolve(__dirname, 'public/images/eb-logo-old.png');
  const logoBuffer = fsSync.readFileSync(logoPath);
  const logoBase64 = logoBuffer.toString('base64');
  const logoDataUrl = `data:image/png;base64,${logoBase64}`;

  console.log('✓ Step 2: Launching browser...');

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();

  // CHANGE THIS: Update to your HTML file path
  const htmlPath = 'file://' + path.resolve(__dirname, 'public/proposals/[YOUR-FILE].html');
  console.log(`✓ Step 3: Loading HTML...`);

  await page.goto(htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(resolve => setTimeout(resolve, 2000));

  console.log('✓ Step 4: Generating PDF with headers/footers...');

  // Header template with logo
  const headerTemplate = `
    <div style="width: 100%; padding: 0; margin: 0; font-size: 9pt; -webkit-print-color-adjust: exact;">
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 48px 12px 48px; border-bottom: 1px solid #e5e9ec;">
        <img src="${logoDataUrl}" style="height: 32px; width: auto;">
        <span style="font-family: -apple-system, system-ui, sans-serif; color: #8899aa; font-weight: 500;">[PROPOSAL TITLE]</span>
        <div style="width: 32px;"></div>
      </div>
    </div>
  `;

  // Footer template with logo and page numbers
  const footerTemplate = `
    <div style="width: 100%; padding: 0; margin: 0; font-size: 8pt; -webkit-print-color-adjust: exact;">
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 48px 0 48px; border-top: 1px solid #e5e9ec;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <img src="${logoDataUrl}" style="height: 18px; width: auto;">
          <span style="font-family: -apple-system, system-ui, sans-serif; color: #8899aa;">Bogen.ai — Dave T Productions</span>
        </div>
        <span style="font-family: -apple-system, system-ui, sans-serif; color: #00a8e1; font-weight: 500;">support@reignation.com</span>
        <span style="font-family: -apple-system, system-ui, sans-serif; color: #8899aa;">Page <span class="pageNumber"></span></span>
      </div>
    </div>
  `;

  const tempPath = path.resolve(__dirname, 'temp-pdf.pdf');

  // Generate PDF with headers/footers on ALL pages
  await page.pdf({
    path: tempPath,
    format: 'Letter',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: headerTemplate,
    footerTemplate: footerTemplate,
    margin: {
      top: '0.85in',    // Space for header
      bottom: '0.75in', // Space for footer
      left: '0.75in',
      right: '0.75in'
    },
    preferCSSPageSize: false
  });

  await browser.close();

  console.log('✓ Step 5: Processing PDF to remove header/footer from cover page...');

  // Load the PDF
  const pdfBytes = await fs.readFile(tempPath);
  const pdfDoc = await PDFDocument.load(pdfBytes);

  // Get all pages
  const pages = pdfDoc.getPages();
  const firstPage = pages[0];

  // Get dimensions
  const { width, height } = firstPage.getSize();

  // Create new PDF
  const newPdfDoc = await PDFDocument.create();

  // First page - full size (no margins for cover)
  const [copiedFirstPage] = await newPdfDoc.copyPages(pdfDoc, [0]);
  copiedFirstPage.setSize(width, height);
  newPdfDoc.addPage(copiedFirstPage);

  // Copy remaining pages with headers/footers
  for (let i = 1; i < pages.length; i++) {
    const [copiedPage] = await newPdfDoc.copyPages(pdfDoc, [i]);
    newPdfDoc.addPage(copiedPage);
  }

  // CHANGE THIS: Update output path and filename
  const outputPath = path.resolve(__dirname, 'public/proposals/[YOUR-FILE].pdf');

  // Save final PDF
  const finalPdfBytes = await newPdfDoc.save();
  await fs.writeFile(outputPath, finalPdfBytes);

  // Clean up
  await fs.unlink(tempPath);

  const fileSizeKB = finalPdfBytes.length / 1024;

  console.log(`✓ Step 6: PDF created: ${outputPath}`);
  console.log(`✓ File size: ${fileSizeKB.toFixed(1)} KB`);
  console.log(`\n✅ PROFESSIONAL PDF GENERATED!`);
  console.log(`\n📄 Cover Page: NO headers/footers`);
  console.log(`📄 Content Pages: Clean headers/footers with working logos`);
}

generatePDF().catch(err => {
  console.error('✗ Error:', err);
  process.exit(1);
});
```

**Dependencies Required:**
```json
{
  "dependencies": {
    "puppeteer": "^21.0.0",
    "pdf-lib": "^1.17.1"
  }
}
```

**Usage:**
```bash
node generate-[proposal-name]-pdf.js
```

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

**Favicon:**
```html
<link rel="icon" type="image/png" href="../images/eb-logo-dark.png">
<link rel="shortcut icon" type="image/png" href="../images/eb-logo-dark.png">
```

**Theme Toggle Button:**
- Fixed position (top-right: 20px)
- Shows current theme and toggle switch
- Persists choice in localStorage with unique key

**PDF Download System:**
- Fixed floating button (bottom-right: 30px)
- Opens modal with embedded PDF preview
- Modal header with Close and Download buttons
- Click outside or press Escape to close

**Print CSS:**
- Letter size pages (@page)
- Hide interactive elements
- Preserve brand colors
- Proper page breaks

## Template Structure

### Complete HTML Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Document Title]</title>
  <link rel="icon" type="image/png" href="../images/eb-logo-dark.png">
  <link rel="shortcut icon" type="image/png" href="../images/eb-logo-dark.png">
  <style>
    /* CSS Variables for theming */
    /* Typography system */
    /* Layout components */
    /* Theme toggle styles */
    /* PDF modal styles */
    /* Floating download button styles */
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
  <button class="download-pdf-button" id="downloadBtn">
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M10 13L5 8L6.41 6.59L9 9.17V2H11V9.17L13.59 6.59L15 8L10 13Z" fill="currentColor"/>
      <path d="M18 16V18H2V16H4V16H16V16H18Z" fill="currentColor"/>
    </svg>
    Download PDF
  </button>

  <!-- PDF Preview Modal -->
  <div class="pdf-modal-overlay" id="pdfModal">
    <div class="pdf-modal">
      <div class="pdf-modal-header">
        <div class="pdf-modal-title">[Client Name] — [Document Title]</div>
        <div class="pdf-modal-actions">
          <button class="btn-close-modal" id="closeModal">Close</button>
          <button class="btn-confirm-download" id="confirmDownload">
            <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M10 13L5 8L6.41 6.59L9 9.17V2H11V9.17L13.59 6.59L15 8L10 13Z" fill="currentColor"/>
              <path d="M18 16V18H2V16H4V16H16V16H18Z" fill="currentColor"/>
            </svg>
            Download PDF
          </button>
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
    function toggleTheme() {
      const body = document.body;
      const current = body.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      body.setAttribute('data-theme', next);
      localStorage.setItem('[unique-key]-theme', next);
    }

    // Restore theme on load
    const saved = localStorage.getItem('[unique-key]-theme');
    if (saved) document.body.setAttribute('data-theme', saved);

    // PDF Modal Functionality
    const pdfModal = document.getElementById('pdfModal');
    const downloadBtn = document.getElementById('downloadBtn');
    const closeModalBtn = document.getElementById('closeModal');
    const confirmDownloadBtn = document.getElementById('confirmDownload');
    const pdfFrame = document.getElementById('pdfFrame');

    // Open modal and load PDF
    downloadBtn.addEventListener('click', () => {
      pdfFrame.src = '[filename].pdf';
      pdfModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });

    // Close modal
    function closePdfModal() {
      pdfModal.classList.remove('active');
      document.body.style.overflow = '';
      setTimeout(() => {
        pdfFrame.src = '';
      }, 300);
    }

    closeModalBtn.addEventListener('click', closePdfModal);

    // Close on background click
    pdfModal.addEventListener('click', (e) => {
      if (e.target === pdfModal) {
        closePdfModal();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && pdfModal.classList.contains('active')) {
        closePdfModal();
      }
    });

    // Download PDF
    confirmDownloadBtn.addEventListener('click', () => {
      const link = document.createElement('a');
      link.href = '[filename].pdf';
      link.download = '[filename].pdf';
      link.click();
    });
  </script>
</body>
</html>
```

## Complete CSS Styles

### Floating Download Button

```css
/* Download Button */
.download-pdf-button {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background: linear-gradient(135deg, #00a8e1 0%, #0088bb 100%);
  color: white;
  padding: 14px 28px;
  border-radius: 50px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 15px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 20px rgba(0, 168, 225, 0.4);
  transition: all 0.3s ease;
  z-index: 1000;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.download-pdf-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 30px rgba(0, 168, 225, 0.6);
  background: linear-gradient(135deg, #0088bb 0%, #006a99 100%);
}

.download-pdf-button:active {
  transform: translateY(0);
}

.download-pdf-button svg {
  width: 20px;
  height: 20px;
}
```

### PDF Modal Styles

```css
/* PDF Modal Overlay */
.pdf-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  padding: 20px;
}

.pdf-modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

.pdf-modal {
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
  max-width: 1100px;
  width: 100%;
  height: 90vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transform: scale(0.9);
  transition: transform 0.3s ease;
}

.pdf-modal-overlay.active .pdf-modal {
  transform: scale(1);
}

.pdf-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 30px;
  border-bottom: 1px solid #e5e9ec;
  background: white;
}

.pdf-modal-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #0d1620;
}

.pdf-modal-actions {
  display: flex;
  gap: 12px;
}

.btn-close-modal,
.btn-confirm-download {
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  transition: all 0.2s ease;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.btn-close-modal {
  background: #f0f4f8;
  color: #0d1620;
}

.btn-close-modal:hover {
  background: #e5e9ec;
}

.btn-confirm-download {
  background: linear-gradient(135deg, #00a8e1 0%, #0088bb 100%);
  color: white;
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-confirm-download:hover {
  background: linear-gradient(135deg, #0088bb 0%, #006a99 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 168, 225, 0.4);
}

.btn-confirm-download svg {
  width: 16px;
  height: 16px;
}

.pdf-modal-body {
  flex: 1;
  overflow: hidden;
  background: #f0f4f8;
}

.pdf-modal-body iframe {
  width: 100%;
  height: 100%;
  border: none;
}
```

### Template Showcase Grid (for showing design options)

```css
/* Template Grid - Optimized for PDF */
@media print {
  .section:has(.template-grid) {
    page-break-inside: avoid !important;
    padding: 0.1rem 0 0 0 !important;
  }

  .section:has(.template-grid) h2 {
    margin-bottom: 0.1rem !important;
    margin-top: 0 !important;
    font-size: 0.95rem !important;
    line-height: 1.1 !important;
  }

  .section:has(.template-grid) p {
    margin-bottom: 0.1rem !important;
    font-size: 0.65rem !important;
    line-height: 1.1 !important;
  }

  .template-grid {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    row-gap: 0.5cm !important;  /* 0.5cm spacing between rows */
    column-gap: 0.3rem !important;
    margin-bottom: 0 !important;
    margin-top: 0.1rem !important;
    page-break-inside: avoid !important;
  }

  .template-card {
    margin: 0 !important;
    padding: 0 !important;
    border: none !important;
    background: none !important;
    page-break-inside: avoid !important;
  }

  .template-image {
    margin: 0 !important;
    padding: 0 !important;
    line-height: 0 !important;
    height: 4.33in !important;  /* Optimized for Letter page */
    overflow: hidden !important;
  }

  .template-image img {
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 100% !important;
    height: 4.33in !important;
    object-fit: contain !important;
  }
}
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

## Print CSS Requirements

```css
@media print {
  .theme-toggle,
  .download-pdf-button,
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
- **Proposals**: `[client-name]-[service]-proposal.html`
- **Workbooks**: `[topic]-workbook.html`
- **PDFs**: Match HTML filename with `.pdf` extension

## Deployment Steps

1. **Create HTML file** in appropriate directory:
   - Pitches: `public/pitches/`
   - Proposals: `public/proposals/`
   - Workbooks: `public/masterminds/`

2. **Generate PDF** using the reusable script:
   - Update `generate-[name]-pdf.js` with file paths
   - Run: `node generate-[name]-pdf.js`
   - PDF saved in same directory as HTML

3. **Compress PDF** (optional but recommended):
   - Use Preview > Export > Reduce File Size
   - Or online compression tool
   - Aim for < 3 MB for fast downloads

4. **Commit and push**:
   ```bash
   git add public/[type]/[files] generate-[name]-pdf.js
   git commit -m "Add [type]: [title]"
   git push
   ```

5. **Trigger deployment** (if using Vercel):
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
- **Logo**: `eb-logo-old.png` (PDFs), `eb-logo-dark.png` (favicon)

### Eytan Benzeno Brand
- **Primary**: Teal (#2B6166)
- **Secondary**: Navy (#0d1620)
- **Accent**: Blue (#00a8e1)
- **Typography**: System fonts throughout

## Examples to Reference

1. **Pitch**: https://eytan.com/pitches/david-may.html
2. **Proposal**: https://eytan.com/pitches/ashth-retainer-proposal.html
3. **Proposal with PDF Modal**: https://bogen.ai/proposals/karis-properties-founding-partner.html
4. **Strategy Doc**: https://eytan.com/pitches/ashth-local-strategy.html
5. **Workbook (Edmund)**: https://www.bogen.ai/masterminds/ai-phone-agent-workbook.html
6. **Workbook (GitHub Pages)**: https://edmundbogen.github.io/zillow-ai-workbook.html

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

### Mobile Responsive PDF Modal

```css
@media (max-width: 768px) {
  .download-pdf-button {
    bottom: 20px;
    right: 20px;
    padding: 12px 24px;
    font-size: 14px;
  }

  .pdf-modal {
    height: 95vh;
    border-radius: 12px;
  }

  .pdf-modal-header {
    padding: 15px 20px;
    flex-direction: column;
    gap: 12px;
    align-items: stretch;
  }

  .pdf-modal-title {
    font-size: 1rem;
  }

  .pdf-modal-actions {
    width: 100%;
  }

  .btn-close-modal,
  .btn-confirm-download {
    flex: 1;
  }
}
```

## Quick Checklist

Before deploying, verify:
- ✅ Correct favicon (`eb-logo-dark.png`)
- ✅ PDF generation script configured with correct paths
- ✅ PDF headers/footers using base64 logo
- ✅ Cover page has NO headers/footers
- ✅ Content pages have headers/footers
- ✅ PDF modal implemented with preview
- ✅ Floating download button styled correctly
- ✅ All interactive elements hidden in print CSS
- ✅ Template grid optimized (if applicable)
- ✅ PDF compressed to < 3 MB
- ✅ Files in correct directory (pitches/proposals/masterminds)
- ✅ Mobile responsive

---

**Note**: Always test the PDF modal and download functionality before deploying. Compress PDFs for faster loading.
