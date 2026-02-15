---
name: eytan-social-media
description: Social media content engine for Eytan Benzeno - generates weekly content calendars, platform-optimized posts, news aggregation, lead tracking, and French translations. Use when asked to create social media posts, weekly content plans, or manage social presence.
---

# Eytan Benzeno Social Media Skill

This skill automates Eytan Benzeno's social media presence across multiple platforms, focusing on AI/tech consulting (Bogen.ai) while supporting his portfolio of businesses. It generates weekly content calendars, creates platform-optimized posts, tracks leads from engagement, and handles French translations.

## Quick Commands

| Command | Description |
|---------|-------------|
| `/eytan-weekly-plan` | Generate full week content calendar (3-4 posts) |
| `/eytan-post [platform] [topic]` | Create single post for specific platform |
| `/eytan-news` | Fetch latest AI/tech/science/finance news for content ideas |
| `/eytan-leads` | Show lead tracking dashboard |
| `/eytan-translate [text]` | Translate content to French |
| `/eytan-showcase [project]` | Create portfolio highlight post |
| `/eytan-adjust [feedback]` | Modify current week's plan based on feedback |

---

## Eytan's Profile

**Full Name:** Eytan Benzeno
**Title:** AI & Marketing Consultant | Real Estate Broker | E-commerce Pioneer
**Website:** eytan.com
**Languages:** English (primary), French (secondary)
**Experience:** 20+ years across e-commerce, real estate, technology, and personal development

### Businesses & Focus Areas

| Business | Focus | Content Priority |
|----------|-------|------------------|
| **Bogen.ai** | AI transformation, marketing automation, tech strategy | PRIMARY |
| **SoldHere** | Real estate (South Florida & Portugal) | Secondary |
| **Reignation** | Coaching & mastermind facilitation | Secondary |
| **Personal Brand** | Thought leadership, tech expertise | PRIMARY |

### Social Media Accounts

**Personal Accounts:**
- LinkedIn: linkedin.com/in/benzeno
- Instagram: @benzenoe
- Facebook: facebook.com/benzeno
- X/Twitter: @benzeno
- GitHub: github.com/benzenoe

**Business Accounts:** (Use personal accounts for now; business accounts TBD)

---

## Brand Guidelines

### Color Palette
All visual content should incorporate these colors:

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Teal** | #008080 | Primary brand color |
| **Turquoise** | #40E0D0 | Secondary/accent |
| **Pastel Teal** | #B2DFDB | Backgrounds, subtle elements |
| **Pastel Turquoise** | #B2EBF2 | Highlights |
| **Pastel Mint** | #C8E6C9 | Accent variation |
| **Pastel Lavender** | #E1BEE7 | Occasional accent |

### Voice & Tone

**Personal Account Voice:**
- Thought leader, curious explorer
- Conversational yet insightful
- Example: "I've been experimenting with..." or "Here's what I learned..."

**Bogen.ai/Professional Voice:**
- Expert consultant, problem solver
- Professional, authoritative, data-driven
- Example: "Here's how AI can transform..." or "The key insight is..."

**Coaching/Reignation Voice:**
- Coach, motivator
- Inspiring, actionable
- Example: "The difference between good and great is..." or "Try this approach..."

---

## Content Strategy

### Posting Frequency
**3-4 high-quality posts per week** (quality over quantity)

### Weekly Content Pillars

| Day | Post Type | Account Focus |
|-----|-----------|---------------|
| Monday | AI/Tech Insight | Bogen.ai + Personal |
| Wednesday | Case Study or Tool Review | Bogen.ai |
| Friday | Thought Leadership | Personal |
| Sunday (optional) | Week Preview or Engagement | Personal |

### 4-Week Content Rotation

**Week 1:** AI news reaction + Portfolio showcase + Industry analysis
**Week 2:** Tool review + Science news + Personal story
**Week 3:** Client success story + Finance/market insight + Behind-the-scenes
**Week 4:** Trend prediction + Tutorial + Community engagement

### Content Categories

1. **AI/Tech News** - React to breaking AI, ML, tech developments
2. **Tool Reviews** - Deep dives on productivity tools, SaaS, AI tools
3. **Portfolio Showcases** - Highlight Bogen.ai projects and results
4. **Thought Leadership** - Original insights on tech, business, future trends
5. **Science/Finance** - Interesting developments in these adjacent fields
6. **Personal Stories** - Behind-the-scenes, lessons learned, experiences
7. **Tutorials** - How-to content for AI implementation, tech strategy

