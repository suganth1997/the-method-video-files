## Introduction
`quote and picture rolls in`

* Hello everyone, welcome to my video, here I would like to talk about a method from one of the greatest ancient mathematicians, engineer, scientist and what not, Archimedes. 

* This method of archimedes which in itself called "The Method" is the most elegant one I have seen for any problem and I believe it would be a great example of how perspectives can help us solve the unsolved.

`law of levers`

* Ofcourse Archimedes lived in the ancient Greece, his time comes after Euclid and even he cites from Euclid elements in his works. 
  
* He lived in the city of Syracuse and is said to have a hunger for knowledge and has helped the Greek kings in the wars. 
  
* When the Romans invaded syracuse, which by the time Archimedes have figures out the law of levers with which he had helped develop catapults and weapons to help the destroy Roman ships.

`law of buoyancy`

* And we would definitely know the Archimedes principle for buoyancy of submerged bodies which is even widely used today and with it the infamous Eureka story. 
  
* The king had given Archimedes with the task of finding if the crown made by the goldsmith was indeed made of pure gold or it was adulterated with silver. 
  
* It is said that when he figured this out with buoyancy during his bath he jumped and ran across the streets of Syracuse shouting Eureka! 
  
* but actually to see how he did it will take another video to explain, so let's move on.

`works on geometry`

* As an engineer, I have heard of the Archimedes principle in the context of fluid statics but what I did not know is that he was a great geometrician. 
  
* The ancient greeks were infact curious about everything and the curved shapes such as circles and conics intrigued them. 
  
* His works on Geometry were recovered from ancient writings and was published in 1897, serves to be the best compilation of his works.

## Value of Pi and area of Parabola
`value of pi`

* I first came across this method when I was reading 'Infinite Powers' by Steven Strogatz, in which he rightfully calls Archimedes as 'the man who harnessed infinity' which also translates to that he discovered integration in his quest. 
  
* To emphasize this, let us first look at a method which he discusses to calculate the value of pi. One thing the Greeks had figured out was the ratio of the circumference to the diameter of a circle is constant, but the value was not known. 
  
* What he does is that he inscribes a polygon inside the circle and circumscribes another polygon outside the circle. 
  
* So the perimeter of the polygons create an upper bound and a lower bound on the value of the circumference of the circle. 
  
* And they had figured out things with straight lines better than curves, so they knew how to calculate the perimeter of polygons even though it was a manual task

* Here I am just showing formulas with sin and tan for validation
  
* As you refine the polygons and increase the number of sides, you inch closer and closer to the value of pi. 
  
* But when the number of sides increases this would take a great deal of manual work to compute the numbers. 
  
* This was actually the best known method to calculate pi, well until Newton came along.

`area of parabola`

* The so called 'The Method' is actually a method he came up with to calculate the area of the parabola, infact he had multiple approaches to calculate this, we will see one such approach and then move on to 'The Method', the reason I want to show this is because to emphasize how he had chopped his problems into small chunks and combined them in brilliant ways to solve the actual problem, which is infact what integration is, harnessing the infinity.
  
* So we take a parabolic segment, any segment and first construct a triangle by joining the ends of the parabolic segment and a point on the parabola. 
  
* The way we choose this point is by taking the line segment closing the parabola and seeing which point on the parabola has a tangent parallel to it. 
  
* This way we continue to divide the parabolic segment in multiple steps. 
  
* Here what he shows is that, a single triangle in the second step of subdivision has an area which is one eigth of the triangle from the previous step. 
  
* This way if we continue to divide the parabola into triangles, we end up with an infinite series and this infinite sum would give the area of the parabola.
  
* Computing this infinite sum with a manipulation trick, we have the area of parabola in terms of the area of the inscribed triangle, and calculating area of triangles was known as half base into height.
  
* Next we will actually move on to 'The Method' which is again to calculate the area of the parabola.

## The Method
`the method -- parabola`

* We will start with the same parabolic segment, even this method is applicable to any parabolic segment, but here I have only considered a regular segment because I am still a beginner to this beautiful animation tool manim, thanks to Grant of 3b1b.

