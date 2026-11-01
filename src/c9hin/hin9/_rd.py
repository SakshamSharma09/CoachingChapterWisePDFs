from hin_lib import P, S
GT = "निम्नलिखित अपठित गद्यांश को पढ़कर नीचे दिए गए प्रश्नों के उत्तर अपनी उत्तर-पुस्तिका में लिखिए।"
PT = "निम्नलिखित अपठित पद्यांश को पढ़कर नीचे दिए गए प्रश्नों के उत्तर अपनी उत्तर-पुस्तिका में लिखिए।"
def G(text, *qa):
    return P("<p>" + text + "</p>", [S(q, a, 1) for q, a in qa], title=GT)
def V(lines, *qa):
    return P("<div class='pt'>" + "<br>".join(lines) + "</div>", [S(q, a, 1) for q, a in qa], title=PT)
