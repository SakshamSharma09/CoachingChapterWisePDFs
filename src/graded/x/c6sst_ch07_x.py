"""Class 6 SST Ch 7 India's Cultural Roots - Hard-tier extras (assertion-reason, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("Vedic hymns were passed down from generation to generation by word of mouth.", "The hymns were memorised and chanted with great care using precise rules.", "a",
     "Careful memorisation and chanting kept the hymns unchanged for thousands of years, explaining A."),
 AR4("The Rig Veda is the oldest of the four Vedas.", "The word Veda comes from the Sanskrit root 'vid' meaning 'to fight'.", "c",
     "A is true; R is false, 'vid' means 'to know'."),
 AR4("The Upanishads were composed before the Vedas.", "The Upanishads build on ideas found in the Vedas.", "d",
     "The Upanishads came after the Vedas, so A is false; R is true."),
 AR4("The Buddha attained enlightenment at Bodh Gaya.", "Ahimsa is a central teaching of Jainism.", "b",
     "Both are true statements about different traditions; neither explains the other."),
 AR4("The word Buddha means 'the enlightened one'.", "Siddhartha Gautama attained enlightenment under the Bodhi tree.", "a",
     "After he attained enlightenment, Siddhartha Gautama came to be called the Buddha."),
 AR4("The Rig Veda says 'Ekam sat vipra bahudha vadanti'.", "This line expresses that truth is one but the wise describe it in many ways.", "a",
     "R is the meaning of the verse in A."),
]

CASE = [
 Q("<b>Case study.</b> Every morning in a gurukul, students sit in a circle and chant hymns exactly as their teacher does. There were no printed books when these hymns were first made, yet they have survived for thousands of years. In 2008, UNESCO recognised Vedic chanting as an intangible cultural heritage. "
   "(i) How many Vedas are there? (ii) Which is the oldest Veda? (iii) Who composed the Vedic hymns? (iv) How were the hymns preserved for so long without printing?",
   "(i) Four (1). (ii) Rig Veda (1). (iii) Rishis and rishikas (seers) (1). (iv) They were memorised and passed orally from teacher to student (1), and chanted with fixed rules of sound and rhythm so that no change crept in (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In the Katha Upanishad a young boy, Nachiketa, goes to meet Yama, the god of death, to learn the secret of life and death. In another text, a woman scholar named Gargi questions the sage Yajnavalkya about the nature of reality. The Upanishads teach that the Self (atman) is one with the universal reality (brahman). "
   "(i) Which Upanishad tells the story of Nachiketa? (ii) Whom did Nachiketa meet? (iii) Who was Gargi? (iv) What do the Upanishads teach about atman and brahman?",
   "(i) Katha Upanishad (1). (ii) Yama, the god of death (1). (iii) A woman scholar (rishika) who debated with Yajnavalkya (1). (iv) That the individual Self (atman) is the same as the universal reality (brahman) (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Siddhartha Gautama was born at Lumbini and attained enlightenment under a tree at Bodh Gaya, after which he was called the Buddha. Mahavira, born near Vaishali, taught the path of the 'jina', or conqueror of the self. Both teachers asked people to avoid hurting living beings. "
   "(i) Where was the Buddha born? (ii) Where did he attain enlightenment? (iii) What does 'jina' mean? (iv) Name the principle common to the teachings of both teachers and explain it.",
   "(i) Lumbini (1). (ii) Bodh Gaya (1). (iii) Conqueror (of oneself) (1). (iv) Ahimsa (1); it means non-violence, not causing harm to any living being in thought, word or deed (1).", "1+1+1+2"),
]

MISTAKES = [
 "Giving the wrong meaning of <b>Veda</b>. It comes from 'vid', <i>to know</i>, and means knowledge, not fight or worship.",
 "Naming the Vedas wrongly: the four are <b>Rig, Yajur, Sama and Atharva</b>; the Rig Veda is the oldest.",
 "Saying the Vedas were written down first. They were passed on <b>orally</b> by chanting and memorising.",
 "Mixing up <b>atman</b> (the individual Self) and <b>brahman</b> (the universal reality).",
 "Confusing the Buddha and Mahavira: the Buddha was born at Lumbini and enlightened at Bodh Gaya; Mahavira was a Jain teacher born near Vaishali.",
 "Writing the three jewels or the Sangha wrongly: the <b>Sangha</b> is the community of Buddhist monks, not a group of kings.",
]
