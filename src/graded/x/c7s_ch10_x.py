"""Class 7 Science Ch 10 Light: Shadows and Reflections - extras."""
from common import AR4, Q

AR = [
 AR4("A shadow is formed when an opaque object comes in the path of light.", "Light travels in straight lines.", "a",
     "Because light cannot bend around the opaque object, a dark region (shadow) forms behind it."),
 AR4("The Moon is a non-luminous object.", "The Sun is a luminous object.", "b",
     "Both are true; the Moon only reflects sunlight, but the luminous nature of the Sun does not explain it."),
 AR4("A plane mirror forms a virtual image.", "The image formed by a plane mirror can be obtained on a screen.", "c",
     "A is true; a virtual image cannot be obtained on a screen, so R is false."),
 AR4("The image formed by a plane mirror is smaller than the object.", "The image in a plane mirror is of the same size as the object.", "d",
     "The image is of the same size, so A is false; R is true."),
 AR4("A pinhole camera forms an inverted image of an object.", "Light travels in straight lines and the rays cross at the pinhole.", "a",
     "Crossing of the straight rays at the hole inverts the image."),
 AR4("In reflection from a plane mirror, the angle of incidence equals the angle of reflection.", "The incident ray, the reflected ray and the normal lie in the same plane.", "b",
     "Both are laws of reflection but one does not explain the other."),
]

CASE = [
 Q("<b>Case study.</b> Arun makes hand shadows of a bird on the wall of his room using a torch. When he moves his hand closer to the torch, the shadow becomes bigger. He also tries a sheet of clear glass and a sheet of butter paper in front of the torch. "
   "(i) Write the three things needed to form a shadow. (ii) What happens to the size of the shadow when the object is moved nearer to the torch? (iii) What type of material is butter paper? (iv) Will the clear glass sheet form a dark shadow? Give a reason.",
   "(i) A source of light, an opaque object and a screen (1). (ii) It becomes larger (1). (iii) Translucent (1). (iv) No (1), because clear glass is transparent and allows almost all the light to pass through (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Divya stands 2 m in front of a large plane mirror. Behind an ambulance parked nearby, she reads the word written on its front as a mirror-reversed word and then understands why it is written that way. "
   "(i) At what distance from the mirror is her image formed? (ii) What is the distance between Divya and her image? (iii) State two features of the image in a plane mirror. (iv) Why is the word AMBULANCE written laterally inverted on the vehicle?",
   "(i) 2 m behind the mirror (1). (ii) $2+2=4$ m (1). (iii) It is virtual and erect, and of the same size as the object (1). (iv) Drivers see the front of the ambulance in their rear-view mirrors (1); lateral inversion makes the word look correct in the mirror so they can read it and give way (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Sameer makes a pinhole camera using a cardboard tube, with a tiny hole at one end and a tracing paper screen at the other end. He points the hole at a burning candle and sees an image on the screen. "
   "(i) Is the image on the screen erect or inverted? (ii) Is the image real or virtual? (iii) What will happen if the hole is made larger? (iv) Why is the image inverted?",
   "(i) Inverted (1). (ii) Real, as it is formed on a screen (1). (iii) The image becomes brighter but blurred (1). (iv) Light travels in straight lines (1), so rays from the top of the flame go to the bottom of the screen and rays from the bottom go to the top after crossing at the hole (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Light and shadows", [
   "Light travels in straight lines. Luminous objects give out their own light (Sun, stars, bulb); non-luminous ones reflect it (Moon, book).",
   "Transparent: light passes fully (clear glass). Translucent: partly (butter paper). Opaque: not at all (wood, metal).",
   "Shadow: needs a source of light, an opaque object and a screen. Shadow of a closer object is larger and darker.",
   "Umbra: the darkest part of a shadow; penumbra: the partly dark region around it."]),
 ("Reflection of light", [
   "Laws: angle of incidence = angle of reflection; incident ray, reflected ray and normal are in the same plane.",
   "Regular reflection: from smooth surfaces (mirrors); diffuse (irregular) reflection: from rough surfaces."]),
 ("Image in a plane mirror", [
   "Image is virtual (cannot be got on a screen), erect and of the same size as the object.",
   "Image distance behind the mirror = object distance in front of it.",
   "Lateral inversion: left appears right and right appears left (AMBULANCE)."]),
 ("Pinhole camera and applications", [
   "Pinhole camera forms an inverted real image; a larger hole gives a brighter but blurred image.",
   "Periscope uses two plane mirrors; kaleidoscope uses mirrors to form patterns by multiple reflection."]),
]

MISTAKES = [
 "Saying that the Moon is luminous; it only <b>reflects</b> sunlight.",
 "Writing that the image in a plane mirror is real; it is <b>virtual</b> and cannot be caught on a screen.",
 "Forgetting that the distance between a person and the image is <b>twice</b> the distance from the mirror.",
 "Saying that a transparent object forms a dark shadow; only <b>opaque</b> objects form dark shadows.",
 "Measuring the angles from the mirror surface instead of from the <b>normal</b>.",
 "Writing that a pinhole camera forms an erect image or that a large hole gives a sharper picture.",
]
