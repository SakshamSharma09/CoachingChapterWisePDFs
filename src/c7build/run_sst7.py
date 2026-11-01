import sys, copy
import compose9
import compose_core as M
_orig = M.shuffle_mcq
def _keep(it, rng):
    if it["opts"][0].startswith("Both A and R"): return copy.deepcopy(it)
    return _orig(it, rng)
M.shuffle_mcq = _keep
CH = {1: "Geographical Diversity of India", 2: "Understanding the Weather", 3: "Climates of India", 4: "How the Land Becomes Sacred",
      5: "New Beginnings: Cities and States", 6: "The Rise of Empires", 7: "The Age of Reorganisation", 8: "The Gupta Era: An Age of Tireless Creativity",
      9: "From the Rulers to the Ruled: Types of Governments", 10: "The Constitution of India: An Introduction", 11: "From Barter to Money", 12: "Understanding Markets"}
cfg = dict(subject="Social Science", chapters=CH, modfmt="c7sst.s%02d", root="/home/claude/out7/SocialScience_Class7_Paper_Generated",
  slug={1: "Geographical_Diversity", 2: "Understanding_the_Weather", 3: "Climates_of_India", 4: "Sacred_Land", 5: "Cities_and_States", 6: "Rise_of_Empires",
        7: "Age_of_Reorganisation", 8: "Gupta_Era", 9: "Types_of_Governments", 10: "Constitution_of_India", 11: "Barter_to_Money", 12: "Understanding_Markets"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)],
  pair_names={(1, 2): "Geography_Diversity_and_Weather", (3, 4): "Climate_and_Sacred_Land", (5, 6): "Cities_States_and_Empires", (7, 8): "Reorganisation_and_Guptas",
              (9, 10): "Governments_and_Constitution", (11, 12): "Money_and_Markets"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Geography_and_Sacred_Land"), ((5, 6, 7, 8), "Unit2_Ch05-08_History"), ((9, 10, 11, 12), "Unit3_Ch09-12_Polity_and_Economics")],
  words=("15–25", "40–60", "80–120"), note="Draw neat maps and diagrams wherever required.",
  full=dict(MCQ={1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 6: 2, 7: 1, 8: 2, 9: 2, 10: 1, 11: 2, 12: 1}, BQ=[1, 3, 4, 6, 8, 9, 11, 12],
            CPLAIN=[2, 3, 5, 7, 10, 12], CORS=[1, 9], DQ=[2, 5, 8, 10]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
