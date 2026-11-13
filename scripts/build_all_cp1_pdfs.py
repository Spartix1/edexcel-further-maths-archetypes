#!/usr/bin/env python3
"""
Compiles all Core Pure 1 problem sheets and answers into PDFs.
Cleans intermediate auxiliary files (.aux, .log, .out).
"""

import os
import subprocess
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP1_DIR = os.path.join(BASE_DIR, "modules", "core-pure-1")

def compile_tex(tex_path):
    directory = os.path.dirname(tex_path)
    filename = os.path.basename(tex_path)
    base_name = os.path.splitext(filename)[0]

    cmd = ["pdflatex", "-interaction=nonstopmode", filename]
    
    result = subprocess.run(cmd, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"    ❌ Error compiling {filename} in {os.path.basename(directory)}")
        return False

    # Second pass for references / outlines
    subprocess.run(cmd, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Clean aux files
    for ext in [".aux", ".log", ".out"]:
        aux_file = os.path.join(directory, base_name + ext)
        if os.path.exists(aux_file):
            try:
                os.remove(aux_file)
            except OSError:
                pass

    return True

def main():
    print("=" * 65)
    print("🛠️  COMPILING CORE PURE 1 WORKBOOK: 9 PROBLEM SHEETS & 9 ANSWERS")
    print("=" * 65)

    chapters = sorted([
        d for d in os.listdir(CP1_DIR)
        if os.path.isdir(os.path.join(CP1_DIR, d)) and d.startswith("ch")
    ])

    total_compiled = 0
    total_target = len(chapters) * 2

    for ch in chapters:
        ch_path = os.path.join(CP1_DIR, ch)
        ps_tex = os.path.join(ch_path, "problem-sheet.tex")
        ans_tex = os.path.join(ch_path, "answers.tex")

        print(f"\n📁 [{ch}]")
        if os.path.exists(ps_tex):
            if compile_tex(ps_tex):
                print(f"  ✓ problem-sheet.pdf compiled.")
                total_compiled += 1

        if os.path.exists(ans_tex):
            if compile_tex(ans_tex):
                print(f"  ✓ answers.pdf compiled.")
                total_compiled += 1

    print("\n" + "=" * 65)
    print(f"🎉 COMPILATION COMPLETE: {total_compiled}/{total_target} PDFs successfully generated!")
    print("=" * 65)

if __name__ == "__main__":
    main()
