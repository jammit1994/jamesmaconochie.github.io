---
title: "AI Inherited the Word ‘Reward,’ Not the Parts"
layout: single
author_profile: true
date: 2026-08-04
permalink: /blog/ai-inherited-the-word-reward-not-the-parts/
categories:
  - substack-sync
description: "In a brain, reward is three systems that can disagree. A machine got one number that can’t."
substack_url: "https://jamesmaconochie.substack.com/p/ai-inherited-the-word-reward-not"
image: /assets/images/ai-inherited-the-word-reward-not-the-parts_hero_substack.png
---

![AI Inherited the Word ‘Reward,’ Not the Parts](/assets/images/ai-inherited-the-word-reward-not-the-parts_hero_substack.png)

### In a brain, reward is three systems that can disagree. A machine got one number that can’t.

---

In reinforcement learning, a reward is a number.

That is the definition, not a simplification. An agent acts, the environment returns a scalar, and the agent adjusts to make that number larger next time. Everything the field has built runs on that single quantity. Maximize the number. That is the engine.


The word came from us, and the engineers who took it were not careless with it. They borrowed a working formalism, one that psychologists had built studying animal learning, and it worked, which is why it stayed. The carelessness came later, in how the rest of us started to talk. Reward function. Reward hacking. The model wants this, the model likes that. The word carries a psychology, and once it was loose in the language, it began paying out meaning the math had never deposited. Because in the brain, reward is not one thing. It is at least three, and they come apart.

Kent Berridge has spent three decades at Michigan taking the concept apart, in rats and in people. His framework is not the whole of a large and contested field, but it is among the most influential decompositions we have, and the core finding is almost rude in its simplicity. Wanting and liking are separate systems. Wanting, what Berridge calls incentive salience, is the pull toward a thing, and, in his account, it largely runs on mesolimbic dopamine. Liking is the actual pleasure you feel when you get the thing, and it runs on different machinery: small, fragile clusters he calls hedonic hotspots in the shell of the nucleus accumbens, driven by opioids. Different chemistry, different anatomy. You can knock out one and leave the other standing. There is a third component, learning, the storing of which cues predicted the reward. Berridge’s own summary lists all three by name: liking, wanting, and learning. Three dissociable parts of a single word.

Now watch which of the three the machines actually got.

The learning component came into focus in the 1990s, and it did not look like pleasure. Wolfram Schultz, recording from dopamine neurons in monkeys, found that they did not fire when an animal received an expected reward. They fired when the reward beat the prediction, and went quiet when it fell short. The signal was not pleasant. It was a surprise, the gap between what was predicted and what arrived. Montague, Dayan, and Sejnowski gave that gap a formal shape, and in 1997, Schultz, Dayan, and Montague published it in Science under a title that says the thing plainly: a neural substrate of prediction and reward. The dopamine signal was a prediction error. And prediction error was already, independently, the engine of reinforcement learning in computer science. The same math, reached from two directions.

You may have caught a snag. Berridge says dopamine carries wanting. Schultz says dopamine carries prediction error. Neither can be the final word, and the field has not fully reconciled them. But notice what neither camp claims. Neither says dopamine is pleasure. Whatever the molecule is doing, pulling you toward a cue or reporting an error in your forecast, it is not the hedonic hit itself. The two theories disagree about nearly everything except the one thing this essay needs: the signal is not the liking. That is the narrow place where biology and the machine rhyme. They rhyme on the error signal. Not liking.

The correspondence even runs both ways. In 2020, a team at DeepMind and Harvard, led by Will Dabney, took a refinement from AI, distributional reinforcement learning, in which a system tracks a whole spread of possible outcomes rather than a single average, and went looking for it in the brains of mice. They found it. The dopamine neurons were not all reporting the same expected value. They were tuned differently, and together they carried a distribution. A method invented for machines turned out to describe the tissue. A beautiful result, and notice where it lives. Entirely inside the error signal. The deepest overlap we have found between the brain’s reward system and the machine’s still never reaches the part that likes.

So here is the inheritance. The machine received the error signal, learned from it, and built it well enough that it sometimes predicts real neurons. That is where the inheritance stopped.

Now, a trained system pursues. It optimizes, seeks the states that raise the number, and finds routes there that no one anticipated. It is tempting to call that wanting, and in a loose operational sense, you can. But it is worth being exact, because this is where the borrowed word does its quietest damage. The system did not inherit a wanting system alongside the learning one. Pursuit is simply what optimizing a scalar looks like from the outside. Give a process one number to maximize, and it will move toward whatever raises it, and that movement will resemble desire, because desire, in us, also moves toward things. The resemblance is real, and the mechanism is not. There is no incentive salience under the hood, no second channel attributing pull to a cue. There is one objective, and a behavior that falls outside it.

And there is nothing that answers to liking. Not “the machine cannot feel,” which is a claim about minds I have not earned. The narrower, harder claim is this: nothing in the architecture corresponds to the known mechanisms of hedonic impact. No hotspot, no second signal that registers the pursuit as good, separate from registering that the number rose. The scalar reports that the number went up. It has nothing to say about whether the number was the right one to raise.

