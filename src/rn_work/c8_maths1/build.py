import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_08', 'Maths', 'Revision_Notes'))
run('c8_maths1', 1, 7, f"{ROOT}/Class8_Maths_Revision_Notes_Part1_Ch01-07.pdf", "Class 8 · Mathematics", "Ganita Prakash — Part 1, Chapters 1 to 7 · CBSE / RBSE Syllabus", "Grade 8 Mathematics · Part 1")
