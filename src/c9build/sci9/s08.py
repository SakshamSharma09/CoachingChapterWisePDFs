from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").rstrip(".")
def opts(v, u, extra=()):
    v = F(v); c = [v * 2, v / 2, v + 10, v * 4, v / 4, v + 5, v * 3]
    out = []
    for x in list(extra) + c:
        x = F(x)
        if x != v and x > 0 and fm(x) != fm(v) and fm(x) not in out: out.append(fm(x))
    return [f"{o} {u}" for o in out[:3]]
A = []
# frequency from oscillations (3)
for n, t in [(10, 2), (50, 5), (120, 6)]:
    f = F(n, t)
    A.append(M4(f"At a point in a medium, {n} density oscillations occur in {t} s. The frequency of the sound wave is:", f"{fm(f)} Hz", opts(f, "Hz", [F(t, n), n + t]), "oscillations ÷ time"))
# time period (3)
for f in [4, 5, 20]:
    T = F(1, f)
    A.append(M4(f"A sound wave of frequency {f} Hz has a time period of:", f"{fm(T)} s", [f"{fm(x)} s" for x in dict.fromkeys([F(f), F(2, f), F(1, f * 2), F(f * 2)]) if x != T][:3], "T = 1/ν"))
# v = fλ (5)
for f, l in [(500, F(2, 5)), (170, 2), (680, F(1, 2)), (1000, F(34, 100)), (2000, F(17, 100))]:
    v = f * l
    A.append(M4(f"A source of frequency {f} Hz produces waves of wavelength {fm(l)} m in a medium. The speed of the wave is:", f"{fm(v)} m s⁻¹", opts(v, "m s⁻¹", [F(f, 1) / l if l else 0, f + l]), "v = ν λ"))
# wavelength (3)
for v, f in [(340, 170), (340, 680), (1500, 500)]:
    l = F(v, f)
    A.append(M4(f"Sound of frequency {f} Hz travels at {v} m s⁻¹. Its wavelength is:", f"{fm(l)} m", opts(l, "m", [F(f, v), v * f]), "λ = v/ν"))
# echo distance (4)
for t, v in [(0.5, 340), (2, 340), (0.2, 340), (3, 340)]:
    d = F(str(t)) * v / 2
    A.append(M4(f"An echo is heard {t} s after a shout. If the speed of sound is {v} m s⁻¹, the distance of the reflecting surface is:", f"{fm(d)} m", opts(d, "m", [F(str(t)) * v]), "distance = vt/2"))
# sonar depth (3)
for t, v in [(4, 1500), (2, 1530), (5, 1525)]:
    d = F(t * v, 2)
    A.append(M4(f"A sonar signal returns from the ocean floor after {t} s. If the speed in water is {v} m s⁻¹, the depth is:", f"{fm(d)} m", opts(d, "m", [t * v]), "d = vt/2"))
