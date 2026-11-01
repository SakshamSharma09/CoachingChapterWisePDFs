import sys
import compose9
CH = {1: "Wonderful World of Science", 2: "Diversity in the Living World", 3: "Mindful Eating", 4: "Exploring Magnets",
      5: "Measurement of Length and Motion", 6: "Materials Around Us", 7: "Temperature and its Measurement", 8: "A Journey through States of Water",
      9: "Methods of Separation in Everyday Life", 10: "Living Creatures: Exploring their Characteristics", 11: "Nature's Treasures", 12: "Beyond Earth"}
cfg = dict(subject="Science", chapters=CH, modfmt="sci6.s%02d", root="/home/claude/out6/Science_Class6_Paper_Generated",
  slug={1: "Wonderful_World_of_Science", 2: "Diversity_in_Living_World", 3: "Mindful_Eating", 4: "Exploring_Magnets", 5: "Length_and_Motion", 6: "Materials_Around_Us",
        7: "Temperature", 8: "States_of_Water", 9: "Methods_of_Separation", 10: "Living_Creatures", 11: "Natures_Treasures", 12: "Beyond_Earth"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)],
  pair_names={(1, 2): "Science_and_Living_World", (3, 4): "Food_and_Magnets", (5, 6): "Measurement_and_Materials", (7, 8): "Temperature_and_Water",
              (9, 10): "Separation_and_Living_Creatures", (11, 12): "Resources_and_Beyond_Earth"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04"), ((5, 6, 7, 8), "Unit2_Ch05-08"), ((9, 10, 11, 12), "Unit3_Ch09-12")],
  words=("10–15", "30–40", "80–100"), note="Draw neat, labelled diagrams wherever required.",
  full=dict(MCQ={1: 1, 2: 2, 3: 2, 4: 1, 5: 2, 6: 2, 7: 1, 8: 2, 9: 2, 10: 2, 11: 2, 12: 1}, BQ=[1, 3, 4, 5, 7, 9, 10, 12],
            CPLAIN=[2, 3, 6, 8, 11, 12], CORS=[5, 9], DQ=[2, 6, 8, 11]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
