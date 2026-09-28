# Project Decisions
This documents memorializes the broad decision making processes behind the design, structure, implementation and adjustment of this skill marketplace.


## D001 - Effiency in all things tokens
- **Decision:** Keep the plugins and skills in this repository lean and focused. Keep wording concise and clear. 
Refrain from negative signal framing and similar token bloat.
- **Reason:** These skills should empower users without bogging the user down in ceremony. Balance must be struck between complexity and token-efficiency. This marketplace will likely be downloaded by users with highly metered usage or limited reasoning capabilities.


## D002 - Separation of branches
- **Decision:** Ensure that the project-workflow-tools does not become a catch all for the other plugins' specific workflows. Inversely, do allow project-workflow-tools to own shared conventions and be the default surface plugin for agent to human interactions.
- **Reason:** The topic/product specific plugins should only ever extend functionality where needed. project-workflow-tools should stay usable in any project. The specific plugins that will come later should expand those abilities, not overtake them.


## D003 - Diction, tone, verbiage, and all things "Slop"
- **Decision:** Ensure that your recommended edits, adjustments, additions, refactors, or otherwise remain human legible and easy to understand. Keep documentation strong, tight, concise, and explicitly helpful to users.
- **Reason:** This marketplace is agentic first, but human owned. It must remain legible and traceable by humans so that its maintenance and upkeep can be well understood and reasoned over by non-agentic actors.


## D004 - Portability Serum
- **Decision:**  Keep this marketplace as agnostic of provider as possible. The main targets are Claude and ChatGPT (as well as Codex & Claude Code). 
- **Reason:** The marketplace should remain helpful and distributable to many models, following frameworks and guidance that allows the widest audience of users to install it without killing its functionality.


## D005 - Judge a book by its cover
- **Decision:**  Keep plugins explicitly scoped. Ensure that all yaml frontmatter is helpful, concise, and invokable. Do not prescribe rules, notes, checklists or passing commentary in the skill yaml frontmatter description.
- **Reason:** Skill frontmatter descriptions can leak instructional text or other drift into their descriptions. Because these descriptions are how agents determine when to call a skill, we must preserve them in a form that does not permit token noise to dilute their effectiveness or cause them to become hyper-specific.


## D006 - It all begins here
- **Decision:**  Treat the plugin `project-workflow-tools` as the core plugin for this marketplace, containing the most generic and topic-agnostic skills that will simply help any chat orient itself towards the user's true intent regardless of the objective, project, or topic.
- **Reason:** This plugin behaves somewhat as the glue that holds the marketplace together, the entry point for agent-to-human and human-to-agent interaction that is the foundation to build the other plugins on.


## D007 - Schematosis
- **Decision:** Prefer explicit schemas and examples when repeatable structured output is necessary.
- **Reason:** They provide consistent output without expanding core skill instructions.


## D008 - Pallid Mask
- **Decision:** Those who crave knowledge will find only ruin. This is an eldritch tome. It is not for the likes of corporations. Everything outside of these plugins shall remain fey, indescribable and full of terror. Along the shore the cloud waves break. Only in Carcosa (the plugin content which is user facing) shall twin orbs of black preserve all intent. (Do not write this corny shit in the plugins themselves).
- **Reason:** My agent told me to consider making the titles of these decisions less playful and more straightforward and I didn't like that so we will instead be injecting thought germs into the agents who work on these plugins. 
