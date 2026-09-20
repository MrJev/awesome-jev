# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Entries](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FMrJev%2Fawesome-jev%2Fmain%2Fdata%2Fstats.json&query=%24.entries&label=entries&color=informational)](#contents)
[![Last reviewed](https://img.shields.io/github/last-commit/MrJev/awesome-jev?label=last%20reviewed)](https://github.com/MrJev/awesome-jev/commits/main)
[![Links](https://github.com/MrJev/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/MrJev/awesome-jev/actions/workflows/links.yml)
[![Project health](https://github.com/MrJev/awesome-jev/actions/workflows/health.yml/badge.svg)](https://github.com/MrJev/awesome-jev/actions/workflows/health.yml)

> A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model: typed decisions with calibrated confidence instead of text.

Jev answers structured questions (**Choice**, **Score**, **Noul**) about program state in a single fast pass. The projects below use it for the questions that come up again and again in real software: *should we, which one, how much, what next?* Open-ended generation and deep reasoning still go to a conventional LLM.

<!-- stats:start -->
**118 entries · every one checked to actually call Jev · last reviewed 2026-09-20**
<!-- stats:end -->

There are over a thousand Jev repositories on GitHub, and most of them only mention it. This list is selective, and the bar is written down:

- **Jev is central.** Someone opened the code and confirmed the project calls Jev (or reproduces it), rather than naming it in a README.
- **10+ stars**, so a day-one burst of near-identical repositories does not fill the list. Official projects and notable teams can arrive earlier.
- **It runs.** A README that explains what it does and how to run it.
- **Numbers carry a source.** Speed, cost and accuracy figures come from the project itself and are marked as author-reported.

Listing is not endorsement, and a description is not a safety review. Several entries here send code, prompts or screen contents to a third party; some have no licence. Read what a tool sends before you install it — [what each tool sends](https://mrjev.com/best-jev-tools/#what-each-tool-sends-and-where) says so for every project we have run.

Browse and filter this list, and read guides on getting started and pricing, at **[mrjev.com](https://mrjev.com/projects/)**.

**This is an unofficial, community-maintained list. It is not affiliated with or endorsed by TypeSafe AI.** Performance numbers quoted here are reported by each project's author unless noted otherwise.


## Contents

- [Trending](#trending)
- [Recent Developments](#recent-developments)
- [What We Found Running These](#what-we-found-running-these)
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

<!-- trending:start -->

## Trending

Stars gained in the last 7 days, from our own daily snapshots. Updated 2026-09-20.

| Project                        | Stars | This week |
| ------------------------------ | ----: | --------: |
| browser-use/jev-ultrafast      | 9,002 |    +5,359 |
| tamaratran/fast-jev-compaction | 4,352 |    +2,397 |
| TianyuCodings/NanoJev          | 1,021 |      +885 |
| jarrodwatts/jev-trader         | 1,324 |      +642 |
| awlevin/typesafe-computer-use  |   529 |      +348 |
| vinnylarouge/jevlike           | 1,002 |      +225 |
| droidrun/mobile-jev            |   232 |      +169 |
| thruwire/foreman               |   402 |      +159 |
| devagrawal09/jev-review        |   358 |      +149 |
| realZachi/pg-jev               |   218 |      +127 |

**New to this list this week:** `jaredpalmer/kev`, `bespokelabsai/nimble`, `githubnext/localjev`, `Sac-Y/Jev-cu`, `featherless-ai/simple-jev` and 31 more.

Sortable, with hands-on reviews: [mrjev.com/projects](https://mrjev.com/projects/?sort=rising).

<!-- trending:end -->

## Recent Developments

The Jev ecosystem is days old and moving; these are the changes that affected the projects below.

| Date       | What changed                                                                                                                                               | Source                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 2026-09-18 | Python SDK 0.7.0. Breaking: Pydantic replaces msgspec, and `system_one()` gains `response_model` to parse answers into your own model.                     | [Release notes](https://github.com/typesafe-ai/typesafe-sdk-python/releases/tag/v0.7.0)  |
| 2026-09-18 | Jev on OpenRouter: `typesafe/jev-1.13` plus a latest alias, at TypeSafe's own price.                                                                       | [Model page](https://openrouter.ai/typesafe/jev-1.13)                                    |
| 2026-09-16 | Jev on Vercel AI Gateway as `typesafe-ai/jev`, through AI SDK 7's experimental evaluate API, with zero-data-retention and no-training as provider options. | [Announcement](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) |
| 2026-09-15 | JavaScript SDK 0.6.0. Breaking: `Score` criteria became an ordered array.                                                                                  | [Release notes](https://github.com/typesafe-ai/typesafe-sdk-js/releases/tag/v0.6.0)      |

Dated timeline with sources: [mrjev.com/changelog](https://mrjev.com/changelog/).

## What We Found Running These

Every project we review is run in a container with a real Jev key. A sample of what that turned up, and what came of it.

| Project               | What running it turned up                                                                                                                     | Review                                                            |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| pi-warden             | Redaction missed the password in a `postgres://` URL, and the holds database failed on a fresh machine. Fixed by the maintainer the same day. | [Read](https://mrjev.com/projects/devmortimer-pi-warden/)         |
| jev-router            | v0.3.0 left recent prompts in `/tmp` readable by other users on Linux. Fix merged upstream.                                                   | [Read](https://mrjev.com/projects/gargpratyush-jev-router/)       |
| jev-browser           | Every typing step presses Enter, so filling a contact form submits it.                                                                        | [Read](https://mrjev.com/projects/jkudish-jev-browser/)           |
| tax-doc-classifier    | Right on every IRS page we tried, but `result.form` still names a form for a page that is not a federal form at all; gate on `gated`.         | [Read](https://mrjev.com/projects/kyotofin-tax-doc-classifier/)   |
| abide                 | The README promises zero data retention on every call; on the direct-key path it is never requested, as we confirmed on the wire.             | [Read](https://mrjev.com/projects/coldteadotai-abide/)            |
| Jev-cu                | The policy gate matches a label already truncated to 120 characters, so a long label can hide the word 'delete'.                              | [Read](https://mrjev.com/projects/sac-y-jev-cu/)                  |
| typesafe-computer-use | The README said no screenshot is sent; the final answer includes one.                                                                         | [Read](https://mrjev.com/projects/awlevin-typesafe-computer-use/) |
| Foreman               | Codex ran with the Jev key in its environment; since v0.3.0 the key is stripped first.                                                        | [Read](https://mrjev.com/projects/thruwire-foreman/)              |

All 38 reviews, with what each tool sends and where: [mrjev.com/best-jev-tools](https://mrjev.com/best-jev-tools/).

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
- [TypeSafe Swift SDK](https://github.com/krzyzanowskim/TypeSafe) - SwiftPM client whose behaviour follows the official JavaScript SDK.

## Libraries & Integrations

- [Advocaat](https://github.com/pithings/advocaat) - Small type-safe TypeScript client for asking Jev about your data, with an agent skill for designing questions.
- [jev-harness](https://github.com/AntonioCoppe/jev-harness) - TypeScript library that wraps Jev answers in policies, confidence gates, shadow mode, and reusable recipes.
- [zod-jev](https://github.com/jomatsu/zod-jev) - Adds Jev semantic checks to Zod 4 schemas. Zod validates the shape; Jev validates the meaning.
- [ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe) - TypeSafe provider for RubyLLM 2.
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) - Experimental Hono router that matches requests against plain-language descriptions instead of paths.
- [jev-tree](https://github.com/reachjalil/jev-tree) - Recursive Choice over a taxonomy, for picking among more options than a single Choice question allows.
- [n8n-nodes-typesafe](https://github.com/zampierid4p/n8n-nodes-typesafe) - n8n community node for asking typed questions inside workflows.
- [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) - Home Assistant integration that turns Jev's answers about your house into entities.
- [jevcache](https://github.com/hyperspaceai/jevcache) - Local decision cache keyed on (model, schema, state), with redaction and canonicalisation before hashing, for cheaper repeats and deterministic replay in CI. No license file at the time of writing.
- [invalidate](https://github.com/chopratejas/invalidate) - Gives every remembered fact a lease and asks Jev whether new evidence ends it, so an agent's memory can be made to go stale on purpose.

## Agent Integrations (MCP & Skills)

- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - MCP server that lets agents such as Claude Code, Claude Desktop, and Codex call Jev directly for Choice, Score, and Noul decisions.
- [jev-mcp](https://github.com/jkudish/jev-mcp) - Proof-of-concept MCP server with ready-made tools for fact checking, prompt-injection detection, and semantic ranking.
- [askjev](https://github.com/pZacca/askjev) - MCP server published on npm, with setup instructions for Claude Code, Claude Desktop, Cursor, and Codex.
- [jev-eval-mcp](https://github.com/BYK/jev-mcp) - Eval-first MCP server that focuses on knowing whether Jev's answers can be trusted for your task.
- [Building with Jev](https://github.com/dbreunig/building-with-jev-skill) - Agent skill for writing programs that call Jev: question design, state structure, confidence thresholds, and diagnosing wrong answers.
- [Jev Sift](https://github.com/kbhuw/jev-sift) - MCP plugin that asks Jev which files, web pages, or text snippets are relevant to a query, so the agent reads selectively.
- [Jevbridge](https://github.com/tacticocc/Jevbridge) - ACP and MCP adapter that pairs Jev with any LLM agent, including Codex, Claude, Grok, and OpenCode, for typed decisions and computer use.
- [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills) - Bundle of skills that hand an agent's small decisions to Jev: model routing, skill selection, retrieval filtering, compaction, and computer use, with a routing dashboard. Works with Hermes, Claude Code, and Codex.
- [evaluate (PyModel)](https://github.com/PyModel/typesafe-mcp) - stdio MCP server exposing one `evaluate` tool; the host agent still reasons, edits, and executes.
- [jev-mcp (burnigtm)](https://github.com/burnigtm/jev-mcp) - MCP server whose tools route the next step and decide whether a partner model is needed, for Cursor, Codex, and any MCP client.
- [jevwire](https://github.com/Brainwires/jevwire) - An MCP server, an embeddable decision library, and an escalate-only Claude Code plugin in one repository.
- [pi-jev](https://github.com/TheoOliveira/pi-jev) - Semantic tool routing and skill discovery for the Pi coding agent: Jev picks which inactive tools to activate for the prompt at hand.

## Coding Agents & Developer Tools

- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Claude Code plugin that replaces the compaction summary with Jev decisions. Every tool call and result is scored; stale ones are dropped or truncated, and everything kept stays verbatim.
- [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) *(archived)* - Picks the model, reasoning depth, and speed mode for every Codex turn based on how hard Jev judges it to be. The author reports about 60% lower cost when replaying 237 real turns.
- [Foreman](https://github.com/thruwire/foreman) - Puts Jev as a fast supervisor above slower coding agents such as Codex, starting from a ticket, spec, or bug report.
- [Winnow](https://github.com/GhalebDweikat/winnow) - Context sieve for Claude Code. Jev judges each tool result (Read, Bash, Grep output) for relevance before it enters the context window.
- [Jev Review](https://github.com/devagrawal09/jev-review) - Staged code-review workflow for JavaScript and TypeScript with a local dashboard. Jev screens correctness, security, reliability, compatibility, and test risk, then scores severity and suggests a reviewer, with no generative model involved.
- [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) - Local-first MCP server for continuous software-quality review by coding agents.
- [Stanley Code](https://github.com/devagrawal09/stanley-code) - Bounded Jev workflows for coding agents (formerly jev-code).
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Rust CLI that ranks which agent skills fit the next step from live session context, with Claude Code hooks.
- [JevLint](https://github.com/huntedman/JevLint) - Checks code against conventions written in plain English, in a write-check-fix loop with your coding agent.
- [compact-adviser](https://github.com/kunchenguid/compact-adviser) - Agent plugin that asks Jev whether the session is at a safe point to `/compact`, and can run it automatically on Pi and Claude Code.
- [jev-pruner](https://github.com/tamaratran/jev-pruner) - Claude Code plugin that uses Jev to trim long Bash output before it reaches the model, leaving errors, source code, and structured output untouched.
- [perch](https://github.com/lakeday-org/perch) - Semantic code linting: rules written as sentences, run over a project from npm with its own CI action and hosted dashboard.
- [jev-lint (mizchi)](https://github.com/mizchi/jev-lint) - Checks whether a function does what its name says, whether a comment is still true, and whether a test verifies what it claims, with a cutoff per rule.
- [patdown](https://github.com/tyler-dot-earth/patdown) - Lints a tree against fuzzy rules kept in one markdown file, behind a provider-neutral interface so the judge can be swapped. Its LICENSE is not a recognised open-source license.
- [agent-dispatcher](https://github.com/nahid-sparktales/agent-dispatcher) - Routes a Claude Code or Codex task to one of 27 specialist roles and defines what evidence will count as done.
- [Jot](https://github.com/runta-dev/jot) - A general-purpose agent loop where Jev picks the next move and Jot runs it. No license file at the time of writing.

## Guardrails & Safety

- [tripwire](https://github.com/noelzappy/tripwire) - Runs seven checks on every LLM response in one Jev call, as AI SDK middleware or an OpenAI-compatible proxy.
- [jev-gates](https://github.com/rashedInt32/jev-gates) - Seven calibrated gates for Claude Code (rules, scope, intent, done, claims, proof, and commit honesty) that escalate but never approve.
- [pi-warden](https://github.com/DevMortimer/pi-warden) - Guardrails for the Pi coding agent. Jev judges every write and edit against the rules in `pi-warden.md`.
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that checks the transcript for evidence before letting a "done" through, and spends one four-question Jev call only when files changed with no passing check since. Fails open on every error path.
- [Abide](https://github.com/coldteadotai/abide) - Hooks into Claude Code, Codex, and OpenCode, and asks Jev one question per rule whether each edit breaks your AGENTS.md or CLAUDE.md rules.
- [jev-guard](https://github.com/leepokai/jev-guard) - Risk-scores every tool call against session context into deny, ask, or allow, and flags prompt injection in tool results.
- [Pi Jev Guard](https://github.com/zszz3/Pi-Jev-Guide) - Pi coding-agent plugin with rules configured by timing, plus risk checks, output redaction, and reminders on repeated failures. Chinese documentation.
- [is-malicious](https://github.com/luantak/is-malicious) - Sends source, configuration, build, and CI files to Jev and points at the files and lines that look deceptive or data-stealing. Its README says a clean report is not proof a project is safe.
- [jevscan-evm](https://github.com/devtooligan/jevscan-evm) - Produces a heat map of likely bugs in EVM code. The author's own warning: a proof of concept whose code they did not read.

## Model Routing

- [jev-router](https://github.com/gargpratyush/jev-router) - Per-turn model routing for Claude Code and Codex. Simple work goes to the fast tier and difficult work to the strong tier.
- [tiershift](https://github.com/iamvatsalpatel/tiershift) - Sends each LLM request to the cheapest model tier that can handle it and escalates on evidence.
- [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) - Neon Function proxy for the Neon AI Gateway. Jev classifies each request and routes it to the right downstream model.
- [jev-gateway](https://github.com/vinilana/jev-gateway) - Local gateway for Codex and Claude Code that asks Jev which tool to call next and passes everything else to your usual model.
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Routes each agent step to a model, subagent, Skill, MCP tool, or CLI with one Jev Choice, requiring confirmation for risky capabilities and keeping decision receipts.
- [Grok Bot Jev Router](https://github.com/Bodila51/grok-bot-jev) - Classifies a Grok Bot request before expensive research, browser, retry, or subagent work, so it can reuse a fresh artifact or stop a failing retry.

## Command-Line Tools

- [SemDecide](https://github.com/sharziki/semdecide) - Unix-style CLI for typed semantic decisions: classify, score, filter, and guard inside shell scripts, CI, and data pipelines.
- [jev-repl](https://github.com/aoprisan/jev-ts-repl) - Terminal REPL for shaping System One requests before writing code. Simulates answers when no API key is set.
- [triagedy](https://github.com/m0rphtail/triagedy) - Security alert triage as a Unix filter: JSONL alerts in, typed decisions out.
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh autosuggestions, ranked by Jev from your recent history.
- [commit-miner](https://github.com/devanshbatham/commit-miner) - Classifies Git commits into bug fixes, security fixes with CWEs, and change types.
- [TypeSafe AI Playground](https://github.com/markjaquith/typesafe-ai-playground) - Rust CLI of Jev experiments, including PHI detection, code-comment review, live tone analysis, and occupation and industry classification.
- [jev-commit](https://github.com/valentynkit/jev-commit) - Pre-commit hook where one Jev call checks whether the commit message matches the staged diff, flags debug leftovers and unmentioned work, and blocks only when it finds a credential.
- [semgrep (uehaj)](https://github.com/uehaj/jev-semgrep) - Grep by meaning: Jev scores each line against a description in any language, with AND, OR, and NOT. A single dependency-free Node file.
- [jeff (Alurith)](https://github.com/Alurith/jeff) - Read-only Go CLI that checks files against rules such as unclear responsibility or weak error handling with Jev, locally or in CI.
- [jegrep](https://github.com/can1357/jegrep) - Semantic grep with no embeddings, index, or daemon: it searches the live tree on every run and matches concepts rather than strings.
- [jgrep](https://github.com/keltokhy/jgrep) - Like grep, but the pattern is a description: it filters piped output as well as files and prints a probability per line.
- [jev-cli](https://github.com/Nasrallah-AL/jev-cli) - Typed judgments from the command line, published to npm as `jevctl`.
- [Sniff Test](https://github.com/DanRWilloughby/snifftest) - Prose linter for AI writing tells: countable regex rules run locally, and one judgment question covers the rest.
- [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) - Rust CLI and MCP server for SEO and GEO work, scraping DuckDuckGo instead of paying for a search API.

## Browser & Computer Use

- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) - Fast browser agent from Browser Use. Jev decides each step and which element to act on; a small model is called only when text needs to be typed. The authors report a full Google Flights search in about 7.1 seconds.
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - macOS computer use without sending screenshots to a large model. The screen is read deterministically and Jev picks the next action.
- [Jev Browser](https://github.com/jkudish/jev-browser) - Headless browser automation through an MCP server, CLI, or library. Jev picks one action per step.
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Android phone automation from DroidRun on its Mobilerun device cloud, with Jev choosing every operation and target. The author reports reaching Uber's payment selection in about 21 seconds.
- [agent-desktop](https://github.com/lahfir/agent-desktop) - macOS desktop automation over accessibility trees. Since v0.9.2, its jev-desktop scripts let Jev choose which control to operate and which action to take.
- [Jev-cu](https://github.com/Sac-Y/Jev-cu) - Codex computer-use skill where Jev picks the next element and action from on-screen text, with a local policy gate for sensitive steps. README in Chinese.
- [voice-browser](https://github.com/moritzkremb/jev-voice-browser) - Voice-controlled Chromium: on each partial transcript, one Jev request judges intent, target element, and whether the command is complete or destructive.
- [JevScout](https://github.com/hqman/JevScout) - Coding-agent skill that drives Chrome over CDP to look for jobs on company sites, with Jev scoring pages and links.
- [macbrow](https://github.com/timpratim/macbrow) - Say a command and it runs as AppleScript, or say a web task and it drives Chrome. Its README opens with a warning about an early version tidying a Desktop rather thoroughly.
- [jev-use](https://github.com/savka777/jev-use) - macOS computer use by voice or typing that reads the screen through the Accessibility tree rather than screenshots. Key stored in the Keychain.
- [Jev Voice](https://github.com/kevinbadi/jev-voice) - Local whisper.cpp for the transcript, then one Jev request picks the action and its typed arguments; code owns execution.
- [Jev macOS Loop](https://github.com/jcpsimmons/jev-macos-loop) - Native macOS GUI automation on Apple silicon: OmniParser CoreML and Apple Vision OCR identify controls locally, Jev selects the action. AGPL-3.0.
- [Jev Desktop](https://github.com/yikangy873-gif/jev-desktop) - Adds a bounded decision loop to Codex Computer Use for browser tabs and native macOS apps.

## Data & Observability

- [pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension to filter, rank, and classify rows with plain-language conditions.
- [jevql](https://github.com/kylemclaren/jevql) - A psql-shaped CLI and Go/TypeScript/Python SDKs that add `jev()`, `jev_prob`, `jev_choice`, and `jev_score` to queries against a vanilla Postgres with no extension. The SQL runs on the server and Jev judges the surviving rows in batches.
- [duckdb-jev](https://github.com/colliber/duckdb-jev) - DuckDB extension that returns Jev's answers as real SQL types.
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores OpenTelemetry logs for diagnostic value, priority, and routing before expensive LLM analysis.
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL extension that calls Jev from SQL for Choice, Noul, and Score, with `EXECUTE` revoked from `PUBLIC` by default.
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Classifies tax-document pages into IRS forms and page kinds with one Jev request per page, driven by a JSON file of form descriptions.
- [doc-router](https://github.com/misbahsy/doc-router) - Rust tool that asks Jev which PDF pages actually need OCR, extracting text pages locally and sending only the rest to your OCR provider.

## Search & Knowledge Graphs

- [Blink](https://github.com/ellipsis-dev/blink) - Semantic codebase search. At each directory level Jev ranks which files and folders are most likely relevant and sends more walkers there.
- [neo4jev](https://github.com/jexp/neo4jev) - Navigates a Neo4j graph by having Jev score neighbouring relationships, then beam-searching for the most probable path.
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim plugin that splits the buffer into functions with Treesitter, has Jev score each one against a plain-language question, and lists the answers in the quickfix window ranked by probability.

## Apps & Browser Extensions

- [unclutter](https://github.com/kitze/unclutter) - Browser extension that removes page clutter using Jev and reusable template rules.
- [TypeSafe AdBlock](https://github.com/realZachi/typesafe-adblock) - Chrome extension that asks Jev whether each DOM element is an ad and removes the ones that are.
- [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) - Discord bot that filters spam and scam links in real time and escalates repeat offenses.
- [jevmeter](https://github.com/ChetasLua/jevmeter) - Scores every sentence in a video and renders a live Jev meter as a 16:9 edit.
- [jev-skip](https://github.com/valentynkit/jev-skip) - Browser extension that reads the caption track and paints a sponsor-probability overlay on the YouTube seek bar before the intro ends, with no crowd database. The author reports catching 77% of SponsorBlock's sponsor seconds across 23 videos at $0.0008 per video.
- [Jev Chat](https://github.com/w3cj/jev-chat) - Chat-style command bar where Jev picks the tool, arguments, and reply type, and code builds every reply from tool data.
- [Sharp](https://github.com/tshmieldev/sharp) - Browser extension that filters your X timeline by plain-language rules, with Jev as the default classifier.
- [lurk](https://github.com/getanyapi-com/lurk) - Self-hostable Reddit buyer-intent finder that uses Jev to judge every post and comment a scan reads.
- [jev-paint](https://github.com/achimala/jev-paint) - Local app that turns Jev's per-pixel probability distributions into paintings.
- [Live Jev](https://github.com/okinaaudio/live-jev) - Control Ableton Live with one sentence, in Japanese or English, from a bar that appears over the session and gets out of the way.
- [x-scanner](https://github.com/oso95/x-scanner) - Chrome extension that labels every post you scroll past on X with six typed questions per post, and counts what it costs in the corner.
- [RefGarden](https://github.com/AlbionaHoti/refgarden) - A three-dimensional reference gallery over The Met, NASA, Cosmos, and the Prelinger Archives, with Jev choosing the search phrases.
- [Cheshi](https://github.com/CheshiAI/Cheshi) - macOS workspace for Codex where Jev finds past sessions and the decisions made in them. Apple silicon only.
- [Jev Reviewer](https://github.com/choxos/jev-reviewer) - Extracts data for systematic reviews from a trial report and its supplements, quoted from the paper, against your own form or a RoB 2 template.

## Evaluation & Benchmarks

- [jevcal](https://github.com/abhixhek/jevcal) - Picks the confidence threshold that meets your accuracy target on your own data, and fails CI when a model update breaks it.
- [Janus](https://github.com/FirasSX914/Janus) - Measures Jev's calibration and confidence-based routing on Banking77 and Web of Science.
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) - Probability-aware evaluation: calibration, and how much work can be automated at a fixed error budget.
- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - Compares LLM structured output with Jev on latency, cost, and judgment quality.
- [Jev Capability Atlas](https://github.com/Zaious/jev-capability-atlas) - A bilingual map of where Jev holds up and where it breaks, built from recorded API calls rather than a leaderboard. Its LICENSE is not a recognised open-source license.
- [jev-align](https://github.com/sutro-sh/jev-align) - CLI from Sutro that finds the examples a Jev function is least sure about, asks you to label them, and uses GEPA to improve the question.

## Open Models & Reproductions

- [SemIf](https://github.com/TheoLeeCJ/SemIf) - Jev-style decisions from a frozen 4B model on a single RTX 3090, with a browser demo. Formerly OpenJev.
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Train a small model that scores a changing list of text options in one pass.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - 0.6B parallel decision model with an end-to-end training pipeline.
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Jev-compatible API server running an open model on SGLang.
- [jevmlx](https://github.com/bnsd55/jevmlx) - Jev-style typed decisions from local MLX models on Apple Silicon.
- [kev](https://github.com/jaredpalmer/kev) - Jev-style decision models from 0.5B to 8B, built as LoRA adapters on Qwen and served behind a Jev-compatible `/v1/systemone` API.
- [LocalJev](https://github.com/githubnext/localjev) - Local Jev-compatible `/v1/systemone` server for Bun that asks DiffusionGemma for probabilities, from GitHub Next.
- [Bespoke Nimble](https://github.com/bespokelabsai/nimble) - Open data, training recipe, and a 9B model for Jev-style choice and true/false decisions on Apple Silicon or NVIDIA GPUs.
- [Simple Jev](https://github.com/featherless-ai/simple-jev) - Turns open Hugging Face models into a Jev-style classifier endpoint by reading next-token logits, with a public demo API.
- [OpenJev](https://github.com/razorback16/openjev) - Jev-compatible decision server on DiffusionGemma 26B-A4B through vLLM, including questions about images. TypeSafe's SDKs work against it unchanged.
- [jeff](https://github.com/logan-markewich/jeff) - Self-hosted implementation of Jev's System One API on the 400M-parameter GLiFormer model. The official SDK works after changing the base URL.
- [Von](https://github.com/wfzyx/von) - Non-autoregressive System One model with Python and TypeScript clients, published on Hugging Face under Apache 2.0. The author reports sub-25ms inference.
- [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) - A 151M non-autoregressive decision model on ModernBERT with calibrated uncertainty and an in-browser WebGPU playground. Its LICENSE is not recognised as the Apache 2.0 its badge claims.
- [OpenDecision](https://github.com/deepanwadhwa/OpenDecision) - Open-source semantic decision engine: state, a question in natural language, and answer criteria in; a structured decision out.
- [Open Alternative to Jev](https://github.com/ikermoel/open-alternative-jev) - Typed, calibrated decisions from any open-weights model in one forward pass, as the Python package `open-alternative-jev`.
- [choosekit](https://github.com/NotXf1le/choosekit) - Scores a finite set of choices with a model you already run in llama.cpp and returns a typed decision with a probability distribution.
- [Jev Local](https://github.com/Argos1111/jev_local) - A local `/v1/systemone` server with two backends: an LFM model zero-shot, and a fine-tuned ModernBERT-Ja cross-encoder. Japanese documentation.

## Games & Real-Time Demos

- [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev) - Three.js quickscope arena where Jev decides movement, aiming, ADS, firing, and jumping at roughly 9 Hz.
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Jev picks NES controller inputs for Super Mario Bros. from emulator state, with no screenshots.
- [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) - Jev plays the first StarCraft shareware mission, with its recorded action probabilities.
- [Jev Pong](https://github.com/ably-labs/jev-pong) - Pong where the ball moves one step per model decision, pitting Jev against chat LLMs.
- [JevPilot](https://github.com/standardagents/jevpilot) - Three.js driving simulator with a Jev-powered autopilot.
- [jev-drone](https://github.com/RomanSlack/jev-drone) - Camera-only quadrotor in MuJoCo with Jev making judgment calls at about 2.5 Hz.
- [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) - Recorded chess experiments with a candid result: Jev on its own still blunders pieces.
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - Pokemon Red on PyBoy where code owns the route and the arithmetic and Jev only picks at branches, logging a Brier-scored faint prediction against RAM state on every battle turn.
- [Jev Self-Driving Sim](https://github.com/vinilana/live-jev) - A 2D top-down car in the browser that turns its sensors into a JSON state every 200 ms and executes four typed answers. No license file at the time of writing.

## Finance

- [Prism](https://github.com/irfndi/prism-liquidity-agent) - Liquidity-provision agent for Meteora DLMM. Jev judges toxic flow, market stress, and mean-reversion likelihood in shadow/advisory mode only, without driving trades. Not financial advice.
- [jev-trader](https://github.com/jarrodwatts/jev-trader) - Asks Jev buy or sell on every Monad block and places real post-only limit orders on the Kuru MON-USDC book. Not financial advice.
- [Jev Trade](https://github.com/aowang-ai/jev-trade) - Hyperliquid trading bot based on jev-trader, where Jev decides buy, sell, or hold on every tick for five coins. Dry-runs without a private key.
- [Jev X Sentiment Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) - Crypto terminal that reads up to 1,000 posts about a ticker alongside market and funding data and turns them into a buy, sell, hold, or take-profit call. No license file at the time of writing. Not financial advice.

## Articles & Analysis

- [Jev: The Language Model That Won't Talk](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont) - Critical look at the "no hallucination" and benchmark claims.
- [A deep dive into Jev](https://flaviocopes.com/jev/) - Hands-on developer walkthrough.
- [Jev: TypeSafe's System One Model That Never Hallucinates](https://www.datacamp.com/blog/system-one-models-jev) - Overview from DataCamp.
- [TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) - Launch coverage from The Register.

## Related Lists

Other community lists of Jev projects, each with its own scope and bar:

- [awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) - Broad list with decision tables and a use-case map.
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) - Category files with written inclusion criteria.
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) - Large list with sourced research notes.
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) - Uses Jev itself to review incoming pull requests.
- [awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) - Structured metadata per entry, in four languages.
- [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) - The largest list, with a searchable site.
- [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) - Tools only, no articles or models.
- [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) - Resources paired with runnable examples.
- [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) - Chinese-language list, refreshed daily.
- [OmniJev/awesome-jev](https://github.com/OmniJev/awesome-jev) - Papers, open reproductions and independent evaluations.

## Contributing

Contributions are welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
