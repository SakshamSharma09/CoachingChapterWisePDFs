"""Class 9 Science Ch 8 Sound Waves: Characteristics and Applications - extras."""
from common import AR4, Q

AR = [
 AR4("Sound cannot travel through a vacuum.", "Sound is a mechanical wave and needs a material medium for its propagation.", "a",
     "With no particles to vibrate, no compressions and rarefactions can form."),
 AR4("Sound waves in air are longitudinal waves.", "The speed of sound is greater in solids than in gases.", "b",
     "Both are true statements but R does not explain A."),
 AR4("The pitch of a sound depends on its frequency.", "A sound of higher pitch has a larger amplitude.", "c",
     "A is true; loudness depends on amplitude, pitch on frequency, so R is false."),
 AR4("Sound travels faster in air than in steel.", "The particles in a solid are closer together and the restoring forces between them are stronger.", "d",
     "Sound is faster in steel than in air, so A is false; R is true."),
 AR4("A distinct echo is heard only if the reflecting surface is at least about 17 m away.", "The ear retains a sound sensation for about 0.1 s, so the reflected sound must reach the ear at least 0.1 s after the original.", "a",
     "Distance $=\\tfrac12\\times340\\times0.1=17$ m."),
 AR4("SONAR uses ultrasonic waves to find the depth of the sea.", "Ultrasonic waves have frequencies above 20 000 Hz.", "b",
     "Both are true; the frequency range defines ultrasound but is not the reason the echo method gives depth."),
]

CASE = [
 Q("<b>Case study.</b> A research ship in the Arabian Sea sends an ultrasonic pulse downward from its SONAR and receives the echo from the sea bed after 0.8 s. The speed of sound in sea water is 1500 m/s. "
   "(i) Expand the term SONAR. (ii) Find the total distance travelled by the pulse. (iii) Find the depth of the sea. (iv) Find the depth at another spot where the echo returns after 1.2 s, and state one reason for using ultrasound in SONAR.",
   r"(i) Sound Navigation And Ranging (1). (ii) $1500\times0.8=1200$ m (1). (iii) Depth $=1200/2=600$ m (1). (iv) Depth $=1500\times1.2/2=900$ m (1); ultrasound travels as a narrow beam over long distances and is not audible to humans or disturbing to sea life (any one reason) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A music teacher strikes a tuning fork of frequency 500 Hz. The sound waves produced have a wavelength of 0.68 m in the air of the classroom. "
   "(i) Find the time period of the vibration. (ii) Find the speed of sound in the room. (iii) Is the sound audible to a normal human ear? (iv) The teacher now uses a fork of 1000 Hz. Find the wavelength, assuming the speed is unchanged, and state how the pitch changes.",
   r"(i) $T=\dfrac1f=\dfrac1{500}=0.002$ s (1). (ii) $v=f\lambda=500\times0.68=340$ m/s (1). (iii) Yes, since 500 Hz lies within the audible range 20 Hz to 20 000 Hz (1). (iv) $\lambda=v/f=340/1000=0.34$ m (1); the pitch becomes higher because the frequency is higher (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A dog trainer in Ludhiana uses a whistle that produces sound of frequency 25 000 Hz. The dog responds immediately, but the people standing nearby hear nothing. Take the speed of sound in air as 340 m/s. "
   "(i) Classify the sound of the whistle as infrasonic, audible or ultrasonic. (ii) Why can the people not hear it? (iii) Find its wavelength in air. (iv) Name two uses of ultrasound.",
   r"(i) Ultrasonic (1). (ii) Its frequency is above the upper limit of human hearing, 20 000 Hz (1). (iii) $\lambda=\dfrac vf=\dfrac{340}{25000}=0.0136$ m (1.36 cm) (1). (iv) Any two: SONAR, detecting flaws in metal castings, ultrasound scanning in medicine, cleaning delicate parts (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Wave nature of sound", ["Sound is produced by vibrating bodies and needs a material medium; it cannot travel through a vacuum.",
   "In air it is a longitudinal wave: compressions (high pressure) and rarefactions (low pressure) travel along the direction of propagation.",
   "Wavelength $\\lambda$: distance between two consecutive compressions (or rarefactions); amplitude: maximum displacement of particles."]),
 ("Wave relations", ["Frequency $f$ (Hz) $=$ number of vibrations per second; time period $T=\\dfrac1f$ (s).",
   "Wave speed $v=f\\lambda$ (m/s).",
   "Speed of sound: solids $>$ liquids $>$ gases (about 340 m/s in air at room temperature, 1500 m/s in sea water); it increases with temperature in a medium."]),
 ("Characteristics of sound", ["Pitch is determined by frequency (higher frequency, higher pitch); loudness by amplitude (larger amplitude, louder sound); quality (timbre) distinguishes sounds of the same pitch and loudness.",
   "Intensity is the energy passing per second per unit area; the loudness level is measured in decibel (dB)."]),
 ("Audible range and echo", ["Audible range for humans: 20 Hz to 20 000 Hz; infrasound $<20$ Hz; ultrasound $>20\\,000$ Hz.",
   "Echo: reflection of sound. For a distinct echo the time gap must be at least $0.1$ s, so the distance of the reflector is at least $\\dfrac{v\\times0.1}{2}\\approx17$ m.",
   "Depth or distance by echo: $d=\\dfrac{v\\,t}{2}$, where $t$ is the time between sending and receiving the sound."]),
 ("Applications", ["SONAR (Sound Navigation And Ranging): depth of sea, submarines, shoals of fish. Ultrasound: flaw detection, medical scans, cleaning. Echolocation: bats, dolphins.",
   "Reverberation and noise: excessive loud sound (about 120 dB and above) can damage hearing; reduce by sound-absorbing materials."]),
]

MISTAKES = [
 "Forgetting to halve the total distance in echo and SONAR problems: the sound goes to the obstacle <i>and back</i>, so $d=vt/2$.",
 "Mixing up pitch and loudness: pitch depends on frequency, loudness on amplitude.",
 "Drawing sound as a transverse wave or saying that the particles travel with the wave; in air the particles vibrate to and fro along the direction of travel.",
 "Saying that sound travels fastest in air and slowest in solids; the order is solids $>$ liquids $>$ gases.",
 "Writing the audible range as 20 kHz to 20 Hz, or calling a sound of 25 kHz infrasonic.",
 "Applying $v=f\\lambda$ with wavelength in cm or frequency in kHz without converting to m and Hz, or saying that the speed of a wave changes when only the frequency is changed in the same medium.",
]
