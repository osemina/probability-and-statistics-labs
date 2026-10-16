"""Lab 4 Excel workbooks (Students + Solutions).
Layout: LEFT (B:H) = task, data and student work in cells; RIGHT (J:P) = guidance in text boxes.
Narrative text lives in text boxes; data, formulas and answers live in cells."""
import math, os, re
import xlsxwriter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'excel')
os.makedirs(OUT, exist_ok=True)
NAME = 'Lab 4 – Probability of Discrete Random Variables'

NAVY, BLUE, GOLD, MUTED = '#003E67', '#1F5F99', '#C39A3D', '#5F6368'
INPUT, GIVEN, HEAD, PALE = '#FFF2CC', '#DDEBF7', '#003E67', '#EEF2F6'
BOX_TASK, BOX_HELP, BOX_LINE = '#FFFFFF', '#F3F6F9', '#C9D6E3'
PX_ROW, CHARS = 20, 78          # default row height in px; characters per line in a guide box

# ------------------------------------------------------------------ task specifications
# Placeholders {name} are replaced by absolute cell addresses of earlier params/answers/ranges.
T = []

T.append(dict(sheet='Task 1', title='Task 1. Spam in Your Inbox',
  focus='Binomial distribution  ·  BINOM.DIST  ·  complement rule  ·  E(X) = np',
  task="Your email provider’s spam filter misses some messages: 10% of the emails that reach your inbox are actually spam. You open your 10 newest emails, and each email is spam independently of the others.\n\n"
       "a) What is the probability that more than 3 of the 10 emails are spam?\n"
       "b) What is the probability that none of the 10 emails is spam?\n"
       "c) How many spam emails do you expect among the 10?",
  blocks=[
   ('params', [('n', 'n (emails opened)', 10, '0'), ('p', 'p (probability of spam)', 0.1, '0.00')],
    "HOW TO READ THIS SHEET\nBlue cells hold the given data. Yellow cells are yours: type a formula there.\n\n"
    "Every formula refers to the blue cells (for example {n}) instead of retyping the numbers. Then, if a number changes, all your answers update automatically."),
   ('work', 'pmf', 'PMF for k = 0, 1, 2, 3', ['k', 'P(X = k)'], [[0], [1], [2], [3]],
    ['=BINOM.DIST({row:0},{n},{p},FALSE)'], '0.0000',
    "STEP 1 – BUILD THE PMF\n1. Click the first yellow cell next to k = 0.\n2. Type =BINOM.DIST( and select the k cell to its left.\n"
    "3. Add the n cell and the p cell. Lock them with F4 so they become {n} and {p}.\n4. Finish with FALSE (exact probability) and press Enter.\n"
    "5. Drag the fill handle (small square at the bottom-right of the cell) down to k = 3."),
   ('answers', [('le3', 'P(X ≤ 3)  (sum of the PMF column)', '=SUM({pmf})', 0.9872, '0.0000'),
                ('a', 'a)  P(X > 3)', '=1-BINOM.DIST(3,{n},{p},TRUE)', 0.0128, '0.0000'),
                ('b', 'b)  P(X = 0)', '=BINOM.DIST(0,{n},{p},FALSE)', 0.3487, '0.0000'),
                ('c', 'c)  E(X) = np', '={n}*{p}', 1, '0.00')],
    "STEP 2 – USE THE COMPLEMENT\n• Add the four PMF values with =SUM( ) to get P(X ≤ 3).\n"
    "• “More than 3” is the complement of “3 or fewer”, so P(X > 3) = 1 − P(X ≤ 3).\n"
    "• Check it with one formula: =1-BINOM.DIST(3, n, p, TRUE). TRUE gives the cumulative probability P(X ≤ 3).\n"
    "• For c) multiply the n cell by the p cell."),
   ('interp', 'Is it likely that more than 3 of your 10 newest emails are spam? Explain in one or two sentences.',
    'No. P(X > 3) is only about 1.3%, so more than 3 spam emails among 10 would be very unusual. On average we expect only 1 spam email.',
    "INTERPRETATION\nCompare the probability with 0.05 (5%). Events below about 5% are usually called unusual. Write your answer in words, not only as a number."),
  ]))

