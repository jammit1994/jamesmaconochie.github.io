---
title: "Who Is Left Holding The Napkin"
layout: single
author_profile: true
date: 2026-09-15
permalink: /blog/who-is-left-holding-the-napkin/
categories:
  - substack-sync
description: "I have told this story before. Six weeks ago I told it to make a point about software. I want to tell it again to make a point about myself, because I think I put the emphasis in the wrong place."
substack_url: "https://jamesmaconochie.substack.com/p/who-is-left-holding-the-napkin"
image: /assets/images/who-is-left-holding-the-napkin_hero_substack.png
---

![Who Is Left Holding The Napkin](/assets/images/who-is-left-holding-the-napkin_hero_substack.png)

### AI has made producing judgements cheap. It has not made checking them cheap.

---

I have told this story before. Six weeks ago I told it to make a point about software. I want to tell it again to make a point about myself, because I think I put the emphasis in the wrong place.

In 1993, I was a final-year civil engineering student at Imperial College, and my design project was an exhibition hall with a column-free interior and a long-span roof carried on a pair of massive tubular arch beams. I modeled it in I-DEAS, a finite element package running on a Silicon Graphics workstation that took up half a desk. The package computed the stresses, checked them against code, and rendered a deformed shape that looked entirely reasonable. It said the structure would stand.


The night before the report was due, for reasons I still cannot reconstruct, I did a hand calculation of the stress at one of the arch supports.

It came back off by a factor of ten.

I had entered the loads in kilograms, but the package read them as newtons. My model was carrying about a tenth of what the real building would have to carry. When I corrected the units and re-ran it, the deformed shape came back flat as a pancake. The structure I had designed would not have stood up.

Last time, I said the software never pushed back; the analysis was fluent all the way down. The correction had to come from outside it. That is true, and it is the smaller half of the story.

The larger half is the napkin.

I had a way to check. It was crude; it took three minutes, and it was decisive. And I had it for a reason that had nothing to do with being careful. I had been taught to size a beam by hand before I was ever allowed near a package that would size it for me. The check wasn’t diligence. It was residue.

### The Word We Only Half Unpacked

Five weeks ago I wrote about the word *reward*, and what happened to it when AI borrowed it from neuroscience.

In the brain, reward is not one thing. Kent Berridge’s work separates it into two systems that can be pulled apart experimentally. **Wanting** is driven by mesolimbic dopamine; it makes you pursue the thing. **Liking** is a distinct hedonic system running on different neural substrates, and it registers how the thing actually landed. Disable one and the other carries on without it. An animal can be made to want, intensely, something it does not like at all.

Machine learning borrowed the word and built the pursuit.

I want to state this more carefully than I did last time, because it is easy to overclaim. Reinforcement learning gives a system an explicit optimization signal and a great deal of patience in following it. What it does not supply, by itself, is anything corresponding to the second system, an independent register of how the result actually landed, sitting outside the objective and capable of disagreeing with it. There are constraints, regularizers, safety layers, human feedback, evaluators. What’s missing is something that stands apart from the optimization and asks whether the objective was the right one.

Drive without a brake, with the caveat that this is a metaphor, and a metaphor is not a schematic. The precise version is duller and harder to knock down: a system optimized to produce an answer is not thereby equipped to establish that the objective, or its reading of the objective, was correct.

I left it there, as a fact about how these systems are built. It is a fact about how they are built.

But nothing is dangerous all by itself. An uncovered hole in the ground is not dangerous sitting in an empty field. It becomes dangerous when someone walks near it. The question I skipped last time is who is walking near this one, and how close.

### Condition Is Not Risk

Engineers separate two things that ordinary language runs together.

Years after the exhibition hall, I spent part of my career in transportation consulting. One project, with colleagues at Cambridge Systematics and Lloyd's Register, built a risk model for the bridges on the US highway system. Every state reports the condition of its bridges to a national inventory, and we used that data to place each structure on a five-by-five grid.

One axis was condition: how structurally sound the bridge actually is. The other was consequence: what happens if it fails, largely how much traffic crosses it, adjusted for how far the detour would be if it closed.

Those two axes aren't the same thing, and keeping them apart is the point. A badly deteriorated bridge on a farm track is in poor condition and carries almost no consequence. A sound bridge carrying a hundred thousand vehicles a day is in fine condition and carries enormous consequence. Neither is where you look first. You look at the corner where both are bad at once: a deteriorating structure carrying heavy traffic with no easy detour. Risk is what you get when condition and consequence coincide.

The structure's condition is a fact about the structure. It is true whether anyone drives across it or not. The risk exists only because people do.

That is the distinction I skipped past five weeks ago. An optimizer without an independent evaluator is a fact about how the thing is built. It is a condition. It is true of the system sitting on its own, doing nothing at all.

What turns a condition into a risk is traffic.

## Two Ways To Hand Something Over

So: who is driving over this bridge, and how heavily?

Not “who uses AI.” Everyone does, and that tells you nothing. The question is narrower. What happens to your own ability to check the answer?

Handing work to something else is not one thing. It comes in two forms that look identical from outside and behave very differently when something goes wrong.

