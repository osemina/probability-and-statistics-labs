"""Step-by-step content for the Lab 8 workbooks (same layout as Labs 6 and 7):
each step = manual explanation -> formula picture(s) -> Excel cells for that step -> Excel note -> green answer; tips on the right.
Every task follows the five steps of a hypothesis test."""


def S(text=None, f=(), cells=(), xl=None, ans=None, tip=None, tipred=False):
    return dict(text=text, f=list(f), cells=list(cells), xl=xl, ans=ans, tip=tip, tipred=tipred)


TIP_TAILS = ('HOW DO I CHOOSE THE TYPE OF TEST?\n• “different”, “a difference” → two-tailed (≠)\n• “more”, “higher”, “greater” → right-tailed (>)\n'
             '• “less”, “fewer”, “smaller”, “faster (shorter time)” → left-tailed (<)\nH₀ always contains the equal sign.')
TIP_STAT = 'THE TEST STATISTIC\ntells us how many standard errors the difference between the two samples is away from 0 (the value in H₀).'


def head(given, find, which):
    return S(f'What is given? {given}\nWhat do we need to find? {find}', tip='WHICH TEST?\n' + which)


def hyp(text, tex, ans):
    return S('Step 1. State the hypotheses. ' + text, f=[tex], ans=ans, tip=TIP_TAILS)


def decision(text, tex, ans, tip=None, tipred=False):
    return S('Step 5. Make a decision and write a conclusion. ' + text, f=[tex], ans=ans, tip=tip, tipred=tipred)


STEPS = {}

# ---------------------------------------------------------------- Task 1: paired t-test, right-tailed
STEPS[1] = [
    head('8 students, each measured twice: x = minutes awake without gaming, y = minutes awake with gaming; α = 0.05.',
         'whether gaming before bed increases the time students stay awake.',
         'The same students are measured twice, so the samples are DEPENDENT (paired). We use the paired t-test on the differences d = y − x.'),
    hyp('With d = y − x, “gaming keeps you awake longer” means that the mean difference is positive:',
        r'H_0:\ \mu_d \leq 0 \qquad H_1:\ \mu_d > 0', 'H₀: μd ≤ 0, H₁: μd > 0 (right-tailed paired t-test).'),
    S('Step 2. Calculate the differences d = y − x for each student (column d in the table) and their mean and standard deviation:',
      f=[r'\bar{d}=\frac{\sum d_i}{n}=\frac{37}{8}=4.625 \qquad s_d=\sqrt{\frac{\sum (d_i-\bar{d})^2}{n-1}}\approx 3.068'],
      cells=['dbar', 'sd'], xl='Excel: =AVERAGE(…) and =STDEV.S(…) of the d column.',
      tip='WHY THE DIFFERENCES?\nEach student is compared with himself or herself, so differences between students (some simply sleep worse) disappear. Only the effect of gaming is left.'),
    S('Step 3. α = 0.05, right-tailed, df = n − 1 = 7. The critical value comes from the t-table:',
      f=[r'df=8-1=7 \qquad t_{\alpha,\,df}=t_{0.05,\,7}=1.895'], cells=['df', 'tc'],
      xl='Excel: =T.INV(0.95, 7) gives the right-tailed critical value.',
      tip='THE CRITICAL VALUE\nis the border of the rejection region. It depends only on α, the type of test and df, not on the data.'),
    S('Step 4. Calculate the test statistic and the p-value:',
      f=[r't=\frac{\bar{d}}{s_d/\sqrt{n}}=\frac{4.625}{3.068/\sqrt{8}}\approx 4.26 \qquad p=P(T_7>4.26)\approx 0.0019'],
      cells=['se', 't', 'p'], xl='Excel: =3.068/SQRT(8), =4.625/(3.068/SQRT(8)) and =T.DIST.RT(4.264, 7).', tip=TIP_STAT),
    decision('4.26 > 1.895 and p ≈ 0.0019 < 0.05.', r't=4.26>1.895 \qquad p=0.0019<0.05',
             'Answer: we reject H₀. Gaming before bed increases the time students stay awake, on average by about 4.6 minutes.',
             tip='COMMON MISTAKE\nTreating the two columns as independent samples. The same students were measured twice, so we must use the differences d and df = n − 1.', tipred=True),
]