T.append(dict(sheet='Task 2', title='Task 2. A Buggy Game Update',
  focus='Poisson approximation of the binomial  ·  POISSON.DIST  ·  “fewer than”',
  task="After a new update of a popular mobile game, on average 1 phone in 800 crashes when the game starts. On the first day, 4,000 players install the update.\n\n"
       "a) Compute the expected value and the variance of the number of phones that crash.\n"
       "b) Compute the probability that fewer than 10 phones crash.\n"
       "c) Compute the probability that exactly 10 phones crash.",
  blocks=[
   ('params', [('n', 'n (players)', 4000, '#,##0'), ('p', 'p (crash probability)', '=1/800', '0.00000')],
    "THE DATA\nThe p cell contains the formula =1/800. Click it and look at the formula bar: Excel keeps the exact value 0.00125.\n\n"
    "Here n is large and p is small, so the number of crashes is well described by a Poisson distribution with λ = n·p."),
   ('answers', [('lam', 'a)  E(X) = λ = n·p', '={n}*{p}', 5, '0.00'),
                ('var', 'a)  Var(X) = n·p·(1 − p)', '={n}*{p}*(1-{p})', 4.99375, '0.0000'),
                ('b', 'b)  P(X < 10) = P(X ≤ 9)', '=POISSON.DIST(9,{lam},TRUE)', 0.9682, '0.0000'),
                ('bx', 'b)  check: exact binomial P(X ≤ 9)', '=BINOM.DIST(9,{n},{p},TRUE)', 0.9683, '0.0000'),
                ('c', 'c)  P(X = 10)', '=POISSON.DIST(10,{lam},FALSE)', 0.0181, '0.0000')],
    "STEPS\n1. Compute λ in the first yellow cell (n cell × p cell).\n2. Variance: the binomial formula n·p·(1 − p).\n"
    "3. “Fewer than 10” does not include 10, so use POISSON.DIST(9, λ, TRUE).\n4. Compare it with the exact binomial result using BINOM.DIST(9, n, p, TRUE). The two should almost match.\n"
    "5. For exactly 10 use FALSE as the last argument."),
   ('interp', 'Would 10 or more crashes on the first day be unusual? What could it tell the developers?',
    'Yes. P(X ≥ 10) = 1 − 0.9682 ≈ 0.03, so 10 or more crashes happen only about 3% of the time. It would suggest that the update has a real problem.',
    "INTERPRETATION\nUse your answer to b): P(X ≥ 10) = 1 − P(X ≤ 9)."),
  ]))

T.append(dict(sheet='Task 3', title='Task 3. Lunch Rush on a Delivery App',
  focus='Poisson distribution  ·  rescaling λ to the interval  ·  E(X) = Var(X) = λ',
  task="During the lunch rush, a food delivery app receives orders at an average rate of 12 orders per minute, and the number of orders follows a Poisson distribution. Find the probability that exactly 10 orders arrive\n\n"
       "a) in a 1-minute interval;\nb) in a 3-minute interval.\n"
       "c) What are the expected value and the variance of the number of orders in each interval?",
  blocks=[
   ('params', [('rate', 'rate (orders per minute)', 12, '0'), ('t1', 'interval a) in minutes', 1, '0'), ('t2', 'interval b) in minutes', 3, '0')],
    "KEY IDEA\nλ must match the length of the interval: λ = rate × minutes.\nCompute λ first, then use it in POISSON.DIST."),
   ('answers', [('l1', 'λ for 1 minute', '={rate}*{t1}', 12, '0'),
                ('l2', 'λ for 3 minutes', '={rate}*{t2}', 36, '0'),
                ('a', 'a)  P(X = 10), 1 minute', '=POISSON.DIST(10,{l1},FALSE)', 0.1048, '0.0000'),
                ('b', 'b)  P(X = 10), 3 minutes', '=POISSON.DIST(10,{l2},FALSE)', 2.337e-7, '0.00E+00'),
                ('e1', 'c)  E(X) and Var(X), 1 minute', '={l1}', 12, '0'),
                ('e2', 'c)  E(X) and Var(X), 3 minutes', '={l2}', 36, '0')],
    "STEPS\n1. Fill the two λ cells (rate cell × minutes cell).\n2. Use =POISSON.DIST(10, λ, FALSE) for exactly 10 orders.\n"
    "3. The 3-minute result is tiny. Excel may show it in scientific notation, like 2.34E-07 = 0.000000234.\n4. For a Poisson distribution E(X) and Var(X) are both equal to λ."),
   ('interp', 'Why is exactly 10 orders quite likely in 1 minute but almost impossible in 3 minutes?',
    'In 1 minute we expect 12 orders, so 10 is close to the average. In 3 minutes we expect 36 orders, so only 10 orders would be far below the average and is extremely unlikely.',
    "INTERPRETATION\nCompare 10 with the expected value in each interval."),
  ]))

