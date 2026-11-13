#!/usr/bin/env python3
"""
Generates the drafted problem sheets and answer sheets for all 9 chapters of Core Pure 1.
Formatted exactly to match the speed-maths design system with:
- \\CPHeader
- \\CPTitleBlock
- 10 targeted question slots mapped to the official Edexcel Core Pure 1 archetypes
- Answers PDF with \\ans, \\method, and \\inv (Investigation Questions) alongside each solution.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CP1_DIR = os.path.join(BASE_DIR, "modules", "core-pure-1")

CHAPTERS = [
    {
        "id": "ch01-complex-numbers",
        "num": 1,
        "title": "Complex Numbers",
        "subtitle": "Cartesian Arithmetic, Conjugates, Roots of Polynomials \\& Square Roots",
        "archetypes": [
            ("DIR", "Division in Cartesian form via complex conjugate multiplication"),
            ("DIR", "Simplification of high integer powers of $i$ and imaginary arithmetic"),
            ("DIR", "Solving quadratic equations with negative discriminant in $\\mathbb{C}$"),
            ("REV", "Finding square roots of a complex number $a + bi$ via simultaneous equations"),
            ("REV", "Equating real and imaginary parts to solve for unknown real parameters"),
            ("PRF", "Formal proof of the Conjugate Pair Theorem for real-coefficient polynomials"),
            ("REV", "Solving a cubic equation with real coefficients given one non-real root"),
            ("REV", "Solving a quartic equation with real coefficients given one non-real root"),
            ("SYN", "Complex numbers in identity expansions and binomial applications"),
            ("SYN", "Quadratic equations with complex coefficients (non-conjugate roots)")
        ]
    },
    {
        "id": "ch02-argand-diagrams",
        "num": 2,
        "title": "Argand Diagrams \\& Loci",
        "subtitle": "Modulus-Argument Form, Geometric Loci \\& Extremum Optimization",
        "archetypes": [
            ("DIR", "Modulus and principal argument determination with $-\\pi < \\theta \\le \\pi$"),
            ("DIR", "Multiplication and division in polar / modulus-argument form"),
            ("GEO", "Circular locus: $|z - z_1| = r$ with geometric plotting and Cartesian form"),
            ("GEO", "Perpendicular bisector locus: $|z - z_1| = |z - z_2|$ and Cartesian line"),
            ("GEO", "Half-line ray locus: $\\arg(z - z_1) = \\alpha$ with initial point exclusion"),
            ("GEO", "Composite inequalities and region shading on Argand diagrams"),
            ("REV", "Optimization: Finding maximum and minimum values of $|z|$ on a circle"),
            ("REV", "Optimization: Finding maximum and minimum values of $\\arg(z)$ via tangent lines"),
            ("SYN", "Exact coordinate intersection of circular and half-line loci"),
            ("PRF", "Geometric verification of angle properties or cyclic configurations in $\\mathbb{C}$")
        ]
    },
    {
        "id": "ch03-series",
        "num": 3,
        "title": "Series \\& Summation",
        "subtitle": "Standard Sums, Index Shifts, Method of Differences \\& Telescoping",
        "archetypes": [
            ("DIR", "Sum of the first $n$ positive integers with shifted lower limits"),
            ("DIR", "Sum of squares formula application and algebraic factorization"),
            ("DIR", "Sum of cubes formula and proving identities of the form $S_n = [f(n)]^2$"),
            ("REV", "Evaluating general cubic polynomials in $r$: sum of $(ar^3 + br^2 + cr + d)$"),
            ("REV", "Parameter determination: finding constant $k$ given total sum $S_n$"),
            ("PRF", "Method of differences: standard partial fraction telescoping sum $\\frac{1}{r(r+1)}$"),
            ("PRF", "Method of differences: stride-2 telescoping cancellation $\\frac{1}{r(r+2)}$"),
            ("PRF", "Method of differences with factorials or trigonometric identities"),
            ("REV", "Convergence and evaluation of infinite telescoping series"),
            ("SYN", "Synoptic series applications linking summation to induction or polynomials")
        ]
    },
    {
        "id": "ch04-roots-of-polynomials",
        "num": 4,
        "title": "Roots of Polynomials",
        "subtitle": "Vieta's Relations, Symmetric Functions \\& Root Transformations",
        "archetypes": [
            ("DIR", "Vieta's relations for quadratic and cubic equations"),
            ("DIR", "Vieta's relations for quartic polynomials: product and pairwise sums"),
            ("DIR", "Evaluating quadratic symmetric expressions: $\\alpha^2 + \\beta^2 + \\gamma^2$"),
            ("REV", "Evaluating reciprocal symmetric sums: $\\frac{1}{\\alpha} + \\frac{1}{\\beta} + \\frac{1}{\\gamma}$"),
            ("REV", "Evaluating cubic symmetric sums: $\\alpha^3 + \\beta^3 + \\gamma^3$"),
            ("REV", "Determining unknown polynomial coefficients from conditions on roots"),
            ("REV", "Linear root transformations: forming equations with roots $\\alpha + k$"),
            ("REV", "Multiplicative root transformations: forming equations with roots $k\\alpha$"),
            ("SYN", "Non-linear root transformations: forming equations with squared roots $\\alpha^2$"),
            ("SYN", "Quartic polynomials with paired conjugate roots and transformed equations")
        ]
    },
    {
        "id": "ch05-volumes-of-revolution",
        "num": 5,
        "title": "Volumes of Revolution",
        "subtitle": "Rotations About Coordinate Axes, Parametric Solids \\& Modelling",
        "archetypes": [
            ("DIR", "Volume generated by rotating $y = f(x)$ through $2\\pi$ radians about the $x$-axis"),
            ("DIR", "Volume generated by rotating $x = g(y)$ through $2\\pi$ radians about the $y$-axis"),
            ("DIR", "Parametric curve rotation about the $x$-axis via $\\pi \\int y^2 \\frac{dx}{dt} dt$"),
            ("REV", "Parametric curve rotation about the $y$-axis with boundary parameterization"),
            ("REV", "Hollow solid: region bounded between a curve and a straight line"),
            ("REV", "Volume of region enclosed between two intersecting curves"),
            ("CTX", "Real-world engineering / container modelling (vase, goblet, bowl)"),
            ("REV", "Reverse volume problem: determining container height $h$ for given capacity"),
            ("SYN", "Rates of change of volume and liquid depth in solids of revolution"),
            ("SYN", "Synoptic comparison of analytical volume with truncated conical formulas")
        ]
    },
    {
        "id": "ch06-matrices",
        "num": 6,
        "title": "Matrices \\& Linear Systems",
        "subtitle": "Determinants, Inverses, Adjugates, Consistency \\& 3D Planes",
        "archetypes": [
            ("DIR", "Determinant calculation for $2\\times2$ and $3\\times3$ matrices with algebraic entries"),
            ("DIR", "Inverse of $3\\times3$ matrix via matrix of minors, cofactors, and adjugate"),
            ("DIR", "Matrix equation solution $M\\mathbf{x} = \\mathbf{b}$ using the matrix inverse"),
            ("REV", "Singular matrices: solving for unknown parameter $k$ such that $\\det(M) = 0$"),
            ("REV", "Inverting parameterized matrices and factoring polynomial determinants"),
            ("GEO", "System consistency: unique point of intersection of three non-parallel planes"),
            ("GEO", "System inconsistency: geometric interpretation as a triangular prism"),
            ("GEO", "System dependency: infinite solutions intersecting along a common line (sheaf)"),
            ("GEO", "Finding the vector equation of the line of intersection for a sheaf"),
            ("GEO", "Geometric arrangements involving parallel or coincident planes")
        ]
    },
    {
        "id": "ch07-linear-transformations",
        "num": 7,
        "title": "Linear Transformations",
        "subtitle": "2D/3D Matrices, Invariant Lines, Area Scales \\& Orientations",
        "archetypes": [
            ("DIR", "2D rotations and reflections derived from unit basis vectors"),
            ("DIR", "Enlargements, stretches, and shears in 2D coordinate space"),
            ("DIR", "Composite transformations: non-commutativity of matrix products $BA$ vs $AB$"),
            ("REV", "Area scale factor and orientation reversal determination via $|\\det(M)|$"),
            ("REV", "Invariant points: finding stationary coordinates satisfying $M\\mathbf{x} = \\mathbf{x}$"),
            ("REV", "Lines of invariant points vs invariant lines passing through origin ($y = mx$)"),
            ("REV", "Invariant lines not passing through the origin ($y = mx + c$)"),
            ("GEO", "3D reflection matrices across Cartesian coordinate mirror planes"),
            ("GEO", "3D rotation matrices about the $x$, $y$, or $z$ coordinate axes"),
            ("SYN", "Volume scale factors and composite geometric mapping in 3D")
        ]
    },
    {
        "id": "ch08-proof-by-induction",
        "num": 8,
        "title": "Proof by Mathematical Induction",
        "subtitle": "Summations, Divisibility, Matrix Powers \\& Recurrence Relations",
        "archetypes": [
            ("PRF", "Formal 4-step induction proof: summation of polynomial sequences"),
            ("PRF", "Induction proof: cubic and quartic series identities"),
            ("PRF", "Induction proof: factorial series summation $\\sum r \\cdot r! = (n+1)! - 1$"),
            ("PRF", "Induction proof: divisibility of exponential differences $a^n - b^n$"),
            ("PRF", "Induction proof: divisibility of expressions like $5^{2n} - 1$ by 24"),
            ("PRF", "Induction proof: divisibility with combined linear and exponential terms"),
            ("PRF", "Induction proof: $n$-th power of a $2\\times2$ matrix $M^n$"),
            ("PRF", "Induction proof: explicit general term of a 1st order recurrence relation"),
            ("PRF", "Induction proof: 2nd order recurrence relations with characteristic roots"),
            ("PRF", "Induction proof: inequality induction bounds (e.g. $2^n > n^2$ for $n \\ge 5$)")
        ]
    },
    {
        "id": "ch09-vectors",
        "num": 9,
        "title": "Vectors \\& 3D Geometry",
        "subtitle": "Lines in 3D, Dot Product, Skew Lines \\& Shortest Distances",
        "archetypes": [
            ("DIR", "Vector, parametric, and symmetric Cartesian forms of lines in 3D"),
            ("DIR", "Scalar dot product evaluation and finding the angle between two 3D lines"),
            ("DIR", "Determining whether two lines in 3D are parallel, intersecting, or skew"),
            ("DIR", "Finding the exact point of intersection of two intersecting 3D lines"),
            ("REV", "Shortest perpendicular distance from an external point to a 3D line"),
            ("REV", "Shortest distance between two parallel lines in 3D space"),
            ("REV", "Shortest distance between two skew lines using a common perpendicular"),
            ("REV", "Finding coordinates of the points of closest approach on two skew lines"),
            ("GEO", "Reflection of a point in a 3D line and symmetric geometric configurations"),
            ("CTX", "Contextual kinematics: minimum separation distance of two moving craft")
        ]
    }
]

def make_problem_sheet_content(ch):
    lines = [
        r"\documentclass[11pt,a4paper]{article}",
        r"\input{../shared/preamble}",
        f"\\CPHeader{{{ch['title']}}}{{{ch['num']}}}",
        r"",
        r"\begin{document}",
        r"\thispagestyle{plain}",
        r"",
        f"\\CPTitleBlock{{{ch['title']}}}{{Problem Sheet \\#{ch['num']} \\enspace$\\cdot$\\enspace {ch['subtitle']}}}",
        r"",
        r"\section*{Section A \quad Procedural \& Direct Foundations \hfill{\normalfont\footnotesize(Questions 1--3)}}",
        r"\begin{enumerate}"
    ]

    for i in range(1, 4):
        code, desc = ch["archetypes"][i-1]
        lines.append(f"%── Q{i} [{code}] ─────────────────────────────────────────────────────────────")
        lines.append(f"\\item \\textbf{{[{code}]}} \\textit{{{desc}}}")
        lines.append(r"\[")
        lines.append(f"\\text{{[Draft Question {i}: Complete examination problem text to be populated]}}")
        lines.append(r"\]")
        lines.append(r"\hfill{\small\textbf{[4--5 marks]}}")
        lines.append(r"")

    lines.append(r"\end{enumerate}")
    lines.append(r"")
    lines.append(r"\section*{Section B \quad Reverse Parameters \& Analysis \hfill{\normalfont\small(Questions 4--6)}}")
    lines.append(r"\begin{enumerate}[resume]")

    for i in range(4, 7):
        code, desc = ch["archetypes"][i-1]
        lines.append(f"%── Q{i} [{code}] ─────────────────────────────────────────────────────────────")
        lines.append(f"\\item \\textbf{{[{code}]}} \\textit{{{desc}}}")
        lines.append(r"\[")
        lines.append(f"\\text{{[Draft Question {i}: Complete examination problem text to be populated]}}")
        lines.append(r"\]")
        lines.append(r"\hfill{\small\textbf{[5--6 marks]}}")
        lines.append(r"")

    lines.append(r"\end{enumerate}")
    lines.append(r"")
    lines.append(r"\section*{Section C \quad Proof, Geometry \& Multi-step \hfill{\normalfont\small(Questions 7--10)}}")
    lines.append(r"\begin{enumerate}[resume]")

    for i in range(7, 11):
        code, desc = ch["archetypes"][i-1]
        lines.append(f"%── Q{i} [{code}] ─────────────────────────────────────────────────────────────")
        lines.append(f"\\item \\textbf{{[{code}]}} \\textit{{{desc}}}")
        lines.append(r"\[")
        lines.append(f"\\text{{[Draft Question {i}: Complete examination problem text to be populated]}}")
        lines.append(r"\]")
        lines.append(r"\hfill{\small\textbf{[6--8 marks]}}")
        lines.append(r"")

    lines.append(r"\end{enumerate}")
    lines.append(r"")
    lines.append(r"\vspace{14pt}")
    lines.append(r"\begin{center}")
    lines.append(r"  {\color{accentline}\rule{0.4\textwidth}{0.4pt}}\\[5pt]")
    lines.append(r"  {\footnotesize\itshape\color{medgray} ``Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding.''}\\[2pt]")
    lines.append(r"  {\scriptsize\scshape\color{medgray} William Paul Thurston}\\[5pt]")
    lines.append(r"  {\color{accentline}\rule{0.4\textwidth}{0.4pt}}")
    lines.append(r"\end{center}")
    lines.append(r"")
    lines.append(r"\end{document}")

    return "\n".join(lines)

def make_answers_content(ch):
    lines = [
        r"\documentclass[11pt,a4paper]{article}",
        r"\input{../shared/preamble}",
        f"\\CPHeader{{{ch['title']}}}{{{ch['num']}}}",
        r"",
        r"\begin{document}",
        r"\thispagestyle{plain}",
        r"",
        f"\\CPTitleBlock{{{ch['title']}}}{{Answers \\& Investigations \\enspace$\\cdot$\\enspace Worked Solutions, Mark Schemes \\& Deep Prompts}}",
        r"",
        r"\section*{Section A \quad Procedural \& Direct Foundations}",
        r"\begin{enumerate}"
    ]

    for i in range(1, 4):
        code, desc = ch["archetypes"][i-1]
        lines.append(f"%── Q{i} [{code}] ─────────────────────────────────────────────────────────────")
        lines.append(f"\\item \\textbf{{[{code}]}} \\textit{{{desc}}}")
        lines.append(r"\ans{[Final algebraic solution and exact values]}")
        lines.append(r"\method{Key method step M1: apply definition or algebraic transformation. Accuracy mark A1: intermediate result. Final accuracy A1: exact form specified in question.}")
        lines.append(f"\\inv{{Investigative exploration for Q{i}: What happens if the boundary condition or sign changes? How does this generalize to higher dimensions or arbitrary parameters?}}")
        lines.append(r"")

    lines.append(r"\end{enumerate}")
    lines.append(r"")
    lines.append(r"\section*{Section B \quad Reverse Parameters \& Analysis}")
    lines.append(r"\begin{enumerate}[resume]")

    for i in range(4, 7):
        code, desc = ch["archetypes"][i-1]
        lines.append(f"%── Q{i} [{code}] ─────────────────────────────────────────────────────────────")
        lines.append(f"\\item \\textbf{{[{code}]}} \\textit{{{desc}}}")
        lines.append(r"\ans{[Final value of unknown parameter and corresponding equation]}")
        lines.append(r"\method{Setup condition M1. Solving the resulting auxiliary polynomial or system M1. Accuracy criteria A1 with explicit rejection of inadmissible values.}")
        lines.append(f"\\inv{{Investigative exploration for Q{i}: Check the geometric or physical interpretation when the discriminant is zero. Identify any bifurcation points.}}")
        lines.append(r"")

    lines.append(r"\end{enumerate}")
    lines.append(r"")
    lines.append(r"\section*{Section C \quad Proof, Geometry \& Multi-step}")
    lines.append(r"\begin{enumerate}[resume]")

    for i in range(7, 11):
        code, desc = ch["archetypes"][i-1]
        lines.append(f"%── Q{i} [{code}] ─────────────────────────────────────────────────────────────")
        lines.append(f"\\item \\textbf{{[{code}]}} \\textit{{{desc}}}")
        lines.append(r"\ans{[Complete deductive proof or multi-part analytical solution]}")
        lines.append(r"\method{Formal proof structure or systematic algebraic elimination. Explicit verification of base cases, cofactor signs, or orthogonal projections.}")
        lines.append(f"\\inv{{Investigative exploration for Q{i}: Can this result be established via an alternative mathematical framework (e.g. geometric vs algebraic)?}}")
        lines.append(r"")

    lines.append(r"\end{enumerate}")
    lines.append(r"")
    lines.append(r"\end{document}")

    return "\n".join(lines)

def main():
    print(f"Generating drafts for all {len(CHAPTERS)} chapters of Core Pure 1...")
    for ch in CHAPTERS:
        if ch["id"] == "ch01-complex-numbers":
            print(f"  ⏭️  {ch['id']}: already fully authored. Skipping draft overwrite.")
            continue
        ch_dir = os.path.join(CP1_DIR, ch["id"])
        os.makedirs(ch_dir, exist_ok=True)

        ps_path = os.path.join(ch_dir, "problem-sheet.tex")
        ans_path = os.path.join(ch_dir, "answers.tex")

        with open(ps_path, "w", encoding="utf-8") as f:
            f.write(make_problem_sheet_content(ch))

        with open(ans_path, "w", encoding="utf-8") as f:
            f.write(make_answers_content(ch))

        print(f"  ✓ {ch['id']}: problem-sheet.tex & answers.tex created.")

if __name__ == "__main__":
    main()