# ---------------------------------------------------------------- Task 2: z-test, two means, right-tailed
STEPS[2] = [
    head('σ = 12 points for both groups (known); front rows: n_X = 36, x̄ = 74.5; back rows: n_Y = 42, ȳ = 68.9; α = 0.05.',
         'whether front-row students score higher on average.',
         'Two independent groups and the population standard deviations are KNOWN, so we use the z-test for two means.'),
    hyp('“Front-row students score higher” means μX − μY > 0:',
        r'H_0:\ \mu_X-\mu_Y \leq 0 \qquad H_1:\ \mu_X-\mu_Y > 0', 'H₀: μX − μY ≤ 0, H₁: μX − μY > 0 (right-tailed z-test).'),
    S('Step 2. α = 0.05 and the test is right-tailed, so the whole α is in the right tail:',
      f=[r'z_{\alpha}=z_{0.05}=1.645'], cells=['zc'], xl='Excel: =NORM.S.INV(0.95) gives the critical value.',
      tip='THE CRITICAL VALUE\nis the border of the rejection region. It depends only on α and on the type of test.'),
    S('Step 3. Calculate the standard error of the difference and the z statistic:',
      f=[r'SE=\sqrt{\frac{\sigma_X^2}{n_X}+\frac{\sigma_Y^2}{n_Y}}=\sqrt{\frac{12^2}{36}+\frac{12^2}{42}}\approx 2.726 \qquad z=\frac{74.5-68.9}{2.726}\approx 2.05'],
      cells=['se', 'z'], xl='Excel: =SQRT(12^2/36+12^2/42) and =(74.5-68.9)/SQRT(12^2/36+12^2/42).', tip=TIP_STAT),
    S('Step 4. Find the p-value (right tail):', f=[r'p=P(Z>2.05)=1-0.9800\approx 0.020'], cells=['p'],
      xl='Excel: =1-NORM.S.DIST(2.055, TRUE).'),
    decision('2.05 > 1.645 and p ≈ 0.020 < 0.05.', r'z=2.05>1.645 \qquad p=0.020<0.05',
             'Answer: we reject H₀. Front-row students score higher on average. This does not prove that sitting in front CAUSES better grades.',
             tip='CORRELATION IS NOT CAUSATION\nMore motivated students may simply choose the front rows. The test shows a difference, not its cause.'),
]

# ---------------------------------------------------------------- Task 3: pooled t-test, two-tailed
STEPS[3] = [
    head('engineering: n_X = 20, x̄ = 9.4, s_X = 3.2; economics: n_Y = 24, ȳ = 7.1, s_Y = 2.9; equal variances; α = 0.05.',
         'whether the average weekly coffee consumption differs between the two groups.',
         'Two independent groups, σ unknown but the variances are assumed EQUAL (3.2² / 2.9² ≈ 1.2 < 2), so we use the pooled t-test.'),
    hyp('“Is there a difference” means ≠:', r'H_0:\ \mu_X-\mu_Y = 0 \qquad H_1:\ \mu_X-\mu_Y \neq 0',
        'H₀: μX − μY = 0, H₁: μX − μY ≠ 0 (two-tailed pooled t-test).'),
    S('Step 2. Pool the two sample variances into one estimate:',
      f=[r's_p^2=\frac{(n_X-1)s_X^2+(n_Y-1)s_Y^2}{n_X+n_Y-2}=\frac{19\cdot 3.2^2+23\cdot 2.9^2}{42}\approx 9.238'], cells=['sp2'],
      xl='Excel: =(19*3.2^2+23*2.9^2)/42.',
      tip='WHY POOL?\nIf the variances are equal, both samples estimate the same σ². Combining them gives a more precise estimate; the larger sample gets more weight.'),
    S('Step 3. df = n_X + n_Y − 2 = 42 and α/2 = 0.025 in each tail:',
      f=[r'df=20+24-2=42 \qquad t_{\alpha/2,\,df}=t_{0.025,\,42}=\pm 2.018'], cells=['df', 'tc'],
      xl='Excel: =T.INV.2T(0.05, 42) gives the positive critical value.'),
    S('Step 4. Calculate the standard error, the t statistic and the p-value:',
      f=[r't=\frac{9.4-7.1}{\sqrt{9.238/20+9.238/24}}=\frac{2.3}{0.920}\approx 2.50 \qquad p=2\cdot P(T_{42}>2.50)\approx 0.016'],
      cells=['se', 't', 'p'], xl='Excel: =SQRT(9.238/20+9.238/24), =(9.4-7.1)/SQRT(9.238/20+9.238/24) and =T.DIST.2T(2.499, 42).', tip=TIP_STAT),
    decision('2.50 > 2.018 and p ≈ 0.016 < 0.05.', r't=2.50>2.018 \qquad p=0.016<0.05',
             'Answer: we reject H₀. Engineering students drink more coffee, about 2.3 cups more per week.',
             tip='COMMON MISTAKE\nUsing df = n − 1. The pooled t-test uses BOTH samples: df = nX + nY − 2.', tipred=True),
]