T.append(dict(sheet='Task 4', title='Task 4. Two Strikers, Same Average',
  focus='Expected value and standard deviation from a table  ·  SUMPRODUCT  ·  column chart',
  task="A football coach compares two strikers. The table shows the probability distribution of the number of goals X that each striker scores in a match.\n\n"
       "a) Compute the expected number of goals for each striker.\nb) Compute the standard deviation for each striker.\n"
       "c) Compare the two strikers. Which striker scores more steadily, and why?",
  blocks=[
   ('data', ['Goals X', 'Striker A: P(X)', 'Striker B: P(X)'],
    [[0, 0.2, 0.1], [1, 0.2, 0.2], [2, 0.2, 0.4], [3, 0.2, 0.2], [4, 0.2, 0.1]], ['0', '0.00', '0.00'], ['x', 'pa', 'pb'],
    "THE DATA\nEach probability column must add up to 1. Quick check: =SUM( ) of a column should give 1."),
   ('answers', [('ea', 'a)  E(X), Striker A', '=SUMPRODUCT({x},{pa})', 2, '0.00'),
                ('eb', 'a)  E(X), Striker B', '=SUMPRODUCT({x},{pb})', 2, '0.00')],
    "STEP 1 – EXPECTED VALUE\n=SUMPRODUCT(range1, range2) multiplies the two ranges row by row and adds the results. That is exactly Σ x·P(x).\n"
    "Select the Goals range, type a comma, then select the probability range of one striker."),
   ('work', 'sq', 'Squared distances from the mean', ['Goals X', '(x − E_A)²', '(x − E_B)²'], [[0], [1], [2], [3], [4]],
    ['=({row:0}-{ea})^2', '=({row:0}-{eb})^2'], '0.00',
    "STEP 2 – SQUARED DISTANCES\nIn the first yellow cell type =( the goals cell − the E(X) cell of Striker A )^2.\nLock the E(X) cell with F4, then fill down. Repeat for Striker B."),
   ('answers', [('va', 'b)  Var(X), Striker A', '=SUMPRODUCT({sq0},{pa})', 2, '0.00'),
                ('vb', 'b)  Var(X), Striker B', '=SUMPRODUCT({sq1},{pb})', 1.2, '0.00'),
                ('sa', 'b)  σ, Striker A', '=SQRT({va})', 1.4142, '0.00'),
                ('sb', 'b)  σ, Striker B', '=SQRT({vb})', 1.0954, '0.00')],
    "STEP 3 – VARIANCE AND σ\nVariance = SUMPRODUCT(squared distances, probabilities).\nStandard deviation = SQRT(variance)."),
   ('chart', 'Number of goals per match', 'Goals X', 'Probability', ['pa', 'pb'], 'x',
    "STEP 4 – CHART\n1. Select the three columns of the data table, including the headers.\n2. Insert → Column Chart → Clustered Column.\n"
    "3. If Excel draws Goals X as a third series, use Select Data and set it as the horizontal axis labels.\n4. Add a chart title and axis titles, and move the chart into the dashed area."),
   ('interp', 'c) Both strikers have the same expected value. Which one scores more steadily? Use the chart and σ in your answer.',
    'Striker B. Both score 2 goals per match on average, but Striker B has the smaller standard deviation (1.10 vs 1.41): B usually scores close to 2 goals, while A is just as likely to score 0 as 4.',
    "INTERPRETATION\nSame mean does not mean same distribution. A smaller σ means the values stay closer to the mean."),
  ]))

T.append(dict(sheet='Task 5', title='Task 5. The Campus Instagram Interview',
  focus='Binomial distribution  ·  k = 0 and k = n  ·  BINOM.DIST',
  task="A survey shows that 70% of students at the university follow the university’s Instagram account. The social media team picks 4 students at random to appear in a short video about a new fast-food outlet on campus. What is the probability that\n\n"
       "a) all 4 students follow the account?\nb) none of the 4 students follows the account?\nc) exactly 2 of the 4 students follow the account?",
  blocks=[
   ('params', [('n', 'n (students picked)', 4, '0'), ('p', 'p (follows the account)', 0.7, '0.00')],
    "SUCCESS = “follows the account”\nSo “all 4 follow” is k = 4, “none follows” is k = 0 and “exactly 2” is k = 2."),
   ('answers', [('a', 'a)  P(X = 4)', '=BINOM.DIST(4,{n},{p},FALSE)', 0.2401, '0.0000'),
                ('b', 'b)  P(X = 0)', '=BINOM.DIST(0,{n},{p},FALSE)', 0.0081, '0.0000'),
                ('c', 'c)  P(X = 2)', '=BINOM.DIST(2,{n},{p},FALSE)', 0.2646, '0.0000')],
    "STEPS\nAll three answers use the same function: =BINOM.DIST(k, n, p, FALSE).\nOnly k changes. Check a) and b) by hand: 0.7^4 and 0.3^4."),
   ('interp', 'Which of the three results would surprise you most if it happened in the video? Why?',
    'A video with no followers at all (P = 0.0081, less than 1%) would be the most surprising, because 70% of students follow the account.',
    "INTERPRETATION\nThe smallest probability describes the most surprising outcome."),
  ]))

