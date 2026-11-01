import sys
import compose9
CH = {1: "Large Numbers Around Us", 2: "Arithmetic Expressions", 3: "A Peek Beyond the Point", 4: "Expressions Using Letter-Numbers",
      5: "Parallel and Intersecting Lines", 6: "Number Play", 7: "A Tale of Three Intersecting Lines", 8: "Working with Fractions"}
cfg = dict(subject="Maths", chapters=CH, modfmt="c7maths.c%02d", root="/home/claude/out7/Maths_Class7_Paper_Generated",
  slug={1: "Large_Numbers", 2: "Arithmetic_Expressions", 3: "Peek_Beyond_the_Point", 4: "Letter_Numbers", 5: "Parallel_and_Intersecting_Lines", 6: "Number_Play", 7: "Three_Intersecting_Lines", 8: "Working_with_Fractions"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8)],
  pair_names={(1, 2): "Large_Numbers_and_Arithmetic_Expressions", (3, 4): "Decimals_and_Letter_Numbers", (5, 6): "Lines_and_Number_Play", (7, 8): "Triangles_and_Fractions"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Numbers_Expressions_Decimals_Algebra"), ((5, 6, 7, 8), "Unit2_Ch05-08_Lines_Number_Play_Triangles_Fractions")],
  words=("20–30", "40–60", "80–100"), note="Draw neat figures wherever required.",
  full=dict(MCQ={1: 3, 2: 2, 3: 3, 4: 2, 5: 3, 6: 2, 7: 3, 8: 2}, BQ=[1, 2, 3, 4, 5, 6, 7, 8], CPLAIN=[1, 3, 4, 5, 7, 8], CORS=[2, 6], DQ=[3, 5, 7, 8]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
