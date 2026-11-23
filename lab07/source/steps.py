"""Step-by-step content for the Lab 7 workbooks (same layout as Lab 6):
each step = manual explanation -> formula picture(s) -> Excel cells for that step -> Excel note -> green answer; tips on the right.
Every task follows the five steps of a hypothesis test."""


def S(text=None, f=(), cells=(), xl=None, ans=None, tip=None, tipred=False):
    return dict(text=text, f=list(f), cells=list(cells), xl=xl, ans=ans, tip=tip, tipred=tipred)


SIGN = {'two': r'\neq', 'right': '>', 'left': '<'}
H0SIGN = {'two': '=', 'right': r'\leq', 'left': r'\geq'}
TAILNAME = {'two': 'two-tailed', 'right': 'right-tailed', 'left': 'left-tailed'}
TIP_KEYWORDS = ('HOW DO I CHOOSE THE TYPE OF TEST?\n• “different”, “changed” → two-tailed (≠)\n• “more than”, “increased” → right-tailed (>)\n'
                '• “less than”, “decreased” → left-tailed (<)\nA claim with “at least” or “no more than” contains the equal sign, so it goes into H₀.')


def head(given, find, concept_tip):
    return S(f'What is given? {given}\nWhat do we need to find? {find}', tip='WHICH TEST?\n' + concept_tip)


def hyp(sym, v, tail, why, ans):
    return S(f'Step 1. State the hypotheses. {why}',
             f=[rf'H_0:\ {sym} {H0SIGN[tail]} {v} \qquad H_1:\ {sym} {SIGN[tail]} {v}'],
             ans=ans, tip=TIP_KEYWORDS)


def crit_z(a, tail, zc, cell='zc'):
    if tail == 'two':
        txt, tex, xl = (f'Step 2. α = {a:g}. In a two-tailed test α is split between both tails, so we need z for the area 1 − α/2 = {1 - a / 2:g}.',
                        rf'z_{{\alpha/2}}=z_{{{a / 2:g}}}=\pm {zc:.3f}'.replace('.000', '.00'),
                        f'Excel: =NORM.S.INV(1-{a:g}/2) gives the positive critical value.')
    elif tail == 'right':
        txt, tex, xl = (f'Step 2. α = {a:g}. In a right-tailed test the whole α is in the right tail, so we need z for the area 1 − α = {1 - a:g}.',
                        rf'z_{{\alpha}}=z_{{{a:g}}}={zc:.3f}', f'Excel: =NORM.S.INV({1 - a:g}) gives the critical value.')
    else:
        txt, tex, xl = (f'Step 2. α = {a:g}. In a left-tailed test the whole α is in the left tail, so the critical value is negative.',
                        rf'-z_{{\alpha}}=-z_{{{a:g}}}=-{abs(zc):.3f}', f'Excel: =-NORM.S.INV({1 - a:g}) gives the critical value.')
    return S(txt, f=[tex], cells=[cell], xl=xl,
             tip='THE CRITICAL VALUE\nis the border of the rejection region. It depends only on α and on the type of test, not on the data.')


def crit_t(a, tail, n, tc):
    df = n - 1
    if tail == 'two':
        return S(f'Step 2. α = {a:g} and σ is unknown, so the critical values come from the t-table with df = n − 1 = {df} and α/2 = {a / 2:g} in each tail.',
                 f=[rf'df={n}-1={df} \qquad t_{{\alpha/2,\,df}}=t_{{{a / 2:g},\,{df}}}=\pm {tc:.3f}'], cells=['df', 'tc'],
                 xl=f'Excel: =T.INV.2T({a:g}, {df}) gives the positive two-tailed critical value.',
                 tip='WHY t AND NOT z?\n• σ is unknown, so we use the sample standard deviation s.\n• The sample is small and approximately normal.\nThe t critical value is a bit larger than z, because s adds extra uncertainty.')
    raise ValueError


def decision(text, f, ans, tip=None, tipred=False, cells=()):
    return S('Step 5. Make a decision and write a conclusion. ' + text, f=f, cells=cells, ans=ans, tip=tip, tipred=tipred)


