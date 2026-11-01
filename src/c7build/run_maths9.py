import sys
import compose9
CH = {1: "Orienting Yourself: The Use of Coordinates", 2: "Introduction to Linear Polynomials", 3: "The World of Numbers",
      4: "Exploring Algebraic Identities", 5: "Circles", 6: "Measuring Space: Perimeter and Area",
      7: "The Mathematics of Maybe: Introduction to Probability", 8: "Predicting What Comes Next: Sequences and Progressions"}
cfg = dict(subject="Maths", chapters=CH, modfmt="content9.ch%02d", root="/home/claude/out9/Maths_Class9_Paper_Generated",
  slug={1: "Coordinates", 2: "Linear_Polynomials", 3: "World_of_Numbers", 4: "Algebraic_Identities", 5: "Circles", 6: "Perimeter_and_Area", 7: "Probability", 8: "Sequences_and_Progressions"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8)],
  pair_names={(1, 2): "Coordinates_and_Linear_Polynomials", (3, 4): "Numbers_and_Algebraic_Identities", (5, 6): "Circles_and_Perimeter_Area", (7, 8): "Probability_and_Sequences"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Coordinates_Polynomials_Numbers_Identities"), ((5, 6, 7, 8), "Unit2_Ch05-08_Circles_Mensuration_Probability_Sequences")],
  words=("20–30", "40–60", "100–150"), note="Draw neat figures wherever required.",
  full=dict(MCQ={1: 3, 2: 2, 3: 3, 4: 2, 5: 3, 6: 3, 7: 2, 8: 2}, BQ=[1, 2, 3, 4, 5, 6, 7, 8], CPLAIN=[1, 2, 3, 4, 6, 7], CORS=[5, 8], DQ=[3, 5, 6, 8]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