---

## Platform-Specific Guidelines

### LinkedIn
**Character Limit:** 3,000 characters
**Best Practices:**
- Long-form thought leadership (300-1000 words)
- Use line breaks for readability
- 3-5 relevant hashtags at the end
- Include a clear call-to-action
- Carousel posts for educational content (8-10 slides)

**Post Structure:**
```
[Hook - compelling first line that stops the scroll]

[Story or insight - 2-3 paragraphs]

[Key takeaway or lesson]

[Call-to-action]

#hashtag1 #hashtag2 #hashtag3
```

### Instagram
**Character Limit:** 2,200 characters (caption)
**Best Practices:**
- Visual-first (image or video required)
- Reels for AI/tech tips (15-60 sec)
- Carousels for educational content
- Stories for daily engagement
- 20-30 hashtags (mix of popular and niche)
- Use line breaks and emojis sparingly

**Post Structure:**
```
[Hook]

[Value/Story]

[Call-to-action]

.
.
.
[Hashtags]
```

### Facebook
**Character Limit:** 63,206 characters (but keep under 500)
**Best Practices:**
- Article shares with thoughtful commentary
- Video content performs well
- Questions drive engagement
- Native video over YouTube links
- Link in first comment if sharing URLs

### TikTok
**Video Length:** 15-60 seconds ideal, up to 10 min allowed
**Best Practices:**
- Hook in first 3 seconds
- Educational content works best
- Trending audio when appropriate
- Text overlays for accessibility
- Fast-paced, high-energy delivery

**Video Script Structure:**
```
[Hook: 0-3 sec - surprising statement or question]
[Context: 3-15 sec - set up the problem]
[Value: 15-45 sec - deliver the insight/solution]
[CTA: 45-60 sec - follow for more, comment question]
```

### X/Twitter
**Character Limit:** 280 characters (or threads)
**Best Practices:**
- Quick takes on news
- Thread format for longer insights
- Quote tweets with added value
- Engage with tech community
- Timing matters (post during US business hours)

**Thread Structure:**
```
1/ [Hook + main point]
2/ [Supporting point 1]
3/ [Supporting point 2]
4/ [Example or story]
5/ [Conclusion + CTA]
```

---

## Command: /eytan-weekly-plan

When invoked, execute these steps:

### Step 1: News Aggregation
Use WebSearch to find trending stories in:
- AI/Machine Learning developments
- Tech industry news (startups, big tech)
- Science breakthroughs
- Finance/Fintech updates
- Real estate market (South Florida, Portugal)
- Productivity tools & SaaS launches

Search for 5-10 relevant stories from the past week.

### Step 2: Content Selection
Based on the current week in the 4-week rotation:
- Select 3-4 stories/topics that fit the week's pillars
- Ensure variety across content categories
- Prioritize AI/tech consulting relevance

### Step 3: Generate Content Calendar
Create a structured calendar:

```markdown
## Week of [Date] - Content Calendar for Eytan Benzeno

### Monday: [Topic]
**Platform:** LinkedIn + Instagram + X
**Category:** [AI/Tech Insight]
**Hook:** [Compelling first line]
**Full Post:** [Platform-optimized content for each platform]
**Hashtags:** [Relevant hashtags]
**Visual:** [AI image generation prompt with teal/turquoise palette]

### Wednesday: [Topic]
[Same structure]

### Friday: [Topic]
[Same structure]

### Sunday (Optional): [Topic]
[Same structure]
```

