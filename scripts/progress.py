#!/usr/bin/env python3
"""
Progress Tracker for Edexcel Further Mathematics Archetype Compendium.
Parses ROADMAP.md and displays completion statistics per module.
"""

import os
import re

ROADMAP_PATH = os.path.join(os.path.dirname(__file__), "..", "ROADMAP.md")

def check_progress():
    if not os.path.exists(ROADMAP_PATH):
        print(f"Error: Could not find {ROADMAP_PATH}")
        return

    with open(ROADMAP_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_module = "General"
    stats = {}

    for line in lines:
        if line.startswith("## "):
            current_module = line.replace("## ", "").strip()
            stats[current_module] = {"total": 0, "completed": 0}
        
        match = re.search(r"^\s*-\s*\[([ xX])\]\s*\*\*(Chapter\s+\d+:?[^*]*)\*\*", line)
        if match:
            box, title = match.groups()
            stats[current_module]["total"] += 1
            if box.lower() == "x":
                stats[current_module]["completed"] += 1

    total_chapters = sum(m["total"] for m in stats.values())
    total_completed = sum(m["completed"] for m in stats.values())
    overall_pct = (total_completed / total_chapters * 100) if total_chapters > 0 else 0

    print("=" * 65)
    print("📊 EDEXCEL FURTHER MATHS QUESTION ARCHETYPE COMPENDIUM")
    print("=" * 65)

    for module, data in stats.items():
        tot = data["total"]
        comp = data["completed"]
        pct = (comp / tot * 100) if tot > 0 else 0
        bar_len = 20
        filled = int(bar_len * (comp / tot)) if tot > 0 else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"{module:<35} [{bar}] {comp:2d}/{tot:2d} ({pct:5.1f}%)")

    print("-" * 65)
    overall_bar_len = 20
    overall_filled = int(overall_bar_len * (total_completed / total_chapters)) if total_chapters > 0 else 0
    overall_bar = "█" * overall_filled + "░" * (overall_bar_len - overall_filled)
    print(f"{'OVERALL COMPLETION':<35} [{overall_bar}] {total_completed:2d}/{total_chapters:2d} ({overall_pct:5.1f}%)")
    print("=" * 65)

if __name__ == "__main__":
    check_progress()
