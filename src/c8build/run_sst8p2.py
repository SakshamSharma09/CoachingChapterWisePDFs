import sys, copy
import compose9
import compose_core as M
_orig = M.shuffle_mcq
def _keep(it, rng):
    if it["opts"][0].startswith("Both A and R"): return copy.deepcopy(it)
    return _orig(it, rng)
M.shuffle_mcq = _keep
CH1 = {1: "Natural Resources and Their Use", 2: "Reshaping India’s Political Map", 3: "The Rise of the Marathas", 4: "The Colonial Era in India",
      5: "Universal Franchise and India’s Electoral System", 6: "The Parliamentary System: Legislature and Executive", 7: "Factors of Production"}
CH2 = {8: "World Geography", 9: "India’s Long Road to Independence", 10: "A Journey Through Indian Architecture", 11: "The Role of the Judiciary",
       12: "Citizenship: Rights and Duties", 13: "Dynamics of Population", 14: "India’s Urban Landscape", 15: "Cultural Currents: 13th to 17th Centuries"}
SL = {1: "Natural_Resources", 2: "Reshaping_Indias_Political_Map", 3: "Rise_of_the_Marathas", 4: "Colonial_Era", 5: "Universal_Franchise", 6: "Parliamentary_System", 7: "Factors_of_Production",
      8: "World_Geography", 9: "Road_to_Independence", 10: "Indian_Architecture", 11: "Role_of_Judiciary", 12: "Citizenship", 13: "Dynamics_of_Population", 14: "Urban_Landscape", 15: "Cultural_Currents"}
mode = sys.argv[1]; lv = sys.argv[2] if len(sys.argv) > 2 else "1234"
base = dict(subject="Social Science", modfmt="sst8.s%02d", slug=SL, words=("10–15", "30–40", "80–100"), note="Draw neat maps and diagrams wherever required.")
if mode == "p2":
    cfg = dict(base, chapters=CH2, root="/home/claude/out8/SocialScience_Class8_Part2_Papers",
      pairs=[(8, 13), (9, 15), (10, 15), (11, 12), (13, 14)],
      pair_names={(8, 13): "Geography_World_and_Population", (9, 15): "History_Independence_and_Culture", (10, 15): "Architecture_and_Cultural_Currents", (11, 12): "Judiciary_and_Citizenship", (13, 14): "Population_and_Urban_India"},
      units=[((8, 13, 14), "Unit4_Geography_Ch08_13_14"), ((9, 10, 15), "Unit5_History_Ch09_10_15"), ((11, 12), "Unit6_Civics_Ch11-12")],
      full=dict(MCQ={}, BQ=[], CPLAIN=[], CORS=[], DQ=[]))
else:
    cfg = dict(base, chapters={**CH1, **CH2}, root="/home/claude/out8/SocialScience_Class8_FullYear_Part1+2", pairs=[], pair_names={}, units=[], full=dict(rot=8))
compose9.run(cfg, lv)
