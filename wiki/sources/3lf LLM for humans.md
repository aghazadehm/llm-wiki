---
type: source
status: draft
title: "3lf LLM for humans"
tags:
  - llm
  - prompting
last_updated: 2026-10-11
---

# 3lf LLM for humans

**"3lf LLM for humans"** (به زبون آدمیزاد LLM آموزش) is a free, self-published Persian-language guide to working with large language models, written for a non-expert audience and updated June 2026. It walks from the fundamentals — tokens, embeddings, next-token prediction — through prompt techniques, sampling parameters, direct API use, tools and function calling, RAG, context engineering, fine-tuning, evaluation, security, and choosing and paying for models, with runnable Python examples throughout. The vault's entire `llm` domain is synthesized from it.

## What it covers

The book is organized as a beginner's tour rather than a reference. Its fundamentals section explains how a model turns text into tokens, how tokens become meaning-bearing embeddings, and that generation is next-token prediction under a few architecture names (Transformer, attention, decoder-only). The prompting section builds from a four-part structure (role, goal, constraints, input) to advanced techniques: separators, output formatting, tone, conditioning before the instruction, few-shot examples, chain-of-thought, and retry-and-improve. It then covers the sampling parameters (temperature, top-p, top-k, penalties, max tokens, stop sequences, seed), system prompts, and direct API calls to OpenAI, Anthropic, and Google, including streaming.

The later sections move to tools and function calling, autonomous agents, RAG (architecture, embedding models, vector databases, chunking, retrieval strategies, and a LangChain example), context engineering, fine-tuning, output evaluation, hallucination and prompt-injection security, Persian-specific tokenization notes, cost management, model selection, and running models locally with Ollama or LM Studio. A closing bilingual glossary maps each Persian term to its English form.

## Related Concepts

- [[Tokenization]] — how text becomes the model's unit of work.
- [[Embedding]] — the numeric form that makes similarity and retrieval possible.
- [[Next Token Prediction]] — the generation mechanism the book builds from.
- [[Prompt Engineering]] and [[Few-Shot Prompting]] — the prompting techniques, from structure to examples.
- [[LLM Parameters]] — temperature, top-p, top-k, and the sampling controls.
- [[Function Calling]] and [[AI Agents]] — giving the model tools and letting it act.
- [[RAG]] — the retrieval-plus-generation pattern, with its vector-database machinery.
- [[Fine-Tuning]] and [[LLM Evaluation]] — adapting a model and measuring its output.

## My Understanding

The book is a survey, not a source of argument: it presents techniques and trade-offs but takes no side in the debates the vault records elsewhere (for example, it explains RAG and fine-tuning side by side without settling when each is the right call). Its value to the vault is breadth and its bilingual glossary, which keeps the Persian prose and the English navigation terms in step. Where the book is dated by design — model names and prices are "a snapshot" of June 2026 — the vault notes the date rather than treating a figure as current.

## Sources

- 3lf, *LLM به زبان آدمیزاد (Teaching LLM in Persian)*, GitHub, 2026. `raw/books/3lf_llm-for-humans_ به زبون آدمیزاد LLM آموزش _ Teaching LLM in Persian.md`