STEPS = {}

# ---------------------------------------------------------------- Task 1: sleep, z, two-tailed
STEPS[1] = [
    head('μ₀ = 7 hours (the claim), n = 40 students, x̄ = 6.6 hours, σ = 1.2 hours (known), α = 0.05.',
         'whether the mean sleep time of students is different from 7 hours.',
         'σ is known, so we use the z-test for a mean. The question asks about a “different” amount, so the test is two-tailed.'),
    hyp(r'\mu', 7, 'two', 'The claim is about the population mean, and “different” means ≠:', 'H₀: μ = 7, H₁: μ ≠ 7 (two-tailed z-test).'),
    crit_z(0.05, 'two', 1.96),
    S('Step 3. Calculate the test statistic. First the standard error σ/√n, then z:',
      f=[r'\frac{\sigma}{\sqrt{n}}=\frac{1.2}{\sqrt{40}}\approx 0.1897 \qquad z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}=\frac{6.6-7}{0.1897}\approx -2.11'],
      cells=['se', 'z'], xl='Excel: type the numbers directly: =1.2/SQRT(40) and =(6.6-7)/(1.2/SQRT(40)).',
      tip='WHAT DOES z = −2.11 MEAN?\nThe sample mean is 2.11 standard errors BELOW the claimed 7 hours.'),
    S('Step 4. Find the p-value. The test is two-tailed, so we double the area in the tail:',
      f=[r'p=2\cdot P(Z<-2.11)=2\cdot 0.0174=0.0348'], cells=['p'],
      xl='Excel: =2*NORM.S.DIST(-2.108, TRUE). For a negative z, NORM.S.DIST already gives the left tail.',
      tip='WHY DO WE DOUBLE IT?\nIn a two-tailed test, a result as extreme as ours could happen on either side, so p counts both tails.'),
    decision('−2.11 < −1.96 and p = 0.0348 < 0.05.', [r'z=-2.11<-1.96 \qquad p=0.0348<0.05'],
             'Answer: we reject H₀. At the 5% significance level, students in Sarajevo do not sleep 7 hours per night on average; the data suggest that they sleep less.',
             tip='COMMON MISTAKE\nWriting “H₀: x̄ = 7”. Hypotheses are always about the population mean μ, never about the sample mean x̄.', tipred=True),
]

# ---------------------------------------------------------------- Task 2: phone bills, z, right-tailed, alpha 0.10
STEPS[2] = [
    head('μ₀ = $52 (the claim), n = 64 customers, x̄ = $53.10, σ = $10 (known), α = 0.10.',
         'whether the average monthly bill is now more than $52.',
         'σ is known, so we use the z-test for a mean. The manager thinks the bills have increased, so the test is right-tailed.'),
    hyp(r'\mu', 52, 'right', '“More than $52” is the new idea, so it goes into H₁:', 'H₀: μ ≤ 52, H₁: μ > 52 (right-tailed z-test).'),
    crit_z(0.10, 'right', 1.2816),
    S('Step 3. Calculate the test statistic:',
      f=[r'\frac{\sigma}{\sqrt{n}}=\frac{10}{\sqrt{64}}=1.25 \qquad z=\frac{53.10-52}{1.25}=0.88'],
      cells=['se', 'z'], xl='Excel: =10/SQRT(64) and =(53.1-52)/(10/SQRT(64)).'),
    S('Step 4. Find the p-value. The test is right-tailed, so p is the area to the RIGHT of z:',
      f=[r'p=P(Z>0.88)=1-0.8106=0.1894'], cells=['p'],
      xl='Excel: =1-NORM.S.DIST(0.88, TRUE). NORM.S.DIST gives the area to the left, so we subtract it from 1.',
      tip='NORM.S.DIST(z, TRUE)\nalways returns the area to the LEFT of z, like the Z-table. For a right tail, use 1 − NORM.S.DIST(z, TRUE).'),
    decision('0.88 < 1.282 and p = 0.1894 > 0.10.', [r'z=0.88<1.282 \qquad p=0.1894>0.10'],
             'Answer: we fail to reject H₀. The data do not support the manager’s claim that the average bill has increased above $52.',
             tip='COMMON MISTAKE\nConcluding that the average bill is exactly $52. “Fail to reject H₀” only means that the sample does not give enough evidence of an increase.', tipred=True),
]

