> One more baby chapter yay

## Statement
Gives a tight upper bound on the probability that a non-zero polynomial accidentally evaluates to 0 at a random point.

This is the mathematical backbone of randomized polynomial identity testing, and in zk it justifies

We can test that two polynomials are equal by checking if all their coefficients are equal, but this takes O(d) is the degree of the polynomial.

If instead we can evaluate the polynomial at a random point u and compare the evaultation in O(1) time

We can combine Lagrange interpolation with the Schwartz-Zippel Lemma to test if two vectors are equal.

How lil bro?

- We can interpolate a polynomial for each vector f(x) and g(x)
- Pick a random point u
- Evaluate the polynomial at u
- f(u)= g(u)

Although computing the polynomials is more work, the final check is much cheaper.