# ---------------------------------------------------------------- Task 4: Welch t-test, left-tailed
STEPS[4] = [
    head('e-scooter: n_X = 15, x̄ = 38.5, s_X = 6.2; tram: n_Y = 25, ȳ = 52.0, s_Y = 15.4; variances unknown and different; α = 0.05.',
         'whether the e-scooter is faster (shorter travel time) on average.',
         'Two independent groups, σ unknown and the variances are clearly DIFFERENT, so we use Welch’s t-test.'),
    hyp('“The e-scooter is faster” means a shorter mean time, μX − μY < 0:',
        r'H_0:\ \mu_X-\mu_Y \geq 0 \qquad H_1:\ \mu_X-\mu_Y < 0', 'H₀: μX − μY ≥ 0, H₁: μX − μY < 0 (left-tailed Welch t-test).'),
    S('Step 2. Check the variances and calculate s²/n for each group:',
      f=[r'\frac{s_Y^2}{s_X^2}=\frac{15.4^2}{6.2^2}\approx 6.2>2 \qquad \frac{s_X^2}{n_X}=\frac{6.2^2}{15}\approx 2.563 \qquad \frac{s_Y^2}{n_Y}=\frac{15.4^2}{25}\approx 9.486'],
      cells=['ratio', 'v1', 'v2'], xl='Excel: =15.4^2/6.2^2, =6.2^2/15 and =15.4^2/25.',
      tip='WHY NOT POOL?\nThe tram variance is about 6 times larger than the scooter variance. Pooling would hide this difference, so each sample keeps its own variance.'),
    S('Step 3. Calculate the standard error, the t statistic and the Welch degrees of freedom ν:',
      f=[r't=\frac{38.5-52.0}{\sqrt{2.563+9.486}}\approx -3.89 \qquad \nu=\frac{(2.563+9.486)^2}{\frac{2.563^2}{14}+\frac{9.486^2}{24}}\approx 34.4'],
      cells=['se', 't', 'nu'], xl='Excel: =SQRT(6.2^2/15+15.4^2/25), =(38.5-52)/SQRT(6.2^2/15+15.4^2/25) and the ν formula with the two numbers above.',
      tip='ν IS A DECIMAL\nFor the t-table, round ν DOWN to 34. Excel functions also cut the decimals, so they use 34 as well.'),
    S('Step 4. Left-tailed test with df = 34: find the critical value and the p-value:',
      f=[r'-t_{\alpha,\,34}=-t_{0.05,\,34}=-1.691 \qquad p=P(T_{34}<-3.89)\approx 0.0002'], cells=['tc', 'p'],
      xl='Excel: =T.INV(0.05, 34) and =T.DIST(-3.889, 34, TRUE).'),
    decision('−3.89 < −1.691 and p ≈ 0.0002 < 0.05.', r't=-3.89<-1.691 \qquad p=0.0002<0.05',
             'Answer: we reject H₀. The e-scooter is faster on average, by about 13.5 minutes, and its travel times are also much more predictable.'),
]