T.append(dict(sheet='Task 6', title='Task 6. Lost Luggage',
  focus='Poisson distribution  ·  “at least” questions  ·  E(X) and σ',
  task="In 2007, airlines mishandled 7 bags per 1,000 passengers on average (R. Yu, USA Today, April 8, 2008). For the next 1,000 passengers, what is the probability that the airline mishandles\n\n"
       "a) no bags?\nb) at least one bag?\nc) at least two bags?\nd) How many mishandled bags should the airline expect, and what is the standard deviation?",
  blocks=[
   ('params', [('lam', 'λ (bags per 1,000 passengers)', 7, '0')],
    "AT LEAST = COMPLEMENT\nP(X ≥ 1) = 1 − P(X = 0)\nP(X ≥ 2) = 1 − P(X ≤ 1)"),
   ('answers', [('a', 'a)  P(X = 0)', '=POISSON.DIST(0,{lam},FALSE)', 0.000912, '0.000000'),
                ('b', 'b)  P(X ≥ 1)', '=1-POISSON.DIST(0,{lam},FALSE)', 0.9991, '0.0000'),
                ('c', 'c)  P(X ≥ 2)', '=1-POISSON.DIST(1,{lam},TRUE)', 0.9927, '0.0000'),
                ('d1', 'd)  E(X)', '={lam}', 7, '0'),
                ('d2', 'd)  σ', '=SQRT({lam})', 2.6458, '0.00')],
    "STEPS\nUse POISSON.DIST(k, λ, FALSE) for one exact value and TRUE for “at most k”.\nThen subtract from 1 for “at least”.\nFor a Poisson distribution E(X) = λ and σ = √λ."),
   ('interp', 'Should the airline expect a flight day with 1,000 passengers and no mishandled bags? Explain.',
    'No. P(X = 0) is only about 0.09%. With 7 bags expected, at least one mishandled bag is almost certain (99.9%).',
    "INTERPRETATION\nLook at a) and b) together."),
  ]))

T.append(dict(sheet='Task 7', title='Task 7. Will the Reel Get Shared?',
  focus='Binomial vs. Poisson approximation  ·  E(X) = np',
  task="The university posts a new reel on Instagram, and 4,000 students see it. Each student shares it with probability 0.001, independently of the others.\n\n"
       "a) How many shares can the university expect?\nb) Use the Poisson approximation to find the probability that nobody shares the reel.\n"
       "c) What is the probability that the reel is shared at least twice?",
  blocks=[
   ('params', [('n', 'n (students who see it)', 4000, '#,##0'), ('p', 'p (shares it)', 0.001, '0.000')],
    "Use λ = n·p for the Poisson approximation.\nAs an extra check, compare it with the exact binomial value."),
   ('answers', [('lam', 'a)  E(X) = λ = n·p', '={n}*{p}', 4, '0.00'),
                ('b', 'b)  P(X = 0), Poisson', '=POISSON.DIST(0,{lam},FALSE)', 0.0183, '0.0000'),
                ('bx', 'b)  check: exact binomial P(X = 0)', '=BINOM.DIST(0,{n},{p},FALSE)', 0.0183, '0.0000'),
                ('c', 'c)  P(X ≥ 2)', '=1-POISSON.DIST(1,{lam},TRUE)', 0.9084, '0.0000')],
    "HINTS\n• Compute λ in the first yellow cell and use that cell in the next formulas.\n• At least twice = 1 − P(X ≤ 1)."),
   ('interp', 'How close is the Poisson approximation to the exact binomial value? When can we use it?',
    'Practically the same (0.0183 in both cases). The Poisson approximation works well when n is large and p is small, as here.',
    "INTERPRETATION\nCompare the two values in b)."),
  ]))

T.append(dict(sheet='Task 8', title='Task 8. How Much Coffee Before the Exam?',
  focus='Valid PMF  ·  building the CDF  ·  E(X) and σ  ·  PMF chart',
  task="During the exam period, X is the number of cups of coffee a randomly chosen student drinks in one day. The table shows its probability distribution, but the value k for 3 cups is missing.\n\n"
       "a) Find k so that this is a valid PMF.\nb) Build the CDF F(x).\nc) Using the CDF, find P(X ≤ 2) and P(X > 1).\nd) Find the expected number of cups and the standard deviation.",
  blocks=[
   ('data', ['Cups X', 'P(X)', 'CDF F(x)'],
    [[0, 0.10, None], [1, 0.30, None], [2, 0.35, None], [3, ('IN', '=1-SUM({pr0},{pr1},{pr2},{pr4})', 0.2), None], [4, 0.05, None]],
    ['0', '0.00', '0.00'], ['x', 'pr', 'cdf'],
    "a) THE MISSING VALUE k\nThe yellow cell in the P(X) column is k. All probabilities must add up to 1, so k = 1 − (sum of the other four).\n\n"
    "b) CDF = RUNNING SUM\nIn the first CDF cell type =SUM($C$r:Cr), where r is the first data row. Only the first C is locked with $. Fill down and the range grows."),
   ('answers', [('c1', 'c)  P(X ≤ 2) = F(2)', '={cdf2}', 0.75, '0.00'),
                ('c2', 'c)  P(X > 1) = 1 − F(1)', '=1-{cdf1}', 0.60, '0.00'),
                ('e', 'd)  E(X)', '=SUMPRODUCT({x},{pr})', 1.8, '0.00'),
                ('v', 'd)  Var(X) = Σ (x − E(X))²·P(x)', '=SUMPRODUCT(({x}-{e})^2,{pr})', 1.06, '0.00'),
                ('s', 'd)  σ', '=SQRT({v})', 1.0296, '0.00')],
    "c) and d)\n• Read F(2) directly from the CDF column.\n• P(X > 1) = 1 − F(1).\n• E(X) with SUMPRODUCT, as in Task 4.\n"
    "• Tip: =SUMPRODUCT((x_range − E)^2, p_range) computes the variance in one formula."),
   ('chart', 'Cups of coffee per day (PMF)', 'Cups X', 'P(X)', ['pr'], 'x',
    "CHART\nSelect the Cups X and P(X) columns and insert a Column Chart. A PMF is shown with separate bars, because X takes only whole-number values."),
   ('interp', 'Describe a typical student during the exam period using E(X) and the CDF.',
    'A typical student drinks about 2 cups a day (E(X) = 1.8). 75% of students drink at most 2 cups, and 60% drink more than one cup.',
    "INTERPRETATION\nUse the numbers you found in c) and d)."),
  ]))

