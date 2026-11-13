# Edexcel A-Level Further Mathematics: Question Archetype Compendium

A structured, systematic decomposition of every question archetype that Pearson Edexcel can ask across **Core Pure 1 (CP1)**, **Core Pure 2 (CP2)**, **Further Pure 1 (FP1)**, and **Decision 1 (D1)**.

---

## 🎯 The Philosophy

Edexcel A-Level Further Maths questions are not completely random. In reality, every chapter is composed of a finite set of **recurring problem archetypes**. 

By cataloguing every archetype, identifying its trigger phrases, noting mark-scheme traps, and providing model solutions, this repository turns an intimidating two-year syllabus into a finite, conquerable checklist.

---

## 📐 Archetype Classification Matrix

Each question subtype in this compendium is categorized using the following 6-tier taxonomy:

| Code | Archetype Name | Core Description |
| :---: | :--- | :--- |
| **`[DIR]`** | **Direct / Procedural** | Standard forward algorithmic computation testing basic fluency. |
| **`[REV]`** | **Reverse / Parameter** | The answer or geometric condition is given; solve for unknown constants ($k, p, q$). |
| **`[PRF]`** | **Rigorous Proof / "Show that"** | Unforgiving algebraic derivation where calculator skips are penalized. |
| **`[GEO]`** | **Geometric / Structural** | Translating algebraic calculations into geometric or network configurations. |
| **`[CTX]`** | **Context & Modelling** | Real-world applications (kinematics, population models, network optimization). |
| **`[SYN]`** | **Synoptic / Hybrid** | Blending two distinct chapters (e.g. Maclaurin series with differential equations). |

---

## 📂 Repository Layout

```text
edexcel-further-maths-archetypes/
├── README.md                  # Project overview, methodology & usage guide
├── ROADMAP.md                 # Complete chapter-by-chapter tracking checklist
├── templates/
│   └── chapter-template.md    # Standard blueprint for documenting a chapter
├── modules/
│   ├── core-pure-1/           # CP1 chapters (Complex, Series, Roots, Matrices, etc.)
│   ├── core-pure-2/           # CP2 chapters (de Moivre, Calc, Hyperbolics, Polar, DEs)
│   ├── further-pure-1/        # FP1 chapters (Vectors, Conics, Inequalities, t-formulae, etc.)
│   └── decision-1/            # D1 chapters (Algorithms, Graph Theory, CPP, CPA, LP)
└── scripts/
    └── progress.py            # CLI script to track completion percentage across the repo
```

---

## 🚀 How to Author a Chapter

1. Copy [`templates/chapter-template.md`](file:///Users/henry/.gemini/antigravity/scratch/edexcel-further-maths-archetypes/templates/chapter-template.md) into the target module folder (e.g. `modules/core-pure-1/02-argand-diagrams.md`).
2. Identify all recurring Edexcel question archetypes for that topic (typically between 5 to 10 archetypes per chapter).
3. For each archetype, provide:
   - **Trigger Keywords**: Exact phrases Edexcel uses (e.g. *"Hence, or otherwise..."*, *"Explain why a dummy activity is needed..."*).
   - **Exemplar Question**: Written in exam style with exact mark allocations `[3]`, `[5]`, etc.
   - **Model Mark Scheme**: Step-by-step with explicit $M$, $A$, and $B$ marks.
   - **Common Pitfalls & Examiner Tips**: Historical failure points from examiner reports.
   - **Calculator Strategy**: Where the Casio ClassWiz or cg50 can be used to verify or save time.
4. Run `python scripts/progress.py` to check your syllabus coverage.

---

## 🔗 Pushing to GitHub

To push this repository to your own GitHub account:

```bash
# 1. Authenticate with GitHub CLI (if not already done)
gh auth login

# 2. Create the remote repository on GitHub and push in one go
gh repo create edexcel-further-maths-archetypes --public --source=. --remote=origin --push

# Alternatively, if you prefer manual remote:
# git remote add origin https://github.com/<your-username>/<repo-name>.git
# git branch -M main
# git push -u origin main
```
