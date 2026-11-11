"""Class 10 Maths Ch 12 Surface Areas and Volumes - extras (combination of two solids, conversion of solids; pi = 22/7)."""
from common import AR4, Q

AR = [
 AR4(r"The total surface area of a solid hemisphere of radius r is $3\pi r^2$.", r"The total surface area of a solid hemisphere is its curved surface area $2\pi r^2$ plus the area $\pi r^2$ of its flat circular face.", "a",
     r"$2\pi r^2+\pi r^2=3\pi r^2$; R gives the reason."),
 AR4(r"A cone and a cylinder have the same base radius and the same height. The volume of the cone is one-third that of the cylinder.", r"The volume of a cone of base radius r and height h is $\pi r^2h$.", "c",
     r"$\tfrac13\pi r^2h$ against $\pi r^2h$: A is true; the cone volume is $\tfrac13\pi r^2h$, so R is false."),
 AR4(r"When a solid metallic sphere is melted and recast into a cylinder, its surface area remains the same.", r"When a solid is melted and recast, its volume remains the same.", "d",
     r"Volume is conserved, not surface area (e.g. 8 small spheres have twice the surface area of the big one): A false; R true."),
 AR4(r"The slant height of a cone of base radius 6 cm and height 8 cm is 10 cm.", r"The volume of a sphere of radius r is $\tfrac43\pi r^3$.", "b",
     r"$l=\sqrt{36+64}=10$ so A is true; R is also true but has no connection with the slant height."),
 AR4(r"A solid is made by placing a cone on a hemisphere of the same radius. The total surface area of the solid is the sum of the curved surface areas of the cone and the hemisphere.", r"The base of the cone and the flat face of the hemisphere are joined together, so neither is exposed.", "a",
     r"The joined faces are inside the solid and are not counted in the total surface area; R explains why only the two curved surfaces are added."),
 AR4(r"The volume of a sphere of radius 3 cm is $36\pi\ \text{cm}^3$.", r"The surface area of a sphere of radius r is $2\pi r^2$.", "c",
     r"$\tfrac43\pi(27)=36\pi$ so A is true; the surface area is $4\pi r^2$, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A medicine capsule is in the shape of a cylinder with a hemisphere stuck at each end. The radius of the cylinder and of each hemisphere is 3.5 mm and the length of the cylindrical part is 7 mm. (Take $\pi=\tfrac{22}{7}$.) "
   r"(i) Find the curved surface area of the cylindrical part. (ii) Find the surface area of the two hemispherical ends together. (iii) Find the total surface area of the capsule. (iv) Find the total length of the capsule and the volume of the cylindrical part.",
   r"(i) $2\pi rh=2\times\tfrac{22}{7}\times3.5\times7=154\ \text{mm}^2$ (1). (ii) Two hemispheres make a sphere: $4\pi r^2=4\times\tfrac{22}{7}\times12.25=154\ \text{mm}^2$ (1). (iii) $154+154=308\ \text{mm}^2$ (1). (iv) Length $=7+3.5+3.5=14$ mm (1); volume of cylinder $=\tfrac{22}{7}\times12.25\times7=269.5\ \text{mm}^3$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A circus tent is made of a cylindrical lower part topped by a conical roof. The base radius of both parts is 7 m, the cylindrical part is 6 m high and the conical part has a vertical height of 24 m. (Take $\pi=\tfrac{22}{7}$.) "
   r"(i) Find the slant height of the cone. (ii) Find the curved surface area of the cone. (iii) Find the curved surface area of the cylindrical part. (iv) Find the total canvas needed and its cost at ₹ 50 per square metre.",
   r"(i) $l=\sqrt{7^2+24^2}=25$ m (1). (ii) $\pi rl=\tfrac{22}{7}\times7\times25=550\ \text{m}^2$ (1). (iii) $2\pi rh=2\times\tfrac{22}{7}\times7\times6=264\ \text{m}^2$ (1). (iv) Total $=550+264=814\ \text{m}^2$ (1); cost $=814\times50=₹\,40{,}700$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A solid metallic sphere of radius 6 cm is melted and recast. (Leave answers in terms of $\pi$.) "
   r"(i) Find the volume of the sphere. (ii) Find the height of a solid cylindrical rod of radius 4 cm that can be made from it. (iii) How many solid spheres of radius 3 cm can be made from the original sphere? (iv) Compare the total surface area of these small spheres with that of the original sphere.",
   r"(i) $\tfrac43\pi(6)^3=288\pi\ \text{cm}^3$ (1). (ii) $\pi(4)^2h=288\pi\Rightarrow h=18$ cm (1). (iii) $\dfrac{288\pi}{\tfrac43\pi(27)}=\dfrac{288}{36}=8$ spheres (1). (iv) Total surface area of 8 small spheres $=8\times4\pi(9)=288\pi\ \text{cm}^2$ against $4\pi(36)=144\pi\ \text{cm}^2$ for the original, i.e. twice as much; volume is conserved but surface area is not (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Cuboid and cube", [r"Cuboid: $V=lbh$; TSA $=2(lb+bh+hl)$; LSA $=2h(l+b)$; diagonal $=\sqrt{l^2+b^2+h^2}$.",
   r"Cube (side a): $V=a^3$; TSA $=6a^2$; LSA $=4a^2$."]),
 ("Cylinder (radius r, height h)", [r"CSA $=2\pi rh$; TSA $=2\pi r(r+h)$; $V=\pi r^2h$."]),
 ("Cone (radius r, height h, slant height l)", [r"$l=\sqrt{r^2+h^2}$; CSA $=\pi rl$; TSA $=\pi r(l+r)$; $V=\tfrac13\pi r^2h$."]),
 ("Sphere and hemisphere (radius r)", [r"Sphere: SA $=4\pi r^2$; $V=\tfrac43\pi r^3$.",
   r"Hemisphere: CSA $=2\pi r^2$; TSA $=3\pi r^2$; $V=\tfrac23\pi r^3$."]),
 ("Combination of solids", [r"Total surface area of the combined solid = sum of the <b>exposed</b> surfaces only (joined faces are not counted).",
   r"Volume of the combined solid = sum of the volumes of the parts.",
   r"Typical solids: cone on a hemisphere, cylinder with hemispherical ends, cone on a cylinder, hemisphere scooped out of a cylinder (subtract its volume)."]),
 ("Conversion of solids", [r"When a solid is melted and recast, volume is conserved (surface area is not).",
   r"Number of small solids $=\dfrac{\text{volume of big solid}}{\text{volume of one small solid}}$.",
   r"Water flowing through a pipe: volume per unit time $=\pi r^2\times\text{speed}$.",
   r"Use $\pi=\dfrac{22}{7}$ unless told otherwise; keep units consistent (1 m = 100 cm; $1\ \text{m}^3=1000$ litres)."]),
]

MISTAKES = [
 r"Counting the joined faces in the total surface area of a combination of solids (e.g. adding the base of a cone resting on a hemisphere).",
 r"Using the vertical height instead of the <i>slant</i> height in the CSA and TSA of a cone.",
 r"Forgetting the $\tfrac13$ in the volume of a cone or using $2\pi r^2$ for the surface area of a full sphere.",
 r"Assuming surface area stays constant when a solid is melted and recast; only the volume is conserved.",
 r"Mixing units (cm, m, mm) or writing cm instead of cm$^2$/cm$^3$ in the answer.",
 r"Using diameter in place of radius while substituting into a formula.",
]
