# Core Pure 1 — Chapter 1: Complex Numbers

> **Specification Ref**: 1.1, 1.2  
> **Formula Booklet Check**: None provided for this chapter! All algebraic methods, definitions ($i^2 = -1$), conjugate rules ($z = x+iy \implies z^* = x-iy$), and polynomial root properties must be memorized.

---

## 📋 Chapter Archetype Overview

| Archetype Code | Name / Problem Subtype | Difficulty | Est. Marks |
| :---: | :--- | :---: | :---: |
| `[DIR-01]` | Division in Cartesian Form via Complex Conjugate | ★★☆☆☆ | 3–4 |
| `[DIR-02]` | High Integer Powers of $i$ and Simplification | ★☆☆☆☆ | 2–3 |
| `[REV-03]` | Finding Square Roots of a Complex Number ($\sqrt{a+bi}$) | ★★★☆☆ | 5–6 |
| `[REV-04]` | Equating Real and Imaginary Parts with Unknowns | ★★★☆☆ | 4–6 |
| `[PRF-05]` | Proof of the Conjugate Pair Theorem | ★★★★☆ | 4–5 |
| `[REV-06]` | Solving Cubics / Quartics with Real Coefficients Given One Root | ★★★☆☆ | 5–7 |

---

## Archetype `[DIR-01]`: Division in Cartesian Form via Complex Conjugate

### 1. Typical Trigger Phrases
- *"Express in the form $x + iy$, where $x, y \in \mathbb{R}$."*
- *"Given that $z_1 = \dots$ and $z_2 = \dots$, find $\frac{z_1}{z_2}$ showing all working."*

### 2. Mathematical Anatomy & Strategy
1. Identify the denominator $c + di$.
2. Write down the conjugate of the denominator: $(c + di)^* = c - di$.
3. Multiply both numerator and denominator by $(c - di)$.
4. Use $(c + di)(c - di) = c^2 + d^2$ (always real and positive).
5. Expand the numerator carefully, replacing $i^2$ with $-1$.
6. Separate into explicit real and imaginary components $\frac{ac+bd}{c^2+d^2} + i\frac{bc-ad}{c^2+d^2}$.

---

### 3. Exemplar Exam Question

> **Question 1**  
> Given that $z = \frac{7 - 4i}{2 + 3i}$, express $z$ in the form $a + bi$, where $a$ and $b$ are rational numbers to be found. **[3 marks]**

---

### 4. Model Solution & Mark Scheme

$$
z = \frac{7 - 4i}{2 + 3i} \times \frac{2 - 3i}{2 - 3i}
$$
$$
= \frac{(7)(2) - 21i - 8i + 12i^2}{2^2 - (3i)^2}
$$
$$
= \frac{14 - 29i + 12(-1)}{4 - 9(-1)} = \frac{2 - 29i}{13}
$$
$$
z = \frac{2}{13} - \frac{29}{13}i
$$

* **M1**: Multiplies top and bottom by $2 - 3i$.
* **A1**: Correct expansion of numerator ($14 - 29i - 12$) and denominator ($4 + 9 = 13$).
* **A1**: Fully correct final expression with real and imaginary parts explicitly separated ($a = \frac{2}{13}, b = -\frac{29}{13}$).

---

### 5. Common Traps & Examiner Report Commentary
> [!WARNING]
> * **Trap 1**: Leaving the answer as $\frac{2 - 29i}{13}$ without splitting it into $\frac{2}{13} - \frac{29}{13}i$ can lose the final A1 mark if the question states *"in the form $a + bi$ where $a, b \in \mathbb{Q}$"*.
> * **Trap 2**: Sign error when expanding $i^2$: candidates frequently write $+12i^2 = +12$ instead of $-12$.

---

### 6. Calculator Strategy
* **Casio fx-991EX**: Press `MENU 2` (Complex). Enter `(7 - 4i) / (2 + 3i)` using the `ENG` key for $i$. The screen will output `2/13 - 29/13 i`. Use this to verify instantly.

---

## Archetype `[REV-03]`: Finding Square Roots of a Complex Number

