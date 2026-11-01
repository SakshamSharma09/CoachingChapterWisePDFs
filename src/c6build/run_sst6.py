import sys
import compose9
CH = {1: "Locating Places on the Earth", 2: "Oceans and Continents", 3: "Landforms and Life", 4: "Timeline and Sources of History",
      5: "India, That Is Bharat", 6: "The Beginnings of Indian Civilisation", 7: "India's Cultural Roots", 8: "Unity in Diversity",
      9: "Family and Community", 10: "Grassroots Democracy – Part 1: Governance", 11: "Grassroots Democracy – Part 2: Local Government in Rural Areas",
      12: "Grassroots Democracy – Part 3: Local Government in Urban Areas", 13: "The Value of Work", 14: "Economic Activities Around Us"}
cfg = dict(subject="Social Science", chapters=CH, modfmt="sst6.s%02d", root="/home/claude/out6/SocialScience_Class6_Paper_Generated",
  slug={1: "Locating_Places", 2: "Oceans_and_Continents", 3: "Landforms_and_Life", 4: "Timeline_and_Sources", 5: "India_That_Is_Bharat",
        6: "Beginnings_of_Indian_Civilisation", 7: "Indias_Cultural_Roots", 8: "Unity_in_Diversity", 9: "Family_and_Community",
        10: "Grassroots_Democracy_1_Governance", 11: "Grassroots_Democracy_2_Rural", 12: "Grassroots_Democracy_3_Urban",
        13: "Value_of_Work", 14: "Economic_Activities"},
  pairs=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)],
  pair_names={(1, 2): "Locating_Places_and_Oceans", (3, 4): "Landforms_and_Timeline", (5, 6): "Bharat_and_Indian_Civilisation",
              (7, 8): "Cultural_Roots_and_Unity", (9, 10): "Family_and_Governance", (11, 12): "Rural_and_Urban_Local_Government",
              (13, 14): "Work_and_Economic_Activities"},
  units=[((1, 2, 3, 4, 5), "Unit1_Ch01-05_Land_and_the_Past"), ((6, 7, 8, 9), "Unit2_Ch06-09_Civilisation_Culture_Community"),
         ((10, 11, 12, 13, 14), "Unit3_Ch10-14_Governance_and_Economy")],
  words=("10–15", "30–40", "80–100"), note="Draw neat maps and diagrams wherever required.",
  full=dict(MCQ={1: 2, 2: 1, 3: 2, 4: 1, 5: 1, 6: 2, 7: 2, 8: 1, 9: 1, 10: 2, 11: 1, 12: 1, 13: 1, 14: 2}, BQ=[1, 3, 4, 6, 7, 10, 13, 14],
            CPLAIN=[2, 5, 8, 9, 11, 12], CORS=[1, 6], DQ=[3, 7, 11, 14]))
compose9.run(cfg, sys.argv[1] if len(sys.argv) > 1 else "1234")
