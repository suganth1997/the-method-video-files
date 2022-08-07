## Introduction
`quote and picture rolls in`

Hello everyone, here I would like to talk about a method from one of the greatest ancient mathematicians, engineer, scientist and what not, Archimedes. This method of archimedes which in itself called "The Method" is the most elegant one I have seen for a problem, is not taught nowadays as it is not needed for modern day mathematics but I believe it would be a great example of how perspectives can help us solve the unsolved.

`law of levers`

Ofcourse Archimedes lived in the ancient Greece, his time comes after Euclid and even he cites from Euclid elements in his works. He lived in the city of Syracuse and is said to have a hunger for knowledge and helped the Greek kings in the wars. When the Romans invaded syracuse, which by the time Archimedes have figures out the law of levers with which he had helped develop catapults and weapons to help the destroy Roman ships.

`law of buoyancy`

And we would definitely know the Archimedes principle for buoyancy of submerged bodies with which the infamous Eureka story. The king of Syracuse had given Archimedes with the task of finding if the crown made by the goldsmith was indeed made of pure gold or it was adulterated with silver. We all might have heard of the story that he figured this out with buoyancy when he was taking his bath and rand across the streets of Syracuse shouting Eureka! but actually to see how he did it will take another video to explain, so let's move on.

`works on geometry`

As an engineer, I have heard of the Archimedes principle in the context of fluid statics but what we might not know is that he was a great geometrician. The ancient greeks were infact curious about everything and the curved shapes such as circles and conics intrigued them. His works on Geometry were recovered from ancient writings and was published in 1858 by **said college** serves to be the best compilation of his works. But the method which I want to talk about here was not recovered in that publication, it was recovered later in 1901 and translated by the same author.

`value of pi`

I first came across this method when I was reading 'Infinite Powers' by Steven Strogatz, in which he rightfully calls Archimedes as 'the man who harnessed infinity' which also translates to that he discovered integration in his quest. To emphasize this, he discusses a method to calculate the value of pi. One thing the Greeks have figured out was the ratio of the circumference to the diameter of a circle is constant, but the value was not known. What he does is that he inscribes a polygon inside the circle and circumscribes another polygon outside the circle. So the perimeter of the polygons create an upper bound and a lower bound on the value of circumference of the circle. And they had figured out things with straight lines better than curves. As you refine your polygons and increase the number of sides, you inch closer and closer to the value of pi. But when the number of sides increases this would take a great deal of manual work to compute the numbers. This was actually the best known method to calculate pi until Newton came along.

`area of parabola`

The so called 'The Method' is actually a method he came up with to calculate the area of the parabola, infact he had multiple approaches to calculate this, we will start with one such approach and then move on to 'The Method', the reason I want to show this is because to emphasize how he had chopped his problems into small chunks and combined them in brilliant ways to solve the actual problem, which is infact what integration is harnessing the infinity.

So we take a parabolic segment, any segment and first construct a triangle by joining the ends of the parabolic segment and a point on the parabola. The way we choose this point is by taking the line segment closing the parabola and seeing which point on the parabola has a tangent parallel to the line segment that is closing the parabola. This way we continue to divide the parabolic segment in multiple steps. Here what he shows is that, a single triangle in the second step of subdivision has an area which is one eigth of the triangle from the previous step. With this we can construct a series to calculate the area of the parabola as the infinite subdivided triangles cover the parabolc segment completely. With this we can see it's a simple manipulation and we have the area of parabola in terms of the area of the inscribed triangle, and the Greeks knew the area of triangles as half base into height.

Even after figuring this out, he did not stop there, he wanted to apply his most elegant reasonings to this problem of area of parabola, which we will see in the so called 'The Method'.

`the method -- parabola`

We will start with the same parabolic segment, even this method is applicable to any parabolic segment, but here I have only considered a regular segment because I am only a beginner to this beautiful animation tool manim, thanks to Grant of 3b1b. 

First let us name the line segment enclosing the parabola as AC, then we will construct a line that is tangent to the parabola from the end C and from the other end A we draw a line parallel to the axis of the parabola which will meet the tangent line at F, same way we also draw a line parallel to the axis of the parabola through the mid point of the line segment D, which meets the parabola at B and the tangent line at E, this makes our parabola as ABC. Now we can form the triangle inscribed by the parabola by joining AB and BC, and we also extend the line BC to meet the line AF at K.

Now we consider any line parallel to the axis of the parabola, let us make such a line MO which meets the line CK at N and the parabola at P. Now if we say something about the line PO, it should and will hold for any line parallel to the axis of the parabola, or any section of the parabola. Here I would like to fast forward a property which Archimedes had proved in his works named the 'Quadrature of the Parabola', I am not getting into proving this but only how he uses this property to arrive at an elegant explanation. So the property is basically this, the ratio of the line MO which is any parallel line to the axis to the line PO which the same line intersects with the parabola is same as the ratio of the line segment AC enclosing the parabola to this length AO. This ratio can also be written in terms of the CK and KN as the triangles ACK and OCN are similar triangles. This we have from Quadrature of the Parabola.

Now in The Method, what he does is that, if we construct a line HK from K by extending the line CK and by construction we choose HK the same length as CK, then we can modify this ratio relation and if we re arrange and write it as a product expression, so now this holds for any section of the parabola.

I think until this point anyone could've done but what he does next is probably only what Archimedes might've done. Now he sees this product relation as a fulcrum and a lever relation. The length of lines MO and PO are just a measure and hence we could consider them balancing on a lever with MO placed at length KN and PO placed at length HK from the center. I would like to say that this is where his engineering comes into play and now he moves on to harness infinity.

So this would apply to any section of the parabola, and hence if we consider every possible sections of the parabola then we could say that the area of the parabola ABC placed at a length HK from the center is in balance with the area of the triangle ACF placed at a length, so this length is a bit tricky as in our relation this length which is KN keeps varying. Actually as this length is varying, he says that it will be at balance when the triangle is hinged at the centroid. To see this better let us consider an isoceles triangle with the same area and same height as triangle ACF, I have modified the base accordingly for construction but the area is the same. With this setup we could intuitively see that it will be in balance when we hinge it at the centroid, and hence KN become one third of HK.

Now we can write the fulcrum lever balance for this setup and substitute this KN and HK relation to arrive at the area of the parabola relating to the area of the triangle, which can be easily calculated. And there is also a relation between the larger triangle and the inscribed triangle and the area of the parabola can be expressed as fourth thirds of it which we also confirmed from one of the earlier methods.

Eureka!

Let us dial back, so he starts by choosing any section of the parabola, builds a property on it, changes the lens to see the same from a different perspective, integrates it over the parabola and he has managed to express the area of a curved shape such as a parabola in terms of a straight shape whose area is known. That sounds incredible, to me atleast, and another venue to emphasize that changing the perspectives can help us solved the unsolved.


`end`

Also to emphasize why just finding the areas which are simple to us were great at that time is because that, we now know integration to calculate areas of curved bodies and algebra to write equations of curved bodies and graph to visualize those equations, but in those days none of the above were there. Even the parabola is defined as shape  you get when you cut the cone is specific angles and not as y=ax^2. Maybe if Descartes and Fermat were born at Syracuse, the brachistochrone problem would've been proposed in Greece itself.

`end quote`

I would like to end here with a quote giving the same emphasis on perspectives. If you have watched this far, thank you for your time and thanks for watching.