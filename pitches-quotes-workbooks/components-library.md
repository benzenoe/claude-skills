# Design Components Library

Extract these exact components from reference files when creating new pitches, quotes, or workbooks.

## Reference Files

1. **Workbook**: `/Users/eytan/claude-code/bogen-ai/public/masterminds/ai-phone-agent-workbook.html`
2. **Pitch**: Check `https://eytan.com/pitches/david-may.html`
3. **Proposal**: Check `https://eytan.com/pitches/ashth-retainer-proposal.html`

## Core CSS System (Copy Exactly)

### CSS Variables - Workbook Style
```css
:root {
  --navy: #1a3e5c;
  --cyan: #00a8e1;
  --white: #ffffff;
  --dark-text: #333333;
  --light-bg: #f4f4f4;
  --muted: #666666;
  --bg: #ffffff;
  --section-alt: #f4f4f4;
  --card-bg: #ffffff;
  --card-border: #e0e0e0;
  --line-color: #cccccc;
  --prompt-bg: #f4f4f4;
  --prompt-border: #e0e0e0;
  --cover-bg: #1a3e5c;
}

[data-theme="dark"] {
  --bg: #0d1b2a;
  --section-alt: #1a3e5c;
  --dark-text: #e0e0e0;
  --muted: #aaaaaa;
  --card-bg: #162a3e;
  --card-border: #2a4a6a;
  --line-color: #3a5a7a;
  --prompt-bg: #162a3e;
  --prompt-border: #2a4a6a;
  --light-bg: #162a3e;
  --cover-bg: #0d1b2a;
}
```

### Theme Toggle (Copy Exactly)
```html
<div class="theme-toggle" onclick="toggleTheme()">
  <span class="theme-toggle-label">Light</span>
  <div class="toggle-switch"></div>
  <span class="theme-toggle-label">Dark</span>
</div>
```

```css
.theme-toggle {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--navy);
  padding: 8px 16px;
  border-radius: 50px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.3);
  cursor: pointer;
  user-select: none;
}

.theme-toggle-label {
  font-size: 9pt;
  font-weight: 600;
  color: var(--white);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.toggle-switch {
  width: 44px;
  height: 24px;
  background: #2a5a8a;
  border-radius: 12px;
  position: relative;
  transition: background 0.3s ease;
}

.toggle-switch::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  background: var(--white);
  border-radius: 50%;
  transition: transform 0.3s ease;
}

[data-theme="dark"] .toggle-switch {
  background: var(--cyan);
}

[data-theme="dark"] .toggle-switch::after {
  transform: translateX(20px);
}
```

### PDF Download Button (Copy Exactly)
```html
<div class="pdf-download">
  <button id="downloadBtn">
    <svg viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
    Download PDF
  </button>
</div>
```

```css
.pdf-download {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 1000;
}

.pdf-download button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--cyan);
  color: var(--white);
  padding: 12px 24px;
  border: none;
  border-radius: 50px;
  font-family: 'Montserrat', sans-serif;
  font-size: 10pt;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(0,168,225,0.4);
  transition: all 0.3s ease;
}

.pdf-download button:hover {
  background: #008aba;
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0,168,225,0.5);
}

.pdf-download button svg {
  width: 16px;
  height: 16px;
  fill: currentColor;
}
```

### PDF Modal (Copy Exactly)
```html
<div class="pdf-modal-overlay" id="pdfModal">
  <div class="pdf-modal">
    <div class="pdf-modal-header">
      <div class="pdf-modal-title">[TITLE] — Preview</div>
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
```

