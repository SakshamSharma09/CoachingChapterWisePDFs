import sys
import compose9
CH = {1: "Patterns in Mathematics", 2: "Lines and Angles", 3: "Number Play", 4: "Data Handling and Presentation", 5: "Prime Time",
      6: "Perimeter and Area", 7: "Fractions", 8: "Playing with Constructions", 9: "Symmetry", 10: "The Other Side of Zero"}
cfg = dict(subject="Maths", chapters=CH, modfmt="content6.ch%02d", root="/home/claude/out6/Maths_Class6_Paper_Generated",
  slug={1: "Patterns_in_Mathematics", 2: "Lines_and_Angles", 3: "Number_Play", 4: "Data_Handling", 5: "Prime_Time", 6: "Perimeter_and_Area",
        7: "Fractions", 8: "Playing_with_Constructions", 9: "Symmetry", 10: "Other_Side_of_Zero"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)],
  pair_names={(1, 2): "Patterns_and_Lines_Angles", (3, 4): "Number_Play_and_Data_Handling", (5, 6): "Prime_Time_and_Perimeter_Area",
              (7, 8): "Fractions_and_Constructions", (9, 10): "Symmetry_and_Integers"},
  units=[((1, 2, 3, 4, 5), "Unit1_Ch01-05_Patterns_Angles_Numbers_Data_PrimeTime"), ((6, 7, 8, 9, 10), "Unit2_Ch06-10_Mensuration_Fractions_Constructions_Symmetry_Integers")],
  words=("10–15", "30–40", "80–100"), note="Draw neat figures wherever required.",
  full=dict(MCQ={c: 2 for c in range(1, 11)}, BQ=[1, 3, 4, 5, 6, 7, 8, 10], CPLAIN=[1, 2, 4, 6, 8, 9], CORS=[5, 10], DQ=[2, 3, 7, 9]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
