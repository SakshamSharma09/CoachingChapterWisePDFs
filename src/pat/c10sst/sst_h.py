import sys; sys.path.insert(0, '/home/claude/pat/c10sst')
from lib_pat import *
import math

# simplified outline of India (lon, lat), clockwise from Kutch
OUT = [(68.2,23.7),(68.8,22.4),(69.7,22.4),(69.1,22.0),(69.8,21.2),(70.8,20.7),(71.5,20.9),(72.2,21.5),(72.6,21.1),(72.7,20.3),(72.9,19.3),(72.8,18.5),(73.3,17.0),(73.8,15.5),(74.2,14.6),(74.7,13.0),(75.3,11.8),(76.1,10.2),(76.6,9.0),(77.5,8.1),(78.2,8.9),(79.1,9.3),(79.8,10.3),(79.8,11.4),(80.3,13.1),(80.1,14.5),(80.2,15.8),(81.8,16.8),(82.5,17.0),(83.4,17.9),(84.8,19.2),(85.9,19.9),(86.8,20.9),(87.0,21.6),(88.2,21.7),(89.0,21.9),(89.0,22.8),(88.7,23.9),(88.2,24.8),(88.9,25.2),(89.8,25.3),(89.8,26.0),(91.0,25.7),(92.0,25.1),(92.3,24.1),(91.7,23.6),(91.4,23.0),(91.9,22.4),(92.5,22.2),(92.4,21.4),(92.8,22.0),(93.2,22.7),(93.3,23.9),(93.9,24.0),(94.6,25.0),(95.2,26.0),(96.2,27.3),(97.0,27.8),(97.4,28.3),(96.0,29.0),(94.5,29.2),(93.0,28.5),(92.1,27.8),(91.6,27.8),(90.3,28.2),(89.5,28.0),(88.9,27.3),(88.8,28.0),(88.1,27.9),(88.0,26.8),(88.3,26.4),(87.3,26.4),(85.9,26.6),(84.6,27.1),(83.4,27.5),(82.0,28.1),(81.0,28.9),(80.2,28.9),(80.3,30.1),(79.1,31.0),(78.7,31.8),(78.7,32.7),(79.4,33.2),(78.9,34.3),(79.6,35.2),(78.1,35.7),(76.8,35.6),(75.9,36.0),(75.0,36.9),(74.1,36.8),(73.6,35.6),(74.2,34.7),(74.0,34.0),(74.6,33.6),(74.6,32.9),(75.3,32.3),(75.0,31.7),(74.5,31.0),(74.0,30.5),(73.4,29.9),(72.3,29.0),(71.2,27.9),(70.3,27.3),(69.6,26.4),(70.2,25.5),(70.4,24.7),(69.5,24.2),(68.4,23.9)]
LON0, LON1, LAT0, LAT1 = 67.5, 98.5, 6.5, 37.5
W = 330; K = W / (LON1 - LON0); H = int((LAT1 - LAT0) * K) + 8
def xy(lon, lat): return ((lon - LON0) * K + 2, (LAT1 - lat) * K + 4)

