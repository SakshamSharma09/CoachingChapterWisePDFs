import copy, random
import compose_core as M
# ───────── shuffling ─────────
def shuf_sub(s, rng):
    s = copy.deepcopy(s)
    if s.get("opts") and not any(M.FIXED.search(o) for o in s["opts"]):
        correct = s["opts"]["abcd".index(s["ans"])]
        rng.shuffle(s["opts"]); s["ans"] = "abcd"[s["opts"].index(correct)]
    return s

def shuffle_data(data, seed):
    rng = random.Random(seed); out = {}
    for k, items in data.items():
        new = []
        for it in items:
            if it["kind"] == "mcq": new.append(M.shuffle_mcq(it, rng))
            elif it["kind"] == "pas":
                it = copy.deepcopy(it); it["subs"] = [shuf_sub(s, rng) for s in it["subs"]]; new.append(it)
            else: new.append(it)
        out[k] = new
    return out


def instr_list(parts, choice=None):
    base = ["All questions are compulsory."] + parts
    if choice: base.append(choice)
    return base + ["Write the question number before each answer.", "Answers must be written in the answer book in the order of the questions."]