```css
.pdf-modal-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.85);
  z-index: 9999;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.pdf-modal-overlay.active {
  display: flex;
}

.pdf-modal {
  background: var(--bg);
  border-radius: 8px;
  width: 100%;
  max-width: 1200px;
  height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
}

.pdf-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 30px;
  border-bottom: 1px solid var(--card-border);
}

.pdf-modal-title {
  font-size: 14pt;
  font-weight: 600;
  color: var(--dark-text);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.pdf-modal-actions {
  display: flex;
  gap: 12px;
}

.pdf-modal-actions button {
  padding: 10px 20px;
  border-radius: 6px;
  font-family: 'Montserrat', sans-serif;
  font-size: 9pt;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.btn-close-modal {
  background: transparent;
  color: var(--muted);
  border: 1px solid var(--card-border);
}

.btn-close-modal:hover {
  background: rgba(0, 0, 0, 0.1);
  color: var(--dark-text);
}

.btn-confirm-download {
  background: var(--cyan);
  color: var(--white);
}

.btn-confirm-download:hover {
  background: #008aba;
}

.pdf-modal-body {
  flex: 1;
  overflow: hidden;
  background: #525659;
}

.pdf-modal-body iframe {
  width: 100%;
  height: 100%;
  border: none;
}
```

### JavaScript (Copy Exactly)
```javascript
// Theme Toggle
function toggleTheme() {
  const body = document.body;
  const current = body.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  body.setAttribute('data-theme', next);
  localStorage.setItem('[unique-key]-theme', next);
}

// Restore saved theme
(function() {
  const saved = localStorage.getItem('[unique-key]-theme');
  if (saved) {
    document.body.setAttribute('data-theme', saved);
  }
})();

// PDF Modal Functions
const pdfModal = document.getElementById('pdfModal');
const downloadBtn = document.getElementById('downloadBtn');
const closeModal = document.getElementById('closeModal');
const confirmDownload = document.getElementById('confirmDownload');
const pdfFrame = document.getElementById('pdfFrame');

downloadBtn.addEventListener('click', function() {
  pdfFrame.src = '[filename].pdf';
  pdfModal.classList.add('active');
});

closeModal.addEventListener('click', function() {
  pdfModal.classList.remove('active');
  pdfFrame.src = '';
});

confirmDownload.addEventListener('click', function() {
  const link = document.createElement('a');
  link.href = '[filename].pdf';
  link.download = '[filename].pdf';
  link.click();
});

pdfModal.addEventListener('click', function(e) {
  if (e.target === pdfModal) {
    pdfModal.classList.remove('active');
    pdfFrame.src = '';
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape' && pdfModal.classList.contains('active')) {
    pdfModal.classList.remove('active');
    pdfFrame.src = '';
  }
});
```

## Workbook-Specific Components

### Page Container
```html
<div class="page">
  <!-- Content here -->
</div>
```

```css
.page {
  max-width: 7.5in;
  margin: 0 auto;
  padding: 0.5in;
  background: var(--bg);
}
```

### Checkbox Item
```html
<div class="checkbox-item">Task or item description</div>
```

```css
.checkbox-item {
  position: relative;
  padding-left: 30px;
  margin-bottom: 10px;
  line-height: 1.5;
  color: var(--dark-text);
}

.checkbox-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 2px;
  width: 14px;
  height: 14px;
  border: 2px solid var(--navy);
  border-radius: 3px;
  background: var(--bg);
}
```

### Write Line
```html
<div class="write-line"></div>
```

```css
.write-line {
  height: 0.35in;
  border-bottom: 1px solid var(--line-color);
  margin: 10px 0;
}
```

### Write Area
```html
<div class="write-area"></div>
```

```css
.write-area {
  min-height: 1in;
  border: 1px solid var(--line-color);
  border-radius: 4px;
  padding: 10px;
  background: var(--bg);
  margin: 10px 0;
}
```

### Navy Box (Highlight Section)
```html
<div class="navy-box">
  <h3>Section Title</h3>
  <p>Content here</p>
</div>
```

```css
.navy-box {
  background: var(--navy);
  color: var(--white);
  padding: 1.5rem;
  border-radius: 8px;
  margin: 1.5rem 0;
}

.navy-box h3 {
  color: var(--white);
  margin-bottom: 1rem;
}
```

