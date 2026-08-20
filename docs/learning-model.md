# Learning Model

The repository is organized around engineering capabilities, not a list of courses.

## The loop

```text
Problem
  ↓
Mental Model
  ↓
Principles
  ↓
System Behavior
  ↓
Technology
  ↓
Implementation
  ↓
Failure / Trade-offs
  ↓
Project
  ↓
Operational Experience
```

## What “knowing” means

### Level 1 — Recognition
You can define the term and identify where it is used.

### Level 2 — Understanding
You can explain why it exists, how it works, and what assumptions it makes.

### Level 3 — Implementation
You can implement the concept with the default stack without following a tutorial step by step.

### Level 4 — Production
You can reason about security, failure modes, performance, observability, scaling, and operational cost.

### Level 5 — Architecture
You can choose between competing approaches and explain the trade-offs.

The Fullstack repository should optimize for Levels 3–5 for core engineering topics.

## Topic template

Every substantial topic should eventually answer these questions:

- **Problem:** What problem exists?
- **Model:** What mental model makes the problem understandable?
- **Mechanism:** How does the system actually work?
- **Interface:** What contract exists between components?
- **Trade-offs:** What are the important alternatives?
- **Failure:** What breaks and how does it degrade?
- **Security:** What can be abused or exposed?
- **Performance:** What controls latency, throughput, and resource usage?
- **Operations:** How do we test, deploy, observe, and debug it?
- **Implementation:** How do Python and TypeScript implement it?
- **Project:** What real system proves the understanding?

## Avoid these failure modes

Do not turn the repository into:

- a collection of framework tutorials
- a list of interview questions
- a link dump
- a weekly schedule that forces artificial pacing
- a glossary without systems context
- copied content from the specialized repositories

The result should feel like an engineer's field guide and reference architecture library.