* First,
  * let us name the line segment enclosing the parabola as AC, 
  * then we will construct a line that is tangent to the parabola from the end C 
  * and from the other end A, we draw a line parallel to the axis of the parabola which will meet the tangent line at F, 
  * same way we also draw a line parallel to the axis of the parabola through the mid point of the line segment D, 
  * which meets the parabola at B and the tangent line at E, 
  * this makes our parabola as ABC. 
  * Now we can form the triangle inscribed by the parabola by joining AB and BC, 
  * and we also extend the line BC to meet the line AF at K.

* Now we consider any line parallel to the axis of the parabola, 
  * let us make such a line MO which meets the line CK at N and the parabola at P. 
  * Now if we say something about the line PO, it should and will hold for any line parallel to the axis of the parabola, or any section of the parabola. 
  * Here I would like to fast forward a property which Archimedes had proved in his works named the 'Quadrature of the Parabola', 
  * I am not getting into proving this but only how he uses this property to arrive at an elegant explanation. 
  * So the property is basically this, the ratio of the line MO which is any parallel line to the axis to the line PO which the same line intersects with the parabola is same as the ratio of the line segment AC enclosing the parabola to this length AO. 
  * This ratio can also be written in terms of the CK and KN as the triangles ACK and OCN are similar triangles. 
  * This we have from Quadrature of the Parabola.

* Now in The Method, 
  * what he does is that, if we construct a line HK from K by extending the line CK and by construction we choose HK the same length as CK, 
  * then we can modify this ratio relation and if we re arrange and write it as a product expression, so now this holds for any section of the parabola.

I think until this point anyone could've done but what he does next is probably only what Archimedes could've done. 

* Now he sees this product relation as a fulcrum and a lever relation. 
  
* The length of lines MO and PO are just a measure and hence we could consider them balancing on a lever with MO placed at length KN and PO placed at length HK from the center. 
  
* I would like to say that this is where his engineering comes into play

So this would apply to any section of the parabola, and hence if we consider every possible sections of the parabola then we could say that the area of the parabola ABC placed at a length HK from the center is in balance with the area of the triangle ACF placed at a length, 

* so this length is a bit tricky as in our relation this length which is KN keeps varying. 
  
* Actually as this length is varying, he says that it will be at balance when the triangle is hinged at the centroid. 
  
* To see this better, for illustration, let us consider a different triangle with the same area and same height as triangle ACF, 
  
* I have modified the base accordingly for construction but the area is the same. 
  
* With this setup we could intuitively say that it will be in balance when we hinge it at the centroid, 
  
* which is also true as if we distribute uniform mass over the triangle, the centroid would be its center of gravity, 
  
* and hence KN become one third of HK.

Now we can write the fulcrum lever balance for this setup and substitute this KN and HK relation to arrive at the area of the parabola relating to the area of the triangle, which can be easily calculated. 

And there is also a relation between the larger triangle and the inscribed triangle and the area of the parabola can be expressed as fourth thirds of it which we also confirmed from one of the earlier methods.

Eureka!

## The Method conclude

Let us dial back, 
* so he starts by choosing any section of the parabola, 
* builds a property on it, 
* changes the lens to see the same from a different perspective, 
* integrates it over the parabola and he has managed to express the area of a curved shape such as a parabola in terms of a straight shape whose area is known. 

That sounds incredible, to me atleast, and another venue to emphasize that changing the perspectives can help us solved the unsolved.


`end`

* Also to emphasize why just finding the areas which are simple to us were great at that time is because that, 
  
* we now know integration to calculate areas of curved bodies and algebra to write equations of curved bodies and graph to visualize those equations, 
  
* but in those days none of the above were there. 
  
* Even the parabola is defined as the shape you get when you cut the cone is specific angles and not as y=ax^2. 
  
* The notion between geometry and algebra become more clearer with the works of Descartes and Fermat, which gave the analytical geometry we study at elementary level in schools
  
* Maybe if they were born at Syracuse, the brachistochrone problem might've been proposed at ancient Greece itself.

## Conclude

`end quote`

I would like to end here with a quote giving the same emphasis on perspectives. If you have watched this far, thank you for your time and thanks for watching.