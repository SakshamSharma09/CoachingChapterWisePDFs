import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_09', 'Maths', 'Revision_Notes'))
run('c9_maths1', 1, 8, f"{ROOT}/Class9_Maths_Revision_Notes_Part1_Ch01-08.pdf", "Class 9 · Mathematics", "Ganita Manjari — Part 1, Chapters 1 to 8 · CBSE / RBSE Syllabus", "Grade 9 Mathematics · Part 1")