# ---------------------------------------------------------------- Task 5: two proportions, right-tailed
STEPS[5] = [
    head('students: n_X = 200, x_X = 46 clicked; staff: n_Y = 210, x_Y = 27 clicked; α = 0.05.',
         'whether students click the phishing link more often than staff.',
         'We compare two PROPORTIONS from independent groups, so we use the z-test for two proportions with the pooled proportion p₀.'),
    S('Step 1a. Calculate the two sample proportions and check that the samples are large enough:',
      f=[r'p_X=\frac{46}{200}=0.23 \qquad p_Y=\frac{27}{210}\approx 0.129'], cells=['p1', 'p2'],
      xl='Excel: =46/200 and =27/210. All counts (46, 154, 27, 183) are at least 5.',
      tip='LARGE ENOUGH?\nIn each group we need at least 5 “successes” and at least 5 “failures”, so that we can use the normal distribution.'),
    hyp('“Students click more often” means πX − πY > 0:', r'H_0:\ \pi_X-\pi_Y \leq 0 \qquad H_1:\ \pi_X-\pi_Y > 0',
        'H₀: πX − πY ≤ 0, H₁: πX − πY > 0 (right-tailed z-test).'),
    S('Step 2. α = 0.05, right-tailed:', f=[r'z_{0.05}=1.645'], cells=['zc'], xl='Excel: =NORM.S.INV(0.95).'),
    S('Step 3. Calculate the pooled proportion, the standard error and z:',
      f=[r'p_0=\frac{46+27}{200+210}\approx 0.178 \qquad z=\frac{0.23-0.129}{\sqrt{0.178\cdot 0.822\cdot(1/200+1/210)}}\approx 2.68'],
      cells=['p0', 'se', 'z'], xl='Excel: =(46+27)/(200+210), =SQRT(0.178*(1-0.178)*(1/200+1/210)) and =(0.23-27/210)/SQRT(…).',
      tip='WHY p₀?\nUnder H₀ both groups have the same proportion, so we estimate it from ALL the data together and use it in the standard error.'),
    S('Step 4. Find the p-value (right tail):', f=[r'p=P(Z>2.68)\approx 0.004'], cells=['p'], xl='Excel: =1-NORM.S.DIST(2.68, TRUE).'),
    decision('2.68 > 1.645 and p ≈ 0.004 < 0.05.', r'z=2.68>1.645 \qquad p=0.004<0.05',
             'Answer: we reject H₀. Students click the phishing link more often than staff (23% vs. 13%). The IT department should run cybersecurity training for students.',
             tip='COMMON MISTAKE\nAveraging the two proportions to get p₀. That is correct only when nX = nY. Always use (xX + xY) / (nX + nY).', tipred=True),
]

# ---------------------------------------------------------------- Task 6: F-test, right-tailed
STEPS[6] = [
    head('iPhone: n_X = 25, s_X² = 2.25; Android: n_Y = 21, s_Y² = 1.20; α = 0.05.',
         'whether iPhone users have more variable screen time than Android users.',
         'We compare two VARIANCES, so we use the F-test.'),
    hyp('“More variable” means a larger variance:', r'H_0:\ \sigma_X^2 \leq \sigma_Y^2 \qquad H_1:\ \sigma_X^2 > \sigma_Y^2',
        'H₀: σX² ≤ σY², H₁: σX² > σY² (right-tailed F-test).'),
    S('Step 2. Degrees of freedom and the critical value (area α = 0.05 to the right):',
      f=[r'v_1=25-1=24 \qquad v_2=21-1=20 \qquad F_{24,\,20,\,0.05}=2.082'], cells=['v1', 'v2', 'fc'],
      xl='Excel: =25-1, =21-1 and =F.INV.RT(0.05, 24, 20).',
      tip='TWO DEGREES OF FREEDOM\nv₁ belongs to the numerator (group X) and v₂ to the denominator (group Y). Swapping them changes the critical value!'),
    S('Step 3. Calculate the F statistic:', f=[r'F=\frac{s_X^2}{s_Y^2}=\frac{2.25}{1.20}=1.875'], cells=['F'], xl='Excel: =2.25/1.2.',
      tip='F IS A RATIO\nF = 1 means equal sample variances. The further F is from 1, the stronger the evidence of a difference.'),
    S('Step 4. Find the p-value (right tail):', f=[r'p=P(F_{24,20}>1.875)\approx 0.079'], cells=['p'], xl='Excel: =F.DIST.RT(1.875, 24, 20).'),
    decision('1.875 < 2.082 and p ≈ 0.079 > 0.05.', r'F=1.875<2.082 \qquad p=0.079>0.05',
             'Answer: we fail to reject H₀. There is not enough evidence that iPhone users have more variable screen time, so the UX designer can use the same reminder rules for both groups.',
             tip='COMMON MISTAKE\nConcluding that the variances are equal. Failing to reject H₀ only means that the samples do not show a significant difference.', tipred=True),
]

