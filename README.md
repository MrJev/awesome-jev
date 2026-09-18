# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model: typed decisions with calibrated confidence instead of text.

Jev answers structured questions (**Choice**, **Score**, **Noul**) about program state in a single fast pass. The projects below use it for the questions that come up again and again in real software: *should we, which one, how much, what next?* Open-ended generation and deep reasoning still go to a conventional LLM.

There are over a thousand Jev repositories on GitHub. This list is selective: every entry has been checked to actually call Jev (or reproduce it) and to have a usable README.

Browse and filter this list, and read guides on getting started and pricing, at **[mrjev.com](https://mrjev.com/projects/)**.

**This is an unofficial, community-maintained list. It is not affiliated with or endorsed by TypeSafe AI.** Performance numbers quoted here are reported by each project's author unless noted otherwise.

## Contents

- [Official Resources](#official-resources)
- [Community SDKs](#community-sdks)
- [Libraries & Integrations](#libraries--integrations)
- [Agent Integrations (MCP & Skills)](#agent-integrations-mcp--skills)
- [Coding Agents & Developer Tools](#coding-agents--developer-tools)
- [Guardrails & Safety](#guardrails--safety)
- [Model Routing](#model-routing)
- [Command-Line Tools](#command-line-tools)
- [Browser & Computer Use](#browser--computer-use)
- [Data & Observability](#data--observability)
- [Search & Knowledge Graphs](#search--knowledge-graphs)
- [Apps & Browser Extensions](#apps--browser-extensions)
- [Evaluation & Benchmarks](#evaluation--benchmarks)
- [Open Models & Reproductions](#open-models--reproductions)
- [Games & Real-Time Demos](#games--real-time-demos)
- [Finance](#finance)
- [Articles & Analysis](#articles--analysis)

## Official Resources

- [TypeSafe AI](https://typesafe.ai) - Homepage and early-access waitlist.
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) - Launch post.
- [Documentation](https://docs.typesafe.ai/introduction) - Concepts, the three question primitives, patterns, and API reference.
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) - First API call.
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Official Python client (`pip install typesafe-sdk`).
- [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - Official JavaScript and TypeScript client (`npm install @typesafe-ai/sdk`).
- [Cookbooks](https://docs.typesafe.ai/cookbooks/llm_guardrails) - Official recipes for guardrails, re-ranking, RAG passage classification, citation checks, and more.
- [Patterns](https://docs.typesafe.ai/patterns) - Confidence-gated routing, speculative fan-out, composite scoring, and intent routing.
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) - Where the current model is known to be weak.
- [Evals](https://evals.typesafe.ai) - TypeSafe's published evaluations.
- [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) - Access Jev through Vercel's AI Gateway.

## Community SDKs

- [typesafe_sdk](https://github.com/nshkrdotcom/typesafe_sdk) - Elixir SDK for the System One API.
- [typesafe-sdk-java](https://github.com/kgonia/typesafe-sdk-java) - Zero-dependency Java client (Java 21+).
- [typesafe-go](https://github.com/Shubham510/typesafe-go) - Go client.
- [kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev) - Rust client, published on crates.io.
- [typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) - .NET SDK.

## Libraries & Integrations

- [Advocaat](https://github.com/pithings/advocaat) - Small type-safe TypeScript client for asking Jev about your data, with an agent skill for designing questions.
- [jev-harness](https://github.com/AntonioCoppe/jev-harness) - TypeScript library that wraps Jev answers in policies, confidence gates, shadow mode, and reusable recipes.
- [zod-jev](https://github.com/jomatsu/zod-jev) - Adds Jev semantic checks to Zod 4 schemas. Zod validates the shape; Jev validates the meaning.
- [ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe) - TypeSafe provider for RubyLLM 2.
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) - Experimental Hono router that matches requests against plain-language descriptions instead of paths.
- [jev-tree](https://github.com/reachjalil/jev-tree) - Recursive Choice over a taxonomy, for picking among more options than a single Choice question allows.
- [n8n-nodes-typesafe](https://github.com/zampierid4p/n8n-nodes-typesafe-ai) - n8n community node for asking typed questions inside workflows.
- [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) - Home Assistant integration that turns Jev's answers about your house into entities.

## Agent Integrations (MCP & Skills)

- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - MCP server that lets agents such as Claude Code, Claude Desktop, and Codex call Jev directly for Choice, Score, and Noul decisions.
- [jev-mcp](https://github.com/jkudish/jev-mcp) - Proof-of-concept MCP server with ready-made tools for fact checking, prompt-injection detection, and semantic ranking.
- [askjev](https://github.com/pZacca/askjev) - MCP server published on npm, with setup instructions for Claude Code, Claude Desktop, Cursor, and Codex.
- [jev-eval-mcp](https://github.com/BYK/jev-mcp) - Eval-first MCP server that focuses on knowing whether Jev's answers can be trusted for your task.
- [Building with Jev](https://github.com/dbreunig/building-with-jev-skill) - Agent skill for writing programs that call Jev: question design, state structure, confidence thresholds, and diagnosing wrong answers.

## Coding Agents & Developer Tools

- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin that replaces the compaction summary with Jev decisions. Every tool call and result is scored; stale ones are dropped or truncated, and everything kept stays verbatim.
- [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) - Picks the model, reasoning depth, and speed mode for every Codex turn based on how hard Jev judges it to be. The author reports about 60% lower cost when replaying 237 real turns.
- [Foreman](https://github.com/thruwire/foreman) - Puts Jev as a fast supervisor above slower coding agents such as Codex, starting from a ticket, spec, or bug report.
- [Winnow](https://github.com/GhalebDweikat/winnow) - Context sieve for Claude Code. Jev judges each tool result (Read, Bash, Grep output) for relevance before it enters the context window.
- [Jev Review](https://github.com/devagrawal09/jev-review) - Staged code-review workflow with a local dashboard. Jev triages correctness, security, reliability, compatibility, and test risk, then hands the important findings to a heavier model.
- [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) - Local-first MCP server for continuous software-quality review by coding agents.
- [jev-code](https://github.com/devagrawal09/jev-code) - Bounded Jev workflows for coding agents.
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI that ranks which agent skills fit the next step from live session context, with Claude Code hooks.
- [JevLint](https://github.com/huntedman/JevLint) - Checks code against conventions written in plain English, in a write-check-fix loop with your coding agent.

## Guardrails & Safety

- [tripwire](https://github.com/noelzappy/tripwire) - Runs seven checks on every LLM response in one Jev call, as AI SDK middleware or an OpenAI-compatible proxy.
- [jev-gates](https://github.com/rashedInt32/jev-gates) - Six calibrated gates for Claude Code (rules, scope, intent, done, claims, and commit honesty) that escalate but never approve.
- [pi-warden](https://github.com/DevMortimer/pi-warden) - Guardrails for the Pi coding agent. Jev judges every write and edit against the rules in `pi-warden.md`.

## Model Routing

- [jev-router](https://github.com/gargpratyush/jev-router) - Per-turn model routing for Claude Code and Codex. Simple work goes to the fast tier and difficult work to the strong tier.
- [tiershift](https://github.com/iamvatsalpatel/tiershift) - Sends each LLM request to the cheapest model tier that can handle it and escalates on evidence.
- [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) - Neon Function proxy for the Neon AI Gateway. Jev classifies each request and routes it to the right downstream model.

## Command-Line Tools

- [SemDecide](https://github.com/sharziki/semdecide) - Unix-style CLI for typed semantic decisions: classify, score, filter, and guard inside shell scripts, CI, and data pipelines.
- [jev-repl](https://github.com/aoprisan/jev-ts-repl) - Terminal REPL for shaping System One requests before writing code. Simulates answers when no API key is set.
- [triagedy](https://github.com/m0rphtail/triagedy) - Security alert triage as a Unix filter: JSONL alerts in, typed decisions out.
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh autosuggestions, ranked by Jev from your recent history.
- [commit-miner](https://github.com/devanshbatham/commit-miner) - Classifies Git commits into bug fixes, security fixes with CWEs, and change types.
- [TypeSafe AI Playground](https://github.com/markjaquith/typesafe-ai-playground) - Rust CLI of Jev experiments, including PHI detection, code-comment review, live tone analysis, and occupation and industry classification.

## Browser & Computer Use

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - Fast browser agent from Browser Use. Jev decides each step and which element to act on; a small model is called only when text needs to be typed. The authors report a full Google Flights search in about 7.1 seconds.
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer use without sending screenshots to a large model. The screen is read deterministically and Jev picks the next action.
- [Jev Browser](https://github.com/jkudish/jev-browser) - Headless browser automation through an MCP server, CLI, or library. Jev picks one action per step.
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Phone automation from DroidRun. The demo sets up an Uber ride in about 21 seconds.
- [agent-desktop](https://github.com/lahfir/agent-desktop/tree/feat/jev-desktop-loop) - Desktop automation over OS accessibility trees. The `feat/jev-desktop-loop` branch uses Jev to choose which control to operate and which action to take.

## Data & Observability

- [pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension to filter, rank, and classify rows with plain-language conditions.
- [duckdb-jev](https://github.com/colliber/duckdb-jev) - DuckDB extension that returns Jev's answers as real SQL types.
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores OpenTelemetry logs for diagnostic value, priority, and routing before expensive LLM analysis.

## Search & Knowledge Graphs

- [Blink](https://github.com/ellipsis-dev/blink) - Semantic codebase search. At each directory level Jev ranks which files and folders are most likely relevant and sends more walkers there.
- [neo4jev](https://github.com/jexp/neo4jev) - Navigates a Neo4j graph by having Jev score neighbouring relationships, then beam-searching for the most probable path.

## Apps & Browser Extensions

- [unclutter](https://github.com/kitze/unclutter) - Browser extension that removes page clutter using Jev and reusable template rules.
- [TypeSafe AdBlock](https://github.com/realZachi/typesafe-adblock) - Chrome extension that asks Jev whether each DOM element is an ad and removes the ones that are.
- [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) - Discord bot that filters spam and scam links in real time and escalates repeat offenses.
- [jevmeter](https://github.com/ChetasLua/jevmeter) - Scores every sentence in a video and renders a live Jev meter as a 16:9 edit.

## Evaluation & Benchmarks

- [jevcal](https://github.com/abhixhek/jevcal) - Picks the confidence threshold that meets your accuracy target on your own data, and fails CI when a model update breaks it.
- [Janus](https://github.com/FirasSX914/Janus) - Measures Jev's calibration and confidence-based routing on Banking77 and Web of Science.
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) - Probability-aware evaluation: calibration, and how much work can be automated at a fixed error budget.
- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - Compares LLM structured output with Jev on latency, cost, and judgment quality.

## Open Models & Reproductions

- [OpenJev](https://github.com/TheoLeeCJ/openjev) - Jev-style decisions from a frozen 4B model on a single RTX 3090, with a browser demo.
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Train a small model that scores a changing list of text options in one pass.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - 0.6B parallel decision model with an end-to-end training pipeline.
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Jev-compatible API server running an open model on SGLang.
- [jevmlx](https://github.com/bnsd55/jevmlx) - Jev-style typed decisions from local MLX models on Apple Silicon.

## Games & Real-Time Demos

- [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev) - Three.js quickscope arena where Jev decides movement, aiming, ADS, firing, and jumping at roughly 9 Hz.
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Jev picks NES controller inputs for Super Mario Bros. from emulator state, with no screenshots.
- [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) - Jev plays the first StarCraft shareware mission, with its recorded action probabilities.
- [Jev Pong](https://github.com/ably-labs/jev-pong) - Pong where the ball moves one step per model decision, pitting Jev against chat LLMs.
- [JevPilot](https://github.com/standardagents/jevpilot) - Three.js driving simulator with a Jev-powered autopilot.
- [jev-drone](https://github.com/RomanSlack/jev-drone) - Camera-only quadrotor in MuJoCo with Jev making judgment calls at about 2.5 Hz.
- [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) - Recorded chess experiments with a candid result: Jev on its own still blunders pieces.

## Finance

- [Prism](https://github.com/irfndi/prism-liquidity-agent) - Liquidity-provision agent for Meteora DLMM. Jev judges toxic flow, market stress, and mean-reversion likelihood in shadow/advisory mode only, without driving trades. Not financial advice.
- [jev-trader](https://github.com/jarrodwatts/jev-trader) - Asks Jev buy or sell on every Monad block and places real post-only limit orders on the Kuru MON-USDC book. Not financial advice.

## Articles & Analysis

- [Jev: The Language Model That Won't Talk](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont) - Critical look at the "no hallucination" and benchmark claims.
- [A deep dive into Jev](https://flaviocopes.com/jev/) - Hands-on developer walkthrough.
- [Jev: TypeSafe's System One Model That Never Hallucinates](https://www.datacamp.com/blog/system-one-models-jev) - Overview from DataCamp.
- [TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) - Launch coverage from The Register.

## Contributing

Contributions are welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