T.append(dict(sheet='Task 9', title='Task 9. Guessing on a Quiz',
  focus='Binomial distribution  ·  E(X), Var(X), σ  ·  full PMF table and chart',
  task="A quiz has 20 multiple-choice questions, each with 4 options and only one correct answer. A student who did not study guesses every answer at random. Let X be the number of correct answers.\n\n"
       "a) Explain why X follows a binomial distribution and write down n and p.\nb) Find the expected value, the variance and the standard deviation of X.\n"
       "c) What is the probability that the student gets exactly 5 answers right?\nd) The student needs at least 10 correct answers to pass. What is the probability of passing by guessing?",
  blocks=[
   ('params', [('n', 'n (questions)', 20, '0'), ('p', 'p (correct guess)', 0.25, '0.00')],
    "a) Write your explanation in the interpretation area at the bottom. The two blue cells already give n and p."),
   ('answers', [('e', 'b)  E(X) = n·p', '={n}*{p}', 5, '0.00'),
                ('v', 'b)  Var(X) = n·p·(1 − p)', '={n}*{p}*(1-{p})', 3.75, '0.00'),
                ('s', 'b)  σ', '=SQRT({v})', 1.9365, '0.00'),
                ('c', 'c)  P(X = 5)', '=BINOM.DIST(5,{n},{p},FALSE)', 0.2023, '0.0000'),
                ('d', 'd)  P(X ≥ 10)', '=1-BINOM.DIST(9,{n},{p},TRUE)', 0.0139, '0.0000')],
    "Less guidance from here on: you already know these functions.\nRemember: “at least 10” = 1 − P(X ≤ 9)."),
   ('work', 'pmf', 'Full PMF for k = 0 to 20', ['k', 'P(X = k)'], [[k] for k in range(21)],
    ['=BINOM.DIST({row:0},{n},{p},FALSE)'], '0.0000',
    "PMF TABLE AND CHART\nFill the first yellow cell, then fill down to k = 20. Then select both columns and insert a Column Chart.\nWhere is the highest bar? Compare it with E(X)."),
   ('chart', 'Number of correct answers by guessing', 'k', 'P(X = k)', ['pmf'], 'pmfk', None),
   ('interp', 'a) Why is X binomial? And is guessing a good strategy for passing the quiz?',
    'Fixed n = 20 independent questions, each answer is right or wrong, and p = 0.25 is the same for every question, so X ~ Binomial(20, 0.25). Guessing gives about 5 correct answers and passes only about 1.4% of the time, so it is not a good strategy.',
    None),
  ]))

T.append(dict(sheet='Task 10', title='Task 10. Hunting for a Rare Skin',
  focus='Geometric distribution  ·  first success  ·  E(X) = 1/p',
  task="In an online game, each loot drop gives a rare skin with probability 0.05, independently of all other drops. A player keeps opening drops until the first rare skin appears. Let X be the number of drops needed.\n\n"
       "a) What is the probability that the first rare skin appears on the 5th drop?\nb) What is the probability that the player gets it within the first 10 drops?\n"
       "c) What is the probability that the player needs more than 10 drops?\nd) Find the expected number of drops and the standard deviation of X.",
  blocks=[
   ('params', [('p', 'p (rare skin per drop)', 0.05, '0.00')],
    "NO BUILT-IN FUNCTION\nExcel has no GEOM.DIST, so type the formulas from Table 2 of the lab:\n"
    "P(X = k) = (1 − p)^(k − 1)·p\nP(X ≤ k) = 1 − (1 − p)^k\nE(X) = 1/p     σ² = (1 − p)/p²"),
   ('answers', [('a', 'a)  P(X = 5)', '=(1-{p})^(5-1)*{p}', 0.0407, '0.0000'),
                ('b', 'b)  P(X ≤ 10)', '=1-(1-{p})^10', 0.4013, '0.0000'),
                ('c', 'c)  P(X > 10)', '=(1-{p})^10', 0.5987, '0.0000'),
                ('d1', 'd)  E(X) = 1/p', '=1/{p}', 20, '0.00'),
                ('d2', 'd)  σ', '=SQRT((1-{p})/{p}^2)', 19.4936, '0.00')],
    "Check: b) and c) must add up to 1."),
   ('interp', 'On average a player needs 20 drops. Why do many players still have no rare skin after 20 drops?',
    'The spread is very large (σ ≈ 19.5). More than half of the players have no rare skin after 10 drops (0.5987), and about 36% still have none after 20 drops (0.95^20 ≈ 0.358).',
    None),
  ]))


