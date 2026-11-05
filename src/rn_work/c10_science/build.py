import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_10', 'Science', 'Revision_Notes'))
S = "NCERT Science — Class 10 · CBSE / RBSE Syllabus 2026-27"
run('c10_science', 1, 4, f"{ROOT}/Class10_Science_Revision_Notes_Part1_Ch1-4.pdf", "Class 10 · Science", f"Chemistry — Chapters 1 to 4 · {S}", "Grade 10 Science · Part 1")
run('c10_science', 5, 8, f"{ROOT}/Class10_Science_Revision_Notes_Part2_Ch5-8.pdf", "Class 10 · Science", f"Biology — Chapters 5 to 8 · {S}", "Grade 10 Science · Part 2")
run('c10_science', 9, 13, f"{ROOT}/Class10_Science_Revision_Notes_Part3_Ch9-13.pdf", "Class 10 · Science", f"Physics and Environment — Chapters 9 to 13 · {S}", "Grade 10 Science · Part 3")
