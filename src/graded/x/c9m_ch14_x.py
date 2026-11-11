"""Class 9 Maths Ch 14 Surface Area and Volume - extras."""
from common import AR4, Q

AR = [
 AR4(r"The volume of a cube of side 5 cm is 125 cm$^3$.", r"The volume of a cube of side $a$ is $a^3$.", "a",
     r"$5^3=125$, using R."),
 AR4(r"The total surface area of a cube of side 4 cm is 96 cm$^2$.", r"The lateral surface area of a cube of side $a$ is $4a^2$.", "b",
     r"TSA $=6a^2=96$, so A is true; R is true but the TSA is $6a^2$, so R does not explain A."),
 AR4(r"The curved surface area of a cylinder is $2\pi rh$.", r"The total surface area of a cylinder is $2\pi rh+\pi r^2$.", "c",
     r"A is correct. R is false because the TSA is $2\pi rh+2\pi r^2=2\pi r(r+h)$ (two circular ends)."),
 AR4(r"The volume of a cone of base radius $r$ and height $h$ is $\pi r^2h$.", r"The volume of a cone is one-third of the volume of a cylinder with the same base and height.", "d",
     r"A is false because the volume of a cone is $\tfrac13\pi r^2h$; R is true."),
 AR4(r"The volume of a sphere of radius 7 cm is $\dfrac{4312}{3}$ cm$^3$ (take $\pi=\frac{22}{7}$).", r"The volume of a sphere of radius $r$ is $\dfrac43\pi r^3$.", "a",
     r"$\dfrac43\times\dfrac{22}{7}\times343=\dfrac{4312}{3}$, using R."),
 AR4(r"When a metal sphere is melted and recast into a cylinder, the volume of the metal stays the same.", r"The surface area of a sphere of radius $r$ is $4\pi r^2$.", "b",
     r"Melting does not change the amount of metal, so A is true; R is a true formula but is not the reason for A."),
]

CASE = [
 Q(r"<b>Case study.</b> A school in Surat has a water tank in the shape of a cuboid, 5 m long, 4 m wide and 3 m deep, with an open top. "
   r"(i) Find the volume of the tank. (ii) Find the capacity of the tank in litres. (iii) Find the total surface area of the closed cuboid of the same size. (iv) Find the area of the inner surface of the open tank to be painted, and the cost at Rs 15 per m$^2$.",
   r"(i) $5\times4\times3=60$ m$^3$ (1). (ii) $60\times1000=60000$ litres (1). (iii) $2(20+12+15)=94$ m$^2$ (1). (iv) Open tank: $94-20=74$ m$^2$ (1); cost $=74\times15=$ Rs 1110 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A cylindrical water bottle has a base radius of 7 cm and a height of 20 cm. Take $\pi=\dfrac{22}{7}$. "
   r"(i) Find its volume. (ii) Find its curved surface area. (iii) Find its total surface area. (iv) How many such bottles are needed to fill a bucket of capacity 30.8 litres?",
   r"(i) $\frac{22}{7}\times49\times20=3080$ cm$^3$ (1). (ii) $2\times\frac{22}{7}\times7\times20=880$ cm$^2$ (1). (iii) $880+2\times154=1188$ cm$^2$ (1). (iv) $30.8$ L $=30800$ cm$^3$ (1); number of bottles $=\dfrac{30800}{3080}=10$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A solid metallic cone has a base radius of 7 cm and a vertical height of 24 cm. Take $\pi=\dfrac{22}{7}$. "
   r"(i) Find its slant height. (ii) Find its curved surface area. (iii) Find its volume. (iv) The cone is melted and recast into a solid cylinder of base radius 7 cm. Find the height of the cylinder.",
   r"(i) $l=\sqrt{7^2+24^2}=25$ cm (1). (ii) $\pi rl=\frac{22}{7}\times7\times25=550$ cm$^2$ (1). (iii) $\tfrac13\times\frac{22}{7}\times49\times24=1232$ cm$^3$ (1). (iv) Volume is unchanged: $\frac{22}{7}\times49\times h=1232$ (1), so $h=8$ cm (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Cuboid and cube", [r"Cuboid ($l, b, h$): volume $=lbh$; TSA $=2(lb+bh+hl)$; LSA $=2h(l+b)$; diagonal $=\sqrt{l^2+b^2+h^2}$.",
   r"Cube (side $a$): volume $=a^3$; TSA $=6a^2$; LSA $=4a^2$; diagonal $=a\sqrt3$."]),
 ("Cylinder", [r"Volume $=\pi r^2h$; CSA $=2\pi rh$; TSA $=2\pi r(r+h)$."]),
 ("Cone", [r"Slant height $l=\sqrt{r^2+h^2}$.", r"Volume $=\tfrac13\pi r^2h$; CSA $=\pi rl$; TSA $=\pi r(l+r)$."]),
 ("Sphere and hemisphere", [r"Sphere: volume $=\tfrac43\pi r^3$; surface area $=4\pi r^2$.",
   r"Hemisphere: volume $=\tfrac23\pi r^3$; CSA $=2\pi r^2$; TSA $=3\pi r^2$."]),
 ("Pyramid and recasting", [r"Pyramid: volume $=\tfrac13\times$ (base area) $\times$ height; lateral area $=$ sum of the areas of the triangular faces.",
   r"Recasting (melting one solid into another): volume is unchanged; number of small solids $=\dfrac{\text{volume of large solid}}{\text{volume of one small solid}}$.",
   r"Units: area in cm$^2$ or m$^2$, volume in cm$^3$ or m$^3$; $1\ \text{m}^3=1000$ litres, $1000\ \text{cm}^3=1$ litre."]),
]

MISTAKES = [
 r"Forgetting the factor $\tfrac13$ in the volume of a cone or pyramid.",
 r"Using the vertical height $h$ instead of the slant height $l$ in $\pi rl$ (CSA of a cone).",
 r"Writing the TSA of a cylinder as $2\pi rh+\pi r^2$; there are two circular ends, so it is $2\pi rh+2\pi r^2$.",
 r"Using the diameter as the radius, or leaving $r$ in the formula when the problem gives $d$.",
 r"Mixing units: converting cm$^3$ to litres needs $\div1000$, and m$^3$ to litres needs $\times1000$.",
 r"For a hemisphere, using the sphere formulas without halving the volume, or taking TSA as $2\pi r^2$ and forgetting the flat circle ($3\pi r^2$ in all).",
]
