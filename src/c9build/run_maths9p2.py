import sys
import copy
import compose9
import compose_core as M
_orig = M.shuffle_mcq
def _keep(it, rng):
    if it['opts'][0].startswith('Both A and R'): return copy.deepcopy(it)
    return _orig(it, rng)
M.shuffle_mcq = _keep
CH1 = {1: "Orienting Yourself: The Use of Coordinates", 2: "Introduction to Linear Polynomials", 3: "The World of Numbers",
      4: "Exploring Algebraic Identities", 5: "Circles", 6: "Measuring Space: Perimeter and Area",
      7: "The Mathematics of Maybe: Introduction to Probability", 8: "Predicting What Comes Next: Sequences and Progressions"}
CH2 = {9: "Propositions and their Converses", 10: "How Quantities Combine: Understanding Data", 11: "The World of Algorithms", 12: "Quadrilaterals", 13: "Two Variables, One Line", 14: "Math of Space: Surface Area and Volume"}
SL = {1: "Coordinates", 2: "Linear_Polynomials", 3: "World_of_Numbers", 4: "Algebraic_Identities", 5: "Circles", 6: "Perimeter_and_Area", 7: "Probability", 8: "Sequences_and_Progressions",
      9: "Propositions_and_Converses", 10: "Understanding_Data", 11: "World_of_Algorithms", 12: "Quadrilaterals", 13: "Two_Variables_One_Line", 14: "Surface_Area_and_Volume"}
mode = sys.argv[1]; lv = sys.argv[2] if len(sys.argv) > 2 else "1234"
base = dict(subject="Maths", modfmt="content9.ch%02d", slug=SL, words=("20–30", "40–60", "100–150"), note="Draw neat figures wherever required.")
if mode == "p2":
    cfg = dict(base, chapters=CH2, root="/home/claude/out9/Maths_Class9_Part2_Papers", pairs=[(9, 10), (11, 12), (13, 14)],
      pair_names={(9, 10): "Propositions_and_Data", (11, 12): "Algorithms_and_Quadrilaterals", (13, 14): "Linear_Equations_and_Mensuration"},
      units=[((9, 10, 11, 12, 13, 14), "Unit3_Ch09-14_Part2_Complete")], full=dict(MCQ={}, BQ=[], CPLAIN=[], CORS=[], DQ=[]))
else:
    cfg = dict(base, chapters={**CH1, **CH2}, root="/home/claude/out9/Maths_Class9_FullYear_Part1+2", pairs=[], pair_names={}, units=[], full=dict(rot=9))
compose9.run(cfg, lv)
