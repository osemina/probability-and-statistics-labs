# -*- coding: utf-8 -*-
"""Solution blocks inserted under each task of the Lab 8 Solutions document (Lab 7 Solutions format)."""


def head(given, find, concept):
    return [('p', '**Solution.**'),
            ('p', f'**What is given?** {given}'),
            ('p', f'**What do we need to find?** {find}'),
            ('p', f'**Which concept applies?** {concept}')]


S = {}
S[1] = head('n = 8 students, each measured twice (no gaming x and with gaming y), α = 0.05.',
            'whether gaming before bed increases the time students stay awake.',
            'the paired t-test for the mean difference, right-tailed, with df = n − 1 = 7.') + [
 ('p', '**a)** The samples are dependent because the **same 8 students** were measured on two nights, so the two measurements form pairs. With d = y − x (with gaming − no gaming), “gaming keeps you awake longer” means μ_{d} > 0:'),
 ('eq', r'$$H_0: \mu_d \le 0 \qquad H_1: \mu_d > 0$$'),
 ('ans', 'Answer: dependent (paired) samples; a right-tailed paired t-test.'),
 ('p', '**b)** The differences are d = 6, 1, 7, 6, −1, 8, 5, 5. Their sum is 37, so:'),
 ('eq', r'$$\bar{d} = \frac{37}{8} = 4.625 \qquad s_d = \sqrt{\frac{\sum (d_i - \bar{d})^2}{n - 1}} = \sqrt{\frac{65.875}{7}} \approx 3.068$$'),
 ('ans', 'Answer: d̄ = 4.625 minutes and s_{d} ≈ 3.068 minutes.'),
 ('p', '**c)** The test statistic is:'),
 ('eq', r'$$t = \frac{\bar{d}}{s_d / \sqrt{n}} = \frac{4.625}{3.068 / \sqrt{8}} = \frac{4.625}{1.085} \approx 4.26$$'),
 ('p', 'For α = 0.05, df = 7 and a right-tailed test, the critical value is t_{7, 0.05} = 1.895. 4.26 > 1.895 and p ≈ 0.0019 < 0.05.'),
 ('ans', 'Answer: we reject H₀. At the 5% significance level, gaming before bed increases the time students stay awake, on average by about 4.6 minutes.'),
 ('p', '**Excel check:** =AVERAGE(d) → 4.625, =STDEV.S(d) → 3.068, =T.INV(0.95, 7) → 1.895 and =T.DIST.RT(4.264, 7) → 0.0019.'),
 ('box', 'mistake', '**Common mistake:** Treating the two columns as independent samples. The same students were measured twice, so we must work with the differences d and use df = n − 1 = 7.'),
]
S[2] = head('σ = 12 points for both groups (known), front rows: n_{X} = 36, x̄ = 74.5; back rows: n_{Y} = 42, ȳ = 68.9; α = 0.05.',
            'whether front-row students score higher on average.',
            'the z-test for two independent means (σ known), right-tailed.') + [
 ('p', '**a)** “Front-row students score higher” means μ_{X} − μ_{Y} > 0:'),
 ('eq', r'$$H_0: \mu_X - \mu_Y \le 0 \qquad H_1: \mu_X - \mu_Y > 0$$'),
 ('ans', 'Answer: a right-tailed test. We use z because the population standard deviations are known.'),
 ('p', '**b)** The standard error and the test statistic are:'),
 ('eq', r'$$SE = \sqrt{\frac{12^2}{36} + \frac{12^2}{42}} = \sqrt{4 + 3.429} \approx 2.726 \qquad z = \frac{74.5 - 68.9}{2.726} \approx 2.05$$'),
 ('ans', 'Answer: SE ≈ 2.726 and z ≈ 2.05.'),
 ('p', '**c)** The critical value is z_{0.05} = 1.645. 2.05 > 1.645 and p = P(Z > 2.05) ≈ 0.020 < 0.05.'),
 ('ans', 'Answer: we reject H₀. Front-row students score higher on average. This does not prove that sitting in front causes better grades: motivated students may simply choose the front rows.'),
 ('p', '**Excel check:** =SQRT(144/36+144/42) → 2.726, =5.6/2.726 → 2.055 and =1-NORM.S.DIST(2.055, TRUE) → 0.020.'),
]
S[3] = head('engineering: n_{X} = 20, x̄ = 9.4, s_{X} = 3.2; economics: n_{Y} = 24, ȳ = 7.1, s_{Y} = 2.9; equal variances; α = 0.05.',
            'whether the average weekly coffee consumption differs between the two groups.',
            'the pooled t-test, two-tailed, with df = n_{X} + n_{Y} − 2 = 42.') + [
 ('p', '**a)** “Is there a difference” means ≠:'),
 ('eq', r'$$H_0: \mu_X - \mu_Y = 0 \qquad H_1: \mu_X - \mu_Y \neq 0$$'),
 ('ans', 'Answer: a two-tailed test. Equal variances are reasonable because the sample variances (10.24 and 8.41) are very similar: their ratio is only about 1.2.'),
 ('p', '**b)** The pooled variance, the t statistic and the degrees of freedom are:'),
 ('eq', r'$$s_p^2 = \frac{19 \cdot 3.2^2 + 23 \cdot 2.9^2}{42} = \frac{194.56 + 193.43}{42} \approx 9.238$$'),
 ('eq', r'$$t = \frac{9.4 - 7.1}{\sqrt{9.238/20 + 9.238/24}} = \frac{2.3}{0.920} \approx 2.50, \qquad df = 42$$'),
 ('ans', 'Answer: s_{p}² ≈ 9.238, t ≈ 2.50 and df = 42.'),
 ('p', '**c)** The critical values are ±t_{42, 0.025} = ±2.018. 2.50 > 2.018 and p ≈ 0.016 < 0.05.'),
 ('ans', 'Answer: we reject H₀. There is a difference in average coffee consumption: engineering students drink more coffee, about 2.3 cups more per week.'),
 ('p', '**Excel check:** =(19*3.2^2+23*2.9^2)/42 → 9.238, =T.INV.2T(0.05, 42) → 2.018 and =T.DIST.2T(2.499, 42) → 0.016.'),
]
S[4] = head('e-scooter: n_{X} = 15, x̄ = 38.5, s_{X} = 6.2; tram: n_{Y} = 25, ȳ = 52.0, s_{Y} = 15.4; variances unknown and different; α = 0.05.',
            'whether the e-scooter is faster (shorter travel time) on average.',
            'Welch’s t-test, left-tailed, with the Welch–Satterthwaite degrees of freedom ν.') + [
 ('p', '**a)** “The e-scooter is faster” means a shorter mean time, μ_{X} − μ_{Y} < 0:'),
 ('eq', r'$$H_0: \mu_X - \mu_Y \ge 0 \qquad H_1: \mu_X - \mu_Y < 0$$'),
 ('ans', 'Answer: a left-tailed test. We use Welch’s t-test because the sample variances are very different: 15.4² / 6.2² ≈ 6.2, far more than 2.'),
 ('p', '**b)** With s_{X}²/n_{X} = 38.44/15 ≈ 2.563 and s_{Y}²/n_{Y} = 237.16/25 ≈ 9.486:'),
 ('eq', r'$$t = \frac{38.5 - 52.0}{\sqrt{2.563 + 9.486}} = \frac{-13.5}{3.471} \approx -3.89$$'),
 ('eq', r'$$\nu = \frac{(2.563 + 9.486)^2}{\frac{2.563^2}{14} + \frac{9.486^2}{24}} \approx 34.4$$'),
 ('ans', 'Answer: t ≈ −3.89 and ν ≈ 34.4, which we round down to 34 for the t-table.'),
 ('p', '**c)** The critical value is −t_{34, 0.05} = −1.691. −3.89 < −1.691 and p ≈ 0.0002 < 0.05.'),
 ('ans', 'Answer: we reject H₀. The e-scooter is faster on average, by about 13.5 minutes, and its travel times are also much more predictable.'),
 ('p', '**Excel check:** =SQRT(6.2^2/15+15.4^2/25) → 3.471, =T.INV(0.05, 34) → −1.691 and =T.DIST(-3.889, 34, TRUE) → 0.0002.'),
]
S[5] = head('students: n_{X} = 200, x_{X} = 46 clicked; staff: n_{Y} = 210, x_{Y} = 27 clicked; α = 0.05.',
            'whether students click the phishing link more often than staff.',
            'the z-test for two proportions with the pooled proportion p₀, right-tailed.') + [
 ('p', '**a)** The sample proportions are p_{X} = 46/200 = 0.23 and p_{Y} = 27/210 ≈ 0.129. All counts (46, 154, 27, 183) are at least 5, so both samples are large enough. “Students click more often” means:'),
 ('eq', r'$$H_0: \pi_X - \pi_Y \le 0 \qquad H_1: \pi_X - \pi_Y > 0$$'),
 ('ans', 'Answer: p_{X} = 0.23, p_{Y} ≈ 0.129; a right-tailed test.'),
 ('p', '**b)** The pooled proportion and the test statistic are:'),
 ('eq', r'$$p_0 = \frac{46 + 27}{200 + 210} = \frac{73}{410} \approx 0.178$$'),
 ('eq', r'$$z = \frac{0.23 - 0.129}{\sqrt{0.178 \cdot 0.822 \cdot (1/200 + 1/210)}} = \frac{0.101}{0.0378} \approx 2.68$$'),
 ('ans', 'Answer: p₀ ≈ 0.178 and z ≈ 2.68.'),
 ('p', '**c)** The critical value is z_{0.05} = 1.645. 2.68 > 1.645 and p ≈ 0.004 < 0.05.'),
 ('ans', 'Answer: we reject H₀. Students click the phishing link more often than staff (23% vs. 13%). The IT department should run cybersecurity training for students, for example in the first week of the semester.'),
 ('p', '**Excel check:** =73/410 → 0.178, =(0.23-27/210)/SQRT(0.178*0.822*(1/200+1/210)) → 2.68 and =1-NORM.S.DIST(2.68, TRUE) → 0.004.'),
]
S[6] = head('iPhone: n_{X} = 25, s_{X}² = 2.25; Android: n_{Y} = 21, s_{Y}² = 1.20; α = 0.05.',
            'whether iPhone users have more variable screen time than Android users.',
            'the F-test for two variances, right-tailed, with v_{1} = 24 and v_{2} = 20.') + [
 ('p', '**a)** “More variable” means a larger variance:'),
 ('eq', r'$$H_0: \sigma_X^2 \le \sigma_Y^2 \qquad H_1: \sigma_X^2 > \sigma_Y^2$$'),
 ('ans', 'Answer: a right-tailed F-test.'),
 ('p', '**b)** The F statistic and the degrees of freedom are:'),
 ('eq', r'$$F = \frac{s_X^2}{s_Y^2} = \frac{2.25}{1.20} = 1.875, \qquad v_1 = 25 - 1 = 24, \quad v_2 = 21 - 1 = 20$$'),
 ('ans', 'Answer: F = 1.875, v_{1} = 24, v_{2} = 20.'),
 ('p', '**c)** The critical value is F_{24, 20, 0.05} = 2.082. 1.875 < 2.082 and p ≈ 0.079 > 0.05.'),
 ('ans', 'Answer: we fail to reject H₀. There is not enough evidence that iPhone users have more variable screen time, so the UX designer can use the same reminder rules for both groups.'),
 ('p', '**Excel check:** =F.INV.RT(0.05, 24, 20) → 2.082 and =F.DIST.RT(1.875, 24, 20) → 0.079.'),
 ('box', 'mistake', '**Common mistake:** Concluding that the variances are equal. Failing to reject H₀ only means that the samples do not show a significant difference.'),
]
S[7] = head('AI: n_{X} = 25, s_{X}² = 6.5; human graders: n_{Y} = 25, s_{Y}² = 14.0; α = 0.05.',
            'whether the AI scores have a smaller variance (are more consistent).',
            'the F-test for two variances, left-tailed, with v_{1} = v_{2} = 24.') + [
 ('p', '**a)** “More consistent” means a smaller variance:'),
 ('eq', r'$$H_0: \sigma_X^2 \ge \sigma_Y^2 \qquad H_1: \sigma_X^2 < \sigma_Y^2$$'),
 ('ans', 'Answer: a left-tailed F-test.'),
 ('p', '**b)** The F statistic and the degrees of freedom are:'),
 ('eq', r'$$F = \frac{6.5}{14.0} \approx 0.464, \qquad v_1 = v_2 = 24$$'),
 ('ans', 'Answer: F ≈ 0.464, v_{1} = v_{2} = 24.'),
 ('p', '**c)** For a left-tailed test, the critical value is F_{24, 24, 0.95} = 0.504. 0.464 < 0.504 and p ≈ 0.033 < 0.05. (Equivalently, with the larger variance in the numerator: 14.0 / 6.5 ≈ 2.15 > F_{24, 24, 0.05} = 1.984.)'),
 ('ans', 'Answer: we reject H₀. The AI scores are more consistent than the human scores. However, consistent does not mean correct: an AI tool can give the same wrong score every time.'),
 ('p', '**Excel check:** =F.INV(0.05, 24, 24) → 0.504 and =F.DIST(0.464, 24, 24, TRUE) → 0.033.'),
]
S[8] = head('Phone A: n_{X} = 25, x̄ = 412, s_{X} = 48; Phone B: n_{Y} = 25, ȳ = 438, s_{Y} = 55; variances unknown; α = 0.05.',
            'whether the average battery life of the two phones differs.',
            'a two-tailed t-test for two independent means; the variance ratio decides between the pooled and Welch’s t-test.') + [
 ('p', '**a)** “Is there a difference” means ≠:'),
 ('eq', r'$$H_0: \mu_X - \mu_Y = 0 \qquad H_1: \mu_X - \mu_Y \neq 0$$'),
 ('ans', 'Answer: a two-tailed test. The variance ratio is 55² / 48² ≈ 1.31 < 2, so we can use the pooled t-test.'),
 ('p', '**b)** The pooled variance, the t statistic and the degrees of freedom are:'),
 ('eq', r'$$s_p^2 = \frac{24 \cdot 48^2 + 24 \cdot 55^2}{48} = 2664.5 \qquad t = \frac{412 - 438}{\sqrt{2664.5/25 + 2664.5/25}} = \frac{-26}{14.60} \approx -1.78$$'),
 ('ans', 'Answer: s_{p}² = 2664.5, t ≈ −1.78 and df = 48.'),
 ('p', '**c)** The critical values are ±t_{48, 0.025} = ±2.011. |−1.78| < 2.011 and p ≈ 0.081 > 0.05.'),
 ('ans', 'Answer: we fail to reject H₀. The 26-minute difference in the sample is not statistically significant, so the YouTuber cannot say that one phone has a better battery.'),
 ('p', '**Excel check:** =T.INV.2T(0.05, 48) → 2.011 and =T.DIST.2T(1.781, 48) → 0.081.'),
 ('box', 'mistake', '**Common mistake:** Concluding that Phone B is better because its sample mean is higher. A difference in the sample is not always a significant difference in the population.'),
]
S[9] = head('σ_{X}² = 0.49 (hybrid), σ_{Y}² = 1.00 (petrol), known; n_{X} = 60, x̄ = 4.6; n_{Y} = 55, ȳ = 5.0; α = 0.01.',
            'whether the average fuel consumption of the two versions differs.',
            'the z-test for two independent means (σ known), two-tailed.') + [
 ('p', '**a)** The hypotheses are:'),
 ('eq', r'$$H_0: \mu_X - \mu_Y = 0 \qquad H_1: \mu_X - \mu_Y \neq 0$$'),
 ('ans', 'Answer: a two-tailed test. We use z because the population variances are known.'),
 ('p', '**b)** The standard error and the test statistic are:'),
 ('eq', r'$$SE = \sqrt{\frac{0.49}{60} + \frac{1.00}{55}} = \sqrt{0.00817 + 0.01818} \approx 0.162 \qquad z = \frac{4.6 - 5.0}{0.162} \approx -2.46$$'),
 ('ans', 'Answer: SE ≈ 0.162 and z ≈ −2.46.'),
 ('p', '**c)** For α = 0.01, the critical values are ±z_{0.005} = ±2.576. |−2.46| < 2.576 and p ≈ 0.014 > 0.01.'),
 ('ans', 'Answer: at α = 0.01 we fail to reject H₀. At α = 0.05 we would reject it, because p ≈ 0.014 < 0.05. The hybrid would save 0.4 L/100 km × 150 × 1.60 € = 96 € per year, so the argument is not clearly won: the evidence is only moderate.'),
 ('p', '**Excel check:** =SQRT(0.49/60+1/55) → 0.162, =NORM.S.INV(0.995) → 2.576 and =2*NORM.S.DIST(-2.464, TRUE) → 0.014.'),
]
S[10] = head('unvaccinated: n_{X} = 480, x_{X} = 96; vaccinated: n_{Y} = 500, x_{Y} = 45; α = 0.05.',
             'whether unvaccinated students are more likely to get the flu.',
             'the z-test for two proportions with the pooled proportion p₀, right-tailed.') + [
 ('p', '**a)** p_{X} = 96/480 = 0.20 and p_{Y} = 45/500 = 0.09. All counts (96, 384, 45, 455) are at least 5. “More likely” means:'),
 ('eq', r'$$H_0: \pi_X - \pi_Y \le 0 \qquad H_1: \pi_X - \pi_Y > 0$$'),
 ('ans', 'Answer: p_{X} = 0.20, p_{Y} = 0.09; a right-tailed test.'),
 ('p', '**b)** The pooled proportion and the test statistic are:'),
 ('eq', r'$$p_0 = \frac{96 + 45}{480 + 500} = \frac{141}{980} \approx 0.144 \qquad z = \frac{0.20 - 0.09}{\sqrt{0.144 \cdot 0.856 \cdot (1/480 + 1/500)}} = \frac{0.11}{0.0224} \approx 4.90$$'),
 ('ans', 'Answer: p₀ ≈ 0.144 and z ≈ 4.90.'),
 ('p', '**c)** The critical value is z_{0.05} = 1.645. 4.90 > 1.645 and p < 0.0001.'),
 ('ans', 'Answer: we reject H₀. Unvaccinated students are more likely to get the flu: their flu rate is 0.20 / 0.09 ≈ 2.2 times higher.'),
 ('p', '**Excel check:** =141/980 → 0.144, =(0.2-0.09)/SQRT(0.144*0.856*(1/480+1/500)) → 4.90 and =1-NORM.S.DIST(4.9, TRUE) → 0.0000005.'),
]

MC_ANS = {1: 'b', 2: 'b', 3: 'a', 4: 'b', 5: 'c', 6: 'c', 7: 'b', 8: 'b', 9: 'b', 10: 'b', 11: 'c', 12: 'b', 13: 'b'}
FILL = {14: ' Answer: v₁ = 15 and v₂ = 20.'}
TF_ANS = {15: 'True', 16: 'False', 17: 'True', 18: 'True', 19: 'False', 20: 'False'}
