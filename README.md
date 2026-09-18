# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of projects, integrations, and resources for [Jev](https://typesafe.ai), TypeSafe AI's System One model: typed decisions with calibrated confidence instead of text.

Jev answers structured questions (**Choice**, **Score**, **Noul**) about program state in a single fast pass. The projects below use it for the questions that come up again and again in real software: *should we, which one, how much, what next?* Open-ended generation and deep reasoning still go to a conventional LLM.

**This is an unofficial, community-maintained list. It is not affiliated with or endorsed by TypeSafe AI.** Performance numbers quoted here are reported by each project's author unless noted otherwise.

## Contents

- [Official Resources](#official-resources)
- [Agent Integrations (MCP)](#agent-integrations-mcp)
- [Coding Agents & Developer Tools](#coding-agents--developer-tools)
- [Command-Line Tools](#command-line-tools)
- [Browser & Computer Use](#browser--computer-use)
- [Model Routing](#model-routing)
- [Search & Knowledge Graphs](#search--knowledge-graphs)
- [Games & Real-Time Demos](#games--real-time-demos)
- [Finance](#finance)
- [Articles & Analysis](#articles--analysis)
- [Contributing](#contributing)

## Official Resources

- [TypeSafe AI](https://typesafe.ai): Homepage and early-access waitlist.
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev): Launch post.
- [Documentation](https://docs.typesafe.ai/introduction): Concepts, the three question primitives, patterns, and API reference.
- [Quick start](https://docs.typesafe.ai/introduction/quickstart): First API call.
- [Python SDK](https://docs.typesafe.ai/sdk/python) and [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript): Official client libraries.
- [Cookbooks](https://docs.typesafe.ai/cookbooks/llm_guardrails): Official recipes for guardrails, re-ranking, RAG passage classification, citation checks, and more.
- [Patterns](https://docs.typesafe.ai/patterns): Confidence-gated routing, speculative fan-out, composite scoring, and intent routing.
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13): Where the current model is known to be weak.
- [Evals](https://evals.typesafe.ai): TypeSafe's published evaluations.

## Agent Integrations (MCP)

- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp): MCP server that lets agents such as Claude Code, Claude Desktop, and Codex call Jev directly for Choice, Score, and Noul decisions.
- [jev-mcp](https://github.com/jkudish/jev-mcp): Proof-of-concept MCP server with ready-made tools for fact checking, prompt-injection detection, and semantic ranking.

## Coding Agents & Developer Tools

- [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router): Picks the model, reasoning depth, and speed mode for every Codex turn based on how hard Jev judges it to be. The author reports about 60% lower cost when replaying 237 real turns.
- [Winnow](https://github.com/GhalebDweikat/winnow): Context sieve for Claude Code. Jev judges each tool result (Read, Bash, Grep output) for relevance before it enters the context window.
- [Jev Review](https://github.com/devagrawal09/jev-review): Staged code-review workflow with a local dashboard. Jev triages correctness, security, reliability, compatibility, and test risk, then hands the important findings to a heavier model.
- [jev-code](https://github.com/devagrawal09/jev-code): Bounded Jev workflows for coding agents.

## Command-Line Tools

- [SemDecide](https://github.com/sharziki/semdecide): Unix-style CLI for typed semantic decisions: classify, score, filter, and guard inside shell scripts, CI, and data pipelines.
- [TypeSafe AI Playground](https://github.com/markjaquith/typesafe-ai-playground): Rust CLI of Jev experiments, including PHI detection, code-comment review, live tone analysis, and occupation and industry classification.

## Browser & Computer Use

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast): Fast browser agent from Browser Use. Jev decides each step and which element to act on; a small model is called only when text needs to be typed. The authors report a full Google Flights search in about 7.1 seconds.
- [agent-desktop](https://github.com/lahfir/agent-desktop/tree/feat/jev-desktop-loop): Desktop automation over OS accessibility trees. The `feat/jev-desktop-loop` branch uses Jev to choose which control to operate and which action to take.

## Model Routing

- [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev): Neon Function proxy for the Neon AI Gateway. Jev classifies each request and routes it to the right downstream model.
- [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router): See [Coding Agents & Developer Tools](#coding-agents--developer-tools).

## Search & Knowledge Graphs

- [Blink](https://github.com/ellipsis-dev/blink): Semantic codebase search. At each directory level Jev ranks which files and folders are most likely relevant and sends more walkers there.
- [neo4jev](https://github.com/jexp/neo4jev): Navigates a Neo4j graph by having Jev score neighbouring relationships, then beam-searching for the most probable path.

## Games & Real-Time Demos

- [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev): Three.js quickscope arena where Jev decides movement, aiming, ADS, firing, and jumping at roughly 9 Hz.

## Finance

- [Prism](https://github.com/irfndi/prism-liquidity-agent): Liquidity-provision agent for Meteora DLMM. Jev judges toxic flow, market stress, and mean-reversion likelihood in shadow/advisory mode only, without driving trades. Not financial advice.

## Articles & Analysis

- [Jev: The Language Model That Won't Talk](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont): Critical look at the "no hallucination" and benchmark claims.
- [A deep dive into Jev](https://flaviocopes.com/jev/): Hands-on developer walkthrough.
- [Jev: TypeSafe's System One Model That Never Hallucinates](https://www.datacamp.com/blog/system-one-models-jev): Overview from DataCamp.
- [TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711): Launch coverage from The Register.

## Contributing

Contributions are welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