PLACES = {  # name: (lat, lon)
 'Amritsar': (31.63, 74.87), 'Delhi': (28.61, 77.21), 'Lahore*': (31.55, 74.34), 'Nagpur': (21.15, 79.09), 'Kolkata': (22.57, 88.36),
 'Chennai': (13.08, 80.27), 'Mumbai': (19.08, 72.88), 'Ahmedabad': (23.02, 72.57), 'Dandi': (20.89, 72.81), 'Champaran': (26.65, 84.9),
 'Kheda': (22.75, 72.68), 'Chauri Chaura': (26.43, 83.65), 'Bardoli': (21.12, 73.11), 'Allahabad': (25.43, 81.84), 'Pune': (18.52, 73.86),
 'Bengaluru': (12.97, 77.59), 'Hyderabad': (17.39, 78.49), 'Kanpur': (26.45, 80.33), 'Lucknow': (26.85, 80.95), 'Surat': (21.17, 72.83),
 'Salal': (33.1, 74.8), 'Bhakra Nangal': (31.41, 76.43), 'Tehri': (30.38, 78.48), 'Rana Pratap Sagar': (24.92, 75.58), 'Sardar Sarovar': (21.83, 73.75),
 'Hirakud': (21.52, 83.87), 'Nagarjuna Sagar': (16.57, 79.31), 'Tungabhadra': (15.27, 76.34), 'Gandhi Sagar': (24.7, 75.55), 'Mettur': (11.8, 77.8),
 'Kandla': (23.03, 70.22), 'Marmagao': (15.4, 73.8), 'New Mangalore': (12.92, 74.82), 'Kochi': (9.97, 76.27), 'Tuticorin': (8.8, 78.15),
 'Visakhapatnam': (17.69, 83.22), 'Paradip': (20.32, 86.61), 'Haldia': (22.03, 88.07), 'Jamshedpur': (22.8, 86.2), 'Bhilai': (21.2, 81.38),
 'Durgapur': (23.5, 87.3), 'Rourkela': (22.25, 84.88), 'Bokaro': (23.67, 86.15), 'Salem': (11.65, 78.16), 'Vijayanagar': (15.17, 76.65),
 'Mayurbhanj': (21.9, 86.7), 'Bailadila': (18.65, 81.25), 'Kudremukh': (13.2, 75.25), 'Bellary': (15.14, 76.92), 'Raniganj': (23.62, 87.13), 'Jharia': (23.75, 86.42),
 'Singrauli': (24.2, 82.67), 'Neyveli': (11.6, 79.5), 'Talcher': (20.95, 85.22), 'Digboi': (27.38, 95.62), 'Naharkatia': (27.28, 95.35), 'Mumbai High': (19.4, 71.3),
 'Ankaleshwar': (21.63, 73.0), 'Kalol': (23.25, 72.5), 'Bassein': (19.3, 72.5), 'Tarapur': (19.83, 72.65), 'Kalpakkam': (12.55, 80.17), 'Narora': (28.17, 78.4),
 'Kakrapara': (21.23, 73.35), 'Kaiga': (14.86, 74.44), 'Ramagundam': (18.75, 79.5), 'Namrup': (27.18, 95.32), 'Thiruvananthapuram': (8.5, 76.95), 'Noida': (28.54, 77.39),
 'Gandhinagar': (23.22, 72.65), 'Jaipur': (26.91, 75.79), 'Kota': (25.2, 75.86), 'Guwahati': (26.14, 91.74), 'Patna': (25.6, 85.1), 'Kanyakumari': (8.08, 77.54),
 'Port Blair': (11.62, 92.73), 'Mysuru': (12.3, 76.65), 'Coimbatore': (11.0, 76.96), 'Indore': (22.72, 75.86), 'Ludhiana': (30.9, 75.85), 'Vishakhapatnam': (17.69, 83.22),
 'Ahmednagar': (19.1, 74.75), 'Gorakhpur': (26.76, 83.37), 'Sabarmati': (23.07, 72.58), 'Sarnath': (25.38, 83.02), 'Simla': (31.1, 77.17), 'Tuticorin ': (8.8, 78.15),
}
def india_map(marks=None, w=W):
    """marks: dict label->place name (draws dot + label) for the answer key; None for blank map."""
    pts = ' '.join(f'{xy(lo, la)[0]:.1f},{xy(lo, la)[1]:.1f}' for lo, la in OUT)
    b = f"<polygon points='{pts}' fill='#f7f3e3' stroke='#222' stroke-width='1.3' stroke-linejoin='round'/>"
    if marks:
        for lab, nm in marks.items():
            la, lo = PLACES[nm]; x, y = xy(lo, la)
            b += f"<circle cx='{x:.1f}' cy='{y:.1f}' r='3.6' fill='#c0392b'/><text x='{x+6:.1f}' y='{y+4:.1f}' font-size='11' font-family='Arial' font-weight='bold' fill='#7b1d12'>{lab}</text>"
    b += f"<text x='{W-8}' y='{H-6}' text-anchor='end' font-size='8' fill='#666' font-family='Arial'>Outline map of India (not to scale)</text>"
    return f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{int(H*w/W)}' viewBox='0 0 {W} {H}'>{b}</svg>"

STMT_OPTS = ["Both statements are correct", "Statement I is correct, Statement II is incorrect", "Statement I is incorrect, Statement II is correct", "Both statements are incorrect"]
def stmt(intro, s1, s2, ans, sol=''):
    q = f"{intro}<br><b>Statement I:</b> {s1}<br><b>Statement II:</b> {s2}"
    return mcq(q, STMT_OPTS, ans, sol)
