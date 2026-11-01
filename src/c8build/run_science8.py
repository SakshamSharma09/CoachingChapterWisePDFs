import sys
import compose9
CH = {1: "Exploring the Investigative World of Science", 2: "The Invisible Living World: Beyond Our Naked Eye", 3: "Health: The Ultimate Treasure",
      4: "Electricity: Magnetic and Heating Effects", 5: "Exploring Forces", 6: "Pressure, Winds, Storms and Cyclones",
      7: "Particulate Nature of Matter", 8: "Nature of Matter: Elements, Compounds and Mixtures", 9: "The Amazing World of Solutes, Solvents and Solutions",
      10: "Light: Mirrors and Lenses", 11: "Keeping Time with the Skies", 12: "How Nature Works in Harmony", 13: "Our Home Earth, a Unique Life-Sustaining Planet"}
cfg = dict(subject="Science", chapters=CH, modfmt="sci8.s%02d", root="/home/claude/out8/Science_Class8_Paper_Generated",
  slug={1: "Investigative_World", 2: "Invisible_Living_World", 3: "Health", 4: "Electricity", 5: "Forces", 6: "Pressure_Winds_Cyclones",
        7: "Particulate_Nature", 8: "Elements_Compounds_Mixtures", 9: "Solutes_Solvents_Solutions", 10: "Light_Mirrors_Lenses",
        11: "Keeping_Time_with_Skies", 12: "Nature_in_Harmony", 13: "Our_Home_Earth"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (12, 13)],
  pair_names={(1, 2): "Investigation_and_Microorganisms", (3, 4): "Health_and_Electricity", (5, 6): "Forces_and_Pressure", (7, 8): "Particles_and_Types_of_Matter",
              (9, 10): "Solutions_and_Light", (11, 12): "Sky_Time_and_Ecosystems", (12, 13): "Ecosystems_and_Earth"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Investigation_Cells_Health_Electricity"), ((5, 6, 7, 8, 9), "Unit2_Ch05-09_Forces_Pressure_Matter_Solutions"), ((10, 11, 12, 13), "Unit3_Ch10-13_Light_Time_Ecosystems_Earth")],
  words=("10–15", "30–40", "80–100"), note="Draw neat, labelled diagrams wherever required.",
  full=dict(MCQ={1: 2, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2, 7: 1, 8: 2, 9: 1, 10: 1, 11: 1, 12: 2, 13: 2}, BQ=[2, 3, 4, 6, 8, 9, 12, 13],
            CPLAIN=[1, 5, 7, 10, 11, 13], CORS=[4, 12], DQ=[3, 6, 9, 12]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