# ---------------------------------------------------------------- Task 7: F-test, left-tailed
STEPS[7] = [
    head('AI: n_X = 25, s_X² = 6.5; human graders: n_Y = 25, s_Y² = 14.0; α = 0.05.',
         'whether the AI scores have a smaller variance (are more consistent).',
         'We compare two VARIANCES, so we use the F-test. “More consistent” = smaller variance, so the test is left-tailed.'),
    hyp('“More consistent” means a smaller variance:', r'H_0:\ \sigma_X^2 \geq \sigma_Y^2 \qquad H_1:\ \sigma_X^2 < \sigma_Y^2',
        'H₀: σX² ≥ σY², H₁: σX² < σY² (left-tailed F-test).'),
    S('Step 2. Degrees of freedom and the LOWER critical value (area α = 0.05 to the left, i.e. 0.95 to the right):',
      f=[r'v_1=v_2=24 \qquad F_{24,\,24,\,0.95}=0.504'], cells=['v1', 'v2', 'fc'],
      xl='Excel: =F.INV(0.05, 24, 24) gives the lower critical value.',
      tip='LEFT-TAILED F-TEST\nThe rejection region is near 0: we reject H₀ if F is SMALLER than the lower critical value.'),
    S('Step 3. Calculate the F statistic:', f=[r'F=\frac{6.5}{14.0}\approx 0.464'], cells=['F'], xl='Excel: =6.5/14.'),
    S('Step 4. Find the p-value (left tail):', f=[r'p=P(F_{24,24}<0.464)\approx 0.033'], cells=['p'], xl='Excel: =F.DIST(0.464, 24, 24, TRUE).',
      tip='ANOTHER WAY\nPut the larger variance on top: 14.0 / 6.5 ≈ 2.15 > F(24, 24, 0.05) = 1.984. Same decision.'),
    decision('0.464 < 0.504 and p ≈ 0.033 < 0.05.', r'F=0.464<0.504 \qquad p=0.033<0.05',
             'Answer: we reject H₀. The AI scores are more consistent than the human scores. But consistent does not mean correct: an AI tool can give the same wrong score every time.'),
]

# ---------------------------------------------------------------- Task 8: pooled t-test, two-tailed, fail to reject
STEPS[8] = [
    head('Phone A: n_X = 25, x̄ = 412, s_X = 48; Phone B: n_Y = 25, ȳ = 438, s_Y = 55; variances unknown; α = 0.05.',
         'whether the average battery life of the two phones differs.',
         'Two independent groups, σ unknown. First compare the sample variances to choose between the pooled and Welch’s t-test.'),
    hyp('“Is there a difference” means ≠:', r'H_0:\ \mu_X-\mu_Y = 0 \qquad H_1:\ \mu_X-\mu_Y \neq 0',
        'H₀: μX − μY = 0, H₁: μX − μY ≠ 0 (two-tailed t-test).'),
    S('Step 2. Compare the variances, then pool them:',
      f=[r'\frac{55^2}{48^2}\approx 1.31<2 \qquad s_p^2=\frac{24\cdot 48^2+24\cdot 55^2}{48}=2664.5'], cells=['ratio', 'sp2'],
      xl='Excel: =55^2/48^2 and =(24*48^2+24*55^2)/48.',
      tip='POOLED OR WELCH?\nThe larger variance is only 1.31 times the smaller one (less than 2), so the pooled t-test is fine.'),
    S('Step 3. df = 25 + 25 − 2 = 48 and α/2 = 0.025 in each tail:',
      f=[r'df=48 \qquad t_{0.025,\,48}=\pm 2.011'], cells=['df', 'tc'], xl='Excel: =T.INV.2T(0.05, 48).'),
    S('Step 4. Calculate the standard error, the t statistic and the p-value:',
      f=[r't=\frac{412-438}{\sqrt{2664.5/25+2664.5/25}}=\frac{-26}{14.60}\approx -1.78 \qquad p=2\cdot P(T_{48}>1.78)\approx 0.081'],
      cells=['se', 't', 'p'], xl='Excel: =SQRT(2664.5/25+2664.5/25), =(412-438)/SQRT(2664.5/25+2664.5/25) and =T.DIST.2T(1.781, 48).', tip=TIP_STAT),
    decision('|−1.78| < 2.011 and p ≈ 0.081 > 0.05.', r'|t|=1.78<2.011 \qquad p=0.081>0.05',
             'Answer: we fail to reject H₀. The 26-minute difference in the sample is not statistically significant, so the YouTuber cannot say that one phone has a better battery.',
             tip='COMMON MISTAKE\nSaying that Phone B is better because its sample mean is higher. A difference in the sample is not always a significant difference in the population.', tipred=True),
]