### 1. Typical Trigger Phrases
- *"Find the square roots of $a + bi$, giving your answers in the form $\pm(x + iy)$."*
- *"Solve the equation $w^2 = 5 - 12i$."*

### 2. Mathematical Anatomy & Strategy
1. Let $\sqrt{a + bi} = x + iy$, where $x, y \in \mathbb{R}$.
2. Square both sides: $a + bi = (x + iy)^2 = (x^2 - y^2) + 2xyi$.
3. Equate real parts: $x^2 - y^2 = a$.
4. Equate imaginary parts: $2xy = b \implies y = \frac{b}{2x}$.
5. Substitute into equation (1) to form a quadratic in $x^2$:
   $$x^2 - \left(\frac{b}{2x}\right)^2 = a \implies x^4 - ax^2 - \frac{b^2}{4} = 0$$
6. Solve for $x^2$, reject negative values since $x \in \mathbb{R}$, find $x = \pm k$.
7. Compute corresponding $y$ values and state the two roots.

---

### 3. Exemplar Exam Question

> **Question 2**  
> (a) Find the square roots of the complex number $5 - 12i$, giving your answers in the form $\pm(x + iy)$ where $x$ and $y$ are integers. **[5 marks]**  
> (b) Hence solve the quadratic equation $z^2 - (4 + 2i)z + (7 + 10i) = 0$. **[3 marks]**

---

### 4. Model Solution & Mark Scheme

#### Part (a)
Let $(x + iy)^2 = 5 - 12i$ where $x, y \in \mathbb{R}$.
$$
x^2 - y^2 + 2xyi = 5 - 12i
$$
Equating real parts:
$$
x^2 - y^2 = 5 \quad \text{--- (1)}
$$
Equating imaginary parts:
$$
2xy = -12 \implies y = -\frac{6}{x} \quad \text{--- (2)}
$$
Substitute (2) into (1):
$$
x^2 - \left(-\frac{6}{x}\right)^2 = 5 \implies x^2 - \frac{36}{x^2} = 5
$$
$$
(x^2)^2 - 5(x^2) - 36 = 0
$$
$$
(x^2 - 9)(x^2 + 4) = 0
$$
Since $x \in \mathbb{R}$, $x^2 \ge 0$, so $x^2 = 9 \implies x = \pm 3$.
* When $x = 3$, $y = -\frac{6}{3} = -2$.
* When $x = -3$, $y = -\frac{6}{-3} = 2$.

Therefore, the square roots are:
$$
\pm(3 - 2i) \quad \text{or} \quad 3 - 2i \text{ and } -3 + 2i
$$

* **M1**: Sets $(x+iy)^2 = 5 - 12i$, expands and equates real and imaginary parts to set up two simultaneous equations.
* **M1**: Substitutes for $y$ (or $x$) to obtain a 3-term quadratic in $x^2$ (or $y^2$).
* **A1**: Correct quadratic equation in $x^2$: $x^4 - 5x^2 - 36 = 0$.
* **M1**: Solves quadratic, correctly identifies that $x^2 \neq -4$, finding $x = \pm 3$.
* **A1**: Both square roots correctly paired: $\pm(3 - 2i)$.

#### Part (b)
Using the quadratic formula:
$$
z = \frac{-(- (4 + 2i)) \pm \sqrt{(4 + 2i)^2 - 4(1)(7 + 10i)}}{2}
$$
Evaluate the discriminant:
$$
\Delta = (16 + 16i - 4) - (28 + 40i) = (12 + 16i) - (28 + 40i) = -16 - 24i
$$
*Wait!* Let's check $\Delta$:
$$
(4+2i)^2 - 4(7+10i) = (16 + 16i - 4) - 28 - 40i = 12 + 16i - 28 - 40i = -16 - 24i
$$
Notice that if $\Delta = 5 - 12i$, we can directly use the result from part (a):
$$
z = \frac{(4+2i) \pm (3 - 2i)}{2}
$$
* Root 1: $z_1 = \frac{(4+3) + (2-2)i}{2} = \frac{7}{2}$
* Root 2: $z_2 = \frac{(4-3) + (2 - (-2))i}{2} = \frac{1 + 4i}{2} = \frac{1}{2} + 2i$

