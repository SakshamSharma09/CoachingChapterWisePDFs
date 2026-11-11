"""Class 10 Science Ch 10 The Human Eye and the Colourful World - extras."""
from common import AR4, Q

AR = [
 AR4(r"Myopia is corrected by using a concave lens.", r"A concave lens diverges the rays so that the image is formed farther back, on the retina.", "a",
     r"In myopia the image forms in front of the retina; the diverging lens shifts it back onto the retina."),
 AR4(r"A rainbow is seen when the Sun is behind the observer and rain is falling in front.", r"A rainbow is formed by dispersion, internal reflection and refraction of sunlight in water droplets.", "b",
     r"Both true; R describes how the rainbow forms but does not explain the required geometry of Sun, observer and rain."),
 AR4(r"Hypermetropia can be corrected using a convex lens.", r"In hypermetropia the eyeball is too long.", "c",
     r"A hypermetropic eye has a short eyeball (or too long a focal length); the eyeball is too long in myopia. So R is false."),
 AR4(r"The colour of the clear sky at noon is red.", r"Light of shorter wavelength is scattered more strongly than light of longer wavelength.", "d",
     r"The sky is blue because blue light is scattered more; so A is false and R is true."),
 AR4(r"A person with myopia cannot see distant objects clearly.", r"In myopia the image of a distant object is formed in front of the retina.", "a",
     r"The image falls short of the retina, so the distant object looks blurred."),
 AR4(r"Danger signal lights are red in colour.", r"Red light is scattered the most by fog and smoke.", "c",
     r"Red has the longest wavelength and is scattered the least, so it is visible from far; R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> Ravi, a Class 10 student, is not able to read the writing on the blackboard from the last bench, though he reads his book comfortably. An eye specialist finds that the farthest point at which he can see clearly is 80 cm from his eye. "
   r"(i) Name the defect of vision from which Ravi suffers. (ii) What type of lens will correct this defect? (iii) Give one cause of this defect. (iv) Calculate the power of the lens required to correct it.",
   r"(i) Myopia (short-sightedness) (1). (ii) Concave (diverging) lens (1). (iii) Excessive curvature of the eye lens, or elongation of the eyeball (1). (iv) The lens must form the image of a distant object at the far point: $f=-80$ cm $=-0.8$ m (1); $P=\dfrac1f=\dfrac1{-0.8}=-1.25$ D (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a science class, Kavya allowed a narrow beam of sunlight to fall on a glass prism and obtained a coloured band on a white screen. Her teacher then explained that the same process occurs in the sky after a shower, giving a rainbow. "
   r"(i) Name the phenomenon by which white light splits into colours. (ii) Which colour deviates the least and which the most? (iii) What is the band of colours called? (iv) Explain how a rainbow is formed in the sky.",
   r"(i) Dispersion (1). (ii) Red the least, violet the most (1). (iii) Spectrum (VIBGYOR) (1). (iv) Tiny water droplets act as small prisms: sunlight is refracted and dispersed, internally reflected inside the drop and refracted again as it comes out (1); different colours reach the eye of the observer from different droplets to form the rainbow (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> At Jaisalmer, Arjun watched the Sun set over the desert and found that the Sun looked red near the horizon but white at noon. The sky overhead looked blue. From the same place, astronauts in space see the sky as dark. "
   r"(i) Name the phenomenon responsible for the blue colour of the sky. (ii) Why do we see the sky blue and not red? (iii) Why is red light used for danger signals? (iv) Explain why the Sun appears red at sunrise and sunset and why the sky appears dark to astronauts.",
   r"(i) Scattering of light (1). (ii) Blue light has a shorter wavelength than red and is scattered much more strongly by atmospheric particles (1). (iii) Red light is scattered the least by fog or smoke, so it can be seen from far (1). (iv) Near the horizon sunlight travels a longer path through the atmosphere, so most blue light is scattered away and red reaches the eye (1); there is no atmosphere in space to scatter sunlight, so the sky looks dark (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Structure and working of the eye", [r"Cornea (most refraction), aqueous humour, iris (controls pupil size), pupil, lens (adjusts focal length), ciliary muscles, retina (image screen), optic nerve.",
   r"Image on the retina is real and inverted; the brain perceives it erect. Accommodation: ciliary muscles change the lens curvature (thick for near, thin for distant vision).",
   r"Normal eye: near point (least distance of distinct vision) $=25$ cm; far point $=$ infinity. Persistence of vision $\approx\dfrac1{16}$ s."]),
 ("Defects and correction", [r"Myopia: far point nearer than infinity; image in front of retina; corrected by concave lens, $f=-$ (far point).",
   r"Hypermetropia: near point farther than 25 cm; image behind the retina; corrected by convex lens.",
   r"Presbyopia: weakening of ciliary muscles with age; bifocal lenses. Cataract: clouding of the lens, restored by surgery.",
   r"Power of a lens $P=\dfrac1f$ ($f$ in metres), unit dioptre (D); concave $-$, convex $+$."]),
 ("Dispersion and atmospheric refraction", [r"Prism: white light splits into VIBGYOR; violet deviates most, red least (red has the highest speed in glass). Newton: a second prism recombines the colours.",
   r"Rainbow: dispersion + internal reflection + refraction in water droplets; Sun behind the observer.",
   r"Atmospheric refraction: twinkling of stars (varying density of air, point source), advance sunrise and delayed sunset by about 2 minutes. Planets do not twinkle (extended source)."]),
 ("Scattering", [r"Tyndall effect: scattering of light by colloidal particles (visible path of a beam in dusty room, forest canopy).",
   r"Blue sky: shorter wavelengths scattered more; red Sun at sunrise and sunset: longer path in the atmosphere; sky dark for astronauts (no atmosphere). Red light: least scattered, used for danger signals."]),
]

MISTAKES = [
 r"Saying that a myopic eye is corrected with a convex lens, or hypermetropia with a concave lens; myopia needs concave and hypermetropia needs convex.",
 r"Believing that most refraction in the eye occurs at the eye lens; it occurs at the outer surface of the cornea, and the lens only fine-tunes the focal length.",
 r"Writing that the image on the retina is erect; it is real and inverted and the brain interprets it as erect.",
 r"Stating that red light is scattered the most; it is scattered the least, and blue light is scattered the most.",
 r"Forgetting the negative sign for a myopia lens, or using $f$ in centimetres to find power; $P=1/f$ with $f$ in metres.",
 r"Saying that planets twinkle like stars; stars twinkle due to atmospheric refraction of a point source, whereas planets appear as extended sources.",
]
