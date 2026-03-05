---
title: "More Instruments, Same Tune"
layout: single
author_profile: true
date: 2026-02-24
permalink: /blog/more-instruments-same-tune/
categories:
  - substack-sync
description: "The dominant AI narrative is seductively simple: scale is all you need. More data, more compute, more parameters, and intelligence emerges. It’s the story that’s justified hundreds of billions in investment, reshuffled the power structure of Silicon Valley, and convinced a generation of executive..."
substack_url: "https://jamesmaconochie.substack.com/p/more-instruments-same-tune"
image: /assets/images/more-instruments-same-tune_hero_substack.png
---

![More Instruments, Same Tune](/assets/images/more-instruments-same-tune_hero_substack.png)

### The Growing Case Against Scaling

---

*This is the first in a three-part series examining the cracks in the AI scaling narrative, from the technical limits, to the financial fragility, to who bears the cost when the correction comes.*

The dominant AI narrative is seductively simple: scale is all you need. More data, more compute, more parameters, and intelligence emerges. It’s the story that’s justified hundreds of billions in investment, reshuffled the power structure of Silicon Valley, and convinced a generation of executives that AGI is just a few training runs away.


But a growing chorus of serious people disagree. Not AI skeptics or Luddites, but pioneers, Turing Award winners, people who built the foundations of what we’re now scaling. Their critiques are converging on an important point. And what they’re circling around might matter more than any of them are quite saying.

### Yann LeCun: World Models, Not Word Models

LeCun, a Turing Award laureate and former chief AI scientist at Meta, left in November 2025 to start AMI Labs, valued at $3.5 billion. His thesis: LLMs are “an off-ramp on the road to human-level AI.”

His argument is architectural. LLMs predict text; they model language, not reality. They can pass the bar exam while lacking the common sense of a house cat. They hallucinate because they have no grounding in how the world actually works.

What’s needed, LeCun argues, are “world models”: systems that build internal representations of reality, that can simulate, predict, and plan. Not language models but cognitive models. His advice to PhD students:

> “LLMs are useful, but they are an off-ramp on the road to human-level AI. If you are a PhD student, don’t work on LLMs.”

### Gary Marcus: Pattern-Matching Is Not Reasoning

Marcus, a cognitive scientist, NYU professor emeritus, and author of *Taming Silicon Valley*, has been the most persistent public critic of the scaling hypothesis. He’s also been the most vindicated.

His core claim: LLMs are sophisticated pattern-matchers, not reasoners. They interpolate within their training distribution but fail outside it. Change a classic reasoning problem slightly, reword it, alter the setup, and performance collapses. This isn’t a bug to be fixed with more data. It’s architectural.

Hallucinations, in Marcus’s view, are unfixable within the current paradigm. And the stakes are real: in medicine, law, and finance, even a 1% hallucination rate can be catastrophic. Systems that traffic only in the statistics of language, without explicit representations of facts or tools to reason over them, will never be reliable. The solution isn’t more scale; it’s hybrid architectures that combine neural networks with symbolic reasoning. The kind of thing AI abandoned decades ago in the rush toward end-to-end learning.

### Rodney Brooks: The Competence Projection Problem

Brooks, an MIT roboticist, founder of iRobot and Robust.ai, and builder of more humanoid robots than perhaps anyone alive, brings the engineer’s skepticism.

His critique is partly about us, not just the technology. When humans see an AI perform a task impressively, we instinctively generalize. We project a sphere of competence around that performance, assuming the system understands in a human-like way. We’re almost always wrong.

LLMs are useful, Brooks says, but narrow. The problem with robotics isn’t language interfaces; it’s control theory, optimization, the hard math of operating in physical reality. Language won’t help you ship 10,000 warehouse orders in two hours; data processing and planning will.

His broader point: 76% of AI researchers surveyed by the AAAI agree that scaling current approaches alone won’t yield AGI (AAAI 2025 Presidential Panel). The insiders know. The narrative hasn’t caught up.

### François Chollet: Fluid Intelligence and the ARC Test

Chollet, creator of Keras and now running the ARC Prize Foundation, offers the most precise diagnosis.

