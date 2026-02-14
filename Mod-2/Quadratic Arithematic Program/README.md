we know
La # Ra = Oa

holds O(1) time instead of O(n) time (where n is the number rows in L, R and O)

But before we do that, we need to understant some key properties of the relationship between vectors and polynomials that represent them.


## Homomorphisms between vector addition and polynomial addition
If we take two vectors, interpolate them with polynomials, then add the polynomials toegther, we get the same polynomial as if we added the vectors together and then interpolate the sum vector.

L(v+w)=L(v)+L(w)

In other words the polynomial result from interpolating vector V and W are thr Same as the polynomial resulting from interpolating the vectors V+W

## Scalar multiplication 

Let lemda be a scalar (specifically, a field elemnt in the finite field)
then 
L(λv)=λL(v)

........


am not understanding a single word at this point bruh


leme just go throught someone else's notes on github 

for reference i got Zigtur's notes which is [here](https://github.com/zigtur/Rareskills-ZK-book/tree/master/quadratic-arithmetic-programs)
A QAP is a system of eqaution where the coeficient are monovariate polynomials and a valid solution results in asingle polynomial eqaulity. They are quadratic because they have exactly one polynomial multiplication. QAP allows the zk-snarks to be fassttt

An R1CS evaluation is not succint due to many matrix multiplications.

One multiplication take about O(n^2.38) by the best algo right now
Due to Schwartz-Zippel Lemma, polynomials allow us to make statements succinct. In a sense, we can compress a polynomial down to a single point. Key idea is:

1. Operations in r1cs form an algebraic ring
2. Polynomials under addition and multiplication are rings
3. There exists an easily computable homormorphism from R1CS to polynomial

I did not knew what rings was, so checked this [video](https://www.youtube.com/watch?v=j_f7O-4Rb9U)

it is very good and consize

## Rings

A ring is simply a set with addition and multiplication and distributive property of both
operator: addition
identity: all vector zero
inverse: vector with elements multiplied by -1
operator: multiplication (hadamard product)
inverse: no inverse for multiplication
Polynomials are also a ring

## Ring homomorphism
Theorem: there exists a ring homorophism from columns vectors of dimension n with real number to polynomials with real coeficients.

We need to think polynomial as an infinite set of pairing (x,y) instead a = ax^2 + bx +c


# R1CS to QAP
Since we know how to test of Av1=Bv2 succintly, can we also test if La # Ra = Oa succintly

The matrices have M columns, so lets break each of the matrices into m coulms and interpolate them on (1,2....n) to produce m polynomial each

Manhhh am not writing that much here, there just matrices all over bruhh

how am i supposed to write altat here, and no am not in the mood to use latex in my personal notes

## Polynomial degree imbalance

However, we can't simply express the final result as 
u(x)v(x)=w(x)
because the degree won't match

multiplying two polynomials together resutls in a profuct polynomial whose degree is the sum of the degree of the two polynomials being multiplied together

# The nexxt chapter
Am including the next chapter in the same because its a small baby chapter.

To make the transformation fro R1CS to QAP less abtract, let's use a real example.

Let's say we are encoding the arithemetic circuit

z= x^4-5y^2x^2

v1=x*x
v2= v1*v1
v3=-5y*y
-v2+x= v3*v1

We need to pick a characteristic of the finite field we will do this over. When we later combine this with elliptic curves, the order of our prime field needs to equal the order of the elliptic curve. (Not matching the two a very common mistake).

But for now, we will pick a small number to make this manageable. We will pick the prime number 79.