# ---------------------------------------------------------------- Task 9: z-test, two-tailed, alpha 0.01
STEPS[9] = [
    head('σ_X² = 0.49 (hybrid), σ_Y² = 1.00 (petrol), known; n_X = 60, x̄ = 4.6; n_Y = 55, ȳ = 5.0; α = 0.01.',
         'whether the average fuel consumption of the two versions differs.',
         'Two independent groups and the population variances are KNOWN, so we use the z-test for two means.'),
    hyp('“Is there a difference” means ≠:', r'H_0:\ \mu_X-\mu_Y = 0 \qquad H_1:\ \mu_X-\mu_Y \neq 0',
        'H₀: μX − μY = 0, H₁: μX − μY ≠ 0 (two-tailed z-test).'),
    S('Step 2. α = 0.01, two-tailed, so α/2 = 0.005 in each tail:', f=[r'z_{0.005}=\pm 2.576'], cells=['zc'],
      xl='Excel: =NORM.S.INV(0.995).', tip='A STRICTER α\nWith α = 0.01 the critical values move further out (±2.576 instead of ±1.96), so we need stronger evidence to reject H₀.'),
    S('Step 3. Calculate the standard error and z:',
      f=[r'SE=\sqrt{\frac{0.49}{60}+\frac{1.00}{55}}\approx 0.162 \qquad z=\frac{4.6-5.0}{0.162}\approx -2.46'],
      cells=['se', 'z'], xl='Excel: =SQRT(0.49/60+1/55) and =(4.6-5)/SQRT(0.49/60+1/55).', tip=TIP_STAT),
    S('Step 4. Find the p-value (two tails):', f=[r'p=2\cdot P(Z<-2.46)\approx 0.014'], cells=['p'], xl='Excel: =2*NORM.S.DIST(-2.464, TRUE).'),
    decision('|−2.46| < 2.576 and p ≈ 0.014 > 0.01. At α = 0.05 we would reject H₀ (p < 0.05). The yearly saving is 0.4 L/100 km × 150 × 1.60 €:',
             r'|z|=2.46<2.576 \qquad p=0.014>0.01 \qquad 0.4\cdot 150\cdot 1.60=96\ \mathrm{EUR}',
             'Answer: at α = 0.01 we fail to reject H₀; at α = 0.05 we would reject it. The hybrid saves about 96 € per year, so the argument is not clearly won.'),
]
STEPS[9][-1]['cells'] = ['save']

# ---------------------------------------------------------------- Task 10: two proportions, right-tailed
STEPS[10] = [
    head('unvaccinated: n_X = 480, x_X = 96; vaccinated: n_Y = 500, x_Y = 45; α = 0.05.',
         'whether unvaccinated students are more likely to get the flu.',
         'We compare two PROPORTIONS from independent groups, so we use the z-test for two proportions with p₀.'),
    S('Step 1a. Calculate the two sample proportions (all counts 96, 384, 45, 455 are at least 5):',
      f=[r'p_X=\frac{96}{480}=0.20 \qquad p_Y=\frac{45}{500}=0.09'], cells=['p1', 'p2'], xl='Excel: =96/480 and =45/500.'),
    hyp('“More likely” means πX − πY > 0:', r'H_0:\ \pi_X-\pi_Y \leq 0 \qquad H_1:\ \pi_X-\pi_Y > 0',
        'H₀: πX − πY ≤ 0, H₁: πX − πY > 0 (right-tailed z-test).'),
    S('Step 2. α = 0.05, right-tailed:', f=[r'z_{0.05}=1.645'], cells=['zc'], xl='Excel: =NORM.S.INV(0.95).'),
    S('Step 3. Calculate the pooled proportion, the standard error and z:',
      f=[r'p_0=\frac{96+45}{480+500}\approx 0.144 \qquad z=\frac{0.20-0.09}{\sqrt{0.144\cdot 0.856\cdot(1/480+1/500)}}\approx 4.90'],
      cells=['p0', 'se', 'z'], xl='Excel: =(96+45)/(480+500), =SQRT(0.1439*(1-0.1439)*(1/480+1/500)) and =(0.2-0.09)/SQRT(…).', tip=TIP_STAT),
    S('Step 4. Find the p-value (right tail):', f=[r'p=P(Z>4.90)<0.0001'], cells=['p'], xl='Excel: =1-NORM.S.DIST(4.905, TRUE).'),
    decision('4.90 > 1.645 and p < 0.0001. The flu rate of unvaccinated students is 0.20 / 0.09 times higher:',
             r'z=4.90>1.645 \qquad \frac{0.20}{0.09}\approx 2.2',
             'Answer: we reject H₀. Unvaccinated students are more likely to get the flu: their flu rate is about 2.2 times higher.'),
]
STEPS[10][-1]['cells'] = ['ratio']
