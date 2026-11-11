"""Class 9 Maths Ch 9 Propositions and their Converses - extras."""
from common import AR4, Q

AR = [
 AR4(r"The converse of 'If a number is divisible by 6, then it is even' is false.", r"The number 4 is even but is not divisible by 6.", "a",
     r"The converse is 'If a number is even, then it is divisible by 6'; 4 is a counterexample, which is exactly R."),
 AR4(r"The statement 'Every prime number is odd' is false.", r"The prime number 2 is not odd.", "a",
     r"A single counterexample, the number 2, disproves the statement."),
 AR4(r"The statement 'If $x=3$, then $x^2=9$' is true.", r"The converse of every true statement is true.", "c",
     r"A is true; R is false because the converse 'If $x^2=9$, then $x=3$' fails for $x=-3$."),
 AR4(r"One example that satisfies a statement is enough to prove the statement true in general.", r"One counterexample is enough to prove a statement false.", "d",
     r"A is false (examples do not prove a general statement); R is true."),
 AR4(r"The statement '$n^2>n$ for every natural number $n$' is false.", r"For $n=1$ we get $1^2=1$, which is not greater than 1.", "a",
     r"$n=1$ is a counterexample, so the statement is false; R states that counterexample."),
 AR4(r"The converse of 'If a quadrilateral is a rectangle, then its opposite sides are equal' is false.", r"The converse of 'If P, then Q' is 'If Q, then P'.", "b",
     r"A parallelogram that is not a rectangle has equal opposite sides, so the converse is false; R is true but only defines the converse and does not show it is false."),
]

CASE = [
 Q(r"<b>Case study.</b> In a maths club, Naveen considers the statement: 'If a number is a multiple of 8, then it is a multiple of 4.' "
   r"(i) Identify the hypothesis and the conclusion. (ii) Write the converse of the statement. (iii) Is the original statement true? (iv) Is the converse true? Support your answer with a counterexample if it is false.",
   r"(i) Hypothesis: a number is a multiple of 8; conclusion: it is a multiple of 4 (1). (ii) 'If a number is a multiple of 4, then it is a multiple of 8' (1). (iii) True, since $8k=4(2k)$ (1). (iv) False (1); 12 is a multiple of 4 but not of 8 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Ria claims: 'The sum of any two prime numbers is even.' Her teacher asks the class to test claims by finding counterexamples or giving proofs. "
   r"(i) Is Ria's claim true or false? (ii) Give a counterexample to it. (iii) Give a counterexample to the claim '$2n+1$ is prime for every natural number $n$'. (iv) Prove that the product of two odd numbers is odd.",
   r"(i) False (1). (ii) $2+3=5$ is odd (1). (iii) For $n=4$, $2n+1=9=3\times3$ is not prime (1). (iv) Let the odd numbers be $2a+1$ and $2b+1$; the product is $4ab+2a+2b+1=2(2ab+a+b)+1$ (1), which is of the form $2m+1$, so it is odd (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Karan is studying quadrilaterals and writes: 'If a quadrilateral is a square, then all its sides are equal.' "
   r"(i) Write the converse. (ii) Is the original statement true? (iii) Is the converse true? (iv) Give a counterexample to the converse and explain why it works.",
   r"(i) 'If all the sides of a quadrilateral are equal, then it is a square' (1). (ii) True, because every square has four equal sides (1). (iii) False (1). (iv) A rhombus with angles $60^\circ$ and $120^\circ$ has all four sides equal (1) but its angles are not right angles, so it is not a square (1).", "1+1+1+2"),
]

FORMULAS = [
 ("If-then statements", [r"A proposition 'If P, then Q' has hypothesis P (the part after 'if') and conclusion Q (the part after 'then').",
   r"Statements like 'All squares are rectangles' can be rewritten as 'If a quadrilateral is a square, then it is a rectangle'."]),
 ("Converse", [r"The converse of 'If P, then Q' is 'If Q, then P' (hypothesis and conclusion are interchanged).",
   r"The converse of a true statement may be true or false and must be checked separately.",
   r"Example: 'If a number is divisible by 10, its ones digit is 0' and its converse are both true; 'If a number is divisible by 6, it is divisible by 3' has a false converse."]),
 ("Counterexamples", [r"A single example that satisfies the hypothesis but fails the conclusion disproves a statement.",
   r"Checking examples never proves a general statement; a logical proof is needed.",
   r"Example: $n^2>n$ fails for $n=1$; 'every prime is odd' fails for 2."]),
 ("Simple proofs", [r"Even number: $2k$; odd number: $2k+1$; multiple of 3: $3k$ (for integers $k$).",
   r"Sum of two even numbers is even; product of two odd numbers is odd: $(2a+1)(2b+1)=2(2ab+a+b)+1$.",
   r"Proof layout: state what is given, use known facts step by step, state the conclusion."]),
]

MISTAKES = [
 r"Swapping the converse incorrectly, e.g. writing 'If not P, then not Q', which is a different statement.",
 r"Assuming the converse of a true statement is also true; always test it with an example.",
 r"Trying to 'prove' a general statement by checking a few examples; examples can only disprove it.",
 r"Giving a counterexample that does not satisfy the hypothesis; it must make the hypothesis true and the conclusion false.",
 r"Confusing hypothesis and conclusion when the statement is written in a form like 'Q, if P'.",
 r"Writing a proof without defining the objects, e.g. not writing odd numbers as $2k+1$ before multiplying.",
]
