import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_07', 'Maths', 'Revision_Notes'))
run('c7_maths', 1, 4, f"{ROOT}/Class7_Maths_Revision_Notes_Part1_Ch1-4.pdf", "Class 7 · Mathematics", "Ganita Prakash — Part 1, Chapters 1 to 4 · CBSE / RBSE Syllabus", "Grade 7 Mathematics · Part 1")
run('c7_maths', 5, 8, f"{ROOT}/Class7_Maths_Revision_Notes_Part2_Ch5-8.pdf", "Class 7 · Mathematics", "Ganita Prakash — Part 2, Chapters 5 to 8 · CBSE / RBSE Syllabus", "Grade 7 Mathematics · Part 2")
