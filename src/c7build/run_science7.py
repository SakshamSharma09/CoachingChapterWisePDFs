import sys
import compose9
CH = {1: "Exploring Substances: Acidic, Basic, and Neutral", 2: "Electricity: Circuits and Their Components", 3: "The World of Metals and Non-metals",
      4: "Changes Around Us: Physical and Chemical", 5: "Adolescence: A Stage of Growth and Change", 6: "Heat Transfer in Nature",
      7: "Measurement of Time and Motion", 8: "Life Processes in Animals", 9: "Life Processes in Plants", 10: "Light: Shadows and Reflections",
      11: "Earth, Moon, and the Sun"}
cfg = dict(subject="Science", chapters=CH, modfmt="c7sci.s%02d", root="/home/claude/out7/Science_Class7_Paper_Generated",
  slug={1: "Acids_Bases_Neutral", 2: "Electricity_Circuits", 3: "Metals_and_Non-metals", 4: "Physical_and_Chemical_Changes", 5: "Adolescence",
        6: "Heat_Transfer", 7: "Time_and_Motion", 8: "Life_Processes_Animals", 9: "Life_Processes_Plants", 10: "Light_Shadows_Reflections",
        11: "Earth_Moon_Sun"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)],
  pair_names={(1, 2): "Acids_Bases_and_Electricity", (3, 4): "Metals_and_Changes", (5, 6): "Adolescence_and_Heat", (7, 8): "Motion_and_Animal_Life",
              (9, 10): "Plant_Life_and_Light"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Substances_Electricity_Metals_Changes"), ((5, 6, 7, 8), "Unit2_Ch05-08_Adolescence_Heat_Motion_Animals"),
         ((9, 10, 11), "Unit3_Ch09-11_Plants_Light_Earth_Moon_Sun")],
  words=("15–25", "40–60", "80–120"), note="Draw neat, labelled diagrams wherever required.",
  full=dict(MCQ={1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1}, BQ=[1, 2, 3, 5, 6, 7, 8, 9],
            CPLAIN=[2, 4, 6, 8, 10, 11], CORS=[1, 9], DQ=[3, 5, 7, 10]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
