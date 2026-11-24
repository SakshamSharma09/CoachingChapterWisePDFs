import os
_R = r"D:\Coaching Chapterwise PDFs\Class_10"
_F = {"Maths": "Maths", "Science": "Science", "SST": "Social_Science", "English": "English", "Hindi": "Hindi"}
CH = {}
for s, f in _F.items():
    p = os.path.join(_R, f, "Graded_Papers")
    CH[s] = sorted(d for d in os.listdir(p) if d.startswith("Ch")) if os.path.isdir(p) else []
CH["English"] += ["SKILL_Reading", "SKILL_Grammar", "SKILL_Writing"]
CH["Hindi"] += ["SKILL_Reading", "SKILL_Grammar", "SKILL_Writing"]
if __name__ == "__main__":
    for k, v in CH.items(): print(k, v)
