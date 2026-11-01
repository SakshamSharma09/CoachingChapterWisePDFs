import sys, copy
import compose9
import compose_core as M
_orig = M.shuffle_mcq
def _keep(it, rng):
    if it["opts"][0].startswith("Both A and R"): return copy.deepcopy(it)
    return _orig(it, rng)
M.shuffle_mcq = _keep
CH = {1: "The Problem of Choice", 2: "The Price Puzzle", 3: "Shaping the Earth's Surface", 4: "Atmosphere and Climate",
      5: "Early Humans and the Beginning of Civilisation", 6: "State and Society up to 1000 CE", 7: "Democracy", 8: "Elections"}
cfg = dict(subject="Social Science", chapters=CH, modfmt="sst9.s%02d", root="/home/claude/out9/SocialScience_Class9_Paper_Generated",
  slug={1: "Problem_of_Choice", 2: "Price_Puzzle", 3: "Shaping_Earths_Surface", 4: "Atmosphere_and_Climate", 5: "Early_Humans_and_Civilisation",
        6: "State_and_Society", 7: "Democracy", 8: "Elections"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8)],
  pair_names={(1, 2): "Economics", (3, 4): "Geography", (5, 6): "History", (7, 8): "Polity"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Economics_and_Geography"), ((5, 6, 7, 8), "Unit2_Ch05-08_History_and_Polity")],
  words=("10–15", "30–40", "100–150"), note="Draw neat maps and diagrams wherever required.",
  full=dict(MCQ={1: 3, 2: 3, 3: 2, 4: 3, 5: 2, 6: 3, 7: 2, 8: 2}, BQ=[1, 2, 3, 4, 5, 6, 7, 8],
            CPLAIN=[1, 3, 4, 5, 6, 7], CORS=[2, 8], DQ=[3, 6, 7, 8]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
