from lib import mcq, Q, OR
from mk9 import M4, build
A = []
def rev(n): return int(str(n)[::-1])
def collatz(n):
    c = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1; c += 1
    return c
def kap(n):
    d = sorted(f"{n:04d}"); return int("".join(d[::-1])) - int("".join(d))
A += [
 M4("A number that reads the same forwards and backwards is a:", "palindrome", ["prime", "supercell", "triangular number"], "e.g. 121"),
 M4("The Kaprekar constant for 4-digit numbers is:", "6174", ["1729", "9999", "1089"], "reached by the Kaprekar routine"),
 M4("In the Collatz process, if the number is even we:", "halve it", ["add 1", "triple it", "subtract 1"], "even rule"),
 M4("In the Collatz process, if the number is odd we:", "multiply by 3 and add 1", ["halve it", "subtract 3", "square it"], "odd rule"),
 M4("The Collatz conjecture is still:", "an unsolved problem", ["proved long ago", "false", "a school test"], "mystery"),
 M4("Starting at 6, the Collatz sequence is 6, 3, 10, 5, 16, 8, 4, 2, 1. The number of steps is:", "8", ["6", "9", "10"], "count of moves"),
 M4("The Kaprekar routine uses:", "the largest and smallest numbers formed from the digits, then subtraction", ["addition of all digits", "multiplication by 9", "division by 7"], "6174 process"),
 M4("The smallest 4-digit number that can be made from 3, 8, 1, 5 is:", "1358", ["1385", "1538", "3158"], "ascending digits"),
 M4("The largest 4-digit number from 3, 8, 1, 5 is:", "8531", ["8513", "8351", "5381"], "descending digits"),
 M4("The sum of the digits of 4567 is:", "22", ["20", "21", "23"], "4+5+6+7"),
 M4("The smallest 3-digit palindrome is:", "101", ["100", "111", "121"], "reads same both ways"),
 M4("Which one is a palindrome?", "2332", ["2331", "2323", "1223"], "symmetrical digits"),
 M4("Rounding 3482 to the nearest hundred gives:", "3500", ["3400", "3000", "3480"], "estimation"),
 M4("Rounding 6743 to the nearest thousand gives:", "7000", ["6000", "6700", "6800"], "estimation"),
 M4("The estimate of 498 + 303 by rounding to hundreds is:", "800", ["700", "900", "1000"], "500+300"),
 M4("The estimate of 61 × 19 by rounding to tens is about:", "1200", ["1000", "1400", "600"], "60×20"),
 M4("Which of the following is an even number?", "5138", ["5137", "5139", "5135"], "last digit 8"),
 M4("On a number line, numbers increase:", "from left to right", ["from right to left", "up to down only", "randomly"], "order"),
 M4("The number of days in a leap year is:", "366", ["365", "364", "367"], "February has 29 days"),
 M4("A supercell is a:", "cell in a grid that is greater than its neighbours", ["cell with 0", "cell with a palindrome", "cell with a prime"], "Number Play idea"),
 M4("‘Mental math’ means:", "calculating quickly in the mind using tricks", ["only using a calculator", "using an abacus", "guessing"], "easy strategies"),
 M4("The number 1089 magic: 3-digit number minus its reverse, then add the reverse of the result. The final answer is:", "1089", ["999", "1001", "1111"], "famous trick"),
 M4("The Kaprekar routine on 3524: 5432 − 2345 = ", "3087", ["3187", "3077", "2087"], "subtract"),
 M4("The number of days between 5 Jan and 20 Jan is:", "15", ["14", "16", "20"], "20−5"),
 M4("Which is the largest 5-digit number?", "99999", ["10000", "98765", "99990"], "all 9s"),
 M4("The number 1001 is a palindrome of how many digits?", "4", ["3", "5", "2"], "four-digit"),
 M4("In a winning-strategy game with two players taking 1 or 2 stones, the player who wants to win should aim to leave a multiple of:", "3", ["2", "4", "5"], "strategy"),
 M4("The digits of a number may be rearranged to make the largest number by writing them:", "in descending order", ["in ascending order", "alphabetically", "randomly"], "place value"),
 M4("The sum of two consecutive counting numbers is always:", "odd", ["even", "a multiple of 4", "a multiple of 3"], "e.g. 4+5=9"),
 M4("A number ending in 5 is:", "divisible by 5", ["divisible by 2", "always prime", "always even"], "last digit rule"),
]
for n in (7, 12, 27 // 3 * 3 if False else 9, 16, 20, 10):
    pass
for n in (7, 9, 10, 12, 20, 16):
    A.append(M4(f"The Collatz sequence starting at {n} takes how many steps to reach 1?", str(collatz(n)), [str(collatz(n) + 1), str(collatz(n) - 1), str(collatz(n) + 3)], "apply the rule repeatedly"))
for n in (3524, 5231, 8741, 6321):
    A.append(M4(f"One step of the Kaprekar routine on {n} gives:", str(kap(n)), [str(kap(n) + 90), str(kap(n) - 90), str(kap(n) + 9)], "largest minus smallest"))
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("What is a palindrome? Give two examples.", "A number or word reading the same both ways; 121 and 4554.", "1+1"),
 Q("Write the largest and smallest 4-digit numbers using the digits 2, 6, 9, 4.", "9642 and 2469.", "1+1"),
 Q("Apply one step of the Kaprekar routine to 4153.", "5431 − 1345 = 4086.", "1+1"),
 Q("Write the Collatz sequence starting from 5.", "5, 16, 8, 4, 2, 1.", "1+1"),
 Q("Estimate 4,876 + 2,123 by rounding to the nearest thousand.", "5000 + 2000 = 7000.", "1+1"),
 Q("What is the Collatz conjecture?", "It says that every starting number eventually reaches 1 with the rule; it is unproved.", "1+1"),
 Q("Is the sum of two odd numbers odd or even? Explain with an example.", "Even; e.g. 3 + 5 = 8.", "1+1"),
 Q("Round 7,468 to the nearest hundred and to the nearest thousand.", "7,500 and 7,000.", "1+1"),
 Q("What is the difference between the smallest and largest 3-digit palindromes?", "999 − 101 = 898.", "1+1"),
 Q("What is a supercell in a number grid?", "A cell whose number is larger than its neighbours (adjacent cells).", "1+1"),
 Q("State the 1089 trick in one line.", "Take a 3-digit number, subtract its reverse, add the result's reverse to get 1089.", "1+1"),
 Q("How many days are there from 12 March to 12 April?", "31 days.", "1+1"),
 Q("What is the digit sum of 98,765?", "35.", "1+1"),
 Q("Write the next two numbers: 3, 6, 12, 24, …", "48 and 96.", "1+1"),
 Q("Why is a number ending in 0 or 5 divisible by 5?", "Multiples of 5 end in 0 or 5.", "1+1"),
 Q("Give an example of mental math to multiply 25 by 8.", "25 × 8 = 200 using 25 × 4 × 2 (100 × 2).", "1+1"),
]
C = [
 Q("Perform the Kaprekar routine on 3087 and describe what happens.", "8730 − 0378 = 8352 (1); 8532 − 2358 = 6174 (1); then it stays at 6174 (1).", "1+1+1"),
 Q("Write the Collatz sequence for 7 and count the steps.", "7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 (2); 16 steps (1).", "2+1"),
 Q("Make 5 different 4-digit palindromes and find their sums with their reverses.", "e.g. 1221, 3443; each palindrome is its own reverse (1.5); sum is twice the number (1.5).", "1½+1½"),
 Q("Estimate 487 × 52 and compare with the exact value.", "500 × 50 = 25,000 (1.5); exact 25,324 (1.5).", "1½+1½"),
 Q("Explain with an example how a palindrome is formed by adding a number to its reverse repeatedly.", "Take 68 + 86 = 154; 154 + 451 = 605; 605 + 506 = 1111 (2); a palindrome (1).", "2+1"),
 Q("Why does the sum of three consecutive numbers always divide by 3? Show with 14, 15, 16.", "Sum is 45 = 3 × 15 (2); it equals 3 times the middle number (1).", "2+1"),
 Q("Describe the 1089 trick with the number 532.", "532 − 235 = 297 (1); 297 + 792 = 1089 (2).", "1+2"),
 Q("How many days from 10 Feb 2025 to 10 May 2025? Show working.", "18 (Feb) + 31 + 30 + 10 = 89 days (3).", "1+2"),
 Q("Two players alternately take 1, 2 or 3 sticks from a pile of 21; whoever takes the last stick wins. Describe a winning strategy for the first player.", "Take 1 stick first, leaving 20, a multiple of 4 (1.5); after each move of the opponent take 4 minus that number (1.5).", "1½+1½"),
 Q("Round 548,123 to the nearest thousand and to the nearest ten thousand.", "548,000 (1.5); 550,000 (1.5).", "1½+1½"),
 Q("What are the largest and smallest 5-digit numbers formed by 7, 0, 3, 9, 1 without repeating a digit? Find their difference.", "97310 and 10379 (2); 86,931 (1).", "2+1"),
 Q("How do you check whether a 3×3 grid of 1 to 9 is a magic square? Which number must be in the centre if every line sums to 15?", "Rows, columns and both diagonals must have equal sums (1.5); the centre number is 5 (1.5).", "1½+1½"),
 Q("Is the sum of four consecutive numbers always even? Explain with 3, 4, 5, 6.", "Sum 18 is even (1); two odds and two evens always give an even sum (2).", "1+2"),
 Q("The number 4_38 is divisible by 3. Which digits can fill the blank?", "Digit sum 15 + x must be a multiple of 3: x = 0, 3, 6, 9 (3).", "1+2"),
 Q("Using mental math calculate 98 + 47 and 103 − 59 with a method.", "98 + 47 = 100 + 45 = 145 (1.5); 103 − 59 = 103 − 60 + 1 = 44 (1.5).", "1½+1½"),
 Q("A month starts on a Monday and has 30 days. How many Sundays does it have?", "Sundays fall on 7, 14, 21, 28 (3).", "1+2"),
 Q("Write the numbers on the number line between 996 and 1004 that are multiples of 4.", "996, 1000, 1004 (3).", "3"),
 Q("Why do we use estimation? Give two situations.", "To get a quick approximate answer (1); shopping and checking results (2).", "1+2"),
 Q("Using the digits 1, 2, 3, 4, form two 2-digit numbers with the greatest sum.", "42 + 31 = 73; (any with tens digits 4 and 3 sum is 73) (3).", "1+2"),
 Q("If today is Wednesday, what day will it be after 100 days?", "100 ÷ 7 leaves 2, so Friday (3).", "1+2"),
 Q("Find the Collatz steps for 12 and for 6. Which is more and why?", "12: 9 steps; 6: 8 steps (2); 12 reaches 6 after its first step (1).", "2+1"),
 Q("List the 3-digit palindromes between 200 and 230.", "202, 212, 222 (3).", "3"),
 Q("Mark the numbers 1,000, 1,500 and 2,000 on a number line and show where 1,730 lies.", "Correct line with scale (2); 1,730 is nearer to 2,000 (1).", "2+1"),
 Q("What are the benefits of playing games with numbers?", "Improves thinking and logic (1); finds patterns (1); builds a winning strategy (1).", "1+1+1"),
]
D = [
 Q("(i) Explain the Kaprekar routine. (ii) Apply it to 2,531. (iii) Show that it reaches 6174.", "(i) Rule (1). (ii) 5321 − 1235 = 4086 (2). (iii) 4086 → 8640 − 0468 = 8172 → 8721 − 1278 = 7443 → 7443 − 3447 = 3996 → 9963 − 3699 = 6264 → 6642 − 2466 = 4176 → 7641 − 1467 = 6174 (2).", "1+2+2"),
 Q("(i) Write the Collatz rules. (ii) Find the sequence for 11. (iii) Count the steps.", "(i) Rules (2). (ii) 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 (2). (iii) 14 steps (1).", "2+2+1"),
 Q("(i) What are palindromic numbers? (ii) List all 3-digit palindromes with digit sum 8. (iii) Find the sum of 247 and its reverse.", "(i) Numbers that read the same both ways (1). (ii) 161, 242, 323, 404 (2). (iii) 247 + 742 = 989 (2).", "1+2+2"),
 Q("<b>Case study:</b> A school bell rings every 15 minutes and a club bell every 20 minutes starting at 9:00. (i) After how many minutes do they ring together? (ii) At what time? (iii) How many times between 9:00 and 12:00? (iv) Which number idea is used?", "(i) 60 minutes (1). (ii) 10:00 (1). (iii) 4 times counting 9:00 (1). (iv) Common multiples (2).", "1+1+1+2"),
 Q("(i) Estimate 3,987 + 5,012 + 1,008. (ii) Estimate 49 × 21. (iii) Compare with exact values.", "(i) 4000 + 5000 + 1000 = 10,000 (1.5). (ii) 50 × 20 = 1000 (1.5). (iii) 10,007 and 1,029 (2).", "1½+1½+2"),
 Q("(i) Describe the 1089 trick. (ii) Check it for 721. (iii) Explain what goes wrong if the digits are all the same.", "(i) Steps (2). (ii) 721 − 127 = 594; 594 + 495 = 1089 (2). (iii) The difference is 0 (1).", "2+2+1"),
 Q("<b>Case study:</b> A calendar shows dates in a 7-column grid. (i) Pick a 2×2 box 8, 9, 15, 16 and find the sum of diagonals. (ii) What do you notice? (iii) Test with another box. (iv) Explain why.", "(i) 8+16 = 24, 9+15 = 24 (1). (ii) Equal (1). (iii) 12, 13, 19, 20: 32 and 32 (1). (iv) Moving down adds 7 and right adds 1 (2).", "1+1+1+2"),
 Q("(i) Explain mental maths strategies for addition. (ii) Compute 99 + 76 mentally. (iii) Compute 5 × 48.", "(i) Break up, round and adjust (2). (ii) 175 (1.5). (iii) 240 (1.5).", "2+1½+1½"),
 Q("(i) What is a number line? (ii) Mark 0, 250, 500, 750 and 1000 on a line. (iii) Which of these is nearest to 640?", "(i) A line showing numbers in order (1). (ii) Correct equal-interval scale (2). (iii) 750 (it is 110 away; 500 is 140 away) (2).", "1+2+2"),
 Q("(i) Describe a number game with a winning strategy. (ii) Explain how the first player wins in a game where players take 1 or 2 objects from 10 and the last wins.", "(i) Rule and idea (2). (ii) Leave multiples of 3: first takes 1, then complements to 3 (3).", "2+3"),
 Q("<b>Case study:</b> In a row of numbers 12, 40, 25, 31, 18, a cell is a supercell if it is larger than its adjacent cells. (i) What is a supercell? (ii) Which numbers are supercells? (iii) How many are there? (iv) Will the largest number in any row always be a supercell? Why?", "(i) A cell larger than its adjacent cells (1). (ii) 40 and 31 (1). (iii) 2 (1). (iv) Yes; no neighbour is larger (2).", "1+1+1+2"),
 Q("(i) Write the rule for digit sum. (ii) Find the digit sum of 12, 345. (iii) Test divisibility by 3 for 12345.", "(i) Add digits (1). (ii) 15 (2). (iii) 15 is a multiple of 3, so divisible (2).", "1+2+2"),
 Q("(i) Why is the Collatz conjecture famous? (ii) Test it for 13. (iii) What did you observe?", "(i) Simple but unproved (2). (ii) 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 (2). (iii) Reaches 1 (1).", "2+2+1"),
 Q("(i) What is a 4-digit palindrome pattern? (ii) Show that every 4-digit palindrome is divisible by 11. (iii) Test with 3443.", "(i) abba (1). (ii) 1001a + 110b = 11(91a + 10b) (2). (iii) 3443 ÷ 11 = 313 (2).", "1+2+2"),
 Q("(i) Write numbers between 1,000 and 2,000 whose digits sum to 3. (ii) How many? (iii) Which is the smallest?", "(i) 1002, 1011, 1020, 1101, 1110, 1200 (2). (ii) 6 (2). (iii) 1002 (1).", "2+2+1"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 15, (len(B), len(C), len(D))
D.append(Q("(i) How is the number line used for comparing numbers? (ii) Order 4,508; 4,058; 4,805; 4,850.", "(i) Numbers to the right are greater (2). (ii) 4,058 < 4,508 < 4,805 < 4,850 (3).", "2+3"))
SETS, POOL = build(A, B, C, D)