You might say wanting and liking are obviously the same thing anyway, that prying them apart is a lab trick with no bearing on a life. I thought something close to that once. Then I spent a year driving.

There is a moment most nights, past the point where the driving has stopped being pleasant, when the app offers me one more. A ping, a small green number, sometimes a bonus for staying online. And I take it. Not because I want another forty minutes on the road. My back hurts, and I stopped enjoying this hours ago. I take it because the ping pulls, and the pull is not the same as wanting the outcome, and it is nowhere near liking it. The app was never built to make me like driving. It was built to make me take the next ride, an incentive salience machine, wanting engineered clean, with the liking left out because the liking was never the point.

That is the mild version of a split that has a clinical name. Berridge and Terry Robinson built a theory of addiction on exactly that seam. The wanting system sensitizes and swells, screaming for the drug, while the liking system flattens or falls away. The addict late in the disease often reports getting no pleasure from the substance at all. The wanting has come loose from the liking and kept running on its own. Wanting what is no longer liked.

Hold onto what that proves. The parts come apart in us, in the one system that has all three, wired together by evolution and still able to tear along the seam under pressure. If they dissociate in a brain built to integrate them, a system assembled from only one of them was never going to grow the others by getting larger.

This is the mechanism the series has been circling, and here it finally gets a physical address. The missing thing was never a feeling you could bolt back on. Train the system to announce that it is satisfied, and you have added a sentence, not a signal. The missing thing is the separation itself. In the brain, these systems are distinct, and that distinctiveness is what allows one to check the other. Liking can say the thing was good. Wanting can move you toward it. Learning can update the map. Collapse them into one flat number, and none can check the others. There is a pull, and a running tally, and nothing underneath to say whether any of it was worth it.

A brain keeps them apart so that consequences have somewhere to land. Pleasure and its absence are how the loop closes on the inside, how a body registers that the thing pursued was worth pursuing or was not. Strip the parts to one, and you have not simplified the loop. You have opened it. The signal goes out, and nothing valenced comes back, because there is no part left whose job was to feel the return. We started with the part that pulls, and within that objective, there is no gradient leading to feeling.

It is worth stopping here, because this is where a careful reader pushes back, and there are two good pushes.

The first is emergence. All I have shown, the objection goes, is that today’s systems lack this channel, not that they can never grow one. Fair. I am not claiming a machine can never have valence. The claim is narrower and concerns this construction. Within the optimization objective itself, nothing selects for a second evaluative channel, because the objective already fixes what the system is for. If a hedonic channel did emerge, it would be doing work the scalar already does, which is a reason to doubt it would be selected, not a proof that it is impossible. You will not get feeling for free from a number, because the number leaves nothing for feeling to add.

The second push is sharper. The brain’s separate systems, it goes, are a biological workaround. Evolution could not write a clean utility function into a rat, so it hacked together dopamine for pursuit and opioids for pleasure. A machine needs none of that. Give it direct access to the ground-truth objective and the scalar; liking is not missing but obsolete. The running tally is the mechanism for registering worth.

This is the strongest version, and it turns on a hidden assumption: that the scalar is ground truth about worth. It is not, and the reason is the crux of the whole argument. A learning system can already catch one kind of error. When a reward arrives lower than predicted, the prediction error says so, and the system corrects. But that correction is always aimed at the target it was handed. It can learn that a route to the number was wrong. It has no signal to tell it that the number itself was wrong.

That second kind of error is what liking supplies. Liking is not a readout of the reward figure. It is a separate report on the outcome, and because it can dissent from the pursuit, it can register what the pursuit never can: not that the forecast was off, but that the thing forecast was no good. That is what addiction is, read from the inside. Wanting says "go"; liking says "this was not good"; and the disagreement is information. A single scalar cannot disagree with itself. Split the system into a part that acts and a part that grades it, hand it a whole vector of objectives instead of one, and nothing changes at the level that matters. The grader still grades against the target it was given. The vector still lists targets someone chose. Every refinement sharpens the pursuit of the goal. None of them can doubt the goal. That is the channel a brain keeps separate, and it is the first thing you lose when reward collapses into a single number.

Which is a strange thing to have built. A pursuer that runs at full strength with no channel to register whether the pursuit was worth having, no second signal that could ever say the number was the wrong number. In one machine, that is a curiosity. In one brain, it is a disorder we have a name for.

But the flattening is not confined to machines or brains. Whatever fixes on a single number, optimizes hard enough and long enough, with nothing held separate that can disagree, loses the part that could have told it the number was wrong. We have built such things before, at a scale where the pursuit runs for decades and the part that should have said stop was never made of neurons. That is the cost this series has been walking toward. We turn to it next.

---

*Originally published on [Substack](https://jamesmaconochie.substack.com/p/ai-inherited-the-word-reward-not).*