# ---------------------------------------------------------------- Task 3: gaming, z, two-tailed
STEPS[3] = [
    head('μ₀ = 3 hours (the platform’s average), σ = 0.8 hours (known), n = 100 students, x̄ = 2.82 hours, α = 0.05.',
         'whether IBU students play a different amount than the platform’s average.',
         'σ is known, so we use the z-test for a mean. “A different amount” means a two-tailed test.'),
    hyp(r'\mu', 3, 'two', 'The question asks about a different amount:', 'H₀: μ = 3, H₁: μ ≠ 3 (two-tailed z-test).'),
    crit_z(0.05, 'two', 1.96),
    S('Step 3. Calculate the test statistic:',
      f=[r'\frac{\sigma}{\sqrt{n}}=\frac{0.8}{\sqrt{100}}=0.08 \qquad z=\frac{2.82-3}{0.08}=-2.25'],
      cells=['se', 'z'], xl='Excel: =0.8/SQRT(100) and =(2.82-3)/(0.8/SQRT(100)).'),
    S('Step 4. Find the p-value (two-tailed):', f=[r'p=2\cdot P(Z<-2.25)=2\cdot 0.0122=0.0244'], cells=['p'],
      xl='Excel: =2*NORM.S.DIST(-2.25, TRUE).',
      tip='BOTH METHODS, ONE DECISION\nThe critical value method (compare z with ±1.96) and the p-value method (compare p with α) always lead to the same decision.'),
    decision('−2.25 < −1.96 and p = 0.0244 < 0.05.', [r'z=-2.25<-1.96 \qquad p=0.0244<0.05'],
             'Answer: we reject H₀. IBU students play a different amount than the platform’s average; the sample suggests that they play less.'),
]

# ---------------------------------------------------------------- Task 4: battery app, t, two-tailed
STEPS[4] = [
    head('μ₀ = 168 minutes (the website’s claim), n = 25 laptops, x̄ = 172.5 minutes, s = 15.4 minutes, α = 0.05.',
         'whether the true average battery life with the app is different from 168 minutes.',
         'σ is unknown (we only have s) and the sample is small, so we use the t-test for a mean with df = n − 1. “Different” means two-tailed.'),
    hyp(r'\mu', 168, 'two', '“Different from 168 minutes” means ≠:', 'H₀: μ = 168, H₁: μ ≠ 168 (two-tailed t-test).'),
    crit_t(0.05, 'two', 25, 2.064),
    S('Step 3. Calculate the test statistic with s in place of σ:',
      f=[r'\frac{s}{\sqrt{n}}=\frac{15.4}{\sqrt{25}}=3.08 \qquad t=\frac{172.5-168}{3.08}\approx 1.46'],
      cells=['se', 't'], xl='Excel: =15.4/SQRT(25) and =(172.5-168)/(15.4/SQRT(25)).'),
    S('Step 4. Find the p-value. The t-table only gives critical values, so we use Excel:', f=[r'p=2\cdot P(T_{24}>1.46)\approx 0.157'], cells=['p'],
      xl='Excel: =T.DIST.2T(1.461, 24) gives the two-tailed p-value directly (t must be positive).',
      tip='T.DIST.2T(t, df)\nworks only with a positive t. For a negative t, use the absolute value: =T.DIST.2T(ABS(t), df).'),
    decision('−2.064 < 1.46 < 2.064 and p ≈ 0.157 > 0.05.', [r'-2.064<t=1.46<2.064 \qquad p\approx 0.157>0.05'],
             'Answer: we fail to reject H₀. The data do not show that the battery life differs from 168 minutes. The students cannot say that the website is wrong, but the test does not prove that it is right either.',
             tip='“FAIL TO REJECT” ≠ “ACCEPT”\nThe sample simply does not give enough evidence against the claim. A larger sample might.', tipred=True),
]

