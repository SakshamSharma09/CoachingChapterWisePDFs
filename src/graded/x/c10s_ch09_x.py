"""Class 10 Science Ch 9 Light - Reflection and Refraction - extras."""
from common import AR4, Q

AR = [
 AR4(r"A convex mirror is used as a rear-view mirror in vehicles.", r"A convex mirror always forms an erect, diminished image and gives a wider field of view.", "a",
     r"The wide field of view of the diminished, erect image lets the driver see more traffic behind."),
 AR4(r"A ray of light passing through the centre of curvature of a concave mirror retraces its path after reflection.", r"The radius of curvature of a spherical mirror is twice its focal length.", "b",
     r"Both true; the ray falls normally on the mirror and retraces its path, which is not explained by $R=2f$."),
 AR4(r"A ray of light going from air into glass bends towards the normal.", r"The speed of light is greater in glass than in air.", "c",
     r"Glass is optically denser: light slows down and bends towards the normal; R is false."),
 AR4(r"A convex lens always forms a real image.", r"A convex lens forms a virtual, erect and magnified image when the object is placed between the optical centre and the focus.", "d",
     r"A is false: a convex lens forms a virtual image for an object between O and F; R is true."),
 AR4(r"The power of a concave lens is negative.", r"The focal length of a concave lens is taken as negative.", "a",
     r"$P=1/f$, so negative $f$ gives negative power."),
 AR4(r"A convex lens of focal length 0.5 m has a power of +2 D.", r"The SI unit of power of a lens is the dioptre.", "b",
     r"$P=1/0.5=+2$ D; R is a true fact about units and does not explain the value."),
]

CASE = [
 Q(r"<b>Case study.</b> A student places a 3 cm tall object on the principal axis of a concave mirror of radius of curvature 40 cm, at a distance of 30 cm from the pole. "
   r"(i) Find the focal length of the mirror. (ii) Find the position of the image. (iii) Find the magnification. (iv) Find the height of the image and state its nature.",
   r"(i) $f=R/2=-20$ cm (1). (ii) $u=-30$, $f=-20$: $\dfrac1v=\dfrac1f-\dfrac1u=-\dfrac1{20}+\dfrac1{30}=-\dfrac1{60}$, so $v=-60$ cm, i.e. 60 cm in front of the mirror (1). (iii) $m=-\dfrac vu=-\dfrac{-60}{-30}=-2$ (1). (iv) Image height $=2\times3=6$ cm (1); real, inverted and enlarged (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Anita uses a convex lens of power +2.5 D to get a sharp image of a candle flame on a screen. She places the candle at 80 cm from the lens. "
   r"(i) Find the focal length of the lens. (ii) Find the image distance. (iii) Find the magnification. (iv) State the nature of the image and where she should place the candle to get a magnified real image.",
   r"(i) $f=\dfrac1P=\dfrac1{2.5}=0.4$ m $=40$ cm (1). (ii) $\dfrac1v=\dfrac1f+\dfrac1u=\dfrac1{40}-\dfrac1{80}=\dfrac1{80}$, so $v=+80$ cm (1). (iii) $m=\dfrac vu=\dfrac{80}{-80}=-1$ (1). (iv) Real, inverted and of the same size (1); for a magnified real image she should place it between $F$ and $2F$, i.e. between 40 cm and 80 cm (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A ray of light travelling in air strikes a glass slab. The refractive index of the glass is 1.5 and the speed of light in air is $3\times10^{8}$ m/s. The sine of the angle of incidence is found to be 0.75. "
   r"(i) Find the speed of light in glass. (ii) Does the ray bend towards or away from the normal in glass? (iii) State Snell's law. (iv) Find the sine of the angle of refraction and the angle of refraction.",
   r"(i) $v=c/n=3\times10^{8}/1.5=2\times10^{8}$ m/s (1). (ii) Towards the normal (glass is denser) (1). (iii) $\dfrac{\sin i}{\sin r}$ = constant for a given pair of media (1). (iv) $\sin r=\dfrac{\sin i}{n}=\dfrac{0.75}{1.5}=0.5$ (1), so $r=30^\circ$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Reflection", [r"Laws: angle of incidence = angle of reflection; incident ray, reflected ray and normal lie in the same plane.",
   r"Plane mirror: image virtual, erect, same size, laterally inverted, as far behind as the object is in front.",
   r"Spherical mirrors: $f=\dfrac R2$; principal focus F; concave converges, convex diverges.",
   r"Mirror formula: $\dfrac1v+\dfrac1u=\dfrac1f$. Magnification: $m=\dfrac{h'}{h}=-\dfrac vu$."]),
 ("Sign convention (Cartesian)", [r"Pole is origin; principal axis is x-axis; object on the left. Distances measured against the incident light are negative.",
   r"Concave mirror: $f<0$; convex mirror: $f>0$. Heights upwards positive, downwards negative ($m<0$ real, inverted; $m>0$ virtual, erect)."]),
 ("Images by concave mirror", [r"Object at infinity: image at F, real, point. Beyond C: between F and C, real, inverted, diminished. At C: at C, real, inverted, same size.",
   r"Between C and F: beyond C, real, inverted, enlarged. At F: at infinity, enlarged. Between P and F: behind mirror, virtual, erect, enlarged."]),
 ("Refraction", [r"Laws: incident ray, refracted ray, normal in one plane; Snell's law $\dfrac{\sin i}{\sin r}=n$ (constant).",
   r"Refractive index $n=\dfrac cv$ (c = $3\times10^{8}$ m/s). Rarer to denser: bends towards normal; denser to rarer: away from normal.",
   r"Rectangular glass slab: emergent ray parallel to incident ray (lateral shift)."]),
 ("Lenses", [r"Lens formula: $\dfrac1v-\dfrac1u=\dfrac1f$; magnification $m=\dfrac vu=\dfrac{h'}h$.",
   r"Power: $P=\dfrac1f$ ($f$ in metres); unit dioptre (D); convex +, concave $-$. For lenses in contact, $P=P_1+P_2$.",
   r"Convex lens: $f>0$; real inverted image when $u>f$; virtual erect enlarged when object between O and F. Concave lens: always virtual, erect, diminished."]),
]

MISTAKES = [
 r"Ignoring the sign convention: for a concave mirror or lens use $u<0$ and, for a concave mirror, $f<0$ (convex lens $f>0$, concave lens $f<0$).",
 r"Using the lens formula $\frac1v-\frac1u=\frac1f$ for mirrors, or the mirror formula $\frac1v+\frac1u=\frac1f$ for lenses.",
 r"Using $f$ in centimetres while calculating power; $P=1/f$ gives dioptres only when $f$ is in <b>metres</b>.",
 r"Saying that light bends away from the normal when entering glass; it bends towards the normal in a denser medium.",
 r"Describing the image formed by a concave mirror when the object is between P and F as real; it is virtual, erect and enlarged.",
 r"Writing the refractive index as $\sin r/\sin i$; Snell's law gives $n=\sin i/\sin r$ for light going from air into the medium.",
]