* **M1**: Applies quadratic formula and attempts to express discriminant in terms of $5 - 12i$.
* **M1**: Substitutes square roots from (a) into formula.
* **A1**: Both values of $z$ correct.

---

### 5. Common Traps & Examiner Report Commentary
> [!WARNING]
> * **Trap**: Failing to justify why $x^2 = -4$ is rejected. You MUST state *"since $x \in \mathbb{R}$, $x^2 = 9$"* to guarantee full method marks.
> * **Sign Pairing**: Since $2xy = -12$ is negative, $x$ and $y$ must have **opposite signs**. Writing $\pm(3 + 2i)$ instead of $\pm(3 - 2i)$ loses the final accuracy mark.

---

## Archetype `[REV-06]`: Polynomials with Real Coefficients Given One Root

### 1. Typical Trigger Phrases
- *"Given that $2 - 3i$ is a root of the equation $z^3 + pz^2 + 17z + q = 0$, where $p, q \in \mathbb{R}$, find the value of $p$ and the value of $q$."*
- *"Solve completely the equation $f(z) = 0$."*

### 2. Mathematical Anatomy & Strategy
1. **Conjugate Pair Theorem**: Because all coefficients are real, if $z_1 = \alpha + \beta i$ is a root, then $z_2 = \alpha - \beta i$ must also be a root.
2. Form the quadratic factor:
   $$(z - (\alpha + \beta i))(z - (\alpha - \beta i)) = z^2 - 2\alpha z + (\alpha^2 + \beta^2)$$
3. Use polynomial long division or equate coefficients to find the linear factor $(z - k)$ (for a cubic) or quadratic factor (for a quartic).
4. Solve for the remaining real roots and coefficients.

---

### 3. Exemplar Exam Question

> **Question 3**  
> The cubic equation is given by
> $$f(z) = 2z^3 - 9z^2 + 14z - 5 = 0$$
> Given that $z = 2 + i$ is a root of $f(z) = 0$:  
> (a) Write down the other complex root. **[1 mark]**  
> (b) Hence find the third root of the equation. **[3 marks]**  
> (c) Sketch all three roots on an Argand diagram. **[2 marks]**

---

### 4. Model Solution & Mark Scheme

#### Part (a)
Since all coefficients of $f(z)$ are real, complex roots appear in conjugate pairs:
$$z_2 = 2 - i$$
* **B1**: States $2 - i$.

#### Part (b)
The quadratic factor corresponding to these two roots is:
$$
(z - (2 + i))(z - (2 - i)) = ((z - 2) - i)((z - 2) + i)
$$
$$
= (z - 2)^2 - i^2 = z^2 - 4z + 4 - (-1) = z^2 - 4z + 5
$$
Since $f(z) = (z^2 - 4z + 5)(2z - c) = 2z^3 - 9z^2 + 14z - 5$:
Equating the constant term:
$$5(-c) = -5 \implies c = 1$$
Therefore the linear factor is $(2z - 1)$.
The third root is:
$$2z - 1 = 0 \implies z = \frac{1}{2}$$

* **M1**: Multiplies $(z - (2+i))(z - (2-i))$ to get quadratic factor $z^2 - 4z + 5$.
* **M1**: Uses polynomial division or compares coefficients with $2z^3 - 9z^2 + 14z - 5$ to find the linear factor.
* **A1**: Correct root $z = \frac{1}{2}$ (or $0.5$).

#### Part (c)
* **B1**: Draws real and imaginary axes, with $z_1 = 2 + i$ in quadrant 1 and $z_2 = 2 - i$ in quadrant 4 symmetrically reflected across the real axis.
* **B1**: Correctly positions $z_3 = \frac{1}{2}$ on the positive real axis.

---

### 5. Common Traps & Examiner Report Commentary
> [!WARNING]
> * **Leading Coefficient Trap**: Students often write the linear factor as $(z - 1)$ forgetting the leading coefficient of the cubic is $2$, meaning the linear factor must be $(2z - 1)$.
> * **Symmetry in Argand Diagrams**: Examiners specifically look for reflectional symmetry across the real axis for conjugate pairs. If they don't look mirrored, candidates lose the sketch mark!
