# -*- coding: utf-8 -*-
MC = [
 ('Which of the following is a correct null hypothesis?', ['H₀: x̄ = 50', 'H₀: μ = 50', 'H₀: μ ≠ 50', 'H₀: x̄ ≠ 50']),
 ('The alternative hypothesis H₁ never contains the sign:', ['≠', '<', '>', '=']),
 ('A Type I error occurs when we:', ['reject H₀ when H₀ is true', 'fail to reject H₀ when H₀ is false', 'reject H₀ when H₀ is false', 'fail to reject H₀ when H₀ is true']),
 ('A Type II error occurs when we:', ['reject H₀ when H₀ is true', 'fail to reject H₀ when H₀ is false', 'reject H₀ when H₀ is false', 'fail to reject H₀ when H₀ is true']),
 ('The probability of a Type I error is:', ['β', '1 − β', 'α', '1 − α']),
 ('The power of a test is:', ['α', 'β', '1 − α', '1 − β']),
 ('A company claims that at least 90% of its customers are satisfied, and you suspect that the true percentage is lower. Which test should you use?', ['a two-tailed test', 'a right-tailed test', 'a left-tailed test', 'no test is needed']),
 ('The p-value of a test is 0.03 and α = 0.05. You should:', ['reject H₀', 'fail to reject H₀', 'accept H₀', 'increase the sample size']),
 ('The p-value of a test is 0.08. Which statement is true?', ['We reject H₀ at α = 0.05.', 'We reject H₀ at α = 0.10, but not at α = 0.05.', 'We reject H₀ at α = 0.01.', 'We can never reject H₀.']),
 ('The critical values of a two-tailed z-test at α = 0.05 are:', ['±1.645', '±1.96', '±2.326', '±2.576']),
 ('We use the t-test instead of the z-test for a mean when:', ['the sample is large', 'the population standard deviation σ is unknown', 'we test a proportion', 'the significance level is small']),
 ('Other things being equal, which change increases the power of a test?', ['a smaller sample size', 'a smaller α', 'a larger sample size', 'more variability in the data']),
 ('In a z-test for a proportion, the standard error is calculated with:', ['the sample proportion p', 'the claimed proportion π₀ from H₀', 'the sample mean x̄', 'the sample standard deviation s']),
]
TF = [
 'Failing to reject H₀ proves that H₀ is true.',
 'The smaller the p-value, the stronger the evidence against H₀.',
 'Other things being equal, if we decrease α, the probability of a Type II error increases.',
 'The rejection region of a right-tailed test is in the left tail of the distribution.',
 'The p-value is the probability that H₀ is true.',
 'The critical value approach and the p-value approach always lead to the same decision.',
]

BLOCKS = [('h1', 'Test Yourself'), ('h2', 'Multiple Choice')]
for i, (q, opts) in enumerate(MC, 1):
    BLOCKS += [('p', f'**7.{i}.** {q}'), ('al', opts)]
BLOCKS.append(('p', '**7.14.** In a t-test for a mean with a sample of n = 20, there are ________ degrees of freedom.'))
BLOCKS.append(('h2', 'True or False'))
for i, s in enumerate(TF, 15):
    BLOCKS.append(('p', f'**7.{i}.** {s}'))

BLOCKS += [
 ('h1', 'Lab Summary'),
 ('ul', ['A **hypothesis test** checks a claim about a population parameter (μ or π) with data from a sample.',
         '**H₀** contains =, ≤ or ≥ and is assumed to be true at first; **H₁** contains ≠, < or >, and its sign decides the type of test (two-tailed, right-tailed or left-tailed).',
         '**α** is the probability of a Type I error (rejecting a true H₀), **β** is the probability of a Type II error (missing a false H₀), and the **power** of the test is 1 − β.',
         'The **test statistic** tells us how many standard errors the sample result is from the claim in H₀.',
         '**Critical value approach:** reject H₀ if the test statistic falls in the rejection region. **p-value approach:** reject H₀ if p < α. Both approaches always lead to the same decision.',
         'Use **z** for a mean when σ is known, **t** (df = n − 1) when σ is unknown, and **z** for a proportion, with π₀ in the standard error.',
         '“Fail to reject H₀” does not mean that H₀ is true: the data simply do not give enough evidence against it.']),
 ('p', 'Table 8 collects the key formulas and Excel functions from this lab.'),
 ('cap', 'Table 8. Key ideas, formulas and Excel functions from this lab.'),
 ('table', 'T8'),
]

TABLES = {
 'T8': {'rows': [['Concept', 'Key formula', 'In Excel'],
                 ['Hypotheses', 'H₀: =, ≤ or ≥;  H₁: ≠, < or >', '–'],
                 ['z-test for μ (σ known)', 'z = (x̄ − μ₀)/(σ/√n)', '=NORM.S.DIST(z, TRUE)'],
                 ['t-test for μ (σ unknown)', 't = (x̄ − μ₀)/(s/√n),  df = n − 1', '=T.DIST.RT(t, df), =T.DIST.2T(|t|, df)'],
                 ['z-test for a proportion', 'z = (p − π₀)/√(π₀(1 − π₀)/n), if nπ₀ ≥ 5 and n(1 − π₀) ≥ 5', '=SQRT(π₀*(1-π₀)/n)'],
                 ['Critical values', 'two-tailed: ±z_{α/2};  right-tailed: z_{α};  left-tailed: −z_{α}', '=NORM.S.INV(1 − α), =T.INV(1 − α, df)'],
                 ['Decision', 'reject H₀ if the test statistic is in the rejection region, or if p < α', '–'],
                 ['Errors and power', 'P(Type I error) = α,  P(Type II error) = β,  power = 1 − β', '–']],
        'widths': [120, 200, 148], 'center': (), 'boldcol0': False},
}
FIGURES = {}
