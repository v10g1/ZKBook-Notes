> This relatively a smaller chapter but lets go through it.



Given an arithmetic circuit encoded as a Rank 1 Constraint System, it is possible to create a ZK-proof of having a witness, albeit not a succinct one. This article describes how to accomplish that.

A zero knowledge proof for an R1CS is accomplished by converting the witness vector into finite field elliptic curve points and replacing the Hadamard product with a bilinear pairing for each row.

Lets say the R1CS is like 
La # Ra=Oa
Where L R O are matrices with n rows and m columns, and a is the witness vector (containing a satisfying assignement to eachb of the singlas in the artimetic circuit).

The vector a has 1 column and m roes and # is the element wise multiplication (Hadamard product).

We Expand all the thing here which will be look like something in the book (i cannot write the whole thing here lil bro)

We are just doing the matrix multiplication here

(Matrix 1) # (Matrix 2)= (result matrix)

In this setup, we can prove to a verifier that we have a witness vector 
a
a that satisfies the R1CS simply by giving them the vector 
a
a, but with the obvious drawback that this is not a zero knowledge proof!

> This is not a Zero knowledger, this is just a knowledge lol

If we encrypt the witness vector by multiplying each entry with g1 or g2, the math will still work properly!!!

To understand this, consider that if we carry out the multiplication 
The discrete logs of the two elliptic curve points in the second matrix multiplication are the same value  as the element of the first matrix multiplication

In other words, each time we multiply the column vector by a row in the square matrix, we carry out two elliptic curve point multiplications and one elliptic curve addition

### Elliptic Curve Notation

Let \( G_1 \) and \( G_2 \) be generators of the groups \( \mathbb{G}_1 \) and \( \mathbb{G}_2 \), respectively.

- We denote  
  \[
  [aG_1]_1
  \]
  as a point in \( \mathbb{G}_1 \) obtained by scalar multiplication of the generator \( G_1 \) with a field element \( a \).

- Similarly,  
  \[
  [aG_2]_2
  \]
  denotes a point in \( \mathbb{G}_2 \) obtained by multiplying the generator \( G_2 \) by the scalar \( a \).

Because of the discrete logarithm problem, given either
\[
[aG_1]_1 \quad \text{or} \quad [aG_2]_2,
\]
it is computationally infeasible to recover the scalar \( a \).

Given points
\[
A \in \mathbb{G}_1, \quad B \in \mathbb{G}_2,
\]
their bilinear pairing is denoted as
\[
A \cdot B.
\]


## Steps for prover
1. encrpt our vector a by multiplyig each entry with the geenrattor point G1 to produce the elliptic curve point [aiG1] 

We just multiply the L matrix with the a (witness) matrix here

Where each of the A element is being multiplied

Similarly we do the same with the R vector with multiplying vector a with g2

After this operation we have a single column of elliptic curve points in G1 originating from the multiplication La and a single column of G2 point from Ra

## verification

The elements will be element wie eqaul if and only if we the prover has provided a valid witness

## Public inputs

IF our knowledge claim is like i know x such that x^3+5x+5=y where y=155 then out witness vector will probably look like the following

where v=x^2 in thiscase, we need [1,y] to be public. to accomplish that, we simply don't encrypt the first two element of the input so that the verfication formula does not change

## Malicious claims and provers
Because the vectors are encrypted, the verifier cannot immediately know if the vector of G1 points encrypts the same values as the vector of G2 point.

That is, the prover is supplying aG1 and aG2. Since the verifier doesn't know the discrete logs of the vector of points, how does the verifier know that the vector of g1 points has the same discrete logs as the vector of g2 points?
The verifier can check for the equality of the discrete logs (without knowing them) by pairing both vectors of points with a vector of the opposite generator and seeing that the resulting G12 points are equal. 





