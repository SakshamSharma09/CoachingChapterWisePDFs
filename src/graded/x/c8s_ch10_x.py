"""Class 8 Science Ch 10 Light: Mirrors and Lenses - extras."""
from common import AR4, Q

AR = [
 AR4("The image formed by a plane mirror cannot be obtained on a screen.", "The image in a plane mirror is virtual.", "a", "A virtual image is formed by rays that only appear to meet, so it cannot be caught on a screen."),
 AR4("Convex mirrors are used as rear-view mirrors in vehicles.", "A convex mirror gives a wider field of view.", "a", "The wide view lets the driver see more traffic behind."),
 AR4("A convex lens can be used to start a fire with sunlight.", "A convex lens spreads out parallel rays of light.", "c", "A is true; R is false, a convex lens converges parallel rays to a point."),
 AR4("Diffuse reflection takes place from a rough surface.", "A concave mirror is used by dentists to see enlarged images of teeth.", "b", "Both are true, but the two statements are unrelated."),
 AR4("The angle of reflection is always greater than the angle of incidence.", "Angles of incidence and reflection are measured from the normal.", "d", "A is false since the two angles are equal; R is true."),
 AR4("We can see a book in a room even though it does not emit light.", "A book reflects the light falling on it into our eyes.", "a", "A non-luminous object is seen through the light it reflects."),
]

CASE = [
 Q("<b>Case study.</b> Anita stands 3 m in front of a large plane mirror in a dance studio in Mumbai. She raises her right hand and sees that her image appears to raise its left hand. She then walks 1 m towards the mirror. "
   "(i) What is the distance between Anita and her image at first? (ii) Which hand does the image seem to raise? (iii) State the type of image formed by a plane mirror. (iv) After walking 1 m, what is the distance between Anita and her image? Give a reason.",
   "(i) 3 + 3 = 6 m (1). (ii) Left hand (lateral inversion) (1). (iii) Virtual, erect and of the same size as the object (1). (iv) She is now 2 m from the mirror, and the image is 2 m behind it, so the distance is 4 m (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Ravi notices that the side mirror of his father's car in Delhi shows a small but wide view of the road behind. His dentist uses a small curved mirror that makes teeth look larger. A torch has a curved reflector behind the bulb to send out a strong parallel beam. "
   "(i) Which type of mirror is used as a car side mirror? (ii) Which type of mirror does the dentist use? (iii) Name the mirror used as the reflector in a torch. (iv) Why is a convex mirror preferred as a rear-view mirror?",
   "(i) Convex mirror (1). (ii) Concave mirror (1). (iii) Concave mirror (1). (iv) It always forms an erect, smaller image and gives a wider field of view, so the driver can see more of the road behind (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Sneha holds a convex lens above a dry leaf in sunlight and moves it until a bright, tiny spot forms on the leaf; after a while the leaf starts to smoulder. Her classmate Imran cannot see the blackboard clearly from the back bench and is advised to wear spectacles with a concave lens. "
   "(i) What is the bright spot called? (ii) Which lens converges light rays? (iii) Which lens is used by Imran if he has short-sightedness (myopia)? (iv) Why does the leaf start to burn?",
   "(i) The focus (focal point) of the lens (1). (ii) Convex lens (1). (iii) Concave lens (1). (iv) The lens concentrates the parallel sunlight rays at a small spot, so a large amount of energy falls on a tiny area and raises its temperature (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Laws of reflection", ["First law: the incident ray, reflected ray and normal lie in the same plane.", "Second law: $\angle i = \angle r$ (both measured from the normal).",
   "A ray along the normal has $\angle i = 0^\circ$ and is reflected back along itself."]),
 ("Plane mirror", ["Image is virtual, erect, same size, laterally inverted.", "Image distance = object distance (image is as far behind the mirror as the object is in front).",
   "Distance between object and image $= 2 \times$ distance of object from mirror."]),
 ("Types of reflection", ["Regular reflection: smooth surface, parallel rays stay parallel.", "Diffuse reflection: rough surface, reflected rays go in different directions.",
   "Real image: can be obtained on a screen. Virtual image: cannot."]),
 ("Spherical mirrors and lenses", ["Concave mirror: converging; used as shaving mirror, torch reflector, by dentists.", "Convex mirror: diverging, wide field of view, erect smaller image; used as rear-view mirror.",
   "Convex lens: thicker at centre, converges rays (magnifying glass, camera). Concave lens: thinner at centre, diverges rays (corrects myopia)."]),
]

MISTAKES = [
 "Measuring angles of incidence and reflection from the mirror surface instead of from the <b>normal</b>.",
 "Saying the image in a plane mirror is real; it is virtual (it cannot be taken on a screen).",
 "Writing that the object-image distance equals the object distance; it is <i>twice</i> the object distance.",
 "Confusing lateral inversion with an upside-down image; left and right are interchanged, not top and bottom.",
 "Mixing up the uses: concave mirror for shaving and torches, convex mirror for rear-view.",
 "Saying a convex lens diverges rays; it converges them, and a concave lens diverges them.",
]
