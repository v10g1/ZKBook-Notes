# 📘 Zero-Knowledge Book — Module 1 Notes

> Note: English is not my first language. These notes focus on clarity of concepts.

---
Abstract Algebra is the study of sets that have one or more operators on that set.

Lets GOO

## Magma
A Magma is a set with a closed binary operator. That’s all.
For example, consider the set of all positive integers and our binary operator be x^y

## SemiGroup
A Semigroup is a Magma where the binary operator must be associative.
(a∗b)∗c=a∗(b∗c)for all a,b,c

All semigroups are magma.

### Question 1
Work out for yourself that concatenating `"foo"`, `"bar"`, and `"baz"` in that order is **associative**.

Recall that associative means:

\[
(A \square B) \square C = A \square (B \square C)
\]

where \( \square \) is the semigroup’s binary operator.

Here, \( \square \) represents **string concatenation**.

Verify that:

\[
(\text{"foo"} \square \text{"bar"}) \square \text{"baz"}
\;=\;
\text{"foo"} \square (\text{"bar"} \square \text{"baz"})
\]
Answer. 
lets consider a string set like {foo,bar,baz}
a= foo b=bar c= baz
a () b = "foobar" () c = foobarbaz
b () c = "barBaz" => a () "barBaz" = foobarbaz

## Question 2
Give an example of a Magma and a Semigroup. The Magma must not be a Semigroup. Don’t use the examples above. This means you must think of a binary operator that is closed but not associative for the Magma, and for the Semigroup, the binary operator must be closed and associative.
Answer. 
Lets try to work this one through
What we Know -> magma is a set with any op
so lets say Addition over Z, this is a magma but also a semigroup.
hmm....
it should not have the thing abc= bca
how about the op log with base a and value b
its surely a magma but not a semigroup 
and for magma, lets say addition/ multiplication over Z or R

## Monoid
A Monoid is a Semigroup with an identity element.
a∗e=e∗a=a
there is a bunch of yapping about this topic in the book, so i just gave it a read but did not actually created notes for it

## Group
A  group is a monoid in whcih each element has an inverse
or to be Explicit it is a set with follow props
- closed
- associative
- identity element
- ever element has an inverse
Lets say there exists one identity element such a () b = i. then
b here is the inverse of b.


It is rather incorrect to say “the set has an inverse.” To be precise, every element has another element in the set that is that element’s inverse.

### Question
Why can’t strings under concatenation be a group?
Answer. hmmm we just proved it was a magma, semi group and monoid
So like
lets focus on the property of group whcih was the identity element and the inverse
lets assume that the identity element is "" the empty string
so like 
"foo" + something = ""
Which is not possible.
So this is the reason.
### Question 
Polynomials under addition satisfy the property of a group. Demonstrate this is the case by showing it matches all the properties that define a group
Lets say the the polynomial was like 
Sum(a_n*x^n)
So like it is under the constraint of addition on the whole set