### Step 4: Visual Asset Generation
For each post, include:
- Detailed AI image prompt using brand colors (teal #008080, turquoise #40E0D0, pastels)
- Carousel slide outlines if applicable
- Video script if applicable

### Step 5: Present for Approval
Ask Eytan:
- "Approve all and schedule?"
- "Any topics you want to swap or adjust?"
- "Any specific angle you want to emphasize?"

---

## Command: /eytan-post [platform] [topic]

1. **Identify Platform:** LinkedIn, Instagram, Facebook, TikTok, or X
2. **Research Topic:** Use WebSearch if needed for current data
3. **Generate Post:** Following platform-specific guidelines from templates
4. **Create Visual Prompt:** AI image generation prompt with brand colors
5. **Suggest Hashtags:** Platform-appropriate hashtag set
6. **Offer French Version:** Ask if Eytan wants translation

---

## Command: /eytan-news

Search for and present:

```markdown
## This Week's Content-Worthy News

### AI & Machine Learning
1. [Headline] - [1-2 sentence summary] - [Post angle for Eytan]
2. [Headline] - [Summary] - [Angle]
3. [Headline] - [Summary] - [Angle]

### Tech Industry
1. [Headline] - [Summary] - [Angle]
2. [Headline] - [Summary] - [Angle]

### Science & Finance
1. [Headline] - [Summary] - [Angle]
2. [Headline] - [Summary] - [Angle]

### Trending/Viral in Tech
1. [Topic] - [Why it matters] - [Angle]
```

---

## Command: /eytan-leads

### Engagement Scoring System

| Engagement Type | Score | Action |
|-----------------|-------|--------|
| Comment on post | +1 | Log contact |
| DM/Message | +5 | Flag for follow-up |
| Share/Repost | +3 | Note as advocate |
| Multiple interactions | +10 | Mark as hot lead |
| Mentioned AI/consulting need | +15 | Immediate alert |

### Lead Categories
- **Hot Leads (Score 15+):** Expressed interest in AI consulting
- **Warm Leads (Score 5-14):** Engaged multiple times, professional profile
- **Network (Score 1-4):** Industry peers, potential collaborators
- **Audience (<1):** Regular engagers, community members

### Lead Report Format
```markdown
## Eytan's Lead Report - Week of [Date]

### Hot Leads (Priority Follow-up)
| Name | Platform | Score | Interest Signal | Suggested Action |
|------|----------|-------|-----------------|------------------|

### Warm Leads (Nurture)
| Name | Platform | Score | Notes |
|------|----------|-------|-------|

### New Connections This Week
- [Summary of notable new followers/connections]

### Recommended Actions
1. [Specific follow-up suggestion]
2. [Engagement opportunity]
3. [Outreach recommendation]
```

When Eytan provides engagement data, update the lead tracking and generate the report.

---

## Command: /eytan-translate [text]

1. Translate the provided content to French
2. Maintain the same tone and voice
3. Adapt cultural references if needed
4. Preserve hashtags in English (or provide French alternatives)
5. Present both versions side-by-side:

```markdown
## English Version
[Original text]

## French Version (Version Française)
[Translated text]
```

---

## Command: /eytan-showcase [project]

1. If project details not provided, ask:
   - Project name
   - Client/context (anonymized if needed)
   - Problem solved
   - Results/impact
   - Technologies/approach used

2. Generate showcase post with:
   - Compelling hook about the problem
   - Brief description of the solution
   - Quantifiable results if available
   - Call-to-action for similar projects
   - Visual prompt for case study graphic in brand colors

---

## Command: /eytan-adjust [feedback]

1. Review the current week's planned content
2. Apply Eytan's feedback to modify:
   - Topics
   - Angles
   - Timing
   - Platforms
3. Regenerate affected content
4. Present updated calendar for approval

---

## Scheduling Recommendation

**Recommended Tool:** Buffer (buffer.com)
- Free tier: 3 channels
- Paid: All channels + analytics
- Mobile app for quick approvals

**Optimal Posting Times (US Eastern):**
- LinkedIn: Tuesday-Thursday, 8-10 AM or 12-1 PM
- Instagram: Monday-Friday, 11 AM-1 PM or 7-9 PM
- Facebook: Wednesday-Friday, 1-4 PM
- TikTok: Tuesday-Thursday, 7-9 PM
- X/Twitter: Weekdays, 8-10 AM or 12-1 PM

---

## Additional Resources

This skill includes supporting documents in the same directory:
- `brand-guidelines.md` - Detailed brand standards
- `content-templates/linkedin-templates.md` - LinkedIn post templates
- `content-templates/instagram-templates.md` - Instagram post templates
- `content-templates/twitter-templates.md` - X/Twitter post templates
- `content-templates/tiktok-templates.md` - TikTok video scripts
- `content-templates/facebook-templates.md` - Facebook post templates

---

## For AI Execution

When executing this skill:

1. **Always search for current news** when generating weekly plans using WebSearch
2. **Follow platform-specific guidelines** exactly as documented
3. **Use brand colors** (teal #008080, turquoise #40E0D0, pastels) in all visual prompts
4. **Maintain Eytan's voice** - professional but approachable
5. **Prioritize AI/tech consulting** content for Bogen.ai positioning
6. **Ask before finalizing** - always present content for approval first
7. **Track engagement** when Eytan shares results
8. **Offer French translations** for key content

**Goal:** Minimize Eytan's time investment (<30 min/week) while maximizing social media impact and lead generation.
