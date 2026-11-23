# -*- coding: utf-8 -*-
"""Solution blocks inserted under each task of the Solutions document (Lab 6 Solutions format)."""


def head(given, find, concept):
    return [('p', '**Solution.**'),
            ('p', f'**What is given?** {given}'),
            ('p', f'**What do we need to find?** {find}'),
            ('p', f'**Which concept applies?** {concept}')]


S = {}
S[1] = head('μ₀ = 7 hours (the claim), n = 40 students, x̄ = 6.6 hours, σ = 1.2 hours (known), α = 0.05.',
            'whether the mean sleep time of students is different from 7 hours.',
            'the z-test for a mean (σ is known), two-tailed because the question asks about a “different amount”.') + [
 ('p', '**a)** The claim is about the population mean, and “different” means ≠:'),
 ('eq', r'$$H_0: \mu = 7 \qquad H_1: \mu \neq 7$$'),
 ('ans', 'Answer: a two-tailed test. We use z because the population standard deviation σ = 1.2 is known.'),
 ('p', '**b)** The test statistic is:'),
 ('eq', r'$$z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} = \frac{6.6 - 7}{1.2 / \sqrt{40}} = \frac{-0.4}{0.1897} \approx -2.11$$'),
 ('p', 'For α = 0.05 in a two-tailed test, α/2 = 0.025 in each tail, so the critical values are ±1.96 (Table 5).'),
 ('ans', 'Answer: z ≈ −2.11 and the critical values are ±1.96.'),
 ('p', '**c)** −2.11 < −1.96, so z falls in the left part of the rejection region. The p-value is:'),
 ('eq', r'$$p = 2 \cdot P(Z < -2.11) = 2 \cdot 0.0174 = 0.0348 < 0.05$$'),
 ('ans', 'Answer: we reject H₀. At the 5% significance level, students in Sarajevo do not sleep 7 hours per night on average; the data suggest that they sleep less.'),
 ('p', '**Excel check:** =(6.6-7)/(1.2/SQRT(40)) → −2.108 and =2*NORM.S.DIST(-2.108, TRUE) → 0.0350. The small difference from 0.0348 comes from rounding z to two decimals.'),
]
S[2] = head('μ₀ = $52 (the claim), n = 64 customers, x̄ = $53.10, σ = $10 (known), α = 0.10.',
            'whether the average monthly bill is now more than $52.',
            'the z-test for a mean (σ is known), right-tailed because the manager thinks that the bills have increased.') + [
 ('p', '**a)** “More than $52” is the new idea, so it goes into H₁:'),
 ('eq', r'$$H_0: \mu \le 52 \qquad H_1: \mu > 52$$'),
 ('ans', 'Answer: a right-tailed test.'),
 ('p', '**b)** The test statistic is:'),
 ('eq', r'$$z = \frac{53.10 - 52}{10 / \sqrt{64}} = \frac{1.10}{1.25} = 0.88$$'),
 ('p', 'For α = 0.10 in a right-tailed test, the whole α is in the right tail, so z_{0.10} = 1.282.'),
 ('ans', 'Answer: z = 0.88 and the critical value is z₀.₁₀ = 1.282.'),
 ('p', '**c)** 0.88 < 1.282, so z does not fall in the rejection region. The p-value is p = P(Z > 0.88) = 1 − 0.8106 = 0.1894, which is larger than α = 0.10.'),
 ('ans', 'Answer: we fail to reject H₀. The data do not support the manager’s claim that the average bill has increased above $52.'),
 ('p', '**Excel check:** =(53.1-52)/(10/SQRT(64)) → 0.88 and =1-NORM.S.DIST(0.88, TRUE) → 0.1894.'),
 ('box', 'mistake', '**Common mistake:** Concluding that the average bill is exactly $52. Failing to reject H₀ only means that the sample does not give enough evidence of an increase.'),
]
S[3] = head('μ₀ = 3 hours (the platform’s average), σ = 0.8 hours (known), n = 100 students, x̄ = 2.82 hours, α = 0.05.',
            'whether IBU students play a different amount than the platform’s average.',
            'the z-test for a mean (σ is known), two-tailed because the question asks about a “different amount”.') + [
 ('p', '**a)** The hypotheses are:'),
 ('eq', r'$$H_0: \mu = 3 \qquad H_1: \mu \neq 3$$'),
 ('ans', 'Answer: a two-tailed z-test.'),
 ('p', '**b)** The test statistic and the p-value are:'),
 ('eq', r'$$z = \frac{2.82 - 3}{0.8 / \sqrt{100}} = \frac{-0.18}{0.08} = -2.25 \qquad p = 2 \cdot P(Z < -2.25) = 2 \cdot 0.0122 = 0.0244$$'),
 ('ans', 'Answer: z = −2.25 and p = 0.0244.'),
 ('p', '**c)** −2.25 < −1.96 and p = 0.0244 < 0.05, so both methods lead to the same decision.'),
 ('ans', 'Answer: we reject H₀. At the 5% significance level, IBU students play a different amount than the platform’s average; the sample suggests that they play less.'),
 ('p', '**Excel check:** =(2.82-3)/(0.8/SQRT(100)) → −2.25 and =2*NORM.S.DIST(-2.25, TRUE) → 0.0244.'),
]
S[4] = head('μ₀ = 168 minutes (the website’s claim), n = 25 laptops, x̄ = 172.5 minutes, s = 15.4 minutes, battery life approximately normal, α = 0.05.',
            'whether the true average battery life with the app is different from 168 minutes.',
            'the t-test for a mean (σ is unknown), two-tailed, with df = n − 1 = 24.') + [
 ('p', '**a)** The hypotheses are:'),
 ('eq', r'$$H_0: \mu = 168 \qquad H_1: \mu \neq 168$$'),
 ('ans', 'Answer: a two-tailed test. We use t because the population standard deviation is unknown and we only have the sample standard deviation s from a small sample.'),
 ('p', '**b)** The test statistic is:'),
 ('eq', r'$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{172.5 - 168}{15.4 / \sqrt{25}} = \frac{4.5}{3.08} \approx 1.46$$'),
 ('p', 'With df = 24 and α/2 = 0.025, the t-table gives t_{0.025, 24} = 2.064.'),
 ('ans', 'Answer: t ≈ 1.46 and the critical values are ±2.064.'),
 ('p', '**c)** −2.064 < 1.46 < 2.064, so t does not fall in the rejection region. In Excel, the p-value is about 0.157, which is larger than 0.05.'),
 ('ans', 'Answer: we fail to reject H₀. The data do not show that the average battery life differs from 168 minutes. The students cannot say that the website is wrong, but the test also does not prove that it is right: the sample simply does not give enough evidence against the claim.'),
 ('p', '**Excel check:** =T.INV.2T(0.05, 24) → 2.064 and =T.DIST.2T(1.461, 24) → 0.157.'),
]
S[5] = head('π₀ = 0.30 (the faculty’s claim), n = 150 students, x = 57 use AI tools, α = 0.05.',
            'whether more than 30% of students use AI tools to write their homework.',
            'the z-test for a proportion, right-tailed, with π₀ in the standard error.') + [
 ('p', '**a)** The sample proportion and the check for the normal approximation are:'),
 ('eq', r'$$p = \frac{57}{150} = 0.38 \qquad n \cdot \pi_0 = 150 \cdot 0.30 = 45 \ge 5 \qquad n \cdot (1 - \pi_0) = 150 \cdot 0.70 = 105 \ge 5$$'),
 ('ans', 'Answer: p = 0.38, and the sample is large enough.'),
 ('p', '**b)** The claim “no more than 30%” contains the equal sign, so it goes into H₀:'),
 ('eq', r'$$H_0: \pi \le 0.30 \qquad H_1: \pi > 0.30$$'),
 ('eq', r'$$\sigma_p = \sqrt{\frac{0.30 \cdot 0.70}{150}} \approx 0.0374 \qquad z = \frac{0.38 - 0.30}{0.0374} \approx 2.14$$'),
 ('p', 'For α = 0.05 in a right-tailed test, z_{0.05} = 1.645, and 2.14 > 1.645.'),
 ('ans', 'Answer: z ≈ 2.14 falls in the rejection region, so we reject H₀.'),
 ('p', '**c)** The p-value is p = P(Z > 2.14) = 1 − 0.9838 = 0.0162, which is smaller than 0.05.'),
 ('ans', 'Answer: p ≈ 0.016. The newspaper can write that the data contradict the faculty’s claim: more than 30% of students use AI tools to write their homework.'),
 ('p', '**Excel check:** =(0.38-0.3)/SQRT(0.3*0.7/150) → 2.138 and =1-NORM.S.DIST(2.138, TRUE) → 0.0163.'),
 ('box', 'mistake', '**Common mistake:** Using p = 0.38 instead of π₀ = 0.30 in the standard error. In a test, we assume that H₀ is true, so the standard error is calculated with π₀.'),
]
S[6] = head('μ₀ = 8000 steps (the company’s claim), σ = 1800 steps (known), n = 36 students, x̄ = 7350 steps, α = 0.05.',
            'whether the data support the claim that users walk at least 8000 steps per day.',
            'the z-test for a mean (σ is known), left-tailed because the claim is “at least”.') + [
 ('p', '**a)** “At least 8000” contains the equal sign, so it goes into H₀:'),
 ('eq', r'$$H_0: \mu \ge 8000 \qquad H_1: \mu < 8000$$'),
 ('ans', 'Answer: a left-tailed test.'),
 ('p', '**b)** The test statistic and the p-value are:'),
 ('eq', r'$$z = \frac{7350 - 8000}{1800 / \sqrt{36}} = \frac{-650}{300} \approx -2.17 \qquad p = P(Z < -2.17) = 0.0150$$'),
 ('ans', 'Answer: z ≈ −2.17 and p ≈ 0.015.'),
 ('p', '**c)** For α = 0.05 in a left-tailed test, the critical value is −1.645. −2.17 < −1.645 and p = 0.015 < 0.05.'),
 ('ans', 'Answer: we reject H₀. The data do not support the company’s claim: users walk fewer than 8000 steps per day on average.'),
 ('p', '**Excel check:** =(7350-8000)/(1800/SQRT(36)) → −2.167 and =NORM.S.DIST(-2.167, TRUE) → 0.0151.'),
]
S[7] = head('π₀ = 0.08 (the company’s claim), n = 200 deployments, x = 21 with critical bugs, α = 0.01.',
            'whether more than 8% of the deployments have critical bugs.',
            'the z-test for a proportion, right-tailed, with π₀ in the standard error.') + [
 ('p', '**a)** The sample proportion and the check are:'),
 ('eq', r'$$p = \frac{21}{200} = 0.105 \qquad n \cdot \pi_0 = 200 \cdot 0.08 = 16 \ge 5 \qquad n \cdot (1 - \pi_0) = 200 \cdot 0.92 = 184 \ge 5$$'),
 ('ans', 'Answer: p = 0.105, and the sample is large enough.'),
 ('p', '**b)** The hypotheses and the test statistic are:'),
 ('eq', r'$$H_0: \pi \le 0.08 \qquad H_1: \pi > 0.08$$'),
 ('eq', r'$$\sigma_p = \sqrt{\frac{0.08 \cdot 0.92}{200}} \approx 0.0192 \qquad z = \frac{0.105 - 0.08}{0.0192} \approx 1.30$$'),
 ('p', 'For α = 0.01 in a right-tailed test, z_{0.01} = 2.326, and 1.30 < 2.326.'),
 ('ans', 'Answer: z ≈ 1.30 does not fall in the rejection region, so we fail to reject H₀ at α = 0.01.'),
 ('p', '**c)** The p-value is p = P(Z > 1.30) = 1 − 0.9032 = 0.0968. At α = 0.10, p = 0.0968 < 0.10 (and z = 1.30 > z₀.₁₀ = 1.282), so we would reject H₀.'),
 ('ans', 'Answer: yes, the decision changes. At α = 0.01 the data are not strong enough to say that more than 8% of the deployments have critical bugs, but at α = 0.10 they are. The choice of α must be made before the test.'),
 ('p', '**Excel check:** =(0.105-0.08)/SQRT(0.08*0.92/200) → 1.303 and =1-NORM.S.DIST(1.303, TRUE) → 0.0963.'),
]
S[8] = head('μ₀ = 3 minutes (the blog’s claim), n = 25 songs, x̄ = 3.4 minutes, s = 0.9 minutes, lengths approximately normal, α = 0.10.',
            'whether the average length of hit songs is different from 3 minutes.',
            'the t-test for a mean (σ is unknown), two-tailed, with df = n − 1 = 24.') + [
 ('p', '**a)** The hypotheses are:'),
 ('eq', r'$$H_0: \mu = 3 \qquad H_1: \mu \neq 3$$'),
 ('ans', 'Answer: a two-tailed test. We use t because σ is unknown and the sample is small.'),
 ('p', '**b)** The test statistic is:'),
 ('eq', r'$$t = \frac{3.4 - 3}{0.9 / \sqrt{25}} = \frac{0.4}{0.18} \approx 2.22$$'),
 ('p', 'With df = 24 and α/2 = 0.05, the t-table gives t_{0.05, 24} = 1.711.'),
 ('ans', 'Answer: t ≈ 2.22 and the critical values are ±1.711.'),
 ('p', '**c)** 2.22 > 1.711, so t falls in the rejection region. In Excel, the p-value is about 0.036, which is smaller than 0.10.'),
 ('ans', 'Answer: we reject H₀. At the 10% significance level, the average length of hit songs is different from 3 minutes; the sample suggests that it is longer.'),
 ('p', '**Excel check:** =T.INV.2T(0.10, 24) → 1.711 and =T.DIST.2T(2.222, 24) → 0.036.'),
]

MC_ANS = {1: 'b', 2: 'd', 3: 'a', 4: 'b', 5: 'c', 6: 'd', 7: 'c', 8: 'a', 9: 'b', 10: 'b', 11: 'b', 12: 'c', 13: 'b'}
FILL = {14: ' Answer: 19'}
TF_ANS = {15: 'False', 16: 'True', 17: 'True', 18: 'False', 19: 'False', 20: 'True'}
