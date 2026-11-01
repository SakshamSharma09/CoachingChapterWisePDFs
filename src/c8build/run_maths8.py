import sys
import compose9
CH = {1: "A Square and a Cube", 2: "Power Play", 3: "A Story of Numbers", 4: "Quadrilaterals", 5: "Number Play",
      6: "We Distribute, Yet Things Multiply", 7: "Proportional Reasoning-1", 8: "Fractions in Disguise", 9: "The Baudhayana–Pythagoras Theorem",
      10: "Proportional Reasoning-2", 11: "Exploring Some Geometric Themes", 12: "Tales by Dots and Lines", 13: "Algebra Play", 14: "Area"}
cfg = dict(subject="Maths", chapters=CH, modfmt="content8.ch%02d", root="/home/claude/out8/Maths_Class8_Paper_Generated",
  slug={1: "Square_and_Cube", 2: "Power_Play", 3: "Story_of_Numbers", 4: "Quadrilaterals", 5: "Number_Play", 6: "Distributive_Property", 7: "Proportional_Reasoning_1",
        8: "Fractions_in_Disguise", 9: "Baudhayana_Pythagoras_Theorem", 10: "Proportional_Reasoning_2", 11: "Geometric_Themes", 12: "Dots_and_Lines", 13: "Algebra_Play", 14: "Area"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)],
  pair_names={(1, 2): "Squares_Cubes_and_Powers", (3, 4): "Number_Story_and_Quadrilaterals", (5, 6): "Number_Play_and_Distributive_Property", (7, 8): "Proportional_Reasoning_and_Percentages",
              (9, 10): "Pythagoras_and_Proportional_Reasoning_2", (11, 12): "Geometric_Themes_and_Data", (13, 14): "Algebra_Play_and_Area"},
  units=[((1, 2, 3, 4, 5), "Unit1_Ch01-05_Numbers_Powers_Quadrilaterals"), ((6, 7, 8, 9, 10), "Unit2_Ch06-10_Algebra_Ratio_Percentage_Pythagoras"), ((11, 12, 13, 14), "Unit3_Ch11-14_Geometry_Data_Algebra_Area")],
  words=("10–15", "30–40", "80–100"), note="Draw neat figures wherever required.",
  full=dict(MCQ={1: 2, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1, 12: 1, 13: 1, 14: 2}, BQ=[2, 3, 5, 7, 9, 10, 12, 14],
            CPLAIN=[1, 4, 6, 8, 11, 13], CORS=[9, 14], DQ=[2, 8, 12, 14]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
