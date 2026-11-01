import sys, copy
import compose9
import compose_core as M
_orig = M.shuffle_mcq
def _keep(it, rng):
    if it["opts"][0].startswith("Both A and R"): return copy.deepcopy(it)
    return _orig(it, rng)
M.shuffle_mcq = _keep
CH = {1: "Natural Resources and Their Use", 2: "Reshaping India’s Political Map", 3: "The Rise of the Marathas", 4: "The Colonial Era in India",
      5: "Universal Franchise and India’s Electoral System", 6: "The Parliamentary System: Legislature and Executive", 7: "Factors of Production"}
cfg = dict(subject="Social Science", chapters=CH, modfmt="sst8.s%02d", root="/home/claude/out8/SocialScience_Class8_Paper_Generated",
  slug={1: "Natural_Resources", 2: "Reshaping_Indias_Political_Map", 3: "Rise_of_the_Marathas", 4: "Colonial_Era", 5: "Universal_Franchise", 6: "Parliamentary_System", 7: "Factors_of_Production"},
  pairs=[(1, 7), (2, 3), (3, 4), (5, 6)],
  pair_names={(1, 7): "Resources_and_Production", (2, 3): "Medieval_India_and_Marathas", (3, 4): "Marathas_and_Colonial_Era", (5, 6): "Elections_and_Parliament"},
  units=[((1, 7), "Unit1_Ch01_and_Ch07_Resources_and_Economy"), ((2, 3, 4), "Unit2_Ch02-04_History"), ((5, 6), "Unit3_Ch05-06_Polity")],
  words=("10–15", "30–40", "80–100"), note="Draw neat maps and diagrams wherever required.",
  full=dict(MCQ={1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 2}, BQ=[1, 2, 3, 4, 5, 6, 7, 4],
            CPLAIN=[1, 2, 3, 5, 6, 7], CORS=[4, 2], DQ=[3, 4, 6, 7]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
