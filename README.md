# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Entries](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FMrJev%2Fawesome-jev%2Fmain%2Fdata%2Fstats.json&query=%24.entries&label=entries&color=informational)](#contents)
[![Last reviewed](https://img.shields.io/github/last-commit/MrJev/awesome-jev?label=last%20reviewed)](https://github.com/MrJev/awesome-jev/commits/main)
[![Links](https://github.com/MrJev/awesome-jev/actions/workflows/links.yml/badge.svg)](https://github.com/MrJev/awesome-jev/actions/workflows/links.yml)
[![Project health](https://github.com/MrJev/awesome-jev/actions/workflows/health.yml/badge.svg)](https://github.com/MrJev/awesome-jev/actions/workflows/health.yml)

> A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model: typed decisions with calibrated confidence instead of text.

Jev answers structured questions (**Choice**, **Score**, **Noul**) about program state in a single fast pass. The projects below use it for the questions that come up again and again in real software: *should we, which one, how much, what next?* Open-ended generation and deep reasoning still go to a conventional LLM.

<!-- stats:start -->
**280 entries · every one checked to actually call Jev · last reviewed 2026-09-23**
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
- [Running Without Jev](#running-without-jev)
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
- [Robotics & Embodied](#robotics--embodied)
- [Finance](#finance)
- [Articles & Analysis](#articles--analysis)

<!-- trending:start -->

## Trending

Stars gained in the last 7 days, from our own daily snapshots. Updated 2026-09-23.

| Project                        |  Stars | This week |
| ------------------------------ | -----: | --------: |
| browser-use/jev-ultrafast      | 18,259 |   +14,616 |
| tamaratran/fast-jev-compaction |  6,354 |    +4,399 |
| TianyuCodings/NanoJev          |  2,020 |    +1,884 |
| jarrodwatts/jev-trader         |  2,084 |    +1,402 |
| awlevin/typesafe-computer-use  |    847 |      +666 |
| vinnylarouge/jevlike           |  1,241 |      +464 |
| devagrawal09/jev-review        |    556 |      +347 |
| droidrun/mobile-jev            |    356 |      +293 |
| thruwire/foreman               |    518 |      +275 |
| lahfir/agent-desktop           |  1,525 |      +263 |

**New to this list this week:** `NandhaKishorM/laya`, `jaredpalmer/kev`, `bespokelabsai/nimble`, `githubnext/localjev`, `kerpopule/hermes-jev-skills` and 168 more.

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

| Project               | What running it turned up                                                                                                                        | Review                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| pi-warden             | Redaction missed the password in a `postgres://` URL, and the holds database failed on a fresh machine. Fixed by the maintainer the same day.    | [Read](https://mrjev.com/projects/devmortimer-pi-warden/)         |
| jev-router            | v0.3.0 left recent prompts in `/tmp` readable by other users on Linux. Fix merged upstream.                                                      | [Read](https://mrjev.com/projects/gargpratyush-jev-router/)       |
| jev-browser           | Every typing step presses Enter, so filling a contact form submits it.                                                                           | [Read](https://mrjev.com/projects/jkudish-jev-browser/)           |
| tax-doc-classifier    | Right on every IRS page we tried, but `result.form` still names a form for a page that is not a federal form at all; gate on `gated`.            | [Read](https://mrjev.com/projects/kyotofin-tax-doc-classifier/)   |
| abide                 | The README promised zero data retention on every call; on the direct-key path it was never requested, as we confirmed on the wire. README fixed. | [Read](https://mrjev.com/projects/coldteadotai-abide/)            |
| Jev-cu                | The policy gate matches a label already truncated to 120 characters, so a long label can hide the word 'delete'.                                 | [Read](https://mrjev.com/projects/sac-y-jev-cu/)                  |
| typesafe-computer-use | The README said no screenshot is sent; the final answer includes one.                                                                            | [Read](https://mrjev.com/projects/awlevin-typesafe-computer-use/) |
| Foreman               | Codex ran with the Jev key in its environment; since v0.3.0 the key is stripped first.                                                           | [Read](https://mrjev.com/projects/thruwire-foreman/)              |
| jeff                  | `jeff check .` sent a `.pem` private key and a config file with a password, whole. Fixed in v0.1.0; we re-ran the harness to confirm.            | [Read](https://mrjev.com/projects/alurith-jeff/)                  |
| Von                   | The published weights lost their classification head, so the default install answered at random. Restored by the author the same day.            | [Read](https://mrjev.com/projects/wfzyx-von/)                     |

All 143 reviews, with what each tool sends and where: [mrjev.com/best-jev-tools](https://mrjev.com/best-jev-tools/).

## Running Without Jev

Jev is a paid API, so a fair question is which of these still work if you would rather not pay for it ([#17](https://github.com/MrJev/awesome-jev/issues/17)). Two things get mixed up in that question, and they are worth separating.

Routing Jev through OpenRouter or Vercel's AI Gateway is **not** an alternative model. It is the same paid model with a different bill and an extra hop. Many entries offer it, and it changes nothing about cost per decision or licensing.

Pointing a tool at a *different* model is the question people are actually asking. The table below is only what we checked ourselves, by running each tool against a server of our own. A project missing from it means we have not checked, not that the answer is no.

| Tool                                                                                 | Points at a non-Jev endpoint?                                           | How we know                                                                       |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [Jevvy](https://mrjev.com/projects/panachy-jevvy/)                                   | Yes — `provider: "custom"`, any endpoint, optional key                  | We ran its Claude Code hook against a local server of ours                        |
| [jev-use](https://mrjev.com/projects/shitianfang-jev-use/)                           | Yes — `TYPESAFE_BASE_URL`, and `JEV_BACKEND=mock` for a keyless dry run | We ran its PreToolUse hook adapter against a local server of ours                 |
| [JCR](https://mrjev.com/projects/niazmorshed2007-jcr/)                               | Yes — the SDK's own `TYPESAFE_BASE_URL`                                 | We ran the resolver against a local server of ours                                |
| [hermes-jev-approvals](https://mrjev.com/projects/anpicasso-hermes-jev-approvals/)   | Yes — a custom `base_url` with an optional `key_env`                    | Read in its code and covered by its own boundary test; we did not drive that path |
| [Jev Skills](https://mrjev.com/projects/wuyoscar-jev-skill/)                         | No — an allow-list of exactly two endpoints, both Jev routes            | We tried a third and it was refused, by design                                    |
| [Jev Agent Skill Router](https://mrjev.com/projects/godsboy-jev-agent-skill-router/) | No — one hardcoded endpoint                                             | We had to patch the constant to test it                                           |
| [Jev DSH](https://mrjev.com/projects/devin-axis-jev-dsh-decision/)                   | No — endpoint constant, no override                                     | We injected a fetcher to test it                                                  |
| [jev-seo](https://mrjev.com/projects/akashpriyadarshii-jev-seo/)                     | No — hardcoded constant, no override                                    | We patched the line, then reverted and diffed                                     |
| [jevscan-evm](https://mrjev.com/projects/devtooligan-jevscan-evm/)                   | No — endpoint constant, no override                                     | Same                                                                              |

For tools that need no Jev at all, the whole Open Models & Reproductions section below is that answer: those projects replace the model rather than the route. Two things to check before picking one. First, the weights' licence, not just the repository's — most are MIT or Apache-2.0 on the code, while the weights vary: OpenThai-SystemOne and PlayJev are Apache-2.0 on both with the base model credited, Von's published weights carry no licence tag at all, and NanoJev declares none on either the model or the dataset. Second, what shape it is: several are a library rather than an API, so choosekit reads probabilities out of a backend you already run and ships an MCP server rather than an HTTP one, while OpenThai-SystemOne and others speak `POST /v1/systemone`, which existing SDK code reaches with a base-URL change.

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

- [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe) - Java client for the System One API on Spring `RestClient`, plus Spring AI integrations that use it as a judge, a guardrail, a RAG post-processor and a tool index.
- [typesafe_sdk](https://github.com/nshkrdotcom/typesafe_sdk) - Elixir SDK for the System One API.
- [typesafe-sdk-java](https://github.com/kgonia/typesafe-sdk-java) - Zero-dependency Java client (Java 21+).
- [typesafe-go](https://github.com/Shubham510/typesafe-go) - Go client.
- [kunobi-jev](https://github.com/kunobi-ninja/kunobi-jev) - Rust client, published on crates.io.
- [typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) - .NET SDK.
- [TypeSafe Swift SDK](https://github.com/krzyzanowskim/TypeSafe) - SwiftPM client whose behaviour follows the official JavaScript SDK.

## Libraries & Integrations

- [pijev](https://github.com/TypeLLM/pijev) - Drop-in wrapper for the official Python SDK that asks each question in several option orders and averages the answers, so a decision does not move when the options are shuffled.
- [system-one](https://github.com/iamaamir/system-one) - Provider-neutral TypeScript runtime for typed decisions: the same call runs against Jev, a local implementation, or any `/v1/systemone` endpoint. No licence file.
- [Jev-Mem](https://github.com/libingzheren/Jev-Mem) - Memory layer for long-running agents that routes the frequent memory-management decisions to Jev and leaves the deeper reasoning to the LLM. Comes with a paper.
- [typesafe.pro](https://github.com/chigwell/typesafe.pro) - The full server behind `api.typesafe.pro`, a free anonymous front door that speaks Jev's request shape and forwards to TypeSafe on the operator's own key. AGPL-3.0, so you can run it yourself.
- [jev-cookbook](https://github.com/nexibeo/jev-cookbook) - Fifteen runnable recipes calling Jev through OpenRouter - support triage, dedupe, PII column scanning, reranking, moderation and more - each shipping the output it produced beside it.
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
- [System One Harness](https://github.com/HarnessRouter/SystemOneHarness) - Turns a decision model into an agent loop: it compiles the environment's finite action space into typed questions, gates each step by confidence, and records the trace.
- [Hunch](https://github.com/carldaws/hunch) - Probabilistic control flow for Ruby and Rails, with predicates that read like ordinary conditionals.
- [Jevalyn](https://github.com/Ray-Hughes/jevalyn) - Rails-native decision layer with typed results, guardrails, a router and test helpers.
- [feelings](https://github.com/BoundaryML/feelings) - BAML language support for an AI if-statement: `.feels()` as a real, typed method backed by a decision model.

## Agent Integrations (MCP & Skills)

- [TypeSafe skill router](https://github.com/DECRUX9812/typesafe-skill-router) - Hermes Agent plugin that names the one skill worth loading before the model call. Off by default, injects nothing when nothing fits, and does not spend its second request when the first gate is not cleared.
- [typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) - MCP server that lets agents such as Claude Code, Claude Desktop, and Codex call Jev directly for Choice, Score, and Noul decisions.
- [jev-mcp](https://github.com/jkudish/jev-mcp) - Proof-of-concept MCP server with ready-made tools for fact checking, prompt-injection detection, and semantic ranking.
- [askjev](https://github.com/pZacca/askjev) - MCP server published on npm, with setup instructions for Claude Code, Claude Desktop, Cursor, and Codex.
- [jev-eval-mcp](https://github.com/BYK/jev-mcp) - Eval-first MCP server that focuses on knowing whether Jev's answers can be trusted for your task.
- [Building with Jev](https://github.com/dbreunig/building-with-jev-skill) - Agent skill for writing programs that call Jev: question design, state structure, confidence thresholds, and diagnosing wrong answers.
- [Jev Sift](https://github.com/kbhuw/jev-sift) - MCP plugin that asks Jev which files, web pages, or text snippets are relevant to a query, so the agent reads selectively.
- [Jevbridge](https://github.com/tacticocc/Jevbridge) - ACP and MCP adapter that pairs Jev with any LLM agent, including Codex, Claude, Grok, and OpenCode, for typed decisions and computer use.
- [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills) - Bundle of skills that hand an agent's small decisions to Jev: model routing, skill selection, retrieval filtering, compaction, and computer use, with a routing dashboard. Works with Hermes, Claude Code, and Codex.
- [jev-mcp (burnigtm)](https://github.com/burnigtm/jev-mcp) - MCP server whose tools route the next step and decide whether a partner model is needed, for Cursor, Codex, and any MCP client.
- [jevwire](https://github.com/Brainwires/jevwire) - An MCP server, an embeddable decision library, and an escalate-only Claude Code plugin in one repository.
- [pi-jev](https://github.com/TheoOliveira/pi-jev) - Semantic tool routing and skill discovery for the Pi coding agent: Jev picks which inactive tools to activate for the prompt at hand.
- [Awesome Jev Skills](https://github.com/wuyoscar/jev-skill) - Nine installable agent skills — triage, routing, code review, document and UI work — with a catalogue of scenarios to copy.
- [Jev DSH Decision Engine](https://github.com/Devin-AXIS/jev-dsh-decision) - Decision plugin for agent harnesses: Jev picks the tool, skill or owner and scores the output, while the agent keeps planning and execution. Ships for DeepSeek Harness and iPolloWork.
- [Jevify](https://github.com/altryne/jevify) - Agent skill for finding where Jev fits in an existing codebase, designing the typed questions, and measuring whether it helped.
- [lorenzini](https://github.com/Nanako0129/lorenzini) - Claude Code skills that wait for CodeRabbit, Copilot or Codex to finish reviewing a pull request, then judge whether the verdict actually permits a merge.
- [Jev Studio](https://github.com/utk2103/jev-studio) - One pip install for experimenting: MCP tools for Choice, Noul and Score, prompt libraries and a slash command per cookbook recipe.
- [jevvy](https://github.com/PanAchy/jevvy) - Plugins for coding agents, starting with one that auto-approves shell permission requests it judges harmless and passes everything uncertain to the normal flow.
- [JCR (Jev Capability Resolver)](https://github.com/NiazMorshed2007/jcr) - One tool that searches a nested capability tree and hands the agent only the documented commands and context a task needs.
- [jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) - Skills framework for coding agents with typed gates on package choices and task completion.
- [jev-use](https://github.com/shitianfang/jev-use) - Claude Code, Codex and pi plugin that hands the agent steps needing no written output to Jev and leaves the prose to the LLM.
- [hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) - Approvals provider for Hermes Agent: it judges shell commands and refuses every other task, registering no hooks.

## Coding Agents & Developer Tools

- [jev-rules](https://github.com/EliaAlberti/jev-rules) - Scores your standing Claude Code instructions against each prompt and delivers only the ones Jev picks, once per session rather than per message. Ships a pane that shows which rules were chosen.
- [Nerve](https://github.com/keeltrace/hermes-nerve) - Supervisory layer for Hermes agents that adds typed decisions, ranking and verification asynchronously, with Jev authoritative and an open model shadowing it.
- [pi-jev](https://github.com/y0usaf/pi-jev) - Jev as a decision layer for the Pi coding agent in three places: a gate that judges `bash`, `write` and `edit` calls before they run, an output judge that reads what a `bash` call printed, and a tool the model can call directly.
- [matchcn](https://github.com/francesco0242/matchcn) - Semantic index across shadcn-format registries: components are tagged once across six dimensions and committed, and your brief is classified at query time to match against them. Ships as an MCP server.
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
- [perch](https://github.com/lakeday-org/perch) - Semantic linter that reads each method together with its callers and callees before asking about it. Rules are sentences in a YAML file.
- [jev-lint (mizchi)](https://github.com/mizchi/jev-lint) - Checks whether a function does what its name says, whether a comment is still true, and whether a test verifies what it claims, with a cutoff per rule.
- [patdown](https://github.com/tyler-dot-earth/patdown) - Lints a tree against fuzzy rules kept in one markdown file, behind a provider-neutral interface so the judge can be swapped. Its LICENSE is not a recognised open-source license.
- [agent-dispatcher](https://github.com/nahid-sparktales/agent-dispatcher) - Routes a Claude Code or Codex task to one of 27 specialist roles and defines what evidence will count as done.
- [Jot](https://github.com/runta-dev/jot) - A general-purpose agent loop where Jev picks the next move and Jot runs it. No license file at the time of writing.
- [oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev) - Oxlint rules written as plain-English questions about a function, call, JSX element or file, reported when the yes-probability clears your cutoff.
- [Jev Agent Skill Router](https://github.com/GodsBoy/jev-agent-skill-router) - Routes a request to the agent skills it needs, with a confidence floor below which it loads nothing.
- [yummy-pi-extensions](https://github.com/sugarforever/yummy-pi-extensions) - Extensions for the Pi coding agent, each released separately, including a Jev-based model router.
- [JevLoop](https://github.com/zjunlp/JevLoop) - An agent loop whose seven forks are typed decisions rather than LLM calls, keeping the model for writing. Zero runtime dependencies, and the demo runs offline with no key and no install.
- [jev-test-filter](https://github.com/mizchi/jev-test-filter) - Reads a Git diff, scores every test for whether the change can alter its outcome, and prints the arguments your runner already understands. Every failure path runs the whole suite instead, including a diff that did not fit the state budget.

## Guardrails & Safety

- [agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) - MCP proxy that screens a tool call before it runs and the tool result before the agent reads it, combining rules in code with typed judgments. Starts in a shadow mode that blocks nothing.
- [tripwire](https://github.com/noelzappy/tripwire) - Runs seven checks on every LLM response in one Jev call, as AI SDK middleware or an OpenAI-compatible proxy.
- [jev-gates](https://github.com/rashedInt32/jev-gates) - Seven calibrated gates for Claude Code (rules, scope, intent, done, claims, proof, and commit honesty) that escalate but never approve.
- [pi-warden](https://github.com/DevMortimer/pi-warden) - Guardrails for the Pi coding agent. Jev judges every write and edit against the rules in `pi-warden.md`.
- [jev-belay](https://github.com/valentynkit/jev-belay) - Claude Code Stop hook that checks the transcript for evidence before letting a "done" through, and spends one four-question Jev call only when files changed with no passing check since. Fails open on every error path.
- [Abide](https://github.com/coldteadotai/abide) - Hooks into Claude Code, Codex, and OpenCode, and asks Jev one question per rule whether each edit breaks your AGENTS.md or CLAUDE.md rules.
- [jev-guard](https://github.com/leepokai/jev-guard) - Risk-scores every tool call against session context into deny, ask, or allow, and flags prompt injection in tool results.
- [Pi Jev Guard](https://github.com/zszz3/Pi-Jev-Guide) - Pi coding-agent plugin with rules configured by timing, plus risk checks, output redaction, and reminders on repeated failures. Chinese documentation.
- [is-malicious](https://github.com/luantak/is-malicious) - Sends source, configuration, build, and CI files to Jev and points at the files and lines that look deceptive or data-stealing. Its README says a clean report is not proof a project is safe.
- [jevscan-evm](https://github.com/devtooligan/jevscan-evm) - Produces a heat map of likely bugs in EVM code. The author's own warning: a proof of concept whose code they did not read.
- [Jevmind](https://github.com/dealerdefi/Jevmind) - Nine skills over one brain: a shell-command gate, a diff triage, a router and more, each decision appended to a hash-chained ledger that names any record edited afterwards. Runs offline on local reflexes or against Jev.
- [Canny](https://github.com/qkal/Canny) - Stop hook for Claude Code and Codex CLI that refuses a "done" while no check has passed since the last edit. Jev can only relax that refusal and never cause one, and it still blocks with no API key at all.
- [dsh-jev](https://github.com/buberlo/dsh-jev) - Decision layer for DeepSeek Harness whose failure policy rejects the value `allow` at configuration time, from plain JavaScript as well as TypeScript. Its verify script installs the built tarballs into a fresh consumer before testing them.

## Model Routing

- [Astra-Ares](https://github.com/miuuyy/Astra-Ares) - Adjusts a Codex task's reasoning effort mid-run by asking Jev how hard the next step looks. Runs a patched Codex CLI and says it is a reference implementation rather than an app.
- [Agent Orchestration SDK](https://github.com/masonlee39/Multi-Agent) - Orchestration engine for multi-agent work with durable mailboxes and warm sessions, routing each task with a typed decision instead of a manager LLM.
- [jev-router](https://github.com/gargpratyush/jev-router) - Per-turn model routing for Claude Code and Codex. Simple work goes to the fast tier and difficult work to the strong tier.
- [tiershift](https://github.com/iamvatsalpatel/tiershift) - Sends each LLM request to the cheapest model tier that can handle it and escalates on evidence.
- [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) - Neon Function proxy for the Neon AI Gateway. Jev classifies each request and routes it to the right downstream model.
- [jev-gateway](https://github.com/vinilana/jev-gateway) - Local gateway for Codex and Claude Code that asks Jev which tool to call next and passes everything else to your usual model.
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Routes each agent step to a model, subagent, Skill, MCP tool, or CLI with one Jev Choice, requiring confirmation for risky capabilities and keeping decision receipts.
- [Grok Bot Jev Router](https://github.com/Bodila51/grok-bot-jev) - Classifies a Grok Bot request before expensive research, browser, retry, or subagent work, so it can reuse a fresh artifact or stop a failing retry.
- [pi-jev-router](https://github.com/philippdubach/pi-jev-router) - Ranks the OpenRouter catalogue per task, takes the Pareto frontier over quality, cost and latency, and routes pi to the knee point.
- [Helm](https://github.com/Jimuelle07/Helm) - Picks which of the coding agents on your machine should take a task, from an answer set a probe builds, so an agent you have not installed cannot be recommended. Installs as a Claude Code plugin, a Gemini CLI extension, or an Agent Skill.

## Command-Line Tools

- [jsort](https://github.com/keltokhy/jsort) - Sorts lines along a plain-English dimension by judging them in pairs, so the sort key is a description rather than a field.
- [jev (shaharia-lab)](https://github.com/shaharia-lab/jev-cli) - Rust CLI whose exit codes separate a false gate from an answer inside your abstain band, so a script can take a third branch and ask a person. Lints the request before it spends anything.
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
- [JevGrep](https://github.com/nassim-arifette/jevgrep) - Semantic code search for agents, as a CLI or MCP server: ask what the code does and get source excerpts with paths and line numbers.
- [evoke](https://github.com/evoke-build/evoke) - Turns a sentence into a call of a small program you installed from Git, run only when the confidence gate allows. A CLI, a package manager for those recipes, and a TypeScript SDK over the same core; your overlay may tighten a reflex's effect but never loosen it.
- [slop-grader](https://github.com/lukstei/slop-grader) - Grades prose against twenty-one named writing tics, asking every rule about every line, and writes its findings as a brief for a coding agent to act on.
- [jgrep (kyu1204)](https://github.com/kyu1204/jgrep) - Semantic grep that packs sixteen chunks and sixteen questions per request, with grep's exit codes and a `--diff` mode for linting a change against a rule written in English.
- [webctl](https://github.com/dorkitude/webctl) - Search CLI for agents: results from up to three backends are scored by Jev against your query and an explicit `--goal`, and only the relevant ones reach the agent's context. Its benchmark excludes an arm it could not observe.
- [jev-cli (tumf)](https://github.com/tumf/jev-cli) - CLI and stdio MCP server for the three Jev primitives, with `--value` for shell scripts and structured stderr errors. `auth set` refuses a key as an argument, keeping it out of shell history.

## Browser & Computer Use

- [jev-browser-skill](https://github.com/hqman/jev-browser-skill) - Agent skill that drives an isolated Playwright Chromium: the agent sets a narrow goal and Jev chooses the in-page actions. Vercel AI Gateway by default, TypeSafe optional.
- [Jev Voice](https://github.com/ronadin2002/jev-cua) - Floating bar for macOS that takes a voice or text command and picks the next action from the Mac's live accessibility controls, looping until the goal is met.
- [Jev Browser Use](https://github.com/wy-coliney/jev-browser-use) - Browser skill that splits the work: Jev handles navigation, clicks, toggles and scrolling while the coding agent thinks and verifies. Uses your existing browser connection, with no extra driver.
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
- [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) - Browser agent that indexes the page into candidates for Jev to pick from, leaves planning and reading to an LLM, and cites a quote from the page for every claim.
- [Jev Social](https://github.com/socai-io/jev-social) - Instagram, TikTok and LinkedIn research where Jev chooses each next operation and a real Chrome session executes it, with the evidence kept.
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) - Manifest V3 port of jev-ultrafast that drives the tab you are already looking at, keeping the same observation format and execution rules.

## Data & Observability

- [pg-jev](https://github.com/realZachi/pg-jev) - PostgreSQL extension to filter, rank, and classify rows with plain-language conditions.
- [jevql](https://github.com/kylemclaren/jevql) - A psql-shaped CLI and Go/TypeScript/Python SDKs that add `jev()`, `jev_prob`, `jev_choice`, and `jev_score` to queries against a vanilla Postgres with no extension. The SQL runs on the server and Jev judges the surviving rows in batches.
- [duckdb-jev](https://github.com/colliber/duckdb-jev) - DuckDB extension that returns Jev's answers as real SQL types.
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores OpenTelemetry logs for diagnostic value, priority, and routing before expensive LLM analysis.
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL extension that calls Jev from SQL for Choice, Noul, and Score, with `EXECUTE` revoked from `PUBLIC` by default.
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Classifies tax-document pages into IRS forms and page kinds with one Jev request per page, driven by a JSON file of form descriptions.
- [doc-router](https://github.com/misbahsy/doc-router) - Rust tool that asks Jev which PDF pages actually need OCR, extracting text pages locally and sending only the rest to your OCR provider.
- [DocJev](https://github.com/jerryjliu/docjev) - Classifies and splits PDF, DOCX and PPTX with Jev and local OCR, asking one typed question per page and per boundary in a single request. Ships the manifest, per-call records and error analysis behind its benchmark.
- [Jeview](https://github.com/andududu/jeview) - Local gateway and live map of every Jev call your code makes, in one dependency-free file. It holds the key itself: a caller's own bearer token is dropped rather than forwarded, and with no key set it will not proxy at all.
- [jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed) - Packs many items into one Jev request for bulk classification. If any item in a pack comes back unanswered it raises and names the item rather than returning a partial result.
- [jevframe](https://github.com/ktaletsk/jevframe) - A `.jev` accessor for pandas and Polars: the request is built from the columns you name and nothing else in the row, and a failed row raises naming the row instead of becoming a null.
- [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) - Rust pipeline that sifts JSONL and Parquet rows against reasoning rubrics, emitting records verbatim with a rejection log that names the question, the probability and the ceiling crossed.

## Search & Knowledge Graphs

- [Jev Search](https://github.com/superagents-lab/jev-search) - Search the web in plain language: Jev answers typed questions about your request, and the app uses those judgments to pick the query, the sources and the time range before ranking what comes back. Installable from the browser as an app.
- [Blink](https://github.com/ellipsis-dev/blink) - Semantic codebase search. At each directory level Jev ranks which files and folders are most likely relevant and sends more walkers there.
- [neo4jev](https://github.com/jexp/neo4jev) - Navigates a Neo4j graph by having Jev score neighbouring relationships, then beam-searching for the most probable path.
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - Neovim plugin that splits the buffer into functions with Treesitter, has Jev score each one against a plain-language question, and lists the answers in the quickfix window ranked by probability.

## Apps & Browser Extensions

- [Jev × WebMCP](https://github.com/sdras/jev-webmcp-extension) - Chrome extension that discovers the WebMCP tools a page exposes and has Jev choose which one a sentence means, then fills in its arguments.
- [changelog.earth](https://github.com/byalex33/changelog.earth) - Treats the planet as software under maintenance: real reporting sorted into new species, balance changes and unresolved bugs, with typed decisions doing the sorting.
- [JevIntent](https://github.com/Nisaka520/JevIntent) - WeChat plugin that reads intent, tone and reply posture from a long-pressed message and shows the verdict locally. Sends nothing and changes no chat history. Chinese.
- [jev-哑巴微信](https://github.com/wuxie888/jev-yaba-wechat) - macOS helper beside the WeChat window: an LLM drafts several possible replies and Jev scores them, leaving you to press send. Chinese.
- [Jev demos](https://github.com/mayank953/Jev) - Seven side-by-side demos that run with no keys and label themselves simulated. Each visitor's key gets its own budget by fingerprint, and any key is redacted out of upstream errors.
- [Passage (Working Memory Jev)](https://github.com/AustinAWay/Working-Memory-Jev) - Localhost tool for educators that flags where instructional text may ask a reader to hold too many ideas at once. Its evaluation opens by naming the two tests its own model fails. Custom licence, not open source.
- [RikkaHub Plus](https://github.com/MiaoWuNYA/rikkahub-sillytavern-android) - Android chat client with a built-in Jev client: it scores stored memories for relevance in batches before retrieval, and exposes Jev to the model as a callable judgment tool. Endpoint and key are set in its settings. Chinese documentation.
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
- [dasheng](https://github.com/wquguru/dasheng) - Read English aloud and see which words were wrong: streaming speech recognition transcribes, Jev judges word by word, and both models can run on your own GPU.
- [Vibe Check for X](https://github.com/RafalWilinski/vibecheck) - Chrome and Firefox extension that scores a draft X post on a dozen dimensions and gives a send-or-don't verdict before you publish.
- [Crush Monitor](https://github.com/FerryCorleone/crush-monitor) - Reads a WeChat conversation and labels each message with emotion and intent, rating how your own replies landed. Local, with your own key.
- [Jevmail](https://github.com/fazlerocks/jevmail) - Read-only Gmail triage that sorts an inbox into five trays with an urgency score, running locally through a gateway key.
- [Call Coach](https://github.com/ZeroGold/call-coach-ai) - Listens to a live sales call and, after each sentence, tells the rep what to do next with a confidence score.
- [Jev Explained](https://github.com/davila7/jev-explained) - Interactive playground that walks through a typed request and its probabilities, with your own key.
- [jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier) - Config-driven inbox classifier that tags, moves, flags and notifies from typed answers.
- [Jeved](https://github.com/mossyfield/ST-jeved) - SillyTavern extension that asks your own questions about each reply and, when a rule matches, adds a line to the prompt, rerolls, or runs a script.

## Evaluation & Benchmarks

- [PZ_Optimization](https://github.com/xD3I/PZ_Optimization) - Performance work on a game, notable here for the harness: the arithmetic and the noise floors are computed in code, and Jev is asked only for the verdict on what the numbers mean. No licence file.
- [jevcal](https://github.com/abhixhek/jevcal) - Picks the confidence threshold that meets your accuracy target on your own data, and fails CI when a model update breaks it.
- [Janus](https://github.com/FirasSX914/Janus) - Measures Jev's calibration and confidence-based routing on Banking77 and Web of Science.
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) - Probability-aware evaluation: calibration, and how much work can be automated at a fixed error budget.
- [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - Compares LLM structured output with Jev on latency, cost, and judgment quality.
- [Jev Capability Atlas](https://github.com/Zaious/jev-capability-atlas) - A bilingual map of where Jev holds up and where it breaks, built from recorded API calls rather than a leaderboard. Its LICENSE is not a recognised open-source license.
- [jev-align](https://github.com/sutro-sh/jev-align) - CLI from Sutro that finds the examples a Jev function is least sure about, asks you to label them, and uses GEPA to improve the question.
- [JevBench](https://github.com/fstandhartinger/jevbench) - Benchmark for typed decision models across several suites, with confidence cascades and committees reported separately.
- [jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark) - Reproducible experiments on whether reranking with Jev improves a small RAG system, on a locked Turkish dataset, with quality, latency and cost reported together.
- [Jev vs. ML](https://github.com/QuicqDev/Jev-vs-ML) - Compares a typed decision model with classical classification pipelines across eight datasets, with a published protocol and an interactive report.
- [jevals](https://github.com/openlayer-ai/jevals) - Agent evals and guardrails as typed questions instead of an LLM judge, packing every eval for a trace into one request. From Openlayer, with a mock backend so the whole library runs without a key.
- [jev-calibrate](https://github.com/smkrv/jev-calibrate) - Checks a Jev question against your own labelled examples and grades it: act on it, only sort by it, or rewrite it. Refuses to grade a question whose classes have too few examples, however good the numbers look.

## Open Models & Reproductions

- [AgentJev](https://github.com/malevrigns/agent-jev) - A 0.6B decision model on a Qwen3 backbone with weights on Hugging Face: state in, a distribution over your options out, nothing decoded.
- [OpenJev-Vision](https://github.com/IamBusy/OpenJev-Vision) - Encodes an image once and answers several typed questions from the shared distribution. Ships synthetic scenes, trained readouts, a dataset and reproducible evaluations.
- [NotJev](https://github.com/9pings/notjev) - Serves the Jev request shape from any OpenAI-compatible endpoint by presenting options as single letters and reading the letter mass out of `logprobs`.
- [FastJev](https://github.com/chengyongru/fastjev) - An independently maintained SemIf fork packaged SDK-first, for deploying an open decision model on your own infrastructure.
- [JevForge](https://github.com/zwliJay/jev-forge) - End-to-end toolkit for the other direction: synthesise decision data, train a calibrated candidate scorer on it, evaluate it, and serve it behind a Jev-compatible endpoint.
- [jevify](https://github.com/fidecastro/jevify) - Makes a model you already serve answer typed questions in one pass the way Jev does, and measures how well it manages it.
- [decider](https://github.com/Mapika/decider) - A family of System One-style models that never generate text: one forward pass over a state and typed questions returns a probability distribution per question. Ships ten text games and a Super Mario Bros agent where each move is one typed decision over the legal actions.
- [reflex](https://github.com/kshetrajna12/reflex) - A small open decision model for your own GPU: fixed answer options in, per-option percentages out, with no free text so it cannot answer off the list.
- [Jev Visual](https://github.com/hr98w/jev-visual) - Multiple typed questions about one image in a single pass, on Qwen3.5-0.8B with MLX on Apple Silicon. States plainly that it explores the pattern and does not claim to reproduce Jev's architecture or training. Chinese and English.
- [Laya](https://github.com/NandhaKishorM/laya) - Non-autoregressive decision engine over 100+ languages: three checkpoints and a router that detects the script and dispatches per request. Its benchmarks end with a limits section naming the datasets it does not generalise to and the headline figure that came from a training split.
- [JEV-CPU](https://github.com/leesk212/JEV-CPU) - A CPU port of SemIf that swaps only the model loader and reuses the scoring code unchanged, so you can read a decision out of a small model's option logits on a laptop with no GPU.
- [Dev-0.4B](https://github.com/mpnikhil/dev-0.4b) - A 399M bidirectional encoder with one universal choice head, answering Choice, Noul and Score in a single forward pass. Every README figure reconciles to an evaluation JSON shipped in the repository.
- [Dohnuts](https://github.com/PsiACE/dohnuts) - Small multimodal models for direct decisions on text, documents and images. Its model card publishes the benchmark it loses and states that its confidence field is not a measured probability of correctness. Weights are CC BY-NC-SA.
- [Open Spark Jev](https://github.com/abhishek085/open-spark-jev) - A local decision model for NVIDIA DGX Spark, labelled from policy engines and solvers rather than an LLM judge. Its evaluation protocol records the time its own corpus leaked most of the test set into training.
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
- [AnyJev](https://github.com/nokia-applied-research/AnyJev) - Turns any open-weights LLM into a typed decider by averaging the option logits over permutations and subtracting a label-free prior, so the answer barely moves when you reorder the options.
- [JevBERT](https://github.com/hawkymisc/typed-decision-bert) - A local server that speaks Jev's `/v1/systemone` shape from a BERT encoder, with a numbered account of every request it refuses that Jev might accept.
- [DeepOpen](https://github.com/deepopen-com/deepopen) - A router and presets over Convai's Laya checkpoints, packaged as its own engine.
- [OpenJevPro](https://github.com/zhangcy122/OpenJev) - Asks an Ollama or OpenAI-compatible model to write a likelihood score per candidate, then softmaxes them with a fixed temperature. PolyForm Noncommercial, not an open-source licence.
- [solar-mini4-jev](https://github.com/hunkim/solar-mini4-jev) - Puts Upstage's Solar Mini4 behind Jev's `/v1/systemone` shape, bring your own Upstage key. Its benchmark grades against a third-party judge rather than a peer model's answers, and every published figure recomputes from the artifacts committed with it.
- [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) - A 151M non-autoregressive decision model on ModernBERT with calibrated uncertainty and an in-browser WebGPU playground. Its LICENSE is not recognised as the Apache 2.0 its badge claims.
- [OpenDecision](https://github.com/deepanwadhwa/OpenDecision) - Open-source semantic decision engine: state, a question in natural language, and answer criteria in; a structured decision out.
- [Open Alternative to Jev](https://github.com/ikermoel/open-alternative-jev) - Typed, calibrated decisions from any open-weights model in one forward pass, as the Python package `open-alternative-jev`.
- [choosekit](https://github.com/NotXf1le/choosekit) - Scores a finite set of choices against a model you already run and returns a typed decision with a probability distribution, from text or images. Backends for llama.cpp, Ollama and OpenRouter, and a `choosekit-mcp` package exposing the same choice as one read-only MCP tool.
- [Jev Local](https://github.com/Argos1111/jev_local) - A local `/v1/systemone` server with two backends: an LFM model zero-shot, and a fine-tuned ModernBERT-Ja cross-encoder. Japanese documentation.
- [LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) - Adapts a local language model into a Jev-style decision engine, answering runtime-defined Choice, Score and Noul questions through SGLang.
- [Laya for Node](https://github.com/receptron/laya) - Runs Laya, an open Jev-compatible System One model, from Node.js and TypeScript through ONNX Runtime.
- [OpenJev (SiliconLabAI)](https://github.com/SiliconLabAI/OpenJev) - Approximates the System One contract on top of any logprob-capable model: a fixed answer space, each option scored independently, all questions in parallel.
- [Open Jev (intikhab49)](https://github.com/intikhab49/open-jev-typed-decision-engine) - A 150M encoder trained to answer typed questions in one pass, with the training notebook written to run on a free GPU.
- [OpenSourceJev](https://github.com/sabeel111/OpenSourceJev) - Research experiment in local System One decisions through llama.cpp logits projection on consumer hardware.
- [OpenThai-SystemOne](https://github.com/iapp-technology/openthai-systemone) - Thai and English decision model with a slot-softmax head whose request and response shape mirrors the official API, so existing SDK code can point at it.
- [PlayJev](https://github.com/OmniJev/PlayJev) - Multimodal decision model that plays browser games from raw pixels, with weights and a hosted demo.
- [djev-run](https://github.com/taeold/djev-run) - Serves DiffusionGemma-Jev behind a compatible API on Cloud Run, with a small game demo on top.
- [Rizzo Flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) - Local typed decisions from Spark-X2.5-4B over llama.cpp, serving both its own schema and Jev's `/v1/systemone`. Its `/v1/models` alias says in its description that it is not answered by Jev, and every published result names its dataset by hash.

## Games & Real-Time Demos

- [Laya vs Jev Arena](https://github.com/PromptEngineer48/laya-vs-jev-arena) - A local open model and the hosted one play a snake race and a fighting game against each other, every move a real decision rather than a script.
- [is-jeven](https://github.com/wobsoriano/is-jeven) - Answers whether a number is even by asking a decision model. The joke is the point, and it is a three-line look at the request shape.
- [Jev experiments](https://github.com/dabit3/jev-experiments) - Latency-focused demos from Nader Dabit, each app in its own directory with its own README. No licence file at the time of writing.
- [Jev Tetris](https://github.com/trungdq88/jev-tetris) - Two models play Tetris on a shared seeded piece sequence under the same clock; a piece that lands before the answer arrives locks where it fell. No licence file.
- [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev) - Three.js quickscope arena where Jev decides movement, aiming, ADS, firing, and jumping at roughly 9 Hz.
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Jev picks NES controller inputs for Super Mario Bros. from emulator state, with no screenshots.
- [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) - Jev plays the first StarCraft shareware mission, with its recorded action probabilities.
- [Jev Pong](https://github.com/ably-labs/jev-pong) - Pong where the ball moves one step per model decision, pitting Jev against chat LLMs.
- [JevPilot](https://github.com/standardagents/jevpilot) - Three.js driving simulator with a Jev-powered autopilot.
- [jev-drone](https://github.com/RomanSlack/jev-drone) - Camera-only quadrotor in MuJoCo with Jev making judgment calls at about 2.5 Hz.
- [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) - Recorded chess experiments with a candid result: Jev on its own still blunders pieces.
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) - Pokemon Red on PyBoy where code owns the route and the arithmetic and Jev only picks at branches, logging a Brier-scored faint prediction against RAM state on every battle turn.
- [Jev Self-Driving Sim](https://github.com/vinilana/live-jev) - A 2D top-down car in the browser that turns its sensors into a JSON state every 200 ms and executes four typed answers. No license file at the time of writing.
- [jevchat](https://github.com/kyle-pena-nlp/jevchat) - Turns a decision model into a chat model by asking which symbol comes next, then sampling from the returned distribution.

## Robotics & Embodied

- [RoboDiag Harness](https://github.com/YueBit/robodiag-harness) - Command-line diagnostics for ROS 2 robots: an evidence-gathering agent whose tool calls are gated by typed decisions before anything touches the robot.
- [EmbodiedJev](https://github.com/FBddcz/embodied-jev) - MuJoCo robot decision workbench in the browser: three simulation tasks, a local small model or a hosted API, and every observe-decide-act step shown.
- [jev-libero](https://github.com/Dimweaker/jev-libero) - Fine-grained robot control on LIBERO tasks with physics previews and configurable task definitions.
- [Jev Reflex Autonomy Lab](https://github.com/khordoo/jev-reflex-autonomy-lab) - Multi-drone simulation where typed reflexes fly the fleet and an optional slower planner may advise but never takes control.
- [RoboJEV](https://github.com/lykycy123/RoboJEV) - Two-stage control of a Franka Panda in MuJoCo from structured simulator state, with physical success checks the model cannot declare for itself.

## Finance

- [BTC 5m Decision Lab](https://github.com/frankda/jev-poly-crypto-demo) - Research tool for Polymarket's BTC 5-minute markets: Jev scores the direction, separate code decides the entry, and any TRADING_MODE other than paper throws at startup. No licence file.
- [Prism](https://github.com/irfndi/prism-liquidity-agent) - Liquidity-provision agent for Meteora DLMM. Jev judges toxic flow, market stress, and mean-reversion likelihood in shadow/advisory mode only, without driving trades. Not financial advice.
- [jev-trader](https://github.com/jarrodwatts/jev-trader) - Asks Jev buy or sell on every Monad block and places real post-only limit orders on the Kuru MON-USDC book. Not financial advice.
- [Jev Trade](https://github.com/aowang-ai/jev-trade) - Hyperliquid trading bot based on jev-trader, where Jev decides buy, sell, or hold on every tick for five coins. Dry-runs without a private key.
- [Jev X Sentiment Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) - Crypto terminal that reads up to 1,000 posts about a ticker alongside market and funding data and turns them into a buy, sell, hold, or take-profit call. No license file at the time of writing. Not financial advice.
- [Jevinik](https://github.com/unicodeveloper/jevocks) - Stock decision terminal that gathers live market evidence and returns a typed view on the next thirty days, with the sources it used.
- [jev_stock](https://github.com/sosopop/jev_stock) - Experiment in forecasting Hong Kong stock direction: it builds a past-only state from market data, asks for an up, flat or down call, and renders a standalone report.

## Articles & Analysis

- [Jev: The Language Model That Won't Talk](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont) - Critical look at the "no hallucination" and benchmark claims.
- [A deep dive into Jev](https://flaviocopes.com/jev/) - Hands-on developer walkthrough.
- [Jev: TypeSafe's System One Model That Never Hallucinates](https://www.datacamp.com/blog/system-one-models-jev) - Overview from DataCamp.
- [TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) - Launch coverage from The Register.

## Related Lists

Other community lists of Jev projects, each with its own scope and bar:

- [kydlikebtc/awesome-jev](https://github.com/kydlikebtc/awesome-jev) - Examples indexed by the decision each one makes, with runnable code beside them.
- [Amal-David/awesome-jev](https://github.com/Amal-David/awesome-jev) - Demos, projects, SDKs and skills, with a curated gallery alongside.
- [awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) - Broad list with decision tables and a use-case map.
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) - Category files with written inclusion criteria.
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) - Large list with sourced research notes.
- [fatwang2/awesome-jev](https://github.com/fatwang2/awesome-jev) - Uses Jev itself to review incoming pull requests.
- [awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) - Structured metadata per entry, in four languages.
- [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) - The largest list, with a searchable site.
- [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) - Tools only, no articles or models.
- [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) - Resources paired with runnable examples.
- [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) - Chinese-language list, refreshed daily.
- [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery) - Papers, open reproductions and independent evaluations.
- [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) - Source-backed field guide, pairing SDKs and demos with independent evaluations.
- [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev) - Catalogue with a stated star threshold, reviewed through pull requests, plus a live gallery.
- [awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live) - Index rebuilt automatically every few hours with no curation threshold, so it is far larger and unfiltered.
- [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) - Applications, libraries, tools and research, in English and Chinese.
- [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) - Large table of projects with stars, language and last-commit date, plus a searchable site.
- [Promethe-us/awesome-jev](https://github.com/Promethe-us/awesome-jev) - Official material, community projects and research, with its sources tracked in a separate file. Bilingual.
- [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) - Demos grouped by use case, with notes on writing criteria and setting thresholds.
- [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) - Use cases with every headline figure tagged self-reported or independent.
- [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) - Use cases paired with patterns and written guidance for building on them.
- [Jev Directory](https://github.com/everyai-com/jev-directory) - Runnable evals and community builds, also served to agents as an MCP server and an `llms.txt` index.
- [JEV HUB](https://github.com/mizzlelover/jev-hub) - Long posts and demo videos from X, each kept as a link to the original rather than rehosted. Chinese.
- [Jev Radar](https://github.com/everyinfra/jev-radar) - A tracked casebook of the ecosystem, kept as a live monitor. Bilingual.
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) - Use cases, projects, SDKs and learning resources in one curated list.
- [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) - Organised by the coding agent you use, with a short primer before the entries.

## Contributing

Contributions are welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