# ---------------------------------------------------------------- Task 5: AI homework, proportion, right-tailed
STEPS[5] = [
    head('π₀ = 0.30 (the faculty’s claim), n = 150 students, x = 57 use AI tools, α = 0.05.',
         'whether more than 30% of students use AI tools to write their homework.',
         'The claim is about a percentage, so we use the z-test for a proportion. The newspaper suspects “more than 30%”, so the test is right-tailed.'),
    S('a) First the sample proportion, and the check that the sample is large enough:',
      f=[r'p=\frac{57}{150}=0.38 \qquad n\pi_0=150\cdot 0.30=45\geq 5 \qquad n(1-\pi_0)=150\cdot 0.70=105\geq 5'],
      cells=['p', 'c1', 'c2'], xl='Excel: =57/150, =150*0.3 and =150*(1-0.3).', ans='Answer: p = 0.38, and the sample is large enough.'),
    hyp(r'\pi', '0.30', 'right', '“No more than 30%” contains the equal sign, so it goes into H₀:', 'H₀: π ≤ 0.30, H₁: π > 0.30 (right-tailed z-test).'),
    crit_z(0.05, 'right', 1.645),
    S('Step 3. Calculate the standard error with π₀ (not p!) and the test statistic:',
      f=[r'\sigma_p=\sqrt{\frac{0.30\cdot 0.70}{150}}\approx 0.0374 \qquad z=\frac{0.38-0.30}{0.0374}\approx 2.14'],
      cells=['se', 'z'], xl='Excel: =SQRT(0.3*0.7/150) and =(0.38-0.3)/SQRT(0.3*0.7/150).',
      tip='COMMON MISTAKE\nUsing p = 0.38 in the standard error. In a test we assume that H₀ is true, so we use π₀ = 0.30.', tipred=True),
    S('Step 4. Find the p-value (right tail):', f=[r'p=P(Z>2.14)=1-0.9838=0.0162'], cells=['pv'],
      xl='Excel: =1-NORM.S.DIST(2.138, TRUE).'),
    decision('2.14 > 1.645 and p ≈ 0.016 < 0.05.', [r'z=2.14>1.645 \qquad p\approx 0.016<0.05'],
             'Answer: we reject H₀. The newspaper can write that the data contradict the faculty’s claim: more than 30% of students use AI tools to write their homework.'),
]

# ---------------------------------------------------------------- Task 6: smartwatch, z, left-tailed
STEPS[6] = [
    head('μ₀ = 8000 steps (the company’s claim), σ = 1800 steps (known), n = 36 students, x̄ = 7350 steps, α = 0.05.',
         'whether the data support the claim that users walk at least 8000 steps per day.',
         'σ is known, so we use the z-test for a mean. The claim is “at least 8000”, so H₁ is “< 8000” and the test is left-tailed.'),
    hyp(r'\mu', 8000, 'left', '“At least 8000” contains the equal sign, so it goes into H₀:', 'H₀: μ ≥ 8000, H₁: μ < 8000 (left-tailed z-test).'),
    crit_z(0.05, 'left', 1.645),
    S('Step 3. Calculate the test statistic:',
      f=[r'\frac{\sigma}{\sqrt{n}}=\frac{1800}{\sqrt{36}}=300 \qquad z=\frac{7350-8000}{300}\approx -2.17'],
      cells=['se', 'z'], xl='Excel: =1800/SQRT(36) and =(7350-8000)/(1800/SQRT(36)).'),
    S('Step 4. Find the p-value. The test is left-tailed, so p is the area to the LEFT of z:', f=[r'p=P(Z<-2.17)=0.0150'], cells=['p'],
      xl='Excel: =NORM.S.DIST(-2.167, TRUE) gives the left-tail area directly.'),
    decision('−2.17 < −1.645 and p = 0.015 < 0.05.', [r'z=-2.17<-1.645 \qquad p=0.015<0.05'],
             'Answer: we reject H₀. The data do not support the company’s claim: users walk fewer than 8000 steps per day on average.'),
]

