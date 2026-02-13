# 📘 Zero-Knowledge Book — Module 1 Notes

> Note: English is not my first language. These notes focus on clarity of concepts.

---

## Sets

A **set** is a well-defined collection of objects.

Examples of sets include:

- Integers
- Rational numbers
- Real numbers
- Complex numbers
- Matrices
- Polynomials
- Polygons

All of these can be treated as collections of elements that follow set rules.

### Properties of Sets

- A set **cannot contain duplicate elements**.
- Order does **not** matter.

---

## Number Systems and Relationships

There is a natural hierarchy among common number systems.

### Definitions

**Natural numbers (ℕ)**  
\[
\{1, 2, 3, 4, 5, \dots\}
\]

**Integers (ℤ)**  
\[
\{\dots, -2, -1, 0, 1, 2, \dots\}
\]

**Rational numbers (ℚ)**  
Numbers that can be written as a fraction:
\[
p/q \quad \text{where } p, q \in \mathbb{Z},\ q \neq 0
\]

**Real numbers (ℝ)**  
All rational and irrational numbers.

**Complex numbers (ℂ)**  
Numbers of the form:
\[
a + ib \quad \text{where } a, b \in \mathbb{R}, \ i^2 = -1
\]

---

## Subset Relationships

Each set is contained inside the next:

\[
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
\]

Meaning:

- Every natural number is an integer  
- Every integer is rational  
- Every rational is real  
- Every real number is complex  

Each inclusion is a **proper subset**.

---

### Question 1

**Define the subset relationship between integers, rational numbers, real numbers, and complex numbers.**

Answer:

\[
\mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
\]

All are proper subsets of the next larger set.

---

### Question 2

**Define the relationship between transcendental numbers and complex numbers. Is it a proper subset?**

### Definition

A **transcendental number** is a number that is **not algebraic**.

An algebraic number satisfies a polynomial equation:

\[
\sum_{n=0}^{k} a_n x^n = 0
\]

where the coefficients \( a_n \) are integers (or rationals).

If a number does **not** satisfy any such polynomial, it is transcendental.

### Examples

- \( \pi \)
- \( e \)

### Relationship with Complex Numbers

- Transcendental numbers are contained inside the complex numbers.
- Not all complex numbers are transcendental (many are algebraic).

Therefore:

\[
T \subset \mathbb{C}
\]

This is a **proper subset**.

## Set Equaliity
Two sets are called equal only and only if the they contain the same elements

Example 
{4,2,5} is same as {2,5,4}

### Cardinality
This is the Number of element that the set contains which is being considered

### Question 3
Using the formal definition of equality above, argue that if two finite sets have different cardinality, they cannot be equal. (Demonstrating this for infinite sets is a little trickier, so we skip that)
Answer . Lets take the example of two sets
lets take Set A= {1,2,3,4,5}
and Set B = {1,2,3,4,5,6}
Here we can clearly see that the cardinality of A is 5 and B is 6
And we can clearly see that the element in B is not present in Set A

That was the answer for the finite sets, let's also talk about infinite  sets.
So Infinite sets can have different cardinality based on the type of set under consideration
lets say set Z, which is the Set of all the integers, its cardanality is finite number on the other hand the cardinatlity for the Set of R is infinite anyway because there is no way to count this.

## Ordered pairs
- pairs of object in which the order of the elements are important
We programmers typically think of an ordered pair as a tuple. We say two ordered pairs are equal in the same sense we say two tuples are equal.
## Cartesian product
We can deine a set such that ever element from one set is one part of an ordered pair with an element from another set
A ={1,2,3}
B={x,y,z}

AxB=> {(1,x),(1,y)...} so on
- cartesian products are not commutative
## Functions
I was wondering why am i even reading this, i have studied all of these in high school.
then this section came up
-The subsets of the cartesian products is functions
To define a function, we need the set we start from and the set we end at. We take the Cartesian product of these two sets, which results in every possible assignment from the input set to the output set. Then we take the subset of the Cartesian product to define the function as we like. 
- Functions are not necessarily computable

Most of the Other things in this blog, was already covered in my UNI
and this was very basic anyway.