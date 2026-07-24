from __future__ import annotations

import re
from pathlib import Path

INDEX_PATH = Path("index.html")


def replace_literal(text: str, old: str, new: str, label: str) -> str:
    """Replace one known fragment, while remaining safe on repeated workflow runs."""
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"Could not locate expected {label} fragment")


def main() -> None:
    text = INDEX_PATH.read_text(encoding="utf-8")

    text = replace_literal(
        text,
        "<title>Srija Harshika | Senior Product Manager · AI/ML</title>",
        "<title>Srija Harshika | Senior Product Manager (AVP) · GenAI & Document Intelligence</title>",
        "page title",
    )
    text = replace_literal(
        text,
        '<meta name="description" content="ISB MBA Product Manager building GenAI products at scale (JIA agentic assistant, RAG, guardrails, evals).">',
        '<meta name="description" content="Senior Product Manager (AVP) with 7+ years building 0→1 GenAI, agentic AI, document-intelligence and FinTech products across regulated enterprise and consumer scale.">',
        "meta description",
    )
    text = replace_literal(
        text,
        "🎓 <span class=\"font-medium\">ISB MBA — Strategy & Leadership, Marketing</span>",
        "🎓 <span class=\"font-medium\">ISB PGP — Strategy & Leadership / Product Management</span>",
        "education badge",
    )
    text = replace_literal(
        text,
        "Senior Product Manager · <span class=\"text-brand-600\">AI/ML</span>",
        "Senior Product Manager (AVP) · <span class=\"text-brand-600\">GenAI & AI Products</span>",
        "hero heading",
    )
    text = replace_literal(
        text,
        "AI-first PM with 6+ years across cloud, telecom, and fintech. Built the JIA agentic assistant and GenAI platform (RAG, guardrails, evals) used across 20M+ devices.",
        "Senior Product Manager with 7+ years building 0→1 GenAI, agentic AI and FinTech products across regulated enterprise and consumer scale—driving 35% accuracy gains, 40%+ lower manual workflows, 50% support deflection and 38% lower acquisition risk.",
        "hero summary",
    )
    text = replace_literal(
        text,
        """          <span class="chip">GenAI · Agents</span>
          <span class="chip">RAG · Gemini · LangChain</span>
          <span class="chip">Evaluation & Guardrails</span>
          <span class="chip">0→1 Delivery</span>""",
        """          <span class="chip">GenAI · Agentic AI</span>
          <span class="chip">Document Intelligence · STP</span>
          <span class="chip">Evaluation · Guardrails · Governance</span>
          <span class="chip">0→1 Product Strategy</span>""",
        "hero capability chips",
    )

    jpmc_block = """<article class="reveal mt-6 p-6 rounded-2xl border border-slate-200 bg-white/85 shadow-soft">
      <header class="flex items-start justify-between gap-4">
        <div>
          <h3 class="font-semibold text-lg">Senior Product Manager, GenAI &amp; Document Intelligence, Lending (AVP) — JPMorganChase</h3>
          <p class="text-sm text-slate-600">Dec 2025 – Present</p>
        </div>
        <a href="./Srija_Harshika_Resume.pdf" class="text-sm underline opacity-80 hover:opacity-100" target="_blank" rel="noopener">Full resume</a>
      </header>
      <ul class="mt-4 grid md:grid-cols-2 gap-3 text-slate-700">
        <li>Owned the end-to-end roadmap for DARwin across OCR, classification, extraction and human-in-the-loop review, improving extraction accuracy by 35% and reducing manual review effort by 40%+.</li>
        <li>Engineered field-level validation using model-confidence thresholds, business rules and source-of-record checks, cutting false positives by 20%+ and document turnaround time by 30%.</li>
        <li>Defined the straight-through-processing vision, eligibility logic, risk thresholds and seven operational KPIs, with a phased roadmap targeting 50%+ auto-pass while preserving precision, traceability and auditability.</li>
        <li>Redesigned an approximately 10-day manual onboarding process into a five-stage AI-assisted workflow spanning schema discovery, template creation, coverage validation, prompt refinement and testing, targeting completion within one sprint.</li>
        <li>Architected exception-led review for borrower/co-borrower mapping and low-confidence routing, strengthening consistency and audit traceability across four critical operational controls.</li>
        <li>Defined a Smart Review Assistant that classified source-of-record comparisons as exact, different or approximate matches, improving reconciliation consistency and reviewer decision quality.</li>
        <li>Aligned six stakeholder groups through PRDs, customer journeys, governance controls and phased releases across product accuracy, compliance, model risk and operations.</li>
      </ul>
    </article>"""

    if "Owned the end-to-end roadmap for DARwin" not in text:
        work_pattern = re.compile(
            r"(\n\s*<!-- WORK -->\s*\n)\s*<article class=\"reveal mt-6 p-6 rounded-2xl border border-slate-200 bg-white/85 shadow-soft\">.*?</article>\s*(\n\s*<section id=\"work\")",
            re.DOTALL,
        )
        text, count = work_pattern.subn(
            lambda match: match.group(1) + "    " + jpmc_block + match.group(2),
            text,
            count=1,
        )
        if count != 1:
            raise RuntimeError("Could not replace the JPMorgan experience block")

    featured_post = """<article class="reveal reveal-delay-2 blog-card p-8 rounded-3xl border border-slate-200 bg-gradient-to-br from-indigo-50 via-white to-cyan-50 shadow-soft">
          <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
            <div class="flex-1 max-w-none">
              <div class="flex items-center gap-3 mb-4">
                <span class="px-3 py-1 text-sm rounded-full bg-gradient-to-r from-indigo-600 to-cyan-600 text-white font-medium shadow-lg pulse-glow">🆕 New Article</span>
                <span class="text-sm text-slate-500 text-slate-600">July 24, 2026</span>
              </div>
              <h3 class="text-2xl lg:text-3xl font-bold mb-4 text-slate-900 leading-tight">From 10-Day Onboarding to One Sprint: Designing Straight-Through Processing for Document Intelligence</h3>
              <p class="text-lg text-slate-700 leading-relaxed mb-6">A product framework for field-level validation, exception-led review, measurable quality gates and safe automation in regulated document workflows.</p>
              <div class="flex flex-wrap gap-2 mb-6">
                <span class="tag px-3 py-1 text-sm rounded-full bg-indigo-100 text-indigo-800 font-medium">Document Intelligence</span>
                <span class="tag px-3 py-1 text-sm rounded-full bg-emerald-100 text-emerald-800 font-medium">STP</span>
                <span class="tag px-3 py-1 text-sm rounded-full bg-cyan-100 text-cyan-800 font-medium">Regulated AI</span>
              </div>
            </div>
            <div class="flex flex-col items-start lg:items-end gap-4 lg:text-right">
              <div class="flex items-center gap-1 text-sm text-slate-500 text-slate-600">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/>
                </svg>
                <span>7 min read</span>
              </div>
              <a href="blog-document-intelligence-stp.html" class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-indigo-600 to-cyan-600 text-white rounded-xl font-medium hover:shadow-lg hover:scale-105 transition-all duration-300">
                Read Article
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
              </a>
            </div>
          </div>
        </article>"""

    if "blog-document-intelligence-stp.html" not in text:
        featured_pattern = re.compile(
            r"(\n\s*<!-- Featured Post -->\s*\n)\s*<article class=\"reveal reveal-delay-2 blog-card.*?</article>\s*(\n\s*<!-- Recent Posts Grid -->)",
            re.DOTALL,
        )
        text, count = featured_pattern.subn(
            lambda match: match.group(1) + "        " + featured_post + match.group(2),
            text,
            count=1,
        )
        if count != 1:
            raise RuntimeError("Could not replace the featured blog card")

    text = text.replace('<span id="year">2025</span>', '<span id="year">2026</span>', 1)
    INDEX_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
