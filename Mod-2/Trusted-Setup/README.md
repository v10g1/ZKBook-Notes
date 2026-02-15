Trusted Set in Zero knowledge proof Systems in one time cryptographic paramster generation parae where secret randomness is used to create public proving/verification keys

If that randomness is leaked or key, the holder can forge for false statements. That's the trust assumption

below is the precise view

# why?
Some proving systems need:
Structured refernce string (SRS)
this SRS contains precomputed group elements like:
[g,tg,t^2g...]

where t is the secret

these power enables:
polynomial commitments

....

A trusted setup is a mechanism ZK-snarks use to evaluate a polynomial at a secret value.


f(x)=3x^3 +2x^2+5x+10, then the coefficients are [3,2,5,10] and we can compute the polynomial at these values

We think as like 
3(2)^3+.....

but we can also do it like
f(2)=<[3,2,5,10],[8,4,2,1]>
= 3.8 + 2.4 + 5.2+ 10.1

damn i never realised this way

Now suppose that someone picks a secret scalar T and computed 
[t^3,t^2,t,1]

then multiplies each of those points with the generator point of a cryptographic elliptic cruve group. The result would be as follow:
[O3,O2,O1,G1]=[t^3G1,t^2G1....]
Now anyone can take the SRS and eval the degree three polynomial of T

example ie we have degree 2poly g(x)=4x^2+7x+8 we can eval g(t) by taking the iner product of the structured reference string with the polynomial

<[0,4,7,8],[O3,O2,O1,G1]> = 4O2+7O1+8G1

Now we know g(t) without knowing T

This is also called a trusted setup because although we don't know what the discrete log of g(t) is, the person who created the structured reference string does. This could lead to leaking information down the line, so we trust that entity.

## Verifying a trusted setup was generated properly

Given a structured referce string, how do we even know that they follow the structure ?

If the person doing the trusted setup also provide Theta= TG2, we can validate the reference string
e(theta,Oi)=e(G2,Oi+1)
Where e is bilinear pairing. Intuitively, we ae comparing t.t^i on left and t^i+1 on the other side.

To validate the theta and O1 have the same discrete logaritms (O1 is supposed to be tG1), we can check that.

## Evaluating a Quadratic Arithmetic program on a trusted setup
> This topic is in other chapter but I think this is closely related to this chapter so should be done here

Evaluating a Quadratic Arithmetic Program (QAP) on a trusted setup enables a prover to demonstrate that a QAP is satisfied without revealing the witness while using a constant sized proof

Specifically, the QAP polynomials are evaluated at an unknow point t. the QAP eqaution


## Example
Lets say the matrix of the R1CS L,R,O have 3 row and 4 columns
Since we have 3 rows, it mean our interpolating polynomial will be of degree 2. because we have 4 columns, each matrix will result in 4 polunomial (fpr a total of 12 polynomials)

