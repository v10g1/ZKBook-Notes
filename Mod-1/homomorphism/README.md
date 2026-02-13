# 📘 Zero-Knowledge Book — Module 1 Notes

> Note: English is not my first language. These notes are meant for quick revision and intuition rather than perfect explanations.

---

# Homomorphisms

A **homomorphism** between two groups exists when there is a **structure-preserving map** between them.

Suppose we have two algebraic structures:

\[
(A, \star) \quad \text{and} \quad (B, \diamond)
\]

where:

- \( \star \) is the operation on \(A\)
- \( \diamond \) is the operation on \(B\)

A **homomorphism** is a function:

\[
\varphi : A \rightarrow B
\]

such that:

\[
\varphi(a_1 \star a_2) = \varphi(a_1) \diamond \varphi(a_2)
\]

This condition is the **homomorphism property**.

---

## Key Points

- The map preserves the operation (structure is maintained).
- The function is **one-way** (from \(A\) to \(B\)).
- It does **not** need to cover every element of \(B\) (not necessarily surjective).
- It does **not** need to be reversible (not necessarily injective).

---

# Examples of Homomorphisms

---

## Example 1 — Integers → Even Integers (Addition)

Let:

\[
A = (\mathbb{Z}, +)
\]
\[
B = (\text{even integers}, +)
\]

Both are groups under addition.

Define:

\[
\varphi(x) = 2x
\]

Check the homomorphism property:

\[
\varphi(x_1 + x_2) = 2(x_1 + x_2)
\]
\[
= 2x_1 + 2x_2
\]
\[
= \varphi(x_1) + \varphi(x_2)
\]

So the structure is preserved.

✓ This is a homomorphism.

---

## Example 2 — Strings → Non-negative Integers (Concatenation → Addition)

Let:

- \(A\) = all strings under **concatenation**
- \(B = \mathbb{Z}_{\ge 0}\) under **addition**

Define:

\[
\varphi(s) = \text{length of string } s
\]

Examples:

- "Rare" → 4  
- "skills" → 6  
- "RareSkills" → 10  

Check:

\[
\varphi("Rare" \mathbin{+\!\!+} "skills") = 10
\]
\[
= 4 + 6
\]
\[
= \varphi("Rare") + \varphi("skills")
\]

✓ Concatenation maps to addition correctly.

So this is also a homomorphism.

---

## Example 3 — Real Numbers → Matrices (Addition)

Let:

\[
A = (\mathbb{R}, +)
\]
\[
B = (M_{n \times m}(\mathbb{R}), +)
\]

Define a map such as:

\[
\varphi(x) =
\begin{bmatrix}
x & 0 & \dots \\
0 & x & \dots \\
\vdots & & \ddots
\end{bmatrix}
\]

(or any consistent way to embed a real number into a matrix)

Check:

\[
\varphi(x_1 + x_2) = \varphi(x_1) + \varphi(x_2)
\]

Matrix addition preserves the structure.

✓ This is a homomorphism.

---

> i used chatgpt for maths syntaxing, idk how do i make it work. thanks for your patience ^_^

There are many more examples in the ZK book which i highly highly recommend reading [Here](https://rareskills.io/post/homomorphisms)