# thunder (2)
for t in [3, 5]:
    d = 340 * t
    A.append(M4(f"Thunder is heard {t} s after lightning is seen. Taking v = 340 m s⁻¹, the lightning is at a distance of:", f"{d} m", opts(d, "m", [d // 2]), "d = v × t"))
A += [
 M4("Sound is produced by:", "vibrating objects", ["steady objects", "light waves", "magnetic fields"], "to and fro motion"),
 M4("Sound cannot travel through:", "vacuum", ["water", "steel", "air"], "needs a medium"),
 M4("Sound waves in air are:", "longitudinal waves", ["transverse waves", "electromagnetic waves", "light waves"], "particles vibrate parallel to propagation"),
 M4("In a sound wave, a region of higher density is called a:", "compression", ["rarefaction", "trough", "crest of a transverse wave"], "particles crowded"),
 M4("The frequency of ultrasonic waves is:", "above 20 kHz", ["below 20 Hz", "between 20 Hz and 20 kHz", "exactly 20 Hz"], "above audible range"),
 M4("Elephants can detect:", "infrasound", ["ultrasound only", "radio waves", "light waves"], "below 20 Hz"),
 M4("The audible range of a human is about:", "20 Hz to 20 000 Hz", ["2 Hz to 200 Hz", "200 Hz to 2000 Hz", "20 kHz to 200 kHz"], "average healthy ear"),
 M4("Loudness of a sound depends mainly on its:", "amplitude", ["frequency", "wavelength", "speed"], "larger amplitude is louder"),
 M4("Pitch of a sound depends mainly on its:", "frequency", ["amplitude", "speed", "intensity"], "high frequency, high pitch"),
 M4("Sound travels fastest in:", "solids", ["liquids", "gases", "vacuum"], "closely packed particles"),
 M4("Loudness is measured in:", "decibel", ["hertz", "metre", "watt"], "dB"),
 M4("The quality of sound that lets us distinguish a sitar from a flute playing the same note is:", "timbre", ["pitch", "amplitude", "echo"], "overtone pattern"),
 M4("The minimum time gap needed to hear an echo separately is:", "0.1 s", ["0.01 s", "1 s", "0.5 s"], "persistence of hearing"),
 M4("Persistence of sound due to multiple reflections is called:", "reverberation", ["echo", "resonance", "pitch"], "gap < 0.05 s"),
 M4("Bats find their prey in the dark by:", "echolocation", ["infrasound", "reverberation", "tone"], "reflected ultrasonic waves"),
 M4("Ultrasound is used for:", "imaging internal organs", ["making loud noises", "detecting colour", "heating food"], "medical imaging"),
 M4("If the frequency of a wave in a medium increases while the speed remains the same, the wavelength:", "decreases", ["increases", "stays the same", "becomes infinite"], "λ = v/ν"),
 M4("The speed of sound in air increases with:", "temperature", ["decrease in temperature", "wavelength only", "frequency"], "331 m/s at 0 °C"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("How is sound produced? Give an example.", "Sound is produced by vibrating objects (1); a plucked rubber band or a tuning fork (1).", "1+1"),
 Q("Why can astronauts not talk directly to each other on a spacewalk?", "There is no medium in space and sound cannot travel in vacuum (2).", "2"),
 Q("Define compression and rarefaction.", "Compression: region of higher density; rarefaction: region of lower density in a medium (1+1).", "1+1"),
 Q("Why is sound called a longitudinal wave?", "The particles of the medium vibrate parallel to the direction of propagation (2).", "2"),
 Q("Define wavelength, frequency and time period of a sound wave.", "λ: distance between two consecutive crests; ν: oscillations per second; T: time for one oscillation (2).", "2"),
 Q("Write the relation between frequency and time period. If ν = 5 Hz, find T.", "T = 1/ν (1); T = 0.2 s (1).", "1+1"),
 Q("State the relation between speed, frequency and wavelength.", "v = ν λ (2).", "2"),
 Q("A wave has a frequency of 200 Hz and a wavelength of 1.7 m. Find its speed.", "v = 200 × 1.7 = 340 m s⁻¹ (2).", "2"),
 Q("Define the amplitude of a sound wave. How is it related to loudness?", "Maximum change in density from the average (1); larger amplitude gives louder sound (1).", "1+1"),
 Q("Distinguish between pitch and loudness.", "Pitch depends on frequency (shrill/deep); loudness depends on amplitude (1+1).", "1+1"),
 Q("Name the three ranges of sound frequencies.", "Infrasonic (< 20 Hz), audible (20 Hz–20 kHz), ultrasonic (> 20 kHz) (2).", "2"),
 Q("What is an echo? What is the minimum condition to hear one?", "Reflected sound heard after the original (1); time gap at least 0.1 s (1).", "1+1"),
 Q("Define reverberation.", "The persistence of sound due to repeated reflections, with gaps less than 0.05 s (2).", "2"),
 Q("Name two uses of ultrasound.", "Imaging organs, breaking kidney stones, cleaning parts, flaw detection (any two) (1+1).", "1+1"),
 Q("What is echolocation? Name two animals using it.", "Locating objects by reflected sound (1); bats and dolphins (1).", "1+1"),
 Q("What does the unit decibel measure? Give two typical values.", "Loudness level (1); normal conversation about 60 dB, firecrackers over 100 dB (1).", "1+1"),
]
C = [
 Q("Describe an activity to show that sound is produced by vibrations.", "Stretch a rubber band over a box and pluck it: vibrations are seen and sound is heard (1.5); when the vibration stops, the sound stops (1.5).", "1½+1½"),
 Q("Describe the bell jar experiment and state the conclusion.", "An electric bell in a jar; air is removed by a pump (1); sound becomes fainter and almost inaudible (1); sound needs a medium (1).", "1+1+1"),
 Q("Explain how sound propagates in air using the piston model.", "The piston compresses and rarefies air in turn (1); the disturbance moves on through collisions (1); particles only oscillate about their mean positions (1).", "1+1+1"),
 Q("Distinguish between longitudinal and transverse waves with one example each.", "Longitudinal: particle vibration parallel to propagation, e.g. sound (1.5); transverse: perpendicular, e.g. light (1.5).", "1½+1½"),
 Q("Explain with the help of a graph the terms crest, trough and wavelength.", "Density against distance curve (1); highest point crest, lowest trough (1); distance between two crests is the wavelength (1).", "1+1+1"),
 Q("If 10 density oscillations occur in 2 s, find the frequency and time period.", "ν = 10/2 = 5 Hz (1.5); T = 1/5 = 0.2 s (1.5).", "1½+1½"),
 Q("Derive v = ν λ.", "Speed = distance/time = λ/T (2); since ν = 1/T, v = ν λ (1).", "2+1"),
 Q("Find the wavelengths for 20 Hz and 20 kHz in air (v = 344 m s⁻¹).", "λ = 344/20 = 17.2 m (1.5); λ = 344/20 000 = 0.0172 m = 1.72 cm (1.5).", "1½+1½"),
 Q("Lightning is seen and thunder is heard 5 s later. Find the distance (v = 340 m s⁻¹).", "Light arrives almost instantly (1); d = 340 × 5 = 1700 m (2).", "1+2"),
 Q("How does the speed of sound vary in solids, liquids and gases? Mention the effect of temperature.", "Fastest in solids, slower in liquids, slowest in gases (2); increases with temperature (1).", "2+1"),
 Q("A person claps in front of a wall and hears an echo after 0.5 s. Find the distance (v = 340 m s⁻¹).", "Sound goes and returns, so d = 340 × 0.5/2 = 85 m (3).", "3"),
 Q("Why is the minimum distance for an echo 17 m?", "Time gap 0.1 s; total distance 340 × 0.1 = 34 m; to and fro, so 17 m (3).", "3"),
 Q("Explain why we hear echoes in a large hall but not in a small room.", "In a small room reflections return in less than 0.1 s so are not separated (1.5); in a hall the gap is longer, so echoes are heard (1.5).", "1½+1½"),
 Q("Explain the working of sonar. A signal returns after 0.9 s; find the depth (v = 1530 m s⁻¹).", "Ultrasonic pulses sent and reflected (1); d = 1530 × 0.45 (1) = 688.5 m (1).", "1+1+1"),
 Q("Describe how bats navigate in the dark.", "Bats emit ultrasonic waves (1); sense the echoes from objects (1); judge the distance and size of obstacles and prey (1).", "1+1+1"),
 Q("State three applications of ultrasound.", "Medical imaging; breaking kidney stones; cleaning delicate parts; detecting flaws in metal blocks (1+1+1).", "1+1+1"),
 Q("What is timbre? Why do a sitar and a flute sound different at the same pitch and loudness?", "Quality of sound (1); overtone patterns differ because of the shape, material and construction (2).", "1+2"),
 Q("What is noise pollution? State two harmful effects and two measures.", "Unwanted or harmful sound (1); sleep disturbance, hearing loss (1); sound-proofing, limiting volume (1).", "1+1+1"),
 Q("Describe how a microphone and a speaker work.", "Microphone: sound makes a membrane vibrate, converted to an electrical signal (1.5); speaker: electrical signal makes a cone vibrate and produce sound (1.5).", "1½+1½"),
 Q("In a movie, a spacecraft explosion in space shows a flash of light along with sound. What is wrong?", "Sound cannot travel in vacuum, so no sound would be heard (3).", "3"),
 Q("A source produces a wave of wavelength 3.44 m at a speed of 344 m s⁻¹. Find the time period.", "ν = 344/3.44 = 100 Hz (1.5); T = 0.01 s (1.5).", "1½+1½"),
 Q("A parking sensor emits ultrasound that is reflected from an obstacle 1.2 m away (v = 345 m s⁻¹). Find the time taken for the round trip.", "Distance = 2.4 m (1); t = 2.4/345 (1) ≈ 0.007 s (1).", "1+1+1"),
 Q("Sound in steel travels at 5000 m s⁻¹ and in air at 340 m s⁻¹. How much sooner does a sound travel through 340 m of steel than through air?", "Air: 1 s (1); steel: 0.068 s (1); difference 0.932 s (1).", "1+1+1"),
 Q("Explain the working of the human ear in brief.", "Sound makes the eardrum vibrate (1); small bones amplify the vibrations (1); the cochlea converts them into electrical signals sent to the brain (1).", "1+1+1"),
]
D = [
 Q("(i) How is sound produced? Describe an activity. (ii) Show that sound needs a medium. (iii) Why can astronauts not hear each other directly?", "(i) Plucked rubber band on a box (2). (ii) Bell jar experiment (2). (iii) No medium in space (1).", "2+2+1"),
 Q("(i) Explain the propagation of sound as compressions and rarefactions. (ii) Is the medium carried along? (iii) Distinguish longitudinal and transverse waves.", "(i) Piston model: alternate compressions and rarefactions (2). (ii) No; particles oscillate about their positions and only energy moves (1). (iii) Parallel vs perpendicular vibration (2).", "2+1+2"),
 Q("<b>Case study:</b> A tuning fork of frequency 256 Hz is struck; the speed of sound in air is 344 m s⁻¹. (i) Find the time period. (ii) Find the wavelength. (iii) How many compressions pass a point in 5 s? (iv) What happens to the wavelength in water if the speed there is 1500 m s⁻¹?", "(i) T = 1/256 s ≈ 0.0039 s (1). (ii) λ = 344/256 ≈ 1.34 m (2). (iii) 1280 (1). (iv) λ = 1500/256 ≈ 5.86 m, larger (1).", "1+2+1+1"),
 Q("(i) Define amplitude, frequency, wavelength and time period. (ii) Relate loudness to amplitude and pitch to frequency. (iii) Give the audible range.", "(i) Four definitions (2). (ii) Larger amplitude is louder; higher frequency, higher pitch (2). (iii) 20 Hz to 20 kHz (1).", "2+2+1"),
 Q("<b>Case study:</b> Human hearing spans about 20 Hz to 20 kHz; take v = 344 m s⁻¹. (i) Find the wavelength at 20 Hz. (ii) Find the wavelength at 20 kHz. (iii) Which is infrasonic and which ultrasonic? (iv) Name one animal that detects each.", "(i) 17.2 m (1). (ii) 1.72 cm (1). (iii) Below 20 Hz is infrasonic; above 20 kHz ultrasonic (1). (iv) Elephants hear infrasound; bats hear ultrasound (2).", "1+1+1+2"),
 Q("(i) Derive v = νλ. (ii) A wave of 500 Hz has a wavelength of 0.68 m; find its speed. (iii) Why does the wavelength change when the wave enters another medium?", "(i) v = λ/T = νλ (2). (ii) 340 m s⁻¹ (1). (iii) The frequency stays the same but the speed changes (2).", "2+1+2"),
 Q("<b>Case study:</b> A ship sends a sonar signal and receives the echo after 5 s; v = 1525 m s⁻¹. (i) Find the depth. (ii) Why is ultrasound used? (iii) Name the principle. (iv) Another signal returns in 2 s; find the depth.", "(i) d = 1525 × 2.5 = 3812.5 m (2). (ii) Ultrasound travels in narrow beams with little spreading (1). (iii) Reflection of sound (1). (iv) 1525 m (1).", "2+1+1+1"),
 Q("(i) What is an echo and when is it heard? (ii) Find the minimum distance of the reflector. (iii) Distinguish echo and reverberation. (iv) How are reverberations controlled in auditoriums?", "(i) Reflected sound heard after the original, gap ≥ 0.1 s (1). (ii) 17 m (1). (iii) Reverberation has gaps < 0.05 s; it is repeated reflections (1). (iv) Absorbing panels, curtains, upholstered seats (2).", "1+1+1+2"),
 Q("<b>Case study:</b> You clap near a cliff and hear an echo after 2 s; v = 340 m s⁻¹. (i) Find the distance to the cliff. (ii) How far does sound travel in total? (iii) If the temperature rises, what happens to the time? (iv) Can you hear a separate echo in a room 5 m wide?", "(i) 340 m (1). (ii) 680 m (1). (iii) Speed increases, so the time decreases (1). (iv) No; 0.03 s is less than 0.1 s (2).", "1+1+1+2"),
 Q("(i) What are ultrasonic waves? (ii) Describe four applications. (iii) How do bats use them?", "(i) Waves above 20 kHz (1). (ii) Imaging, kidney stone breaking, cleaning, flaw detection, sonar (2). (iii) Echolocation (2).", "1+2+2"),
 Q("(i) Define timbre and tone. (ii) Why do instruments sound different at the same pitch? (iii) What is an octave? (iv) Who studied the acoustics of Indian drums?", "(i) Single frequency vs mixture; timbre = quality (2). (ii) Different overtone patterns (1). (iii) Frequency ratio 2 : 1 (1). (iv) C. V. Raman (1).", "2+1+1+1"),
 Q("<b>Case study:</b> Exposure to loud sound for a long time is harmful. (i) Define noise. (ii) Give the decibel level of normal conversation and firecrackers. (iii) State health effects. (iv) Suggest three ways to reduce noise pollution.", "(i) Unwanted or harmful sound (1). (ii) About 60 dB and over 100 dB (1). (iii) Hearing loss, sleep loss, stress (1). (iv) Use of earplugs, sound barriers, limiting volume (2).", "1+1+1+2"),
 Q("(i) Describe the structure of the human ear and the path of sound. (ii) Why do we have two ears?", "(i) Eardrum, small bones, cochlea, nerve to the brain (3). (ii) The brain compares arrival times to find the direction (2).", "3+2"),
 Q("(i) Compare the speed of sound in air, water and steel (344, 1500, 5000 m s⁻¹). (ii) Find the ratios water/air and steel/water. (iii) Explain the trend.", "(i) Fastest in steel (1). (ii) 4.36 and 3.33 (2). (iii) Particles are more closely packed and interact more strongly in solids (2).", "1+2+2"),
 Q("(i) How is sound used for exploration beyond hearing? Give two applications. (ii) Explain audio surveillance and the use of infrasound.", "(i) Sonar and ocean temperature study, or soil microbe sounds (3). (ii) Detecting drones from their hum; detecting earthquakes and storms from infrasound (2).", "3+2"),
 Q("<b>Case study:</b> Two friends stand 340 m apart along a steel fence. One strikes the fence; sound reaches the other through steel (5000 m s⁻¹) and air (340 m s⁻¹). (i) Find the time through air. (ii) Find the time through steel. (iii) Find the time difference. (iv) Can she hear two separate sounds?", "(i) 1 s (1). (ii) 0.068 s (1). (iii) 0.932 s (1). (iv) Yes, since the gap exceeds 0.1 s (2).", "1+1+1+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
