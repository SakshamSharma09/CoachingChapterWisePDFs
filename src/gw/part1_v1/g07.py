VERBS = """arise arose arisen|awake awoke awoken|be was/were been|bear bore borne|beat beat beaten|become became become|begin began begun|bend bent bent|bet bet bet|bind bound bound|bite bit bitten|bleed bled bled|blow blew blown|break broke broken|breed bred bred|bring brought brought|build built built|burn burnt/burned burnt/burned|burst burst burst|buy bought bought|cast cast cast|catch caught caught|choose chose chosen|cling clung clung|come came come|cost cost cost|creep crept crept|cut cut cut|deal dealt dealt|dig dug dug|do did done|draw drew drawn|dream dreamt/dreamed dreamt/dreamed|drink drank drunk|drive drove driven|dwell dwelt dwelt|eat ate eaten|fall fell fallen|feed fed fed|feel felt felt|fight fought fought|find found found|flee fled fled|fling flung flung|fly flew flown|forbid forbade forbidden|forget forgot forgotten|forgive forgave forgiven|freeze froze frozen|get got got|give gave given|go went gone|grind ground ground|grow grew grown|hang hung hung|have had had|hear heard heard|hide hid hidden|hit hit hit|hold held held|hurt hurt hurt|keep kept kept|kneel knelt knelt|know knew known|lay laid laid|lead led led|lean leant/leaned leant/leaned|leap leapt/leaped leapt/leaped|learn learnt/learned learnt/learned|leave left left|lend lent lent|let let let|lie lay lain|light lit lit|lose lost lost|make made made|mean meant meant|meet met met|mistake mistook mistaken|overcome overcame overcome|pay paid paid|put put put|quit quit quit|read read read|rid rid rid|ride rode ridden|ring rang rung|rise rose risen|run ran run|saw sawed sawn|say said said|see saw seen|seek sought sought|sell sold sold|send sent sent|set set set|sew sewed sewn|shake shook shaken|shed shed shed|shine shone shone|shoot shot shot|show showed shown|shrink shrank shrunk|shut shut shut|sing sang sung|sink sank sunk|sit sat sat|sleep slept slept|slide slid slid|smell smelt/smelled smelt/smelled|sow sowed sown|speak spoke spoken|speed sped sped|spell spelt/spelled spelt/spelled|spend spent spent|spill spilt/spilled spilt/spilled|spin spun spun|spit spat spat|split split split|spoil spoilt/spoiled spoilt/spoiled|spread spread spread|spring sprang sprung|stand stood stood|steal stole stolen|stick stuck stuck|sting stung stung|stink stank stunk|strike struck struck|string strung strung|strive strove striven|swear swore sworn|sweep swept swept|swell swelled swollen|swim swam swum|swing swung swung|take took taken|teach taught taught|tear tore torn|tell told told|think thought thought|throw threw thrown|thrust thrust thrust|tread trod trodden|understand understood understood|undo undid undone|upset upset upset|wake woke woken|wear wore worn|weave wove woven|weep wept wept|win won won|wind wound wound|withdraw withdrew withdrawn|wring wrung wrung|write wrote written"""
def _rows():
    out=[]
    for item in VERBS.split("|"):
        p=item.split(" ")
        out.append([p[0],p[1],p[2]])
    return out
_r=_rows()
_half=(len(_r)+1)//2
_tab=[ _r[i]+(_r[i+_half] if i+_half<len(_r) else ["","",""]) for i in range(_half)]

