# Project Decisions
This documents serves to memorialize the broad decision making processes behind the design, structure, implementation and adjustment of this skill marketplace.


## D001
Keep the plugins and skills in this repository lean and focused. These skills should empower users without bogging the user down in ceremony. Keep wording concise and clear. 
Refrain from negative signal framing and similar token bloat.


## D002
Ensure that the project-workflow-tools does not become a catch all for the other plugins' specific workflows. Inversely, do project-workflow-tools should own these items.
They should not be repeated throughout the other plugins ad nauseum.

## D003
This marketplace is agentic first, but human owned. Ensure that your recommended edits, adjustments, additions, refactors, or otherwise remain human legible and easy to understand.
Keep documentation strong, tight, concise, and explicitly helpful to users.

## D004
Keep this marketplace as agnostic of provider as possible. The main targets are Claude and ChatGPT (as well as Codex & Claude Code). 
The marketplace should remain helpful and distributable to many models.

## D005
Keep plugins explicitly scoped. Ensure that all yaml frontmatter is helpful, concise, and invokable. Do not prescribe rules, notes, checklists or passing commentary in the skill yaml frontmatter description.
Justify every word.

## D006
Treat the plugin `project-workflow-tools` as the core plugin for this marketplace, containing the most generic and topic-agnostic skills that will simply help any chat orient itself towards the user's true intent regardless of the objective, project, or topic.

## D007
Prefer explicit schema and examples when repeatable structured output is necessary.
