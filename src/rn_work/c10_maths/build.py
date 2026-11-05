import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_10', 'Maths', 'Revision_Notes'))
S = "NCERT Mathematics — Class 10 · CBSE / RBSE Syllabus 2026-27"
run('c10_maths', 1, 5, f"{ROOT}/Class10_Maths_Revision_Notes_Part1_Ch1-5.pdf", "Class 10 · Mathematics", f"Chapters 1 to 5 · {S}", "Grade 10 Mathematics · Part 1")
run('c10_maths', 6, 9, f"{ROOT}/Class10_Maths_Revision_Notes_Part2_Ch6-9.pdf", "Class 10 · Mathematics", f"Chapters 6 to 9 · {S}", "Grade 10 Mathematics · Part 2")
run('c10_maths', 10, 14, f"{ROOT}/Class10_Maths_Revision_Notes_Part3_Ch10-14.pdf", "Class 10 · Mathematics", f"Chapters 10 to 14 · {S}", "Grade 10 Mathematics · Part 3")
