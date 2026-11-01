import sys, copy
import compose9
import compose_core as M
_orig = M.shuffle_mcq
def _keep(it, rng):
    if it["opts"][0].startswith("Both A and R"): return copy.deepcopy(it)
    return _orig(it, rng)
M.shuffle_mcq = _keep
CH1 = {1: "The Problem of Choice", 2: "The Price Puzzle", 3: "Shaping the Earth's Surface", 4: "Atmosphere and Climate",
      5: "Early Humans and the Beginning of Civilisation", 6: "State and Society up to 1000 CE", 7: "Democracy", 8: "Elections"}
CH2 = {9: "Oceans and Life", 10: "Life on Earth", 11: "Resistance and Resilience (1000–1700 CE)", 12: "Governance and Public Policy",
       13: "Managing Your Personal Finances", 14: "From Ideas to Startups"}
SL = {9: "Oceans_and_Life", 10: "Life_on_Earth", 11: "Resistance_and_Resilience", 12: "Governance_and_Public_Policy", 13: "Personal_Finances", 14: "Ideas_to_Startups",
      1: "Problem_of_Choice", 2: "Price_Puzzle", 3: "Shaping_Earths_Surface", 4: "Atmosphere_and_Climate", 5: "Early_Humans_and_Civilisation", 6: "State_and_Society", 7: "Democracy", 8: "Elections"}
mode = sys.argv[1]; lv = sys.argv[2] if len(sys.argv) > 2 else "1234"
base = dict(subject="Social Science", modfmt="sst9.s%02d", slug=SL, words=("10–15", "30–40", "100–150"), note="Draw neat maps and diagrams wherever required.")
if mode == "p2":
    cfg = dict(base, chapters=CH2, root="/home/claude/out9/SocialScience_Class9_Part2_Papers",
      pairs=[(9, 10), (11, 12), (13, 14)],
      pair_names={(9, 10): "Geography_Oceans_and_Life", (11, 12): "History_and_Polity", (13, 14): "Economics_Finance_and_Startups"},
      units=[((9, 10, 11, 12, 13, 14), "Unit3_Ch09-14_Part2_Complete")],
      full=dict(MCQ={}, BQ=[], CPLAIN=[], CORS=[], DQ=[]))
else:
    allc = {**CH1, **CH2}
    cfg = dict(base, chapters=allc, root="/home/claude/out9/SocialScience_Class9_FullYear_Part1+2", pairs=[], pair_names={}, units=[],
      full=dict(rot=9))
compose9.run(cfg, lv)
