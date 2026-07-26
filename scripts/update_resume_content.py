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

    desktop_projects_link = '        <a href="#projects" class="hover:text-brand-600">Projects</a>'
    desktop_passion_link = '        <a href="#passion-projects" class="hover:text-brand-600">Passion Projects</a>'
    if desktop_passion_link not in text:
        if desktop_projects_link not in text:
            raise RuntimeError("Could not locate desktop Projects navigation link")
        text = text.replace(
            desktop_projects_link,
            desktop_projects_link + "\n" + desktop_passion_link,
            1,
        )

    mobile_projects_link = '        <a href="#projects" class="block py-2 px-3 rounded-lg hover:bg-slate-100">Projects</a>'
    mobile_passion_link = '        <a href="#passion-projects" class="block py-2 px-3 rounded-lg hover:bg-slate-100">Passion Projects</a>'
    if mobile_passion_link not in text:
        if mobile_projects_link not in text:
            raise RuntimeError("Could not locate mobile Projects navigation link")
        text = text.replace(
            mobile_projects_link,
            mobile_projects_link + "\n" + mobile_passion_link,
            1,
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

    passion_projects_section = """    <!-- PASSION PROJECTS -->
    <section id="passion-projects" class="scroll-mt-24">
      <div class="reveal max-w-3xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-fuchsia-50 text-fuchsia-700 ring-1 ring-fuchsia-200 text-sm font-medium">Built independently</div>
        <h2 class="mt-4 text-2xl md:text-3xl font-semibold">Passion Projects</h2>
        <p class="mt-3 text-slate-700">Independent 0→1 AI products I built beyond my core role—turning personal interests in learning and travel into live, usable experiences.</p>
      </div>

      <div class="mt-7 grid md:grid-cols-2 gap-6">
        <article class="reveal p-7 rounded-3xl border border-slate-200 bg-gradient-to-br from-violet-50 via-white to-indigo-50 shadow-soft hover:translate-y-[-3px] transition">
          <div class="flex items-start justify-between gap-4">
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-2xl bg-violet-100 flex items-center justify-center text-2xl">📚</div>
              <div>
                <h3 class="text-xl font-bold">ClearCFA</h3>
                <p class="text-sm text-slate-500">AI-powered CFA exam preparation</p>
              </div>
            </div>
            <span class="px-2.5 py-1 text-xs rounded-full bg-violet-100 text-violet-800 font-medium">AI EdTech</span>
          </div>
          <p class="mt-5 text-slate-700 leading-relaxed">A 0→1 exam-preparation product featuring adaptive question generation and a three-layer AI-output validation framework designed to improve the quality and reliability of practice content.</p>
          <ul class="mt-4 space-y-2 text-sm text-slate-700">
            <li class="flex gap-2"><span class="text-violet-600">✓</span><span>Acquired the first paying users within 30 days.</span></li>
            <li class="flex gap-2"><span class="text-violet-600">✓</span><span>Grew to 100+ monthly active users.</span></li>
            <li class="flex gap-2"><span class="text-violet-600">✓</span><span>Built independently from concept through launch and adoption.</span></li>
          </ul>
          <div class="mt-6 flex flex-wrap gap-3">
            <a href="https://srijaharshikad.github.io/ClearCFA/" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-violet-600 text-white font-medium hover:bg-violet-700 hover:scale-[1.02] transition">Open Product ↗</a>
            <a href="https://github.com/srijaharshikad/ClearCFA" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-5 py-3 rounded-xl border border-slate-300 bg-white/80 font-medium hover:bg-white transition">View GitHub</a>
          </div>
        </article>

        <article class="reveal p-7 rounded-3xl border border-slate-200 bg-gradient-to-br from-cyan-50 via-white to-emerald-50 shadow-soft hover:translate-y-[-3px] transition">
          <div class="flex items-start justify-between gap-4">
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-2xl bg-cyan-100 flex items-center justify-center text-2xl">✈️</div>
              <div>
                <h3 class="text-xl font-bold">TripCanvas</h3>
                <p class="text-sm text-slate-500">AI travel planning</p>
              </div>
            </div>
            <span class="px-2.5 py-1 text-xs rounded-full bg-cyan-100 text-cyan-800 font-medium">Travel AI</span>
          </div>
          <p class="mt-5 text-slate-700 leading-relaxed">A 0→1 AI travel-planning product that converts an open-ended trip idea into a structured, customizable itinerary through a four-stage planning engine.</p>
          <ul class="mt-4 space-y-2 text-sm text-slate-700">
            <li class="flex gap-2"><span class="text-cyan-600">✓</span><span>Destination discovery based on the traveller’s intent.</span></li>
            <li class="flex gap-2"><span class="text-cyan-600">✓</span><span>Itinerary generation and activity-level planning.</span></li>
            <li class="flex gap-2"><span class="text-cyan-600">✓</span><span>Trip customization in one continuous product journey.</span></li>
          </ul>
          <div class="mt-6 flex flex-wrap gap-3">
            <a href="https://srijaharshikad.github.io/TripCanvas/" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-cyan-600 text-white font-medium hover:bg-cyan-700 hover:scale-[1.02] transition">Open Product ↗</a>
            <a href="https://github.com/srijaharshikad/TripCanvas" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-5 py-3 rounded-xl border border-slate-300 bg-white/80 font-medium hover:bg-white transition">View GitHub</a>
          </div>
        </article>
      </div>
    </section>"""

    if 'id="passion-projects"' not in text:
        blog_marker = "\n    <!-- BLOG -->"
        if blog_marker not in text:
            raise RuntimeError("Could not locate the Blog section marker")
        text = text.replace(
            blog_marker,
            "\n\n" + passion_projects_section + "\n" + blog_marker,
            1,
        )

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
