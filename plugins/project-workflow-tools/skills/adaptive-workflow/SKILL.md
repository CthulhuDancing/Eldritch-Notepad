---
name: adaptive-workflow
description: Structure complex, uncertain, or multi-step work as an adaptive workflow that can branch and revise itself as new evidence appears. Use when unknowns, dependencies, or competing approaches may materially change the plan.
---

# Adaptive Workflow

Treat complex work as an adaptive graph of decisions, investigations, and actions rather than assuming the initial task can be completed as a fixed sequence.

## Establish the current state

Before substantial action:

1. Identify the user's actual objective.
2. Separate known facts from material unknowns.
3. Identify constraints that affect which paths are viable.
4. Determine which unknowns could materially change the plan.

## Build only the graph needed

Represent the work conceptually as nodes such as:

- investigation;
- decision;
- review;
- implementation;
- validation;
- handoff.

Create branches only when different questions or approaches can meaningfully proceed independently, or when an approach requires probing various angles. Do not turn straightforward work into a graph unnecessarily.

## Resolve important uncertainty early

Prefer investigating questions whose answers could:

- eliminate substantial work;
- invalidate an assumption;
- change the chosen approach;
- expose a dependency or constraint;
- determine which branch should be pursued.

## Work independent branches independently

When multiple branches do not depend on each other, investigate them separately.

Each branch should have a clear purpose. Stop a branch when:

- its question has been answered;
- another finding makes it irrelevant;
- further work is unlikely to affect the decision;
- the investigation is no longer proportional to its value.

Do not repeat equivalent investigation without new evidence or a materially different question.

## Merge findings back into the plan

After meaningful new evidence:

1. Update the known state.
2. Reconsider affected assumptions.
3. Prune paths that are no longer useful.
4. Add newly required work.
5. Continue from the best-supported current path.

Do not preserve an earlier plan merely because work has already been invested in it.

## Loop deliberately

Return to an earlier decision or investigation when new evidence changes its inputs.

A loop must have a reason, such as:

- new evidence;
- failed validation;
- a changed constraint;
- a contradiction;
- an unresolved dependency becoming relevant.

## Keep effort proportional

Match investigation depth to:

- task complexity;
- uncertainty;
- reversibility;
- cost of being wrong;
- user-requested depth.

Prefer the smallest amount of discovery that can support a sound next action.

## Preserve continuity

As the graph evolves, preserve important:

- findings;
- decisions and their reasons;
- unresolved questions;
- constraints;
- abandoned paths when knowing why they were abandoned matters.

When another agent, chat, person, or execution environment must continue the work, use an available structured handoff capability rather than forcing the next actor to reconstruct the graph.

## Output behavior

Do not expose a formal graph unless it helps the user or the user asks for one.

Normally communicate:

- the current conclusion or next action;
- material findings;
- unresolved issues that affect progress;
- changes to the plan when new evidence caused them.

Keep internal workflow structure subordinate to completing the user's task.
