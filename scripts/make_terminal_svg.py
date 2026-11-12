#!/usr/bin/env python3
"""
Generate an animated terminal telemetry SVG for Zakariae Chelle.
"""
import os
import html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "zakariae-ascii.svg")

lines = [
    "┌── zakariae@ai-cluster: ~/workspace/agentic-ai ───────────────────────────────┐",
    "│ $ python -m agentic_core.deploy --env production --profile sovereign-slm     │",
    "└──────────────────────────────────────────────────────────────────────────────┘",
    " [i] HOST: EMSI Tanger / AI & Data Science Engineering Node                    ",
    " [i] RUNTIME: Python 3.11 • PyTorch • FastAPI • LangGraph • Docker             ",
    "                                                                               ",
    " ═══════════════════════════════ NEURAL TOPOLOGY ══════════════════════════════",
    "                                                                               ",
    "      [Log Stream] ──▶ ┌──────────────────────┐                                ",
    "                       │ Router Agent (Qwen)  │                                ",
    "                       └──────────┬───────────┘                                ",
    "                                  │                                            ",
    "                 ┌────────────────┴────────────────┐                           ",
    "                 ▼                                 ▼                           ",
    "        ┌──────────────────┐              ┌──────────────────┐                 ",
    "        │   RCA Analysis   │              │   Runbook RAG    │                 ",
    "        │ (QLoRA 4-bit)    │              │ (Deterministic)  │                 ",
    "        └────────┬─────────┘              └────────┬─────────┘                 ",
    "                 │                                 │                           ",
    "                 └────────────────┬────────────────┘                           ",
    "                                  ▼                                            ",
    "                       ┌──────────────────────┐                                ",
    "                       │ Validated Resolution │                                ",
    "                       └──────────────────────┘                                ",
    "                                                                               ",
    " ════════════════════════════ BENCHMARK METRICS ═══════════════════════════════",
    "                                                                               ",
    "  • Severity Accuracy   : [████████████████████] 99.1%                         ",
    "  • Root Cause Match    : [███████████████████░] 98.4%                         ",
    "  • Hallucination Rate  : [░░░░░░░░░░░░░░░░░░░░] 0.0%                          ",
    "  • Runbook Recall@3    : [████████████████████] 100.0%                        ",
    "                                                                               ",
    " ════════════════════════════ ENGINE TELEMETRY ════════════════════════════════",
    "                                                                               ",
    "  • Microservice Latency: 0.99s (FastAPI ASGI Async Engine)                    ",
    "  • Memory Consumption  : 1.2 GB VRAM (Ultra-compact Footprint)                ",
    "  • Orchestration       : Apache Airflow DAGs • Kafka • Spark                  ",
    "  • Observability       : Prometheus & Grafana Exporters :9090                 ",
    "                                                                               ",
    " ──────────────────────────────────────────────────────────────────────────────",
    "  STATUS : All Agents Active. Open for 6-Month PFE Internship (Early 2027) ⚡  ",
    " ──────────────────────────────────────────────────────────────────────────────"
]

W, H = 840, 880
PAD = 20
TITLEBAR_H = 30
INK = "#c9d1d9"
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
TITLE_TEXT = "#7d8590"

n_rows = len(lines)
row_step = (H - TITLEBAR_H - PAD * 2) / n_rows

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.1f}" height="{H:.1f}" viewBox="0 0 {W:.1f} {H:.1f}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#111722"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>',
    f'<rect width="{W:.1f}" height="{H:.1f}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1:.1f}" height="{H-1:.1f}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
    '<circle cx="20" cy="15.0" r="5" fill="#ff5f56"/>',
    '<circle cx="36" cy="15.0" r="5" fill="#ffbd2e"/>',
    '<circle cx="52" cy="15.0" r="5" fill="#27c93f"/>',
    f'<text x="{W/2:.1f}" y="19.0" fill="{TITLE_TEXT}" font-size="12" text-anchor="middle">zakariae@ai-node: ~$ ./agent_core.py</text>'
]

for i, line in enumerate(lines):
    y = TITLEBAR_H + PAD + (i + 0.8) * row_step
    dur = 0.05
    begin = 0.04 * i
    clip_id = f"r{i}"
    escaped_line = html.escape(line)
    svg_parts.append(
        f'<clipPath id="{clip_id}"><rect x="20" y="{y - row_step * 0.7:.1f}" height="{row_step:.1f}" width="0">'
        f'<animate attributeName="width" from="0" to="800.0" begin="{begin:.3f}s" dur="{dur:.2f}s" fill="freeze"/>'
        f'</rect></clipPath>'
    )
    svg_parts.append(
        f'<g clip-path="url(#{clip_id})"><text xml:space="preserve" x="20" y="{y:.1f}" fill="{INK}" font-size="13.5" textLength="800.0" lengthAdjust="spacing">'
        f'{escaped_line}'
        f'</text></g>'
    )
    svg_parts.append(
        f'<rect y="{y - row_step * 0.6:.1f}" width="8" height="{row_step * 0.8:.1f}" fill="#61dafb" opacity="0">'
        f'<animate attributeName="x" from="20" to="820.0" begin="{begin:.3f}s" dur="{dur:.2f}s" fill="freeze"/>'
        f'<set attributeName="opacity" to="0.85" begin="{begin:.3f}s"/>'
        f'<set attributeName="opacity" to="0" begin="{begin + dur:.3f}s"/>'
        f'</rect>'
    )

svg_parts.append('</svg>')
out_svg = "".join(svg_parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(out_svg)
print(f"Generated {OUT} ({len(out_svg)//1024} KB)")