def match(intro, rows, opts, ans, sol='', h=("Column I", "Column II")):
    t = f"<table class='t'><tr><th>{h[0]}</th><th>{h[1]}</th></tr>" + "".join(f"<tr><td style='text-align:left'>{a}</td><td style='text-align:left'>{b}</td></tr>" for a, b in rows) + "</table>"
    import re as _re; opts=[_re.sub(r"^\([a-d]\)\s*","",o) for o in opts]
    return mcq(f"{intro}{t}", opts, ans, sol)
def mapq(intro, items, key_marks, marks, qno_note=''):
    """items: list of text; the figure shown only in the question (blank map). key_marks: dict for key."""
    q = intro + "<ol type='i' style='margin:1mm 0 0 5mm;padding-left:3mm'>" + "".join(f"<li>{t}</li>" for t in items) + "</ol>"
    d = sa(q, marks, "Locate and label correctly:<br>" + "; ".join(f"<b>{l}</b> – {n}" for l, n in key_marks.items()) + "<br>" + india_map(key_marks, 250), fig=None)
    d['_blank'] = True
    return d
def blank_map_fig(): return india_map(None, 280)
def src(text): return text

def map_pair(hist, geo, geo_m=3, geo_extra=''):
    """hist: list of (letter, place, description) -> pre-marked A/B on map, student names them.
       geo: list of (description, place) (4 items; attempt any 3). Returns (hist_q, geo_q)."""
    pre = {l: p for l, p, d in hist}
    fig = india_map({l: p for l, p, d in hist}, 300)
    # question shows only letters (labels are letters already); key shows letter + name
    ql = "On the political outline map of India, two places are marked as A and B. Identify these places and write their names." + \
         "<ol type='i' style='margin:1mm 0 0 5mm;padding-left:3mm'>" + "".join(f"<li>{d} <b>(1)</b></li>" for l, p, d in hist) + "</ol>" + \
         "<div style='font-size:8.5pt;font-style:italic'>Note: A separate question is provided for visually impaired candidates: write the name of the State/UT in which each of the above places is located.</div>"
    kmarks = {f"{l}: {p}": p for l, p, d in hist}
    hist_q = sa(ql, 2, "Award 1 mark each: " + "; ".join(f"<b>{l}</b> = {p} ({d})" for l, p, d in hist) + "<br>" + india_map({f"{l} – {p}": p for l, p, d in hist}, 260), fig=fig)
    gq = f"On the same outline map of India provided for Question No. 9, locate and label any <b>three</b> of the following with appropriate symbols:{geo_extra}" + \
         "<ol type='i' style='margin:1mm 0 0 5mm;padding-left:3mm'>" + "".join(f"<li>{d}</li>" for d, p in geo) + "</ol>" + \
         "<div style='font-size:8.5pt;font-style:italic'>For visually impaired candidates (in lieu of this question; any three): name the State/UT in which each of the above is located.</div>"
    allm = {f"{l} – {p}": p for l, p, d in hist}
    for d, p in geo: allm[p] = p
    geo_q = sa(gq, geo_m, "Award 1 mark for each correctly located and labelled place (any three): " + "; ".join(f"<b>{p}</b> ({d})" for d, p in geo) + "<br>" + india_map(allm, 300))
    return hist_q, geo_q

def case_n(text, subs, fig=None): return case(text, subs, fig, lab='num')
INSTR = ["There are 38 questions in the question paper. All questions are compulsory.",
 "The question paper has four sections: Section A – History, Section B – Geography, Section C – Political Science and Section D – Economics.",
 "Each section is of 20 marks and has Multiple Choice Questions, Very Short Answer, Short Answer, Long Answer and Case Based questions.",
 "Very Short Answer type questions carry two marks each (answer in not more than 40 words). Short Answer type questions carry three marks each (not more than 60 words). Long Answer type questions carry five marks each (not more than 120 words). Case Based questions have three sub-questions and carry 4 marks each (1+1+2; answer in not more than 100 words).",
 "The Map based question carries five marks with two parts – Section A: History (2 marks) and Section B: Geography (3 marks).",
 "There is no overall choice. However, an internal choice has been provided in a few questions. Only one of the choices in such questions must be attempted.",
 "A separate question has been provided for Visually Impaired candidates in lieu of the map question."]
def meta(n): return dict(cls=10, subject='Social Science', title='CLASS X — SOCIAL SCIENCE · FULL SYLLABUS PRACTICE PAPER', title_extra='Session 2026-27 | CBSE / Delhi DoE Mid-Term Pattern', set_no=n, time='3 Hours', marks=80, secmarks=[20,20,20,20], instr=INSTR)