The first is **delegation**. You give away the task and keep the ability to judge what comes back. A managing editor does not write the article, but can read it and say it isn’t working. I gave the stress calculations to I-DEAS and kept, without ever thinking about it, a way to test the answer. The work moved. The judgment stayed.

The second is **offloading**. You give away the task, and the ability to judge the result goes with it. What comes back is a conclusion, arriving without the reasoning that produced it, and there is nothing left on your side that can weigh it. You can accept it or refuse it on instinct. You cannot check it.

From outside, these look the same. A person asks, a system answers, the person proceeds. The difference is invisible until the answer is wrong.

The obvious objection is that delegation is just offloading on a longer timescale, that if you never do the work yourself, the ability to judge it must eventually go.

That objection is correct, and it is the most important thing in this essay. Delegation is not a stable condition. It decays into offloading unless something actively holds it in place. This raises the question of what could hold it there, and whether anything does.

### Bainbridge, 1983

The obvious answer is that this is a matter of discipline. Keep your hand in. Check the work.

Lisanne Bainbridge answered that in 1983, in a paper on industrial process control written long before any of this existed.

Her observation came to be called the ironies of automation. When you automate a process, you leave a human to monitor it and take over if it fails. But monitoring something that runs smoothly is exactly the condition under which manual skill decays. The operator does less, for longer, and the ability to intervene erodes quietly while nothing appears to be wrong.

Then the automation fails, which is the moment it needs a person, and the person it gets is the one whose skills have been eroding for years, worn down by the very smoothness that made everything look fine.

The skill you need at the moment of failure is precisely the skill that the absence of failure has been taking away.

So the decay isn't hypothetical, and vigilance isn't the answer. Which leaves the question of what is.

### What The Napkin Actually Was

Here is where I have to be careful, because the obvious reading of my own story is wrong.

The obvious reading is: hold on to the old skill. Learn to do it by hand so you can always do it by hand. And that cannot be the lesson, because it does not survive contact with how anything works. I cannot fabricate a semiconductor, sequence a genome, or derive the cryptography my bank runs on. I use all three every day, and I should. If the answer to automation were personally retaining the underlying method, the answer would be useless.

Look again at what I actually had that night.

It was not the ability to reproduce what I-DEAS did. The package solved a system of equations across thousands of elements. I could not have done that by hand in a month, and nothing in my training suggested I should try. What I had was cruder and far more valuable: a way to arrive at an approximate answer by a route that did not pass through the package.

That is the whole thing. Not reproduction — **verification by an independent route.**

Which gives the test:

**Is there a way to check the output that does not run through the thing that produced it?**

Sometimes that route is retained expertise, as mine was. But it can be many other things. An empirical test the world adjudicates. A formal constraint the output must satisfy. A second system built on genuinely different principles rather than a near-copy of the first. An audit trail that lets someone reconstruct how a conclusion was reached. A deliberately adversarial process staffed by people whose interests differ.

The napkin is one instance of the category. It is not the category.

And that changes what is at stake. The scarce resource is not craftsmanship, and this is not an argument about the dignity of doing things by hand. What is scarce is independent routes, and unlike a bridge, a route can disappear without anyone noticing.

There is a collective version of this, and it is worse.

My napkin worked because it was a *different method*. Different assumptions, a different path to the answer, and this is the part that matters: different ways of being wrong. Independence is not a property of having a second opinion. It is a property of the second opinion failing differently from the first.

Which means a field can hold on to checking as a habit and still lose it as a safeguard. If everyone verifies with the same tools, calibrated against the same standards, trained on the same material, then a thousand checks are one check performed a thousand times. The errors line up. And nobody notices, because everybody is still checking.

### A Case Where The Route Has Already Closed

That risks staying abstract, so here is a live one.

A student submits an essay. A detector reports that it was machine-written. The student is now the subject of a judgment with real consequences: a failed assignment, an academic misconduct process, occasionally the end of a degree.

What check is available?

The student can deny it, which is an assertion, not evidence. Or the work can be run through a second detector: a system of the same class, trained on broadly the same signals, sharing the same blind spots and making correlated errors. That is not an independent route. That is the first opinion in a different font.

Sam Illingworth reached the image before I did, writing about Substack’s own detector: an AI adjudicating whether text is AI. A turtle standing on a turtle.

Look at where this sits on the grid. The condition is the familiar one, a system producing a confident verdict with nothing in it that stands outside the verdict and disagrees. The consequence is high and lands on a particular person. And the independent route is not merely weak; for the accused student it is very nearly absent, because every available check fails in the same direction as the accusation.

Then the third thing, which is the worst of it. Nobody assembles the failures. A wrongly accused student who cannot prove a negative mostly disappears from the record; the case is dropped, or it isn’t, and either way it does not become a data point. There is no inquiry, no docket, no count. The bridge falls down, and nobody hears it.

This is not a warning about something that might happen. It is running now, at scale, in institutions that adopted it faster than they built any way to evaluate it.

### Where The Traffic Is Heaviest

Now scale this up, carefully, because the obvious version of this argument is wrong.

