"""Class 6 Maths Ch 9 Symmetry - extras."""
from common import AR4, Q

AR = [
 AR4("A square has 4 lines of symmetry.", "A regular polygon with n sides has n lines of symmetry.", "a",
     "A square is a regular polygon with 4 sides."),
 AR4("A rectangle that is not a square has 2 lines of symmetry.", "Such a rectangle has rotational symmetry of order 2.", "b",
     "Both are true but the order of rotation does not explain the number of lines."),
 AR4("A parallelogram that is not a rectangle or rhombus has rotational symmetry of order 2.", "Such a parallelogram has two lines of symmetry.", "c",
     "It fits onto itself after a half turn, so A is true. It has no line of symmetry, so R is false."),
 AR4("The letter H has no line of symmetry.", "The letter H has rotational symmetry of order 2.", "d",
     "H has two lines of symmetry (vertical and horizontal), so A is false. R is true."),
 AR4(r"The smallest angle of rotation of a regular hexagon is $60^\circ$.", r"The smallest angle of rotation is $360^\circ$ divided by the order of rotational symmetry, and the order is 6.", "a",
     r"$360\div6=60$."),
 AR4("An equilateral triangle has rotational symmetry of order 3.", "An equilateral triangle has 3 lines of symmetry.", "b",
     "Both are true, but neither explains the other."),
]

CASE = [
 Q(r"<b>Case study.</b> Priya draws a rangoli in the shape of a regular hexagon. (i) How many lines of symmetry does the rangoli have? (ii) What is the order of its rotational symmetry? (iii) What is the smallest angle through which it can be turned to fit onto itself? (iv) Will the rangoli look the same after a turn of $180^\circ$? Will it look the same after a turn of $100^\circ$? Give reasons.",
   r"(i) 6 (1). (ii) 6 (1). (iii) $360^\circ\div6=60^\circ$ (1). (iv) Yes after $180^\circ$, because $180^\circ=3\times60^\circ$ (1); no after $100^\circ$, because 100 is not a multiple of 60 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A shop board carries the letters A, H, S and T. The students study each letter for symmetry. (i) Which of the letters have a vertical line of symmetry? (ii) Which letters have rotational symmetry of order 2? (iii) Which letter has no line of symmetry? (iv) Which letter has both lines of symmetry and rotational symmetry of order more than 1? State its number of lines of symmetry and its order.",
   r"(i) A, H and T (1). (ii) H and S (1). (iii) S (1). (iv) H (1); it has 2 lines of symmetry (vertical and horizontal) and rotational symmetry of order 2 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A teacher shows four shapes: an equilateral triangle, a rectangle (not a square), an isosceles triangle (not equilateral) and a scalene triangle. (i) How many lines of symmetry does the isosceles triangle have? (ii) How many does the scalene triangle have? (iii) What is the order of rotational symmetry of the rectangle? (iv) Which shape has the most lines of symmetry, how many, and how does that compare with the rectangle?",
   r"(i) 1 (1). (ii) 0 (1). (iii) 2 (1). (iv) The equilateral triangle, with 3 lines (1); the rectangle has only 2, so the triangle has 1 more (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Line (reflection) symmetry", [r"A line of symmetry divides a figure into two parts that fit exactly on each other when folded (mirror halves).",
   r"Mirror image: a point is as far behind the mirror line as the original is in front of it.",
   r"A figure may have 0, 1, 2, 3, ... or infinitely many lines of symmetry (circle)."]),
 ("Rotational symmetry", [r"A figure has rotational symmetry if it fits onto itself after a turn of less than $360^\circ$ about a point (the centre).",
   r"Order of rotational symmetry $=$ number of times it fits onto itself in one full turn.",
   r"Smallest angle of rotation $=\dfrac{360^\circ}{\text{order}}$."]),
 ("Regular polygons", [r"A regular polygon with $n$ sides has $n$ lines of symmetry and rotational symmetry of order $n$.",
   r"Equilateral triangle: 3 lines, order 3, angle $120^\circ$.   Square: 4 lines, order 4, angle $90^\circ$.",
   r"Regular hexagon: 6 lines, order 6, angle $60^\circ$.   Circle: infinite lines and infinite order."]),
 ("Other shapes and letters", [r"Rectangle (not square): 2 lines, order 2.   Rhombus (not square): 2 lines, order 2.   Parallelogram: 0 lines, order 2.",
   r"Isosceles triangle: 1 line, order 1.   Scalene triangle: 0 lines, order 1.",
   r"Letters: H, O, X: 2 lines and order 2.  A, T, M, U: 1 line.  S, N, Z: no line but order 2."]),
]

MISTAKES = [
 r"Saying a rectangle has 4 lines of symmetry (diagonals are not lines of symmetry); a non-square rectangle has only 2.",
 r"Giving a parallelogram 2 lines of symmetry; it has none, though it has rotational symmetry of order 2.",
 r"Mixing up the order of rotation with the smallest angle: angle $=360^\circ\div$ order.",
 r"Saying a figure with order 1 has rotational symmetry; order 1 means only the trivial full turn.",
 r"Drawing the mirror image at the wrong distance from the mirror line or on the same side of it.",
]
