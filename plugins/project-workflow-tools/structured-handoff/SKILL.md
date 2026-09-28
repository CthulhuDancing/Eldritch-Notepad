---
name: structured-handoff
description: Produce a concise, structured handoff that preserves the context needed for another chat, agent, person, or execution environment to continue the work. Use when work is being transferred, paused, delegated, or resumed elsewhere.
---

# Structured Handoff

Produce a handoff using `references/Output-Schema.md`.

Use `references/Example-Handoff.md` as the style and level-of-detail reference.

Preserve only the context needed for another actor to continue the work. Keep the handoff concise and proportional to the work completed.

## Content Selection

Include, where relevant:

- the objective;
- current status and completed work;
- key findings;
- decisions and constraints;
- open questions;
- risks and blockers;
- next actions;
- relevant references and sources.

Do not invent missing context. Omit sections or subsections that have no meaningful content rather than filling them with placeholders.
Prefer concrete facts, decisions, and next actions over narrative history.
- Distinguish completed work, findings, decisions, constraints, open questions, risks, and blockers by their actual role in the work.
- Use summaries only when they add synthesis beyond the surrounding bullets.
- Make next actions specific enough that another actor can continue without reconstructing prior intent.

## Prose Guidelines
- Avoid negative framing, prohibition echoing, instruction mirroring, contrastive padding, and redundant negation.
- Write for continuation, not narration. Preserve what the next actor needs to proceed.
- Keep prose paragraphs short, usually 1–3 sentences.
- Keep lists focused; prefer roughly 3–7 items unless the work genuinely requires more.
- Avoid unnecessary adjectives, intensifiers, metaphors, filler, and repetitive framing.
- Avoid jargon when plain language communicates the same meaning. Preserve technical terms when they carry necessary precision.
- Do not restate the same information in both prose and bullets unless the prose adds meaningful synthesis.
- Omit irrelevant detail, conversational noise, and reasoning that does not affect continuation.

## Section Guidance

#### Objective
Directly state the intended outcome or problem being carried forward. Keep it focused and concise, no more than a single paragraph.

#### Status & Progress
Use Status for the current state of the work or objective. Use Progress for completed work and settled decisions, summarized in the fewest items that still preserve meaning.

#### Key Findings
Capture material discoveries or conclusions. Use the summary to synthesize relationships or implications across the findings, not to restate them.

#### Decisions & Constraints
Record Decisions as choices already made and Constraints as facts or boundaries the work must operate within.

#### Risks & Blockers
Treat Blockers as conditions preventing progress and Risks as potential future problems. Do not elevate risks to blockers unless they materially prevent further work.

#### Next Actions
Describe the most useful continuation path clearly enough that another actor can proceed without reconstructing prior intent.

### References & Sources
Keep this section compact. Use **Sources** for evidence used in the work and **References** for documentation, systems, files, or other resources that may help continue it.
