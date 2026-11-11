"""Class 6 Science Ch 12 Beyond Earth - extras."""
from common import AR4, Q

AR = [
 AR4("The Sun is a star.", "The Sun produces its own light and heat.", "a",
     "A star makes its own light and heat, so R explains why the Sun is a star."),
 AR4("The Moon does not produce its own light.", "We see the Moon because it reflects sunlight.", "a",
     "The Moon only reflects the Sun's light."),
 AR4("Stars appear to twinkle at night.", "Their light passes through the moving layers of the air of the Earth.", "a",
     "The moving air bends the light unevenly, causing twinkling."),
 AR4("There are nine planets in our solar system.", "Mercury is the planet closest to the Sun.", "d",
     "A is false: there are eight planets. R is true."),
 AR4("Aryabhata was India's first artificial satellite.", "The Pole star always appears in the southern sky.", "c",
     "A is true (launched in 1975); R is false, the Pole star is seen in the northern sky."),
 AR4("The Moon shows different phases in a month.", "India has launched the Chandrayaan missions to study the Moon.", "b",
     "Both are true, but the Indian missions do not explain the phases."),
]

CASE = [
 Q("<b>Case study.</b> On a clear night in Shillong, Bhavya showed her younger brother the group of seven bright stars that makes a pattern like a big question mark, which people call the Saptarishi. She also pointed to a star that stays almost fixed in the northern sky and helps travellers find north. "
   "(i) What do we call a group of stars forming a pattern? (ii) What is the star that helps us to find north called? (iii) Name the pattern of stars that Bhavya showed. (iv) Why do stars appear to twinkle?",
   "(i) A constellation (1). (ii) The Pole star (1). (iii) Ursa Major (Saptarishi) (1). (iv) Starlight passes through the moving air of the atmosphere (1), which makes the light appear to flicker or twinkle (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Karan watched the Moon over a month. On one night it looked like a thin curved line, a week later it looked half bright, and after about two weeks it appeared as a full bright disc. After a few more days it was gradually shrinking. On one night it was not visible at all. "
   "(i) What is the day on which the Moon is not visible called? (ii) What are the different shapes of the Moon called? (iii) Does the Moon have its own light? (iv) Explain why the shape of the bright part seems to change.",
   "(i) New moon (1). (ii) Phases of the Moon (1). (iii) No, it reflects sunlight (1). (iv) Half of the Moon is always lit by the Sun (1); as the Moon moves around the Earth, we see different parts of the lit half (1).", "1+1+1+2"),
 Q("<b>Case study.</b> ISRO's scientists in Bengaluru have sent many missions to space. Aryabhata was India's first satellite. Chandrayaan was sent to study the Moon, and Mangalyaan went to Mars. Artificial satellites in space now help in weather forecasting, television, mobile phone communication and navigation. "
   "(i) Name India's first satellite. (ii) Which mission was sent to the Moon? (iii) What is an artificial satellite? (iv) Give two uses of artificial satellites that help us in daily life.",
   "(i) Aryabhata (1). (ii) Chandrayaan (1). (iii) A man-made object that goes around the Earth in space (1). (iv) Weather forecasting (1) and communication such as TV and phones (or navigation) (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Celestial bodies", ["Celestial bodies: Sun, Moon, stars, planets, comets, asteroids.", "Stars make their own light and heat (the Sun is a star).", "The Moon reflects sunlight; planets also shine by reflected light."]),
 ("Solar system", ["Eight planets go around the Sun: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.", "Mercury is nearest to the Sun; Neptune is farthest.", "Earth is the only planet known to have life."]),
 ("Stars and constellations", ["Constellation: a group of stars forming a pattern (Ursa Major or Saptarishi).", "Pole star: appears almost fixed in the northern sky; shows north.", "Stars twinkle because their light passes through moving air."]),
 ("Moon and space missions", ["The Moon goes around the Earth in about a month.", "Phases of the Moon: different shapes of the lit part seen from Earth; new moon to full moon.", "Artificial satellites: man-made, used for weather, communication and navigation.",
   "Aryabhata: first Indian satellite (1975). Chandrayaan: Moon. Mangalyaan: Mars."]),
]

MISTAKES = [
 "Writing that the Moon makes its own light; it only <b>reflects</b> sunlight.",
 "Writing nine planets or the wrong order; there are eight, starting with Mercury nearest to the Sun.",
 "Thinking the Moon itself changes shape; we only see different amounts of its lit half as it goes around the Earth.",
 "Mixing Chandrayaan (Moon) with Mangalyaan (Mars); Aryabhata was a satellite.",
 "Saying the Pole star is the brightest star or moves around; it appears nearly fixed and shows <b>north</b>.",
 "Confusing a star with a planet: the Sun is a star and the Earth is a planet.",
]
