import sys; sys.path.insert(0, '/home/claude/rnlib')
from notes import *
ch = dict(num=1, title="The Problem of Choice", tag="Economics", theme="Scarcity, opportunity cost, PPC",
 intro="Every person, family and country must choose how to use limited resources. This chapter builds the basic ideas of economics from that one fact.",
 big_questions=["Why must every society make choices?", "What do we give up when we choose?"],
 blocks=[("h2", "1.1 Scarcity and Choice"), ("p", "**Scarcity** means resources are limited while wants are unlimited, so choice is unavoidable."),
  ("ul", ["Resources: land, labour, capital.", "Wants keep growing."]),
  ("note", "DEFINITION", "**Opportunity cost** is the value of the next best alternative given up."),
  ("table", ["Term", "Meaning", "Example"], [["Scarcity", "Limited resources", "Water"], ["Choice", "Selecting among options", "Crop to grow"]]),
  ("h2", "1.2 PPC"), ("steps", [("Step 1 — Draw axes", "Show two goods."), ("Step 2 — Plot points", "Join them.")]),
  ("h2", "1.3 Quick check"), ("qa", [("What is scarcity?", "Limited resources against unlimited wants.")])],
 takeaways=["Scarcity forces **choice**.", "Opportunity cost is the **next best** alternative lost."])
check_chapters([ch])
build_pdf(dict(title="Class 9 · Social Science", sub="Sample", label="Grade 9 Social Science"), [ch], "/home/claude/rnlib/sample.pdf")
