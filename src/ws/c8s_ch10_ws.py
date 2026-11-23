"""Class 8 Science Ch 10 - Light: Mirrors and Lenses: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8s_ch10"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_sci" / f"ch{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks
assert 90 - 40 == 50 and 90 - 30 == 60 and 2 * 30 == 60 and 90 - 70 == 20 and 2 * 20 == 40
assert 3 + 3 == 6 and 2 + 2 == 4 and 90 - 60 == 30

WS = [
# ---------------- EASY ----------------
 W("A concave mirror is a spherical mirror whose reflecting surface is:", 1, "(a) curved inwards, like the inside of a bowl (1).", "E",
   opts=["curved inwards", "curved outwards", "flat", "rough"]),
 W("The side-view mirror of a scooter is a:", 1, "(c) convex mirror, which gives a wide field of view (1).", "E",
   opts=["plane mirror", "concave mirror", "convex mirror", "concave lens"]),
 W("The image formed by a convex mirror is always:", 1, "(b) erect and diminished (1).", "E",
   opts=["inverted and enlarged", "erect and diminished", "inverted and diminished", "erect and enlarged"]),
 W("Which of these is thicker in the middle than at the edges?", 1, "(d) a convex lens (1).", "E",
   opts=["a concave lens", "a concave mirror", "a flat glass plate", "a convex lens"]),
 W("A beam of parallel rays falling on a concave mirror, after reflection:", 1, "(a) converges (comes together) (1).", "E",
   opts=["converges", "diverges", "remains parallel", "stops"]),
 W("The angle of incidence is the angle between:", 1, "(b) the incident ray and the normal (1).", "E",
   opts=["incident ray and the mirror surface", "incident ray and the normal", "incident ray and reflected ray", "reflected ray and the mirror surface"]),
 W("Which of the following is used by a dentist to see an enlarged image of teeth?", 1, "(c) concave mirror (1).", "E",
   opts=["plane mirror", "convex mirror", "concave mirror", "convex lens"]),
 W("A ray of light falls on a plane mirror at an angle of incidence of 30°. Write the angle of reflection and the angle between the incident and the reflected rays.", 2,
   "Angle of reflection = angle of incidence = 30° (1). Angle between the two rays = 30° + 30° = 60° (1).", "E"),
 W("Define the normal at the point of incidence.", 1, "The line drawn at 90° to the mirror surface at the point where the incident ray strikes it (1).", "E"),
 W("Rohan looks at his face on the inner (curved-in) side of a shiny steel spoon and on the outer (bulging) side. Name the type of mirror each side acts as and say what he sees in each.", 2,
   "Inner side = concave mirror: image is inverted (when held away) (1). Outer side = convex mirror: image is erect and smaller (1).", "E", wp=True),
 W("Why is a concave reflector used behind the bulb in a torch?", 2,
   "A concave mirror makes the light of the bulb into a strong beam (1) in the forward direction, so the torch lights up a distant spot (1).", "E", wp=True),
 W("A jeweller in Jaipur fixes a convex mirror in the corner of his shop. Why?", 2,
   "A convex mirror has a much wider field of view (1), so he can watch a large part of the shop and avoid theft (1).", "E", wp=True),
 W("True or false? Give a reason. 'The laws of reflection are followed only by plane mirrors.'", 2,
   "False (1). They hold for all mirrors - plane, concave and convex; a ray falls and reflects obeying i = r at every point (1).", "E"),
 W("Name any two devices that use a convex lens.", 2, "Any two of: magnifying glass, spectacles, camera, microscope, telescope (1 + 1).", "E"),
 W("Name two kinds of mirrors that always form an erect image.", 2, "Plane mirror (1) and convex mirror (1).", "E"),
 W("A ray of light falls on a mirror along the normal. What are the angle of incidence and the angle of reflection?", 1, "Both are 0° (the ray returns along itself) (1).", "E", wp=True),
 W("Why must we never look directly at the Sun, or its reflection from a mirror or lens?", 2,
   "Sunlight concentrated by a mirror or lens is very strong (1) and can seriously damage the eyes; we focus only on the paper (1).", "E", wp=True),

# ---------------- MEDIUM ----------------
 W("A ray makes an angle of 30° with a plane mirror (with the mirror surface). Meena says the angle of reflection is 30°. Find her mistake and give the correct angles.", 2,
   "She measured from the mirror, but angles of incidence and reflection are measured from the normal (1). Angle of incidence = 90° − 30° = 60°, so the angle of reflection is also 60° (1).", "M"),
 W("A ray strikes a plane mirror at 40° to the normal. What angle does the reflected ray make with the mirror surface? What is the angle between the incident and reflected rays?", 2,
   "Reflected ray: r = 40°; with the surface = 90° − 40° = 50° (1). Angle between rays = 40° + 40° = 80° (1).", "M", wp=True),
 W("Three unknown mirrors are tested with a small toy. Mirror X: image always erect and of the same size. Mirror Y: image always erect and smaller. Mirror Z: image erect and enlarged when the toy is close, inverted when it is far. Identify X, Y and Z.", 3,
   "X = plane mirror (1); Y = convex mirror (1); Z = concave mirror (1).", "M"),
 W("At a sharp bend on a hill road near Mount Abu, a convex mirror is fixed. Give two reasons for using a convex mirror here.", 3,
   "It gives a wide field of view, so the driver can see traffic coming round the bend (1.5). The image is erect, so vehicles and people are recognised, which avoids collisions (1.5).", "M", wp=True),
 W("A side-view mirror carries the words 'Objects in mirror are closer than they appear'. Explain why.", 3,
   "The mirror is convex (1). A convex mirror forms images that are smaller than the objects (1), so vehicles look farther away than they really are (1).", "M", wp=True),
 W("In a school activity, Sunita focuses sunlight on a paper with a concave mirror and the paper starts smoking. Why? Name two precautions.", 3,
   "A concave mirror converges the parallel rays of the Sun to a bright spot (1) and the heat is concentrated there (1). Precautions: do the activity with a teacher present; never look at the Sun or its reflection - look only at the paper (1).", "M", wp=True),
 W("Why do solar cookers use shiny curved surfaces? Name the type of surface and say what it does to sunlight.", 2,
   "They use concave (converging) reflectors (1) that bring the sunlight together, concentrating heat to cook food (1).", "M", wp=True),
 W("Distinguish a convex lens from a concave lens in three points.", 3,
   "Convex lens: thicker at the middle; converges parallel light; image erect and enlarged when near, inverted when far (1.5). Concave lens: thicker at the edges; diverges parallel light; image always erect and diminished (1.5).", "M"),
 W("Complete the table for a parallel beam of light: plane mirror ___, concave mirror ___, convex mirror ___, convex lens ___, concave lens ___.", 3,
   "Plane mirror: remains parallel; concave mirror: converges; convex mirror: diverges; convex lens: converges; concave lens: diverges (5 correct = 3; 3-4 correct = 2) (3).", "M"),
 W("Describe how a water drop on a flat transparent strip can work as a lens. What do the letters look like through it?", 2,
   "A small water drop has a curved (bulging) surface and acts like a convex lens (1); the letters under it look larger (enlarged) (1).", "M"),
 W("Anjali places a pencil behind a transparent tumbler. When she fills the tumbler halfway with water, the part of the pencil seen through the water looks different. What does the water-filled tumbler act like, and what change does she see?", 2,
   "The curved, water-filled tumbler behaves like a lens (1), so the pencil seen through the water appears changed in shape and size (for example, enlarged or shifted) compared with the dry glass (1).", "M", wp=True),
 W("A dentist uses a small curved mirror to look at a back tooth. Name the mirror and state the nature of the image she gets and why she keeps it close to the tooth.", 2,
   "Concave mirror (1). When the object is close, the image is erect and enlarged, giving a magnified view of the tooth (1).", "M", wp=True),
 W("The word AMBULANCE is written laterally inverted on the front of the vehicle. Why? Which mirror type shows lateral inversion?", 2,
   "A driver ahead sees it correctly in the rear-view mirror because the mirror swaps left and right (1). Lateral inversion occurs in all three types of mirrors - plane, concave and convex (1).", "M", wp=True),
 W("Why is a concave reflector used in the headlight of a car and not a convex one?", 2,
   "A concave mirror converges the light of the bulb into a strong forward beam (1); a convex mirror would spread it out and the road ahead would be poorly lit (1).", "M", wp=True),
 W("Ravi stands 3 m in front of a large plane mirror in his dance class. (i) How far is his image from him? (ii) He moves 1 m towards the mirror. What is the new distance between him and his image?", 3,
   "(i) The image is 3 m behind the mirror, so the distance is 3 + 3 = 6 m (1.5). (ii) Distance from mirror = 2 m, so the distance between him and the image = 2 + 2 = 4 m (1.5).", "M", wp=True),
 W("In Activity 10.5 the reflected beam from a mirror on chart paper disappears when the extended part of the paper is bent. What does this show?", 2,
   "The incident ray, the normal and the reflected ray lie in the same plane (1); bending the paper takes the reflected ray out of that plane so it can no longer be seen on the paper (1).", "M"),
 W("Over 800 years ago, in the time of Bhaskara II, Indian astronomers used shallow bowls of water and tubes to view stars and planets. Which property of light did this use, and what did the water surface act as?", 2,
   "They used reflection of light (1); the still water surface acted like a mirror that gave a reflected image of the stars and planets (1).", "M"),
 W("The human eye has a convex lens that changes its shape. Why is this useful?", 2,
   "By changing its shape the lens can focus on both near and far objects (1), so we can see things clearly at different distances (1).", "M"),
 W("Match each device to the mirror/lens used: (i) shaving/dentist's mirror (ii) vehicle side-view mirror (iii) magnifying glass (iv) spectacle lens for some eye defects (concave).", 3,
   "(i) concave mirror (ii) convex mirror (iii) convex lens (iv) concave lens (all four = 3; any three = 2) (3).", "M"),
 W("Priya holds a magnifying glass over a line of print. What does she see when it is close to the print and what happens to the image as she moves it away from the print?", 3,
   "The magnifying glass is a convex lens (1). Close to the print, the letters look erect and enlarged (1). As she moves it away, the image becomes inverted, first enlarged and then diminished (1).", "M", wp=True),

# ---------------- HARD ----------------
 W("<b>Case study.</b> A school bus in Kota has a convex mirror above the driver's seat, and the school shop has a similar mirror in the corner. In the science lab, Aman sends a thin beam of light from a torch through a comb slit on to a mirror lying upright on white paper and measures i and r from the normal, getting i = 20°, r = 20° and, for another position, i = 45°, r = 45°. (i) Why is a convex mirror used in the bus and shop? (ii) What do Aman's readings show? (iii) What angle does the beam make with the mirror surface when i = 45°? (iv) If the beam is sent along the normal, what are i and r?", 5,
   "(i) Convex mirror gives an erect, diminished image and a wide field of view, so a large area can be watched (1). (ii) The angle of incidence equals the angle of reflection (1). (iii) 90° − 45° = 45° (1). (iv) Both are 0° (the ray returns along the same path) (2: 1 each).", "H", wp=True),
 W("Parallel beams reflected from a concave mirror converge, even though every ray obeys the laws of reflection (i = r). A student is confused. Explain how this is possible.", 3,
   "The surface of a spherical mirror is curved, so the normal at each point of the mirror points in a different direction (1.5). Every ray obeys i = r with respect to its own normal, but the rays fall on different points with different normals, so the reflected rays come together (converge) on a concave mirror and spread out on a convex one (1.5).", "H"),
 W("Why is a plane mirror not preferred as a vehicle's side-view mirror? Give three reasons using the properties of images.", 3,
   "A plane mirror shows an image of the same size, so it covers only a small field of view (1). A convex mirror shows a wider area behind (1) with an erect image, giving more information about following vehicles at once (1).", "H", wp=True),
 W("Design a simple test to find out which of three unknown mirrors (plane, concave, convex) is which. Describe what you would do and what you would see.", 4,
   "Hold a small toy/object near each mirror, then move it slowly away and look at the image (1). The mirror that always gives an image of the same size as the object is plane (1). The mirror that always gives an erect, smaller image is convex (1). The one that gives an erect, enlarged image when the object is close and an inverted one when it is far is concave (1).", "H"),
 W("A ray of light makes an angle of 70° with a plane mirror. Find (i) the angle of incidence (ii) the angle of reflection (iii) the angle between the incident and reflected rays (iv) the angle between the reflected ray and the mirror.", 3,
   "(i) 90° − 70° = 20° (1). (ii) 20° (0.5). (iii) 20° + 20° = 40° (1). (iv) 70° (0.5).", "H", wp=True),
 W("Assertion (A): A convex mirror is used in shops to watch customers. Reason (R): A convex mirror forms an erect image and gives a wide field of view. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). Because a convex mirror gives a wide field of view, a large area of the shop can be seen in one mirror (1), and the erect image lets people be recognised (1).", "H"),
 W("Assertion (A): A convex lens can burn a piece of paper in sunlight. Reason (R): A convex lens converges parallel rays to a bright spot. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). The lens brings the parallel sunlight to a small bright spot (1) where the heat is concentrated, so the paper can smoke and burn (1).", "H"),
 W("Compare a convex lens and a convex mirror: write two similarities and two differences.", 4,
   "Similarities: both have a curved bulging (convex) surface; both can form erect images; both change the direction of light rays (any two, 2). Differences: light passes through a lens but is reflected by a mirror; a convex lens converges parallel light whereas a convex mirror diverges it; a lens's image can be inverted but a convex mirror's is always erect and diminished (any two, 2).", "H"),
 W("A solar concentrator uses many mirrors to focus sunlight on a pipe. Explain (i) the type of mirror surface it needs, (ii) how the heat is used to generate electricity, and (iii) why such a device can even melt steel in a solar furnace.", 4,
   "(i) Concave (converging) mirrors (1). (ii) The concentrated heat produces steam, which runs a turbine/generator for electricity (1). (iii) Concentrating a large amount of sunlight on a very small spot gives a very high temperature (2).", "H", wp=True),
 W("On a narrow road with a hairpin bend, the panchayat plans to put up a mirror. Which type would you suggest and why? Mention one advantage and one limitation (think of how big vehicles look in it).", 4,
   "A convex mirror (1). Advantage: wide field of view, erect image, so oncoming vehicles round the bend are seen early (1.5). Limitation: the images are diminished, so vehicles look smaller and farther than they really are, and the driver must judge carefully (1.5).", "H", wp=True),
 W("Describe how the image of an object in a concave mirror changes as the object is moved slowly from very near the mirror to far away.", 3,
   "Very near: erect and enlarged (1). As the object moves away, the image changes to inverted (1), at first enlarged and then diminished, i.e. the image keeps getting smaller as the distance grows (1).", "H"),
 W("Priya notes the images given by an unknown device when the object is moved away: very near - erect and enlarged; farther - inverted and enlarged; far away - inverted and diminished. (i) Name two devices that could give this. (ii) How would you tell them apart without measuring any image?", 3,
   "(i) A concave mirror or a convex lens (1). (ii) With a lens, light passes through it and the image is seen through/behind the lens; with a mirror, light is reflected and the image is seen in the front, on the side the object is (2).", "H"),
 W("Can a convex mirror be used to start a fire with sunlight? Give a reason and name the device that can.", 3,
   "No (1). A convex mirror makes parallel rays diverge, so sunlight is not concentrated (1). A concave mirror or a convex lens converges the rays to a bright spot and can start a fire (1).", "H"),
]

_base = _old(10)
_i = max(i for i, b in enumerate(_base["blocks"]) if b[0] == "h2")
_extra = [
 ("h2", "Worked Examples and Reasoning Skills"),
 ("steps", [
   ("Example 1 — Angles of reflection", "A ray makes **30° with the mirror surface**. The angle of incidence is measured from the normal, so i = 90° − 30° = **60°**; by the law of reflection r = 60°. The angle between the incident and reflected rays = i + r = 120°, and the reflected ray makes 30° with the mirror on the other side."),
   ("Example 2 — Ray along the normal", "A ray falls along the normal (90° to the mirror). Then i = 0°, so r = 0°, and the ray returns along the same path. The angle between incident and reflected rays is 0°."),
   ("Example 3 — Identify the mirror from the image", "A toy placed close gives an **erect, enlarged** image; moved far it gives an **inverted** image — this is a **concave mirror**. If the image is **always erect and smaller**, it is **convex**. If it is **always erect and of the same size**, it is **plane**."),
   ("Example 4 — Distance in a plane mirror", "Ravi stands 3 m from a plane mirror. The image is 3 m behind it, so he and the image are 6 m apart. After moving 1 m closer he is 2 m from the mirror and 4 m from his image."),
   ("Example 5 — Choosing a device", "To see a **large area** at a road bend: convex mirror. To get a **strong beam** from a bulb: concave reflector. To read tiny print: convex lens. To see an **enlarged tooth**: concave mirror. To start a fire from sunlight: concave mirror or convex lens (**never look at the Sun**)."),
 ]),
 ("h2", "Comparison at a Glance"),
 ("table", ["Property", "Plane mirror", "Concave mirror", "Convex mirror"], [
   ["Shape of reflecting surface", "Flat", "Curved inwards", "Curved outwards"],
   ["Effect on parallel beam", "Remains parallel", "Converges", "Diverges"],
   ["Image size", "Same as object (always)", "Enlarged near, then smaller as object moves away", "Always smaller (diminished)"],
   ["Image orientation", "Erect (always)", "Erect when near; inverted when far", "Erect (always)"],
   ["Lateral inversion", "Yes", "Yes", "Yes"],
   ["Obeys laws of reflection?", "Yes", "Yes", "Yes"]]),
 ("note", "REMEMBER", "**Common mistakes:** (1) Measuring the angles of incidence and reflection from the mirror surface — they are measured from the **normal**. (2) Thinking that curved mirrors break the laws of reflection — every ray still follows i = r with respect to the normal **at that point**. (3) Confusing the two lenses: **convex = thicker in the middle = converging**; **concave = thicker at the edges = diverging**. (4) Saying a convex mirror can burn paper — it spreads the light out. (5) Forgetting that light passes **through** lenses but is **reflected** by mirrors. (6) Believing the warning on side mirrors means they are enlarging; they diminish the image."),
 ("h2", "Real-Life Connections"),
 ("ul", ["**Road safety:** convex mirrors at hairpin bends and junctions, and vehicle side-view mirrors, give a wide field of view; the warning on them reminds drivers that images look smaller and farther.",
         "**Health:** dentists use concave mirrors for enlarged views of teeth; spectacles use lenses (convex or concave) to help vision; the eye itself has a convex lens that changes shape to focus.",
         "**Energy and cooking:** concave mirrors and convex lenses concentrate sunlight in solar cookers, solar concentrators and solar furnaces.",
         "**Everyday devices:** torch and headlight reflectors (concave), cameras, microscopes, telescopes and magnifying glasses (convex lenses), shops' security mirrors (convex).",
         "**Heritage:** Indian astronomers used shallow bowls of water to see reflected images of stars and planets at the time of Bhaskara II."]),
]
_qa2 = [
  ("A ray falls at 60° to the normal on a plane mirror. Find the angle of reflection and the angle between the two rays.", "r = 60°; angle between rays = 60° + 60° = 120°."),
  ("Why do we say light is converged by a concave mirror even though each ray obeys i = r?", "The normal changes direction from point to point on a curved surface, so rays reflect towards a common point."),
  ("What is the difference between a lens and a mirror in how they handle light?", "Light passes through a lens but is reflected from a mirror."),
]
_blocks = list(_base["blocks"])
_blocks[_i + 1] = ("qa", list(_blocks[_i + 1][1]) + _qa2)
CH = dict(_base, blocks=_blocks[:_i] + _extra + _blocks[_i:],
          takeaways=_base["takeaways"] + ["Angles of incidence and reflection are measured from the **normal**, never from the mirror surface.",
                                          "Never look at the Sun or its reflection; concave mirrors and convex lenses can focus sunlight strongly enough to burn paper."])

if __name__ == "__main__":
    run(__file__, BANK, 8, "Science", WS, CH)