Every generation loses skills to its tools. My grandfather could do long division faster than I ever could. Nobody navigates by the stars. Slide rules are museum pieces. Those losses were real, and almost none of them mattered.

So the claim cannot be that skills are being lost. Skills are always being lost. The claim has to be narrower: what matters is whether an independent route survives the loss.

When calculators replaced slide rules, one usually did. Order-of-magnitude estimation is cheap, teachable, and doesn't run through the calculator, which is why someone who kept it can still catch a wrong answer. Not everyone did, and that is precisely the point: the route existed, and its survival depended on whether anyone bothered to maintain it. What did not happen is the route becoming unavailable in principle.

That is the real question about any tool. Not what it does for you, but what it leaves you.

Now take the work where the output is a judgment rather than a quantity. Whether this candidate should be hired. Whether these symptoms fit together. Whether this clause creates an exposure. Whether this strategy is sound.

It would be too strong to say these fields have no external check. Medicine has pathology, imaging, and outcomes. Law has evidence, precedent, and procedure. Hiring has job performance. Strategy has results. What they lack is my beam, a check that is fast, cheap, and mechanically decisive. Their checks are slow, noisy, expensive, contestable, and often arrive years after the decision they would have corrected. Structural engineering sits at one end of that spectrum, with physics as an unusually brutal validator. These fields sit at the other.

A reader will say: those fields never had a napkin, so nothing is being lost there. You have diagnosed a problem in engineering and applied it by analogy to places it does not belong.

That is right, and it is the more uncomfortable version of the argument. They were always at the far end of the spectrum, running on checks that were slow and arguable. They lived with it because the volume of judgment passing through them was bounded by how many trained people could be put in the room. What has changed is not the check. It is the traffic.

Put those fields on the bridge grid, and the relevant condition is not identical across them: a diagnostic system, a hiring model, and a drafting assistant are not the same architecture, but it is analogous, and it is analogous in the way that matters: the recipient of the output frequently has no route to evaluate it that does not run back through a system of the same kind.

The bridge model had it easier in one respect, and it is worth saying so. A bridge that fails announces itself. Nobody has to detect the collapse. A hiring decision, a missed diagnosis, a badly drafted clause fail quietly and can keep failing for years without anyone assembling the fact that they failed at all.

That is not a third axis I want to add to the grid. It is a reason the grid flatters the situation.

And here I will make a prediction rather than a statement of fact, and mark it as one, so it can be held against me later. I think the independent routes in these fields will thin faster than they are replaced, because keeping one costs time and money now and pays only in failures that never happen. That is the hardest kind of expenditure to defend and the first kind to be cut.

### The Question That Decides It

Which turns the usual question inside out.

The question almost always asked about these systems is how good they are. Can it pass the exam, write the brief, read the scan? That question has an answer, and the answer improves every few months. It is a fair question. But it is a question about condition, and condition is not risk.

The question that decides the outcome is about the arrangement we put the system into. When the work comes back, is there any route to judging it that does not run through the thing that produced it?

That is a design question, and design questions have answers. That doesn't mean hoping people stay vigilant; Bainbridge disposed of that in 1983. Tonie Marie Gordon, who works on cognitive ergonomics, puts the same point in its sharpest form: *“The presence of a human in the loop is not oversight. The design of that human’s cognitive role is what determines whether the oversight is meaningful or decorative.”* A person positioned where they cannot check anything is not a safeguard. They are a diagram.

That is what I mean by augmented human intelligence, and it is duller than the phrase suggests: designing the arrangement so that human judgment retains an independent route to the answer, rather than being placed downstream of a system it can only accept or refuse.

The obvious objection is economic, and I cannot dispose of it. Maintaining an independent route costs time and money, and an organization that pays for one competes against organizations that don’t. Market pressure runs steadily against every recommendation in this essay. Building codes exist because that argument was lost on the merits and had to be won by regulation instead, in exactly the field I started in, and only after enough structures had fallen down to make the cost visible. I do not know what the equivalent looks like here, or what it will take.

And there is a harder version of the objection that I am not sure I can answer at all.

Bainbridge called the erosion an irony, which implies that nobody wanted it. In some arrangements it is not an irony. A workforce that cannot check the system is cheaper, more interchangeable and easier to replace than one that can. Where that is true, the missing route is not an unfortunate side effect of efficiency. It is the efficiency. And no amount of thoughtful design will supply a check that somebody is deliberately economizing on.

I would like to end by saying I caught that error because I was careful. I wasn't. I was a student the night before a deadline, doing an arithmetic exercise for no reason I could ever reconstruct.

I had three minutes and a route that didn't go through the package.

It would have let me submit. It couldn't tell me anything was wrong, didn't try, and would have gone on, fluent and confident, about a building that would have fallen down. Not because it was badly built, because nothing in a system that produces an answer is positioned to tell you the answer is wrong. That has to come from somewhere else.

Whether anything is still standing in that somewhere else is the only question that matters.

---

*Originally published on [Substack](https://jamesmaconochie.substack.com/p/who-is-left-holding-the-napkin).*
