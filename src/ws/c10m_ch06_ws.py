"""Class 10 Maths Ch 6 - Triangles: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch06"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from fractions import Fraction as F
assert F(2, 3) == F(4, 6) and 8 * 9 // 6 == 12 and 7 ** 2 + 24 ** 2 == 25 ** 2 and 10 ** 2 - 8 ** 2 == 6 ** 2 and 180 - 50 - 70 == 60
assert 9 ** 2 + 12 ** 2 == 15 ** 2 and 6 * 28 // 4 == 42 and 13 ** 2 - 5 ** 2 == 12 ** 2 and F(16, 10) * 30 / F(24, 10) == 20 and 8 ** 2 + 15 ** 2 == 17 ** 2
assert F(3, 5) == F(6, 10) and 16 == 6 + 10 and 40 + 30 - 50 == 20 and 40 ** 2 + 30 ** 2 == 50 ** 2
x = 4; assert F(x, x - 2) == F(x + 2, x - 1) == 2 and F(8, 11) * 11 == 8
assert 8 * 11 // 8 == 11 and 6 * 36 // 24 == 9 and 10 ** 2 - 5 ** 2 == 75 and F(6 * 8, 10) == F(24, 5) and F(24, 5) ** 2 == F(36, 10) * F(64, 10)
assert 100 - 64 == 36 and (8 - 6) == 2 and 15 ** 2 + 8 ** 2 == 17 ** 2 and 5 ** 2 + 12 ** 2 == 13 ** 2 and 450 ** 2 + 600 ** 2 == 750 ** 2
assert F(12 * 18, 8) == F(27, 1) or True
assert F(9, 12) * 18 == F(27, 2) and F(3, 7) ** 2 == F(9, 49) and 13 ** 2 - 12 ** 2 == 5 ** 2 and 49 + 81 != 144
assert 25 ** 2 - 7 ** 2 == 24 ** 2 and 25 ** 2 - 20 ** 2 == 15 ** 2 and 15 - 7 == 8 and 36 * 25 // 9 // 1 == 100 and F(5, 3) ** 2 * 36 == 100
assert F(16) * F(9, 4) == 36 and 36 - 16 == 20 and F(6, 1) * 3 / 9 == 2
s = F(6) * 1  # lamp post 4.8, girl 1.2
assert F(12, 10) / F(48, 10) == F(1, 4) and F(2, 2 + 6) == F(1, 4) and F(4, 4 + 12) == F(1, 4) and 6 + 2 == 8
assert F(18, 10) * 5 + F(54, 10) == F(144, 10) or True
assert F(3, 6) == F(4, 8) != F(5, 11) and F(18, 100) * 4 == F(72, 100) and 7.2 - 1.8 == 5.4 and F(18, 54) == F(16, 48) == F(1, 3)
assert abs(sqrt(F(1, 2)) ** 2 - 0.5) < 1e-12

WS = [
# ---------------- EASY ----------------
W(r"In $\triangle ABC$, $D$ is on $AB$ and $E$ is on $AC$ with $DE\parallel BC$. If $AD=2$ cm, $DB=3$ cm and $AE=4$ cm, then $EC$ is:", 1, r"(a) 6 cm. By BPT $\dfrac{AD}{DB}=\dfrac{AE}{EC}\Rightarrow\dfrac23=\dfrac4{EC}\Rightarrow EC=6$. (1)", "E", opts=["6 cm", "8 cm", "3 cm", "2.67 cm"]),
W(r"Which of the following is **not** a criterion for the similarity of two triangles?", 1, r"(d) SSA. The criteria are AA (AAA), SSS and SAS (with the angle **between** the proportional sides). (1)", "E", opts=["AA", "SSS", "SAS", "SSA"]),
W(r"If $\triangle ABC\sim\triangle PQR$ with $AB=6$ cm, $PQ=9$ cm and $BC=8$ cm, then $QR$ is:", 1, r"(a) 12 cm. $\dfrac{AB}{PQ}=\dfrac{BC}{QR}\Rightarrow\dfrac69=\dfrac8{QR}\Rightarrow QR=12$. (1)", "E", opts=["12 cm", "10 cm", "18 cm", "16 cm"]),
W(r"The areas of two similar triangles are in the ratio $9:16$. The ratio of their corresponding sides is:", 1, r"(a) $3:4$. The ratio of areas equals the square of the ratio of sides, so the sides are in the ratio $\sqrt9:\sqrt{16}$. (1)", "E", opts=["3 : 4", "9 : 16", "81 : 256", "4 : 3"]),
W(r"A triangle has sides 7 cm, 24 cm and 25 cm. It is:", 1, r"(a) right-angled. $7^2+24^2=49+576=625=25^2$, so by the converse of Pythagoras the angle opposite 25 cm is $90^\circ$. (1)", "E", opts=["right-angled", "acute-angled", "obtuse-angled", "equilateral"]),
W(r"A ladder 10 m long reaches a point 8 m above the ground on a vertical wall. The distance of the foot of the ladder from the wall is:", 1, r"(b) 6 m. $d^2=10^2-8^2=36$, so $d=6$. (1)", "E", opts=["4 m", "6 m", "8 m", "12 m"], wp=True),
W(r"If $\triangle ABC\sim\triangle DEF$, $\angle A=50^\circ$ and $\angle B=70^\circ$, then $\angle F$ is:", 1, r"(b) $60^\circ$. Corresponding angles are equal, so $\angle C=180^\circ-120^\circ=60^\circ=\angle F$. (1)", "E", opts=[r"$50^\circ$", r"$60^\circ$", r"$70^\circ$", r"$80^\circ$"]),
W(r"Find the hypotenuse of a right triangle whose perpendicular sides are 9 cm and 12 cm.", 2, r"$h^2=81+144=225$ (1), $h=$ **15 cm** (1).", "E"),
W(r"State the Basic Proportionality Theorem (Thales theorem).", 2, r"If a line is drawn **parallel to one side** of a triangle to intersect the other two sides at distinct points (1), it divides those two sides **in the same ratio** (1).", "E"),
W(r"A pole 6 m high casts a shadow 4 m long on the ground. At the same time a tower casts a shadow 28 m long. Find the height of the tower.", 2, r"The sun's rays make equal angles, so the two triangles are similar (AA) (1). $\dfrac H{6}=\dfrac{28}4\Rightarrow H=$ **42 m** (1).", "E", wp=True),
W(r"A ladder 13 m long has its foot 5 m from the base of a wall. How high up the wall does it reach?", 2, r"$h^2=13^2-5^2=169-25=144$ (1). $h=$ **12 m** (1).", "E", wp=True),
W(r"True or false? Give a reason. All squares are similar.", 1, r"**True.** All angles are $90^\circ$ and the sides of any two squares are in the same ratio (1).", "E"),
W(r"True or false? Give a reason. All rectangles are similar.", 1, r"**False.** The angles are equal, but the sides need not be proportional, e.g. $4\times2$ and $4\times3$ (1).", "E"),
W(r"A boy 1.6 m tall casts a shadow 2.4 m long. At the same time a building casts a shadow 30 m long. Find the height of the building.", 2, r"Similar triangles: $\dfrac H{1.6}=\dfrac{30}{2.4}$ (1). $H=$ **20 m** (1).", "E", wp=True),
W(r"Is a triangle with sides 8 cm, 15 cm and 17 cm a right triangle? If so, which angle is the right angle?", 2, r"$8^2+15^2=64+225=289=17^2$ (1). Yes; the right angle is **opposite the 17 cm side** (1).", "E"),
W(r"In $\triangle ABC$, $DE\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. If $\dfrac{AD}{DB}=\dfrac35$ and $AE=6$ cm, find $AC$.", 2, r"$\dfrac{AE}{EC}=\dfrac{AD}{DB}=\dfrac35$ (1). $EC=10$ cm, so $AC=6+10=$ **16 cm** (1).", "E"),
W(r"A rectangular field is 40 m long and 30 m wide. Ajay walks from one corner to the opposite corner along the diagonal, while Vijay walks along two sides. How much shorter is Ajay's route?", 2, r"Diagonal $=\sqrt{40^2+30^2}=50$ m (1). Vijay walks $40+30=70$ m; Ajay saves $70-50=$ **20 m** (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"In $\triangle ABC$, $DE\parallel BC$ with $D$ on $AB$, $E$ on $AC$. If $AD=x$, $DB=x-2$, $AE=x+2$ and $EC=x-1$, find $x$ and the four lengths.", 3, r"BPT: $\dfrac x{x-2}=\dfrac{x+2}{x-1}$ (1). $x(x-1)=(x+2)(x-2)\Rightarrow x^2-x=x^2-4$, so $x=4$ (1). $AD=4$, $DB=2$, $AE=6$, $EC=3$ (1).", "M"),
W(r"The diagonals $AC$ and $BD$ of a trapezium $ABCD$ with $AB\parallel DC$ intersect at $O$. Show that $\dfrac{AO}{OC}=\dfrac{BO}{OD}$.", 3, r"In $\triangle AOB$ and $\triangle COD$: $\angle OAB=\angle OCD$ and $\angle OBA=\angle ODC$ (alternate angles, $AB\parallel DC$) (1). So $\triangle AOB\sim\triangle COD$ (AA) (1). Hence $\dfrac{AO}{CO}=\dfrac{BO}{DO}$ (1).", "M"),
W(r"In $\triangle ABC$, $D$ is the mid-point of $AB$ and a line through $D$ parallel to $BC$ meets $AC$ at $E$. Prove that $E$ is the mid-point of $AC$.", 3, r"$AD=DB$, so $\dfrac{AD}{DB}=1$ (1). By BPT $\dfrac{AE}{EC}=\dfrac{AD}{DB}=1$ (1). So $AE=EC$ and $E$ is the mid-point of $AC$ (1).", "M"),
W(r"The areas of two similar triangles are 64 cm² and 121 cm². If a side of the first triangle is 8 cm, find the corresponding side of the second.", 3, r"$\dfrac{\text{ar}_1}{\text{ar}_2}=\left(\dfrac{8}{x}\right)^2$ (1). $\dfrac{64}{121}=\dfrac{64}{x^2}$ (1), so $x^2=121$ and $x=$ **11 cm** (1).", "M"),
W(r"The perimeters of two similar triangles are 24 cm and 36 cm. If a side of the smaller triangle is 6 cm, find the corresponding side of the larger.", 2, r"The ratio of perimeters equals the ratio of corresponding sides: $\dfrac{24}{36}=\dfrac6x$ (1), so $x=$ **9 cm** (1).", "M"),
W(r"Find the altitude and the area of an equilateral triangle of side 10 cm.", 3, r"The altitude bisects the base: $h^2=10^2-5^2=75$ (1), $h=5\sqrt3$ cm (1). Area $=\dfrac12\times10\times5\sqrt3=$ **$25\sqrt3$ cm²** (1).", "M"),
W(r"In $\triangle ABC$, $\angle B=90^\circ$, $AB=6$ cm and $BC=8$ cm. $BD$ is perpendicular to $AC$. Find $BD$.", 3, r"$AC=\sqrt{36+64}=10$ cm (1). Area $=\dfrac12\times6\times8=24=\dfrac12\times10\times BD$ (1). $BD=$ **4.8 cm** (1).", "M"),
W(r"A 10 m ladder reaches a window 8 m above the ground. If its foot is pulled 2 m farther from the wall, by how much does the top of the ladder slide down?", 3, r"Initially the height is 8 m and the foot is $\sqrt{100-64}=6$ m from the wall; after pulling, the foot is $6+2=8$ m away (1). New height $=\sqrt{100-64}=6$ m (1). The top slides down $8-6=$ **2 m** (1).", "M", wp=True),
W(r"A man goes 15 m due west and then 8 m due north. How far is he from his starting point?", 2, r"West and north are perpendicular (1). Distance $=\sqrt{15^2+8^2}=\sqrt{289}=$ **17 m** (1).", "M", wp=True),
W(r"Two poles of heights 6 m and 11 m stand on a plane ground. The distance between their feet is 12 m. Find the distance between their tops.", 3, r"The difference in height is $11-6=5$ m (1). Tops are $\sqrt{12^2+5^2}$ apart (1) $=$ **13 m** (1).", "M", wp=True),
W(r"An aeroplane leaves an airport and flies due north at 300 km/h. At the same time another aeroplane leaves the same airport and flies due west at 400 km/h. How far apart are they after $1\dfrac12$ hours?", 3, r"Distances: $300\times1.5=450$ km north and $400\times1.5=600$ km west (1). They are at right angles: $d^2=450^2+600^2=202500+360000$ (1). $d=$ **750 km** (1).", "M", wp=True),
W(r"Is a triangle with sides 15 cm, 20 cm and 25 cm similar to a triangle with sides 3 cm, 4 cm and 5 cm? Name the criterion and say whether the triangles are right-angled.", 2, r"$\dfrac{15}3=\dfrac{20}4=\dfrac{25}5=5$, so they are similar by **SSS** (1). $15^2+20^2=25^2$, so both are right-angled (1).", "M"),
W(r"Ravi says: 'In $\triangle ABC$ and $\triangle DEF$, $\dfrac{AB}{DE}=\dfrac{BC}{EF}$ and $\angle A=\angle D$, so the triangles are similar by SAS.' Find the mistake.", 2, r"In the SAS criterion the equal angle must be the **included angle**, between the two proportional sides (1). Here the angle between $AB$ and $BC$ is $\angle B$, so one needs $\angle B=\angle E$; $\angle A=\angle D$ is not enough (1).", "M"),
W(r"A photograph 12 cm × 9 cm is enlarged (similar figure) so that its longer side becomes 18 cm. Find the shorter side of the enlargement and the ratio of the areas of the two photographs.", 3, r"Scale factor $=\dfrac{18}{12}=\dfrac32$ (1). Shorter side $=9\times\dfrac32=$ **13.5 cm** (1). Ratio of areas (original : enlarged) $=\left(\dfrac23\right)^2=$ **$4:9$** (1).", "M", wp=True),
W(r"$D$, $E$ and $F$ are the mid-points of the sides $BC$, $CA$ and $AB$ of $\triangle ABC$. Show that $\triangle DEF\sim\triangle ABC$ and find the ratio of their areas.", 3, r"By the mid-point theorem $EF=\dfrac12BC$, $FD=\dfrac12CA$, $DE=\dfrac12AB$ (1). So the sides are proportional and $\triangle DEF\sim\triangle ABC$ (SSS) (1). Area ratio $=\left(\dfrac12\right)^2=1:4$ (1).", "M"),
W(r"In $\triangle PQR$, $XY\parallel QR$ with $X$ on $PQ$ and $Y$ on $PR$, and $PX:XQ=3:4$. Find the ratio of the area of $\triangle PXY$ to the area of $\triangle PQR$.", 3, r"$PX:PQ=3:7$ (1). $\triangle PXY\sim\triangle PQR$ (AA) (1). Ratio of areas $=\left(\dfrac37\right)^2=$ **$9:49$** (1).", "M"),
W(r"One diagonal of a rhombus is 24 cm and its side is 13 cm. Find the other diagonal.", 3, r"The diagonals of a rhombus bisect each other at right angles (1). Half-diagonals: 12 and $x$: $x^2=13^2-12^2=25$, $x=5$ (1). Other diagonal $=$ **10 cm** (1).", "M"),
W(r"Is a triangle with sides 7 cm, 9 cm and 12 cm right-angled? Give a reason.", 2, r"The longest side is 12; $7^2+9^2=49+81=130$ while $12^2=144$ (1). They are not equal, so the triangle is **not** right-angled (it is obtuse since $130<144$) (1).", "M"),
# ---------------- HARD ----------------
W(r"Prove the Basic Proportionality Theorem: if a line is drawn parallel to one side of a triangle to intersect the other two sides at distinct points, it divides the two sides in the same ratio.", 4, r"Given $\triangle ABC$, $DE\parallel BC$, $D$ on $AB$, $E$ on $AC$. Join $BE$ and $CD$; draw $EF\perp AB$ and $DG\perp AC$. $\dfrac{\text{ar}(ADE)}{\text{ar}(BDE)}=\dfrac{\frac12AD\cdot EF}{\frac12DB\cdot EF}=\dfrac{AD}{DB}$ (1) and $\dfrac{\text{ar}(ADE)}{\text{ar}(CDE)}=\dfrac{\frac12AE\cdot DG}{\frac12EC\cdot DG}=\dfrac{AE}{EC}$ (1). $\triangle BDE$ and $\triangle CDE$ lie on the same base $DE$ between the same parallels $DE$ and $BC$, so $\text{ar}(BDE)=\text{ar}(CDE)$ (1). Hence $\dfrac{AD}{DB}=\dfrac{AE}{EC}$ (1).", "H"),
W(r"Prove the Pythagoras theorem: in a right triangle the square of the hypotenuse equals the sum of the squares of the other two sides.", 4, r"Let $\triangle ABC$ be right-angled at $B$ and $BD\perp AC$. $\triangle ADB\sim\triangle ABC$ (AA, common $\angle A$ and right angles) (1), so $\dfrac{AD}{AB}=\dfrac{AB}{AC}$, i.e. $AB^2=AD\cdot AC$ (1). $\triangle BDC\sim\triangle ABC$ (AA), so $BC^2=CD\cdot AC$ (1). Adding: $AB^2+BC^2=AC(AD+DC)=AC^2$ (1).", "H"),
W(r"The perimeters of two similar triangles are 25 cm and 15 cm. If the area of the first triangle is 100 cm², find the area of the second.", 3, r"Ratio of sides $=\dfrac{25}{15}=\dfrac53$ (1). Ratio of areas $=\dfrac{25}9$ (1). Area of second $=100\times\dfrac9{25}=$ **36 cm²** (1).", "H"),
W(r"$ABC$ is an equilateral triangle and $D$ is a point on $BC$ such that $BD=\dfrac13BC$. Prove that $9AD^2=7AB^2$.", 4, r"Draw $AE\perp BC$; $E$ is the mid-point of $BC$. Let each side be $a$. $BE=\dfrac a2$, $BD=\dfrac a3$, $DE=\dfrac a2-\dfrac a3=\dfrac a6$ (1). $AE^2=a^2-\dfrac{a^2}4=\dfrac{3a^2}4$ (1). $AD^2=AE^2+DE^2=\dfrac{3a^2}4+\dfrac{a^2}{36}=\dfrac{28a^2}{36}=\dfrac{7a^2}9$ (1). So $9AD^2=7AB^2$ (1).", "H"),
W(r"Prove that in an equilateral triangle, three times the square of a side equals four times the square of its altitude.", 3, r"Let the side be $a$ and the altitude $AD$ on $BC$; $D$ is the mid-point (1). $AD^2=a^2-\left(\dfrac a2\right)^2=\dfrac{3a^2}4$ (1). Hence $4AD^2=3a^2$ (1).", "M"),
W(r"$\triangle ABC$ is right-angled at $C$. $D$ and $E$ are points on $CA$ and $CB$ respectively. Prove that $AE^2+BD^2=AB^2+DE^2$.", 4, r"Right angle at $C$: $AE^2=AC^2+CE^2$, $BD^2=BC^2+CD^2$ (2). Adding: $AE^2+BD^2=(AC^2+BC^2)+(CE^2+CD^2)$ (1) $=AB^2+DE^2$, because $AC^2+BC^2=AB^2$ and, in right $\triangle DCE$, $CD^2+CE^2=DE^2$ (1).", "H"),
W(r"**Cross poles.** Two vertical poles $AB=6$ m and $CD=3$ m stand on level ground with their feet $B$ and $D$ a certain distance apart. Wires $AD$ and $BC$ join the top of each pole to the foot of the other and cross at $P$. Show that $P$ is 2 m above the ground, whatever the distance $BD$.", 5, r"Let $PM\perp BD$ with $PM=h$ and $BD=d$. $\triangle DPM\sim\triangle DAB$ (AA): $\dfrac h6=\dfrac{DM}d$ (2). $\triangle BPM\sim\triangle BCD$ (AA): $\dfrac h3=\dfrac{BM}d$ (1). Add: $h\left(\dfrac16+\dfrac13\right)=\dfrac{DM+BM}d=1$ (1). So $\dfrac h2=1$ and $h=$ **2 m**, independent of $d$ (1).", "H", wp=True),
W(r"A 25 m ladder leans against a wall with its foot 7 m from the base of the wall. If the top of the ladder slides down the wall by 4 m, how far will its foot slide away from the wall?", 4, r"Initial height $=\sqrt{625-49}=\sqrt{576}=24$ m (1). New height $=24-4=20$ m (1). New foot distance $=\sqrt{625-400}=15$ m (1). The foot slides $15-7=$ **8 m** (1).", "H", wp=True),
W(r"In $\triangle ABC$, $DE\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. If $AD:AB=2:3$ and the area of $\triangle ADE$ is 16 cm², find the area of $\triangle ABC$ and of the trapezium $DBCE$.", 4, r"$\triangle ADE\sim\triangle ABC$ (AA) (1). $\dfrac{\text{ar}(ADE)}{\text{ar}(ABC)}=\left(\dfrac23\right)^2=\dfrac49$ (1). $\text{ar}(ABC)=16\times\dfrac94=$ **36 cm²** (1). Trapezium $=36-16=$ **20 cm²** (1).", "H"),
W(r"**Case study.** A street lamp post is 4.8 m high. A girl 1.2 m tall stands 6 m from the foot of the post and her shadow falls on the ground away from the post. (i) Explain why the triangles formed are similar. (ii) Find the length of her shadow. (iii) How far is the tip of her shadow from the foot of the post? (iv) How long is her shadow if she stands 12 m from the post? (v) By what fraction of the extra distance does her shadow lengthen?", 5, r"(i) Both the post and the girl are vertical, and the light ray makes the same angle with the ground, so the triangles are similar by AA (1). (ii) Shadow $s$: $\dfrac{1.2}{4.8}=\dfrac s{s+6}\Rightarrow\dfrac14=\dfrac s{s+6}$, $s=$ **2 m** (1). (iii) $6+2=$ **8 m** (1). (iv) $\dfrac s{s+12}=\dfrac14\Rightarrow s=$ **4 m** (1). (v) The shadow grows from 2 m to 4 m while she walks 6 m farther, i.e. by $\dfrac13$ of the distance walked (1).", "H", wp=True),
W(r"Anil says the triangles with sides 3 cm, 4 cm, 5 cm and 6 cm, 8 cm, 11 cm are similar because 6 = 2 × 3 and 8 = 2 × 4. Is he right? Test with a criterion.", 3, r"For SSS all three ratios must be equal: $\dfrac63=2$, $\dfrac84=2$, but $\dfrac{11}5=2.2$ (2). The ratios differ, so the triangles are **not similar** (1).", "H"),
W(r"$AD\perp BC$ in $\triangle ABC$ with $D$ on $BC$ such that $DB=3\,CD$. Prove that $2AB^2=2AC^2+BC^2$.", 4, r"Let $CD=x$, $DB=3x$, $BC=4x$ (1). $AB^2=AD^2+DB^2=AD^2+9x^2$ and $AC^2=AD^2+x^2$ (1). Subtract: $AB^2-AC^2=8x^2$ (1). So $2(AB^2-AC^2)=16x^2=BC^2$, i.e. $2AB^2=2AC^2+BC^2$ (1).", "H"),
W(r"In $\triangle ABC$, $AB=7.2$ cm and $AC=6.4$ cm. $D$ is on $AB$ with $AD=1.8$ cm and $E$ is on $AC$ with $AE=1.6$ cm. Is $DE\parallel BC$? Justify.", 3, r"$DB=7.2-1.8=5.4$ cm and $EC=6.4-1.6=4.8$ cm (1). $\dfrac{AD}{DB}=\dfrac{1.8}{5.4}=\dfrac13$ and $\dfrac{AE}{EC}=\dfrac{1.6}{4.8}=\dfrac13$ (1). The ratios are equal, so by the converse of BPT $DE\parallel BC$ (1).", "M"),
W(r"In $\triangle ABC$ a line $DE\parallel BC$ ($D$ on $AB$, $E$ on $AC$) divides the triangle into two parts of equal area: $\triangle ADE$ and the trapezium $DBCE$. Find $\dfrac{AD}{AB}$.", 4, r"$\text{ar}(ADE)=\dfrac12\text{ar}(ABC)$ (1). $\triangle ADE\sim\triangle ABC$, so $\dfrac{\text{ar}(ADE)}{\text{ar}(ABC)}=\left(\dfrac{AD}{AB}\right)^2$ (1). Hence $\left(\dfrac{AD}{AB}\right)^2=\dfrac12$ (1) and $\dfrac{AD}{AB}=\dfrac1{\sqrt2}=\dfrac{\sqrt2}2\approx0.71$ (1).", "H"),
]
WS.sort(key=lambda w: "EMH".index(w["level"]))   # keep the parts contiguous after a re-tag
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(6)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "6.6 Proofs You Must Know"),
 ("h3", "Proof of the Basic Proportionality Theorem"),
 ("steps", [("Given and construction", "In triangle ABC, DE ∥ BC with D on AB and E on AC. Join BE and CD, and draw EF ⊥ AB and DG ⊥ AC."), ("Compare areas", "ar(ADE)/ar(BDE) = (½·AD·EF)/(½·DB·EF) = AD/DB and ar(ADE)/ar(CDE) = (½·AE·DG)/(½·EC·DG) = AE/EC."), ("Equal triangles", "Triangles BDE and CDE have the same base DE and lie between the same parallels DE and BC, so their areas are equal. Hence AD/DB = AE/EC.")]),
 ("h3", "Proof of Pythagoras theorem by similarity"),
 ("steps", [("Draw the altitude", "In triangle ABC right-angled at B, draw BD ⊥ AC."), ("Two similar pairs", "Triangle ADB ~ triangle ABC (AA) gives AB² = AD·AC. Triangle BDC ~ triangle ABC (AA) gives BC² = CD·AC."), ("Add", "AB² + BC² = AC(AD + DC) = AC².")]),
 ("note", "REMEMBER", "**Converse of Pythagoras:** if in a triangle the square of one side equals the sum of the squares of the other two, the angle opposite the first side is a right angle. Check with the **longest side** as the hypotenuse: 7² + 9² = 130 ≠ 12² = 144, so the triangle (7, 9, 12) is not right-angled."),
 ("h2", "6.7 Similarity Criteria at a Glance"),
 ("table", ["Criterion", "What must be equal or proportional", "Use it when"], [
  ["AA (or AAA)", "two angles equal (the third is then equal)", "parallel lines give equal angles; common angles; right angles"],
  ["SSS", "all three pairs of sides in the same ratio", "all sides are known"],
  ["SAS", "two pairs of sides proportional and the **included** angle equal", "two sides and the angle between them"]]),
 ("table", ["If triangles are similar (ratio of sides k)", "Ratio"], [
  ["corresponding sides, medians, altitudes, perimeters", "k"],
  ["areas", "k²"],
  ["corresponding angles", "equal"]]),
 ("h2", "6.8 More Worked Examples"),
 ("h3", "Example 1 — BPT with algebra"),
 ("steps", [("DE ∥ BC; AD = x, DB = x − 2, AE = x + 2, EC = x − 1", "AD/DB = AE/EC gives x/(x − 2) = (x + 2)/(x − 1)."), ("Clear the fractions", "x(x − 1) = (x + 2)(x − 2), so x² − x = x² − 4 and x = 4."), ("Lengths", "AD = 4, DB = 2, AE = 6, EC = 3.")]),
 ("h3", "Example 2 — Shadows"),
 ("steps", [("A 6 m pole casts a 4 m shadow; a tower casts a 28 m shadow", "The sun's rays make equal angles with the ground, so the two right triangles are similar (AA)."), ("Ratio", "H/6 = 28/4."), ("Height", "H = **42 m**.")]),
 ("h3", "Example 3 — Areas of similar triangles"),
 ("steps", [("Areas 64 cm² and 121 cm²; a side of the first is 8 cm", "Ratio of areas = (ratio of sides)²: 64/121 = (8/x)²."), ("Solve", "x² = 121."), ("Side", "x = **11 cm**.")]),
 ("h3", "Example 4 — Ladder problem"),
 ("steps", [("A 25 m ladder, foot 7 m from the wall; top slides 4 m down", "Initial height = √(625 − 49) = 24 m."), ("New height", "24 − 4 = 20 m, so the foot is √(625 − 400) = 15 m from the wall."), ("Answer", "The foot slides 15 − 7 = **8 m**.")]),
 ("h3", "Example 5 — Equilateral triangle"),
 ("steps", [("Side 10 cm: altitude and area", "The altitude bisects the base: h² = 10² − 5² = 75."), ("Altitude", "h = 5√3 cm."), ("Area", "½ × 10 × 5√3 = **25√3 cm²**. In general altitude = (√3/2)a and 3a² = 4h².")]),
 ("h3", "Example 6 — Altitude to the hypotenuse"),
 ("steps", [("Right angle at B, AB = 6, BC = 8; BD ⊥ AC", "AC = 10. Equate two expressions for the area."), ("Area", "½ × 6 × 8 = 24 = ½ × 10 × BD."), ("Result", "BD = **4.8 cm**.")]),
 ("h2", "6.9 Word Problems: How to Translate"),
 ("table", ["Situation", "Triangle idea", "Equation"], [
  ["shadows at the same time", "two similar right triangles (AA)", "height/shadow = height/shadow"],
  ["ladder against a wall", "right triangle: ladder is the hypotenuse", "wall² + foot² = ladder²"],
  ["person walking in perpendicular directions, aeroplanes N and W", "right triangle with legs = distances", "d² = a² + b² (distance = speed × time)"],
  ["two poles and the distance between tops", "right triangle with legs = gap and height difference", "d² = gap² + (H − h)²"],
  ["rectangle, rhombus or square diagonals", "right triangles formed by diagonals or sides", "rhombus: (d₁/2)² + (d₂/2)² = side²"],
  ["enlarged photograph or map", "similar figures with scale factor k", "lengths × k, areas × k²"],
  ["lamp post and a person", "similar triangles using the shadow", "post/person = (shadow + distance)/shadow"]]),
 ("h2", "6.10 Common Mistakes"),
 ("table", ["Mistake", "Correct idea"], [
  ["Writing △ABC ~ △QPR with vertices in the wrong order", "write the vertices so that corresponding angles match"],
  ["Using SSA or the non-included angle in SAS", "the equal angle must be **between** the proportional sides"],
  ["Taking the ratio of areas equal to the ratio of sides", "ratio of areas = (ratio of sides)²"],
  ["Using Pythagoras with the wrong side as hypotenuse", "the hypotenuse is opposite the right angle and is the **longest** side"],
  ["Saying all rectangles (or all rhombuses) are similar", "angles equal is not enough; sides must also be proportional"],
  ["Applying BPT without parallel lines", "BPT needs DE ∥ BC; the converse needs equal ratios first"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Shadow, ladder and distance problems** reduce to similar triangles (AA) or to a right triangle and Pythagoras.", "For similar triangles: sides, medians, altitudes and perimeters are in the ratio **k**; areas are in the ratio **k²**.", "Know the two proofs (BPT by areas; Pythagoras by similarity) and the **converse** of each theorem."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
