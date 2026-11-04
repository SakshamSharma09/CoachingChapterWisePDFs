import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_06', 'Maths', 'Revision_Notes'))
run('c6_maths', 1, 5, f"{ROOT}/Class6_Maths_Revision_Notes_Part1_Ch1-5.pdf", "Class 6 · Mathematics", "Ganita Prakash — Part 1, Chapters 1 to 5 · CBSE / RBSE Syllabus", "Grade 6 Mathematics · Part 1")
run('c6_maths', 6, 10, f"{ROOT}/Class6_Maths_Revision_Notes_Part2_Ch6-10.pdf", "Class 6 · Mathematics", "Ganita Prakash — Part 2, Chapters 6 to 10 · CBSE / RBSE Syllabus", "Grade 6 Mathematics · Part 2")
