[Source](https://rareskills.io/post/bilinear-pairing)
###
Pairings->
Assume three numbers like A B C where ab=c then we can encrypt them like E(a) E(b) E(c) and then send the two encrypted values to the Verifier who can verify E(a)E(b)=E(c) but don't know the original values, we can use Bilieanr pairing to prove that a 3rd number is the product of the first two or not without knowing the first two original numbers.

> This is in python, i will try to do the same in rust, cuz i like rust more and that is obviously superior

Now lets get back to work

Whena saclar is multiplied by a Point on an elliptic curve, another elliptic curve point is produced

this was actually tought in the mod-1, if you haven't check that out please do UwU

Given P and G we cannot determine P
assume Pq=r

P=pG
Q=qG
R=rG
Where G is the generator.
we need to convince the verifier that the discrete logs of P and Q multiple to produce the discrete log of R

if pq=r (given)
and other conditions
then we need to have a function such that
F(P,Q)=R
and not eqaul to R when pq!=r

Which is the basic point point of the whole conversation haha

Now the blog stated, that we don't actaully express it as the above but instead we do this as 

f(P,Q)= f(R,G)

Why? Will learn the reason later in this notes (because right now, even i don't know lol)
G is the generator point, and can be thought of as 1.

So our bilinear pairing is a function that if you plug in two elliptic curve point you get an output that corresponds to the products of the discrete logns of those two point


Okay i did not understand that last sentence leme just gpt that

Okay i do not understand what that dumb AI is saying eigther. ＞︿＜

Lets skip this part for now

- Bilinear mean that if a function takes two arguments and one of them is held constant and other vaires, then the output linearly varies with the non constant part.

if F(x,y) is bilinear and c is constant then z = f(x,c) varies linearly with x and z=f(c,y) varies with y

Damn this is interesting
> By the end of these notes i am pretty sure i will fall in love with maths again.

By this we can say
f(aG,bG)=f(abG,G)=f(g,abG)


## but what this actualy is?
what is this actaully returning?

what do you mean v10g? 

i mean this e(P,Q)

hmmmm......

According to the blog we should just keep it as a mystry value that return nothing but maths.

Okay sherlock, what else?

the blog stated
```md
It’s best to treat e(P,Q) as a black box similar to how most programmers treat hash functions like black boxes.
```

Okay lil bro, we know alot of things from this like
- Gt is a cylic group
- binary operator of gt is associative
- has an indenity element
- Each element in Gt has an inverse
- it has a generator
-Because the group is cyclic and finite, then finite cyclic groups are homomorphic to Gt

It is a 12 dimensional object.
No shit.

## Symmetric and Asymmeteric Groups
When the Generator for all curves are same then we can say
e(aG,bG)=e(abG,G)

but this might not be true
e(a,b)-> c a:G1 b:G2 c:G3

e(aG1,BG2)=e(abG1,G2)=e(g1,AbG2)

In the above equation, the group Gt is not explicityly shown but that is the co-domain output space of e(G1,G2)

One could think of G1 and G2 being different elliptic curve equations with different parameters (but the same number of points) and that would be valid because those are different groups.

### Field Extensions and the G2 point in Python
Bilinear pairings are rather agnostic to the kinds of groups you opt for, but Ethereum’s G2 uses elliptic curves with field extensions. If you want to be able to read Solidity code that uses ZK-SNARKS, you’ll at least need a rough idea of what these are.

too much yap

crux of it->
-> Elliptic curve in g2 is an elliptic cruve where both the X and Y element are two Dimenesional Objects.

Look the test.py file for this.

g1 AND g2 are the generator points for their groups.

 Small note -> order of the group is the number of points on the curve

 Both G1 and G2 have the same order.

## Equality of products
Simple stuff

## Eip-197
This specifies the working of the bilinear pairing on EVM
py_ecc is maintained by Ethereum foundation 
Ethereum precompiled defined in EIP-197 wokrs on point in G1 and G2, and implicitly works on point in Gt
The specification of this precompile will seem a little wierd at first. It takes in a list of G1 and G2 points laid out as follows:
`A1A2B1....`
These were originally created as 
A1= a1G1

..

and so on

precompile returns 1 if the following is true

a1b1 + a2b2+.....= 0

otherwise 0

The first problem is that elements in Gt  are large, specifically, they 12-dimensional objects.

This will take up a lot of space in memory leader to larger gas costs. Also because how most Zk verificatio algorightm work (this is outside the scope of this article), we generally don't check the value of the output of a pairing, but only that it equal to other pairings.

In the final steps of Groth16 (used by tornado cash) looks something like
e(A1,B2)=e(alpha1,beta2)+ e(L1,gama2)+e(C1,delta2)


Where each varaibles is an elliptic curve point of eigther G1 or G2 based on its subscript notation 

> I have No idea how this will used in Groth16, but i believe em
The meanings of these variables is not important at this stage. The fact that it can be written as the sum of “products” (elliptic curve pairing) is what matters. Specifically, we can write it as


## Missing knowledge
during the reading after this point, they used the property like
e(A1,B2)=e(alpha1,beta2)+ e(L1,gama2)+e(C1,delta2)

become

0=e(-A1,B2)+e(alpha1,beta2)+ e(L1,gama2)+e(C1,delta2)

I don;t remeber where this was introduced so asked my friend gpt to explain this and it said



Fix Q ∈ G₂.

Define

    φ(P) = e(P, Q)

Then φ is a group homomorphism:

    φ : G₁ → G_T

Meaning it preserves the group operation:

    φ(P + R) = φ(P) + φ(R)

Substitute definition of φ:

    e(P + R, Q) = e(P, Q) + e(R, Q)

This is exactly bilinearity of the pairing.

---



In any group:

    P + (-P) = 0

Apply φ:

    φ(P + (-P)) = φ(0)

Using homomorphism:

    φ(P) + φ(-P) = 0

So:

    φ(-P) = -φ(P)

Substitute back:

    e(-P, Q) = -e(P, Q)

---



If G_T is written multiplicatively:

    e(P + R, Q) = e(P, Q) · e(R, Q)

Then:

    e(P, Q) · e(-P, Q) = 1

So:

    e(-P, Q) = e(P, Q)^{-1}

I got confused between the addition notation and multiplicative notation in the blog

Let me summarise it
 for addition

 e(-a,b)=-e(a,b)

and for multiplication 

e(-a,b)=e(a,b)^-1

Okay now lets continue.
---

It’s not just Groth16, most zk algorithm have verification formula that looks like that, which is why the precompile was designed to work with sums of pairings rather than return the value of a single pairing.

## Sum of discrete log

ab+ cd =0

yup thats it

## A mega Example in solidity
