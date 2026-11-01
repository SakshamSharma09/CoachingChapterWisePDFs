import sys
import compose9
CH = {1: "Exploration: Entering the World of Chemistry", 2: "Exploring Mixtures and Their Separation", 3: "The Atomic Foundations of Matter",
      4: "Journey Inside the Atom", 5: "Describing Motion Around Us", 6: "How Forces Affect Motion",
      7: "Work, Energy and Simple Machines", 8: "Sound Waves: Characteristics and Applications", 9: "Cell: The Building Block of Life",
      10: "Tissues in Action", 11: "Patterns in Life: Diversity and Classification", 12: "Reproduction: How Life Continues",
      13: "Earth as a System: Energy, Matter and Life"}
cfg = dict(subject="Science", chapters=CH, modfmt="sci9.s%02d", root="/home/claude/out9/Science_Class9_Paper_Generated",
  slug={1: "Exploration_Chemistry", 2: "Mixtures_and_Separation", 3: "Atomic_Foundations_of_Matter", 4: "Journey_Inside_the_Atom", 5: "Describing_Motion",
        6: "How_Forces_Affect_Motion", 7: "Work_Energy_Simple_Machines", 8: "Sound_Waves", 9: "Cell", 10: "Tissues_in_Action",
        11: "Diversity_and_Classification", 12: "Reproduction", 13: "Earth_as_a_System"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)],
  pair_names={(1, 2): "Chemistry_Exploration_and_Mixtures", (3, 4): "Atoms_and_Atomic_Structure", (5, 6): "Motion_and_Forces", (7, 8): "Energy_and_Sound",
              (9, 10): "Cells_and_Tissues", (11, 12): "Classification_and_Reproduction"},
  units=[((1, 2, 3, 4), "Unit1_Ch01-04_Chemistry"), ((5, 6, 7, 8), "Unit2_Ch05-08_Physics"), ((9, 10, 11, 12, 13), "Unit3_Ch09-13_Biology_and_Earth_System")],
  words=("10–15", "30–40", "100–150"), note="Draw neat, labelled diagrams wherever required.",
  full=dict(MCQ={1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 6: 2, 7: 1, 8: 1, 9: 2, 10: 1, 11: 1, 12: 2, 13: 1}, BQ=[1, 3, 5, 6, 9, 10, 12, 13],
            CPLAIN=[2, 4, 7, 8, 10, 11], CORS=[3, 13], DQ=[3, 6, 9, 12]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
