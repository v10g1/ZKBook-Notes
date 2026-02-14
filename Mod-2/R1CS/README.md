Ohhhhh boy we are getting to the good part 

> read Mod-1 first lil bro

## R1CS
Rank 1 constraint system is an arithematic circuit which with the requirement that each eqaulity constraint has one multiplication 

This makes the representation of arithmetic circuit compatible with the use of bilinear pairing

The output of a pairing G1 # G2 -> Gt cannot be paired again, because as an element in Gt cannot be used as part of the input of another pairing.
> I will use my native langauge for a bit, sorry for the inconvience
## Witness
Kya hai witness? 
witness ek aisi setg of values ki jab sare wires/ variables ko value de di jaye to sare eqautions true ban jaye.
In R1CS the witness vector is 1Xn that contains the value of all the input variabes, the out variable, and the intermediate values. It Shows you have executed the circuit from the start to finish, knowing both the inpt, output and all the intermediate values.


By convention, the first element is always 1 to make calc easier.

example constraint
z=x^2y
v1=x*x
z=v1y

witness means we on;t just know xyz and we must know every variable

`[1,x,y,z,v1]`
# Example
z=xy
lets say 41*103=4223

there out witness vector is `[1,4223,41,103]` as an assignment to `[1,x,y,z]`

before we can create an R1CS our contract need to be of the form
result = left_hand*rightHand
luckily this time it already is

Our goal is to create a system of equations of the form:
Oa=la # ra
where  o l a are the matrices of size nxm

Matrix L encoddes the variable on the left of the multiplication and R encodes the variabled on the right of the multiplication. O encodes the result varaibles. The vector a is the witness vector.

L R O are the matrices wo=ith the same number of columns as the witness a and each column represents the same varaibles the index is using.

So for our example, the witness has 4 elements (1,x,y,z) so
each of our matrices will have 4 columns, so m =4

The number of rows correspond to the number of contraint in the ciruit. In our case, we have only one constraint z=x*y, So we will only have one row so n=1

Let’s jump to the answer and explain how we obtained it.
```
[0,1,0,0]a=[0,0,1,0]a # [0,0,0,1]
```
In this example, each item in the matrix serves as an indicaator variable for wheather or not the variable the column corresponds to is present

# Example 2
Transforming r = x * y * z * u
v1=xy
v2=zu
r=v1v2

There are 7 variables
(1,x,y,z,u,v1,v2)
i cannot do alot of the maths work here because they are using matrices.