CH = dict(num=7, title="Verbs", tag="The Heart of the Sentence · Classes 5–8",
intro="The verb is the most important word in a sentence: without it there is no sentence. Verbs show action, state and being, and they change form for tense, person and number. This chapter covers kinds of verbs, auxiliaries, transitive and intransitive use, regular and irregular forms (with a table of over 140 verbs), finite and non-finite forms, and phrasal verbs.",
blocks=[
("h2","7.1 What a Verb Does"),
("note","NOTE","Grade guide: Classes 5–6: action verbs, helping verbs, three forms of common verbs, transitive/intransitive. Classes 7–8: full irregular-verb table, lie/lay, rise/raise confusions, finite and non-finite verbs, phrasal verbs, verbs followed by gerund or infinitive, stative verbs."),
("p","A **verb** says what the subject does (*run, write*), what happens to it (*is broken*), or what it is (*is, seems*). Every verb has five forms:"),
("table",["Form","Name","Example (write)","Used for"],[
["V1","Base form / root","write","present (I, you, we, they), infinitive, imperatives, after modals/did/do"],
["V1 + s/es","-s form","writes","present tense with he, she, it"],
["V2","Past simple","wrote","simple past tense"],
["V3","Past participle","written","perfect tenses, passive voice"],
["V1 + ing","Present participle / gerund","writing","continuous tenses, adjectives, gerunds"]]),
("h2","7.2 Main Verbs and Helping Verbs"),
("p","A **main (principal) verb** carries the meaning. A **helping (auxiliary) verb** helps the main verb to form tenses, questions, negatives and the passive voice. There are two groups:"),
("table",["Primary auxiliaries","Modal auxiliaries"],[
["be (am, is, are, was, were, been, being), have (has, had), do (does, did)","can, could, may, might, will, would, shall, should, must, ought to, need, dare, used to"]]),
("ul",["*She **is** singing.* (helping + main) | *She **is** a singer.* (main verb)","*I **have** finished.* (helping) | *I **have** a pen.* (main verb)","*I **do** not know.* (helping) | *I **do** my homework.* (main)","Modals have no -s in the third person and no -ing/-ed forms. After a modal use V1: *He can swim* (not *can swims*)."]),
("h2","7.3 Transitive and Intransitive Verbs"),
("table",["Type","Meaning","Examples"],[
["Transitive","Action passes to an object (answers 'what?' or 'whom?')","She **ate** an apple. He **wrote** a letter."],
["Intransitive","No object; action stops with the doer","The baby **cried**. The sun **rises**. They **arrived**."],
["Both","Many verbs can be used either way","He **sings** (intr.). He **sings** a song (tr.)"],
["Ditransitive","Takes two objects (indirect and direct)","She **gave** me (indirect) a pen (direct)."],
["Linking (copular)","Joins subject and a complement; no action","She **is** a nurse. It **seems** easy. The leaf **turned** brown."]]),
("p","To test: ask *What?* or *Whom?* after the verb. If you get an answer, it is transitive. Only transitive verbs can be made passive."),
("h3","Confusing pairs"),
("table",["Intransitive","Transitive","Examples"],[
["lie – lay – lain (recline)","lay – laid – laid (put down)","He **lies** on the bed. She **laid** the book on the table."],
["rise – rose – risen","raise – raised – raised","The sun **rises**. They **raise** the flag."],
["sit – sat – sat","seat – seated – seated","He **sat** down. She **seated** the guests."],
["fall – fell – fallen","fell – felled – felled (cut down)","Leaves **fall**. They **felled** the tree."],
["lie (tell a falsehood) – lied – lied","—","He **lied** to me."],
["hang – hung – hung (things)","hang – hanged – hanged (execution)","The picture **hung** on the wall. The criminal was **hanged**."]]),
("h2","7.4 Regular and Irregular Verbs"),
("p","**Regular verbs** form V2 and V3 by adding -ed (or -d): *walk–walked–walked; love–loved–loved*. Spelling: consonant + y → -ied (*carry–carried*); double the final consonant of short stressed verbs (*stop–stopped, plan–planned*); just add -d to verbs ending in -e. **Irregular verbs** have other forms and must be memorised."),
("table",["V1","V2","V3","V1","V2","V3"],_tab),
("note","IMPORTANT","Common mistakes: *He buyed / brang / teached / runned / taked* → **bought, brought, taught, ran, took**. *I have went / She has wrote / It was broke* → **have gone, has written, was broken**. *He has did it* → **has done**. V2 is used alone (no helping verb) in simple past; V3 needs 'have/has/had' or 'be'."),
("h2","7.5 Finite and Non-finite Verbs"),
("p","A **finite verb** has a subject and changes with tense, number and person: *She **sings**. They **sang**. I **will sing**.* A **non-finite verb** does not show tense or number and cannot be the only verb of a sentence: the infinitive (*to sing*), the gerund (*singing* as a noun) and the participle (*singing / sung* as adjectives)."),
("table",["Type","Example","Function"],[
["Infinitive","I want **to sing**.","noun / purpose"],["Gerund","**Singing** is fun.","noun"],["Present participle","The **singing** bird","adjective"],["Past participle","The **broken** glass","adjective"]]),
("p","Non-finite verbs are covered in depth in a separate chapter."),
("h2","7.6 Stative Verbs (Not Used in Continuous Tenses)"),
("p","Verbs of state, thought, feeling, possession and senses are normally not used in continuous form: *know, believe, understand, remember, forget, want, like, love, hate, prefer, need, belong, own, have (possess), see, hear, smell (sense), seem, appear, contain, consist*."),
("table",["Wrong","Correct"],[
["I am knowing him.","I know him."],["She is having a car.","She has a car."],["He is belonging to Jaipur.","He belongs to Jaipur."],["I am understanding the lesson.","I understand the lesson."],["They are wanting water.","They want water."]]),
("p","Some of these verbs have an action meaning and can be continuous: *She is having lunch* (eating), *I am thinking of a plan*, *He is seeing the doctor* (meeting)."),
("h2","7.7 Verbs Followed by Gerund or Infinitive"),
("table",["Followed by -ing (gerund)","Followed by to + V1 (infinitive)"],[
["enjoy, finish, avoid, mind, practise, suggest, deny, admit, stop (quit), keep, miss, risk, imagine, consider, delay, postpone","want, decide, hope, plan, promise, refuse, agree, manage, learn, expect, need, afford, offer, seem, fail, wish"]]),
("p","Verbs that change meaning: *stop to eat* (stop in order to eat) vs *stop eating* (quit); *remember to lock* (not forget to) vs *remember locking* (recall the past act); *try to open* (attempt) vs *try opening* (experiment); *forget to post* vs *forget posting*. After prepositions use -ing: *interested in reading, fond of swimming, look forward to meeting*."),
("h2","7.8 Phrasal Verbs (Introduction)"),
("p","A **phrasal verb** is a verb combined with an adverb or preposition, giving a new meaning: *give up* (stop), *look after* (care for), *put off* (postpone), *turn down* (refuse), *break down* (stop working), *carry on* (continue)."),
("table",["Phrasal verb","Meaning","Example"],[
["look after","take care of","She looks after her grandmother."],["look for","search","I am looking for my keys."],["look up","consult","Look up the word in a dictionary."],["look into","investigate","The police are looking into the case."],["give up","stop trying","Never give up."],["put off","postpone","The match was put off."],["put on","wear","Put on your coat."],["put out","extinguish","Firemen put out the fire."],["take off","remove / leave the ground","The plane took off."],["take after","resemble","He takes after his father."],["turn down","refuse","She turned down the offer."],["turn up","arrive","He turned up late."],["call off","cancel","The trip was called off."],["call on","visit","I'll call on you."],["come across","find by chance","I came across an old photo."],["get along (with)","be on good terms","I get along with my cousins."],["go through","examine / experience","Go through the notes."],["run out of","have none left","We ran out of milk."],["set off","begin a journey","They set off at six."],["bring up","raise (a child)","She was brought up by her aunt."],["break out","start suddenly","A fire broke out."],["carry out","perform","Carry out the order."],["make up","invent","He made up a story."],["pass away","die","Her grandfather passed away."]]),
("note","NOTE","Separable phrasal verbs allow the object between the parts (*put the light off*); with a pronoun the object must go in the middle (*put it off*, not *put off it*). Inseparable ones do not (*look after her*)."),
("h2","7.9 The Verb Be, Have and Do in Detail"),
("table",["Verb","Present","Past","V3 / -ing","Notes"],[
["be","am (I), is (he/she/it), are (you/we/they)","was (I/he/she/it), were (you/we/they)","been / being","'were' for all persons in unreal wishes: *If I were you…*"],
["have","have / has","had","had / having","Possession; helps perfect tenses; *have to* = must"],
["do","do / does","did","done / doing","Helps in negatives and questions; main verb 'to perform'"]]),
("note","IMPORTANT","Do/does/did are followed by V1, never V2/V3 or -s: *She does not **like** it* (not *likes*); *Did he **come**?* (not *came*)."),
("qa",[("Give V2 and V3 of: write, bring, choose, lay.","wrote/written; brought/brought; chose/chosen; laid/laid."),
("Is the verb in 'The baby slept' transitive?","No; it has no object (intransitive)."),
("Correct: 'He has went to Delhi.'","He has gone to Delhi."),
("Correct: 'I am knowing the answer.'","I know the answer."),
("Fill: She ___ (lie) on the sofa yesterday.","lay"),
("Phrasal verb meaning 'cancel':","call off")]),
],
takeaways=["Every verb has five forms: V1, V1+s, V2, V3 and V1+ing.","Helping verbs (be, have, do and modals) help main verbs; after do/does/did and modals use V1.","Only transitive verbs have a passive voice; learn lie/lay, rise/raise, sit/seat.","Memorise the irregular verb table; never write 'have went' or 'has did'.","Stative verbs (know, want, belong) are not used in continuous tenses."])
