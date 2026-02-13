# 📘 Zero-Knowledge Book — Module 1 Notes

> Note: English is not my first language. These notes are meant for quick revision and intuition rather than perfect explanations.

## Defination
The set of point on an elliptic curve form a group under elliptic curve point addition

The equation looks something like
y^2= x^3 + ax + b

a point on an EC is an (x,y) pain that satifies the above equation
ofcourse for a give A and B 

## Important note
Elliptic Curves form an abelian group under addition

We won't know how the Binary operator works we do know that it takes two points on the cutve and return another point on the curve. Becasue the operator is closed, we know that the point will be in fact a valid colution to the elliptic curve eqaution,
Bot a Point somewhere else
We also Know that this binary operator is associative ( and commutativ, per thr section heading).
So give three point os the curve A B C, then we know the folloring true

(A something B) something c = A something ( B something C)

Something can be any binary function. (some might not work tho)

Point that falls on the curve is combined with the identity element, the output is the same (x,y) point unchanged. which is obvious

Each element also has a inverse.
such that 
P something P_i = I 

## Identity element
The Blog said you need to think the elemeent as the "the point of nowhere" because this point will make you go no where (*hahahaha....you got it? anyone..... no?*)

it also said that binary operator are just subsets of the catesian products, and we can define the relation however we like, We can have as many hacky "if statements" in our arithematic as we please

I can not quiet understant what this mean, let me just quick chatgpt this shit

According to my friend
binary op on a set is essentially a function 
*:SxS -> S
input: an ordered pair (a,b)
output: another element is S
so this mean we can do whatever we want and make the function as defined as we like?
...

interesting

## Addition is close
In the blog they had taken an example of the simulation and the graph of the two function, and show the intersection of two curves one was a elliptic curve and the other was a straight line and then they said 

->
If a straight line crosses an elliptic curve at exactly two points, and neither of the intersection points are tangent intersections, then it must be perfectly vertical.

Yea, no shit sherlock. 🙏

I drew some graphs on the [desmos](https://www.desmos.com/calculator)
You should also do the same.

### But wait?
What about invserse
the Blog said a subtle line about this
The inverse of an elliptic curve point is the negative of the y value of the pair.

so (x,y)'s inserve is (x,-y)
Interesting.

## abelian group
A little breather -> A group who is also commutative is a abelian group
When we pick two point, there is only one other third point, You can't get four intersections in a elliptic curve.
well yea for a straight line, it is true.

## Formula for addition
P1=(x1,y1)
P2=(x2,y2)
One can derive how to compute P3= (x3,y3)
Where P3= P1 OP P2
lemda= y2-y1/x2-x2
we got the slope 🤔
x3= (lemda)^2 -x1-x2
y3=lemda(x1-x3)=y1