### Stat Grid
```html
<div class="stat-grid">
  <div class="stat-card">
    <div class="stat-label">Metric Name</div>
    <div class="stat-value">$44.5B</div>
    <div class="stat-desc">Description text</div>
  </div>
</div>
```

```css
.stat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.stat-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-top: 3px solid var(--cyan);
  padding: 1.5rem;
  border-radius: 8px;
}

.stat-label {
  font-size: 0.8rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--cyan);
  margin-bottom: 0.5rem;
}

.stat-desc {
  font-size: 0.85rem;
  color: var(--muted);
}
```

### Signature Section
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

```css
.signature-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}

.signature-section label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--dark-text);
}

.sig-line {
  border-bottom: 2px solid var(--line-color);
  height: 40px;
}
```

### Day Card (Implementation Plan)
```html
<div class="day-card">
  <div class="day-label">Day 1 — Setup</div>
  <div class="checkbox-item">Task 1</div>
  <div class="checkbox-item">Task 2</div>
  <div class="checkbox-item">Task 3</div>
</div>
```

```css
.day-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-left: 4px solid var(--cyan);
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.day-label {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Cover Page (Workbook)
```html
<div class="cover">
  <img src="Images/hero.png" alt="Hero Image" class="cover-hero">
  <div class="cover-type">Complete Implementation Workbook</div>
  <h1>Main Title</h1>
  <div class="cover-subtitle">Subtitle or tagline</div>
  <div class="cover-tagline">"Quote or memorable phrase"</div>
  <div class="cover-date">Session 1: Date & Time</div>
  <div class="cover-zoom">Zoom: <a href="https://zoom.link">zoom.link</a></div>
  <div class="cover-brand">Brand Name</div>
</div>
```

```css
.cover {
  background: var(--cover-bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 3rem 2rem;
  color: var(--white);
}

.cover-hero {
  max-width: 500px;
  width: 80%;
  margin-bottom: 2rem;
  border-radius: 12px;
}

.cover-type {
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--cyan);
  margin-bottom: 1.5rem;
  font-weight: 600;
}

.cover h1 {
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  font-weight: 700;
  margin-bottom: 1rem;
  line-height: 1.2;
  color: var(--white);
}

.cover-subtitle {
  font-size: clamp(1.2rem, 2vw, 1.5rem);
  font-weight: 400;
  margin-bottom: 1rem;
  max-width: 700px;
}

.cover-tagline {
  font-size: 1.3rem;
  font-style: italic;
  color: var(--cyan);
  margin-bottom: 2rem;
}

.cover-date {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.cover-zoom {
  font-size: 1rem;
  margin-bottom: 2rem;
}

.cover-zoom a {
  color: var(--cyan);
  text-decoration: none;
}

.cover-brand {
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 2rem;
}
```

## Print CSS (Copy Exactly)

```css
@page {
  size: letter;
  margin: 0.6in 0.75in;
  @bottom-center {
    content: "Brand Name | Document Title | Date | Page " counter(page);
    font-family: 'Montserrat', sans-serif;
    font-size: 8pt;
    color: #666666;
  }
}

@media print {
  .page-break { page-break-after: always; }
  .no-break { page-break-inside: avoid; }
  body { font-size: 10pt; background: #ffffff !important; color: #333333 !important; }
  .theme-toggle, .pdf-download { display: none !important; }
  .cover { min-height: 9.5in; }
  .page { padding: 0; }
  h1, h2, h3, h4 { color: #1a3e5c !important; }
  .navy-box { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  [data-theme="dark"] { --bg: #ffffff; --dark-text: #333333; }
  * {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
}
```

## Usage Instructions

When creating a new pitch, quote, or workbook:

1. **Copy the exact HTML structure** from reference files
2. **Use the exact CSS variables and styles** listed above
3. **Include theme toggle, PDF button, and PDF modal** exactly as shown
4. **Replace only the content** - keep all styling intact
5. **Update localStorage key** to be unique per document
6. **Update PDF filename** in all references

**Do not modify**: CSS values, component structure, JavaScript logic
**Do modify**: Text content, images, brand-specific colors if needed