# ---------------------------------------------------------------- Task 7: deployments, proportion, right-tailed, alpha 0.01
STEPS[7] = [
    head('π₀ = 0.08 (the company’s claim), n = 200 deployments, x = 21 with critical bugs, α = 0.01.',
         'whether more than 8% of the deployments have critical bugs, and whether the decision changes at α = 0.10.',
         'The claim is about a percentage, so we use the z-test for a proportion, right-tailed (“more than 8%”).'),
    S('a) The sample proportion and the check:',
      f=[r'p=\frac{21}{200}=0.105 \qquad n\pi_0=200\cdot 0.08=16\geq 5 \qquad n(1-\pi_0)=200\cdot 0.92=184\geq 5'],
      cells=['p', 'c1', 'c2'], xl='Excel: =21/200, =200*0.08 and =200*(1-0.08).', ans='Answer: p = 0.105, and the sample is large enough.'),
    hyp(r'\pi', '0.08', 'right', '“No more than 8%” contains the equal sign, so it goes into H₀:', 'H₀: π ≤ 0.08, H₁: π > 0.08 (right-tailed z-test).'),
    crit_z(0.01, 'right', 2.326),
    S('Step 3. Calculate the standard error with π₀ and the test statistic:',
      f=[r'\sigma_p=\sqrt{\frac{0.08\cdot 0.92}{200}}\approx 0.0192 \qquad z=\frac{0.105-0.08}{0.0192}\approx 1.30'],
      cells=['se', 'z'], xl='Excel: =SQRT(0.08*0.92/200) and =(0.105-0.08)/SQRT(0.08*0.92/200).'),
    S('Step 4. Find the p-value (right tail):', f=[r'p=P(Z>1.30)=1-0.9032=0.0968'], cells=['pv'], xl='Excel: =1-NORM.S.DIST(1.303, TRUE).'),
    decision('1.30 < 2.326 and p ≈ 0.097 > 0.01.', [r'z=1.30<2.326 \qquad p\approx 0.097>0.01'],
             'Answer: we fail to reject H₀ at α = 0.01: the data are not strong enough to say that more than 8% of the deployments have critical bugs.'),
    S('c) What happens at α = 0.10? The critical value becomes z₀.₁₀ = 1.282:', f=[r'z=1.30>1.282 \qquad p\approx 0.097<0.10'], cells=['zc10'],
      xl='Excel: =NORM.S.INV(0.90).',
      ans='Answer: yes, the decision changes: at α = 0.10 we would reject H₀.',
      tip='WHY CHOOSE α BEFORE THE TEST?\nThe same data give different decisions for different α. Choosing α after seeing p would let us pick the answer we like.'),
]

# ---------------------------------------------------------------- Task 8: hit songs, t, two-tailed, alpha 0.10
STEPS[8] = [
    head('μ₀ = 3 minutes (the blog’s claim), n = 25 songs, x̄ = 3.4 minutes, s = 0.9 minutes, α = 0.10.',
         'whether the average length of hit songs is different from 3 minutes.',
         'σ is unknown and the sample is small, so we use the t-test for a mean with df = n − 1 = 24. “Different” means two-tailed.'),
    hyp(r'\mu', 3, 'two', '“Different from 3 minutes” means ≠:', 'H₀: μ = 3, H₁: μ ≠ 3 (two-tailed t-test).'),
    crit_t(0.10, 'two', 25, 1.711),
    S('Step 3. Calculate the test statistic:',
      f=[r'\frac{s}{\sqrt{n}}=\frac{0.9}{\sqrt{25}}=0.18 \qquad t=\frac{3.4-3}{0.18}\approx 2.22'],
      cells=['se', 't'], xl='Excel: =0.9/SQRT(25) and =(3.4-3)/(0.9/SQRT(25)).'),
    S('Step 4. Find the p-value with Excel:', f=[r'p=2\cdot P(T_{24}>2.22)\approx 0.036'], cells=['p'], xl='Excel: =T.DIST.2T(2.222, 24).'),
    decision('2.22 > 1.711 and p ≈ 0.036 < 0.10.', [r't=2.22>1.711 \qquad p\approx 0.036<0.10'],
             'Answer: we reject H₀. At the 10% significance level, the average length of hit songs is different from 3 minutes; the sample suggests that it is longer.'),
]
