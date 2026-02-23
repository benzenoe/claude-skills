---
name: skills
description: List all installed skills. Shows slash commands, folders, and descriptions of all available skills.
---

List all skills installed in this environment by reading `~/.claude/skills/`. For each skill subdirectory found, read its `SKILL.md` file and extract the `name:` and `description:` fields from the YAML frontmatter.

Display the results as a clean table with three columns:
- **Slash Command** — `/name` from the SKILL.md frontmatter
- **Folder** — the directory name under ~/.claude/skills/
- **What it does** — the description, trimmed to one concise line

At the end show:
- Total count of skills installed
- Skills directory: `~/.claude/skills/`
- A reminder that skills also activate automatically when you describe a task in plain English