# ------------------------------------------------------------------ builder
def col(c):
    return xlsxwriter.utility.xl_col_to_name(c)

def ref(r, c, absolute=True):
    return xlsxwriter.utility.xl_rowcol_to_cell(r, c, row_abs=absolute, col_abs=absolute)

def lines(text):
    return sum(max(1, math.ceil(len(t) / CHARS)) for t in text.split('\n'))

def box_h(text, extra=22):
    return lines(text) * 15 + extra

def build(solutions):
    fn = os.path.join(OUT, f'{NAME} – {"Solutions" if solutions else "Students"}.xlsx')
    wb = xlsxwriter.Workbook(fn, {'use_future_functions': True})
    wb.set_properties({'title': f'{NAME} – {"Solutions" if solutions else "Students"}', 'author': 'Emina Osmić'})
    F = lambda **k: wb.add_format(dict({'font_name': 'Arial', 'font_size': 10, 'valign': 'vcenter'}, **k))
    f_title = F(bold=True, font_size=16, font_color=NAVY)
    f_focus = F(italic=True, font_color=MUTED)
    f_sec = F(bold=True, font_size=11, font_color=NAVY, bottom=2, bottom_color=GOLD)
    f_lab = F(border=1, border_color=BOX_LINE)
    f_head = F(bold=True, font_color='#FFFFFF', bg_color=HEAD, border=1, border_color=HEAD, align='center')
    f_tag = F(bold=True, font_size=8, font_color=GOLD, align='center')
    num = {}
    def fmt(kind, nf):
        key = (kind, nf)
        if key not in num:
            base = dict(num_format=nf, border=1, align='center')
            if kind == 'given': base.update(bg_color=GIVEN, border_color='#9DC3E6')
            elif kind == 'input': base.update(bg_color=INPUT, border_color=GOLD)
            elif kind == 'data': base.update(border_color=BOX_LINE)
            num[key] = F(**base)
        return num[key]
    f_ans = F(bg_color=INPUT, border=1, border_color=GOLD, text_wrap=True, valign='top')

    def setup(ws):
        ws.set_column('A:A', 2); ws.set_column('B:E', 13); ws.set_column('F:F', 15); ws.set_column('G:H', 11)
        ws.set_column('I:I', 3); ws.set_column('J:P', 10)
        ws.set_zoom(100)

    def textbox(ws, row, colname, text, width, h, fill, line=BOX_LINE, bold=False, size=10, color='#202020'):
        ws.insert_textbox(f'{colname}{row + 1}', text, {
            'width': width, 'height': h, 'x_offset': 2, 'y_offset': 4,
            'font': {'name': 'Arial', 'size': size, 'color': color, 'bold': bold},
            'align': {'vertical': 'top'}, 'fill': {'color': fill}, 'line': {'color': line, 'width': 1},
            'object_position': 1})

    # ---------------- Start sheet
    ws = wb.add_worksheet('Start'); setup(ws)
    ws.write('B2', f'Lab 4 – Probability of Discrete Random Variables' + (' – SOLUTIONS' if solutions else ''), f_title)
    ws.write('B3', 'FENMS 0021 Probability and Statistics  ·  International Burch University', f_focus)
    intro = ("HOW TO USE THIS WORKBOOK\n"
             "Each task has its own sheet. The task and your work are on the LEFT. Step-by-step help is on the RIGHT, next to the part it explains.\n\n"
             "Work through the tasks in order. The help becomes shorter in later tasks, because you already know the functions. "
             "The tasks you do not finish in class can be completed at home.\n\n"
             + ("This is the SOLUTIONS workbook: every yellow cell contains the formula used. Click a cell and read the formula bar." if solutions else
                "Always type a formula (starting with =) in the yellow cells, so that you can check your work by clicking the cell."))
    textbox(ws, 4, 'B', intro, 640, box_h(intro, 26) + 10, BOX_TASK)
    r0 = 4 + math.ceil((box_h(intro, 26) + 20) / PX_ROW) + 1
    ws.write(r0, 1, 'Cell colours', f_sec)
    ws.write(r0 + 1, 1, '', fmt('given', '0')); ws.write(r0 + 1, 2, 'given data (do not change)', F())
    ws.write(r0 + 2, 1, '', fmt('input', '0')); ws.write(r0 + 2, 2, 'YOUR FORMULA / RESULT', F(bold=True))
    ws.write(r0 + 3, 1, '', f_ans); ws.write(r0 + 3, 2, 'YOUR INTERPRETATION (write in words)', F(bold=True))
    r1 = r0 + 6
    ws.write(r1, 1, 'Excel functions for this lab', f_sec)
    funcs = [('Distribution', 'Exact P(X = k)', 'Cumulative P(X ≤ k)'),
             ('Binomial', '=BINOM.DIST(k, n, p, FALSE)', '=BINOM.DIST(k, n, p, TRUE)'),
             ('Poisson', '=POISSON.DIST(k, λ, FALSE)', '=POISSON.DIST(k, λ, TRUE)'),
             ('Geometric', '=(1-p)^(k-1)*p', '=1-(1-p)^k'),
             ('Expected value', '=SUMPRODUCT(values, probabilities)', '')]
    for i, (a, b, c) in enumerate(funcs):
        f = f_head if i == 0 else f_lab
        ws.write_string(r1 + 1 + i, 1, a, f)
        ws.merge_range(r1 + 1 + i, 2, r1 + 1 + i, 4, '', f); ws.write_string(r1 + 1 + i, 2, b, f)
        ws.merge_range(r1 + 1 + i, 5, r1 + 1 + i, 7, '', f); ws.write_string(r1 + 1 + i, 5, c, f)
    r2 = r1 + 8
    ws.write(r2, 1, 'Tasks', f_sec)
    for i, t in enumerate(T):
        ws.write_url(r2 + 1 + i, 1, f"internal:'{t['sheet']}'!A1", F(font_color=BLUE, underline=1), t['title'])
    ws.activate(); ws.set_landscape(); ws.fit_to_pages(1, 1); ws.set_paper(9); ws.print_area(0, 0, r2 + 12, 9)

    # ---------------- task sheets
    for t in T:
        ws = wb.add_worksheet(t['sheet']); setup(ws)
        ws.write('B2', t['title'], f_title)
        ws.write('B3', 'Learning focus:  ' + t['focus'], f_focus)
        th = box_h(t['task'], 26)
        textbox(ws, 4, 'B', t['task'], 640, th, BOX_TASK, line=NAVY)
        textbox(ws, 4, 'J', 'HELP FOR THIS TASK\nRead the boxes on this side from top to bottom. Each box sits next to the part of the sheet it explains.',
                470, box_h('x' * 120, 22), BOX_HELP, color=NAVY)
        row = 4 + math.ceil((th + 10) / PX_ROW) + 1
        names = {}
        rng = {}

        def sub(s, extra=None):
            def rep(m):
                k = m.group(1)
                if extra and k in extra: return extra[k]
                if k in names: return names[k]
                if k in rng: return rng[k]
                raise KeyError(k)
            return re.sub(r'\{([^{}]+)\}', rep, s)

        for blk in t['blocks']:
            kind = blk[0]
            start = row
            guide = blk[-1]
            if kind == 'params':
                ws.write(row, 1, 'Given data', f_sec); row += 1
                for key, label, val, nf in blk[1]:
                    ws.merge_range(row, 1, row, 3, label, f_lab)
                    if isinstance(val, str): ws.write_formula(row, 4, val, fmt('given', nf), eval(val[1:]))
                    else: ws.write_number(row, 4, val, fmt('given', nf))
                    names[key] = ref(row, 4); row += 1
            elif kind == 'data':
                heads, rows_, nfs, keys = blk[1], blk[2], blk[3], blk[4]
                ws.write(row, 1, 'Data', f_sec); row += 1
                for j, h in enumerate(heads): ws.write(row, 1 + j, h, f_head)
                row += 1; r_first = row
                for i, rr in enumerate(rows_):
                    for j, v in enumerate(rr):
                        c = 1 + j
                        if v is None:
                            # empty work cell (e.g. CDF): student fills it
                            if solutions: ws.write_formula(row, c, f'=SUM({ref(r_first, c - 1, True)}:{ref(row, c - 1, False)})', fmt('input', nfs[j]))
                            else: ws.write_blank(row, c, None, fmt('input', nfs[j]))
                        elif isinstance(v, tuple):
                            for jj in range(len(rows_)):
                                rng[f'{keys[j]}{jj}'] = ref(r_first + jj, c)
                            if solutions: ws.write_formula(row, c, sub(v[1]), fmt('input', nfs[j]), v[2])
                            else: ws.write_blank(row, c, None, fmt('input', nfs[j]))
                        else:
                            ws.write_number(row, c, v, fmt('data', nfs[j]))
                    row += 1
                for j, k in enumerate(keys):
                    rng[k] = f'{ref(r_first, 1 + j)}:{ref(row - 1, 1 + j)}'
                    for jj in range(len(rows_)): rng[f'{k}{jj}'] = ref(r_first + jj, 1 + j)
                rng['_first'], rng['_n'] = r_first, len(rows_)
            elif kind == 'work':
                key, title, heads, rows_, formulas, nf = blk[1:7]
                ws.write(row, 1, title, f_sec); row += 1
                c0, lead = 1, len(rows_[0])
                for j, h in enumerate(heads): ws.write(row, c0 + j, h, f_head)
                row += 1; r_first = row
                for i, rr in enumerate(rows_):
                    for j, v in enumerate(rr): ws.write_number(row, c0 + j, v, fmt('data', '0'))
                    for j, fm in enumerate(formulas):
                        c = c0 + lead + j
                        extra = {'row:0': ref(row, c0, False)}
                        if solutions: ws.write_formula(row, c, sub(fm, extra), fmt('input', nf))
                        else: ws.write_blank(row, c, None, fmt('input', nf))
                    row += 1
                for j in range(len(formulas)):
                    c = c0 + lead + j
                    rng[f'{key}{j}' if len(formulas) > 1 else key] = f'{ref(r_first, c)}:{ref(row - 1, c)}'
                rng[key + 'k'] = f'{ref(r_first, c0)}:{ref(row - 1, c0)}'
            elif kind == 'answers':
                ws.write(row, 1, 'Your answers' if start == row else '', f_sec)
                ws.write(row, 5, 'YOUR FORMULA', f_tag); row += 1
                for key, label, fm, val, nf in blk[1]:
                    ws.merge_range(row, 1, row, 4, label, f_lab)
                    if solutions: ws.write_formula(row, 5, sub(fm), fmt('input', nf), val)
                    else: ws.write_blank(row, 5, None, fmt('input', nf))
                    names[key] = ref(row, 5); row += 1
            elif kind == 'chart':
                title, xt, yt, series, cat = blk[1:6]
                ws.write(row, 1, 'CREATE CHART HERE' if not solutions else 'Chart', f_sec); row += 1
                h_rows = 15
                if solutions:
                    ch = wb.add_chart({'type': 'column'})
                    colors = [BLUE, GOLD]
                    for i, s in enumerate(series):
                        a, b = rng[s].split(':')
                        hdr_r, hdr_c = xlsxwriter.utility.xl_cell_to_rowcol(a.replace('$', ''))
                        ch.add_series({'name': [t['sheet'], hdr_r - 1, hdr_c] if s != 'pmf' else 'P(X = k)',
                                       'categories': f"='{t['sheet']}'!{rng[cat]}", 'values': f"='{t['sheet']}'!{rng[s]}",
                                       'fill': {'color': colors[i % 2]}, 'gap': 60})
                    ch.set_title({'name': title, 'name_font': {'name': 'Arial', 'size': 11, 'color': NAVY}})
                    ch.set_x_axis({'name': xt, 'name_font': {'name': 'Arial', 'size': 9}, 'num_font': {'name': 'Arial', 'size': 9}})
                    ch.set_y_axis({'name': yt, 'name_font': {'name': 'Arial', 'size': 9}, 'num_font': {'name': 'Arial', 'size': 9}, 'major_gridlines': {'visible': True, 'line': {'color': '#E6E6E6'}}})
                    ch.set_legend({'position': 'bottom' if len(series) > 1 else 'none', 'font': {'name': 'Arial', 'size': 9}})
                    ch.set_size({'width': 640, 'height': h_rows * PX_ROW - 10})
                    ws.insert_chart(row, 1, ch, {'x_offset': 2, 'y_offset': 2, 'object_position': 1})
                else:
                    ws.insert_textbox(row, 1, 'Place your chart here', {
                        'width': 640, 'height': h_rows * PX_ROW - 10, 'x_offset': 2, 'y_offset': 2,
                        'font': {'name': 'Arial', 'size': 10, 'color': '#9AA4AE', 'italic': True},
                        'align': {'vertical': 'middle', 'horizontal': 'center'},
                        'fill': {'none': True}, 'line': {'color': '#9AA4AE', 'width': 1, 'dash_type': 'dash'}, 'object_position': 1})
                row += h_rows
            elif kind == 'interp':
                q, model = blk[1], blk[2]
                ws.write(row, 1, 'Interpretation', f_sec); row += 1
                qh = box_h(q, 14)
                textbox(ws, row, 'B', q, 640, qh, BOX_TASK, line=BOX_LINE, color=NAVY, bold=True)
                row += math.ceil((qh + 8) / PX_ROW)
                ws.write(row, 1, 'YOUR INTERPRETATION', f_tag); row += 1
                ws.merge_range(row, 1, row + 3, 7, model if solutions else '', f_ans)
                row += 4
            # guidance box aligned with the start of the block
            if guide:
                g = re.sub(r'\{(\w+)\}', lambda m: names.get(m.group(1), m.group(0)), guide)
                if solutions and kind == 'answers':
                    g = guide + '\n\nSOLUTION: click a yellow cell to see the formula in the formula bar.'
                gh = box_h(g)
                textbox(ws, start, 'J', g, 470, gh, BOX_HELP)
                row = max(row, start + math.ceil((gh + 8) / PX_ROW))
            row += 2
        ws.set_landscape(); ws.fit_to_pages(1, 0); ws.set_paper(9)
        ws.print_area(0, 0, row, 15)
    wb.close()
    return fn

if __name__ == '__main__':
    for s in (False, True):
        print(build(s))