He distinguishes between crystallized intelligence (accumulated knowledge, memorized patterns) and fluid intelligence (the ability to adapt to genuinely novel problems). LLMs excel at the former. They’re vast repositories of crystallized knowledge, able to retrieve and recombine what they’ve seen. But fluid intelligence, the thing that lets a child solve a puzzle they’ve never encountered, is largely absent. As Chollet puts it:

> “Memorization is useful, but intelligence is something else.”

His ARC benchmark tests exactly this: abstract reasoning tasks are trivial for humans, but brutal for LLMs. GPT-4o scores around 5%. Humans score 84%. The gap isn’t closing with scale.

Chollet’s prescription: program synthesis. Systems that can construct new cognitive programs on the fly, recombining primitives to handle novel situations. “Memorize, fetch, apply” won’t get us there. We need systems that can genuinely invent.

### Where They Converge

These critics come from different traditions (cognitive science, robotics, deep learning research), but their diagnoses are converging:

* **Brute-force pre-training scaling is hitting diminishing returns.** The spectacular gains of 2020–2023 have flattened. Each new model is marginally better at an enormous cost.
* **Current benchmarks mask fundamental limitations.** High scores on contaminated tests don’t equal general intelligence.
* **World models and grounding are essential.** Systems need to represent reality, not just language about reality.
* **Architectural innovation is required.** More of the same won’t work. Something structurally different is needed.

There’s also an uncomfortable economic dimension here. The scaling narrative isn’t just a technical hypothesis; it’s the justification for hundreds of billions in concentrated infrastructure investment. When the thesis and the money are this entangled, technical course corrections become financially painful. That structural fragility is worth examining on its own terms, and it’s where I’m headed next week.

### Where They Diverge

The agreement ends at prescription. LeCun wants embodied world models trained on sensory experience. Marcus wants symbolic-neural hybrids that can reason explicitly. Brooks wants constrained domains with realistic expectations. Chollet wants program synthesis and test-time adaptation.

These aren’t necessarily incompatible; they might all be part of whatever comes next. But there’s no unified alternative vision yet, just a shared sense that the current path is incomplete.

### What They’re Not Quite Saying

Here’s what strikes me: the skeptics are all still focused on building artificial general intelligence. Better AI. Smarter machines. Systems that can eventually match or exceed human cognition.

But what if the frame itself is wrong?

What if the goal isn’t to replace human intelligence but to augment it? Not AGI but AHI: Augmented Human Intelligence. If LeCun is right that LLMs lack world models, and Chollet is right that they lack fluid intelligence, then their best use isn’t to replace the human driver but to serve as a high-powered navigation system. Modular AI architectures are designed to amplify human capability rather than substitute for it. Systems that handle what they’re good at (retrieval, pattern recognition, tireless execution) while humans handle what we’re good at (judgment, meaning-making, genuine novelty).

The scaling skeptics have correctly diagnosed the disease: current approaches won’t yield general intelligence. But they’re still chasing the same endpoint. The alternative I’ve been exploring in this series is different: not smarter machines, but smarter human-machine partnerships. Architectures inspired by how the brain actually works: modular, specialized, integrated through attention rather than unified in a single massive model. [Link to earlier AHI posts]

This doesn’t mean AHI is without its own hard questions. Who gets augmented? Who controls the tools? Any architecture that amplifies human capability will amplify it unevenly unless we’re deliberate about access and governance. But those are design problems, solvable ones, not the fundamental architectural dead-end that monolithic scaling represents.

This is precisely the kind of architectural shift the critics call for. Their critiques of monolithic scaling point directly toward modular, human-centered design. The pieces are all there. They just haven’t been assembled this way.

The scaling-is-everything narrative is cracking. What comes next is genuinely open. That’s worth paying attention to, and, for those of us thinking about it, worth shaping.

---

*Next week: If the scaling thesis is cracking, what happens to the hundreds of billions riding on it? In “When the Music Stops,” I examine the structural fragility of the AI boom, from concentrated market bets and ballooning infrastructure debt to the gap between demo magic and enterprise reality. The technology is real. The question is whether the valuations are.*

---

*Originally published on [Substack](https://jamesmaconochie.substack.com/p/more-instruments-same-tune).*
