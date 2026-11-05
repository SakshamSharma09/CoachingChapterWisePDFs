import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rnbuild import run
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Class_10', 'Social_Science', 'Revision_Notes'))
SUB = "Contemporary India, India and the Contemporary World, Democratic Politics, Understanding Economic Development"
parts = [(1, 5, "Part1_Ch1-5", "History (Ch 1-5)"), (6, 10, "Part2_Ch6-10", "Geography (Ch 6-10)"), (11, 15, "Part3_Ch11-15", "Geography, Political Science (Ch 11-15)"), (16, 21, "Part4_Ch16-21", "Political Science, Economics (Ch 16-21)"), (22, 22, "Part5_Ch22", "Economics (Ch 22)")]
want = sys.argv[1:]
for a, b, nm, lab in parts:
    if want and str(a) not in want: continue
    run('c10_sst', a, b, f"{ROOT}/Class10_SocialScience_Revision_Notes_{nm}.pdf", "Class 10 · Social Science", f"{lab} · CBSE / RBSE Syllabus", f"Grade 10 Social Science · {nm.split('_')[0]}")
