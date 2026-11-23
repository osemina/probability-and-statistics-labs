# -*- coding: utf-8 -*-
MC = [
 ('Measuring the same students before and after a course gives:', ['independent samples', 'dependent (paired) samples', 'two proportions', 'two variances']),
 ('In a paired t-test, the degrees of freedom are:', ['n_{X} + n_{Y} − 2', 'n − 1, where n is the number of pairs', 'n_{X} − 1', 'ν (Welch)']),
 ('Which test compares two means when σ_{X} and σ_{Y} are known?', ['the z-test', 'the pooled t-test', 'Welch’s t-test', 'the F-test']),
 ('The pooled variance s_{p}² is used when the population variances are:', ['known', 'unknown and assumed equal', 'unknown and unequal', 'equal to zero']),
 ('The degrees of freedom of the pooled t-test are:', ['n − 1', 'n_{X} + n_{Y}', 'n_{X} + n_{Y} − 2', 'ν (Welch)']),
 ('Welch’s t-test is used when the population variances are:', ['known', 'unknown and assumed equal', 'unknown and unequal', 'equal to 1']),
 ('The pooled proportion p₀ is calculated as:', ['(p_{X} + p_{Y}) / 2', '(x_{X} + x_{Y}) / (n_{X} + n_{Y})', 'x_{X} / n_{X}', 'p_{X} − p_{Y}']),
 ('The F statistic for comparing two variances is:', ['s_{X} − s_{Y}', 's_{X}² / s_{Y}²', 's_{X} / s_{Y}', 'σ_{X}² / σ_{Y}²']),
 ('The F-distribution is:', ['symmetric around 0', 'skewed to the right and never negative', 'skewed to the left', 'the same as the t-distribution']),
 ('You want to test whether group X varies more than group Y. The alternative hypothesis is:', ['H₁: σ_{X}² ≠ σ_{Y}²', 'H₁: σ_{X}² > σ_{Y}²', 'H₁: σ_{X}² < σ_{Y}²', 'H₁: μ_{X} > μ_{Y}']),
 ('Testing whether men and women differ in average height is a:', ['left-tailed test', 'right-tailed test', 'two-tailed test', 'F-test']),
 ('Two independent samples have sample variances 64 and 16. Which test should you use to compare their means?', ['the pooled t-test', 'Welch’s t-test', 'the paired t-test', 'the F-test']),
 ('The p-value of a test is 0.04 and α = 0.01. You should:', ['reject H₀', 'fail to reject H₀', 'accept H₁', 'change α to 0.05']),
]
TF = [
 'In a paired t-test, we first calculate the difference for each pair.',
 'The pooled t-test can be used when one sample variance is 6 times larger than the other.',
 'The Welch degrees of freedom ν can be a decimal number.',
 'In the z-test for two proportions, the pooled proportion p₀ is used only in the denominator.',
 'An F value of 0.5 is impossible.',
 'If two sample means are different, we always reject H₀.',
]

BLOCKS = [('h1', 'Test Yourself'), ('h2', 'Multiple Choice')]
for i, (q, opts) in enumerate(MC, 1):
    BLOCKS += [('p', f'**8.{i}.** {q}'), ('al', opts)]
BLOCKS.append(('p', '**8.14.** In an F-test with n_{X} = 16 and n_{Y} = 21, the degrees of freedom are v_{1} = ________ and v_{2} = ________.'))
BLOCKS.append(('h2', 'True or False'))
for i, s in enumerate(TF, 15):
    BLOCKS.append(('p', f'**8.{i}.** {s}'))

BLOCKS += [
 ('h1', 'Lab Summary'),
 ('ul', ['First decide whether the samples are **dependent (paired)** (the same people measured twice) or **independent** (two unrelated groups), and whether you compare **means**, **proportions** or **variances**.',
         '**Paired samples:** calculate the differences d = x − y for each pair and use the **paired t-test** with df = n − 1.',
         '**Two independent means:** use the **z-test** if σ_{X} and σ_{Y} are known, the **pooled t-test** (df = n_{X} + n_{Y} − 2) if the variances are unknown but equal, and **Welch’s t-test** (df = ν) if they are unknown and unequal.',
         '**Two proportions:** use the z-test with the **pooled proportion** p₀ = (x_{X} + x_{Y}) / (n_{X} + n_{Y}) in the standard error.',
         '**Two variances:** use the **F-test**, F = s_{X}² / s_{Y}², with v_{1} = n_{X} − 1 and v_{2} = n_{Y} − 1. The F-distribution is skewed to the right and never negative.',
         'Every test follows the same five steps as in Lab 7: hypotheses, α and the critical value, test statistic, p-value, decision.',
         '“Fail to reject H₀” does not mean that H₀ is true: the data simply do not give enough evidence against it.']),
 ('p', 'Table 19 collects the key formulas and Excel functions from this lab.'),
 ('cap', 'Table 19. Key formulas and Excel functions from this lab.'),
 ('table', 'T19'),
]

TABLES = {
 'T19': {'rows': [['Test', 'Test statistic', 'In Excel'],
                  ['Paired t-test', 't = d̄ / (s_{d}/√n),  df = n − 1', '=T.DIST.RT(t, df), =T.DIST.2T(|t|, df)'],
                  ['z-test, two means (σ known)', 'z = (x̄ − ȳ) / √(σ_{X}²/n_{X} + σ_{Y}²/n_{Y})', '=NORM.S.DIST(z, TRUE), =NORM.S.INV(1 − α)'],
                  ['Pooled t-test', 't = (x̄ − ȳ) / √(s_{p}²/n_{X} + s_{p}²/n_{Y}),  df = n_{X} + n_{Y} − 2', '=T.INV(1 − α, df), =T.INV.2T(α, df)'],
                  ['Welch’s t-test', 't = (x̄ − ȳ) / √(s_{X}²/n_{X} + s_{Y}²/n_{Y}),  df = ν', '=T.DIST(t, ν, TRUE)'],
                  ['z-test, two proportions', 'z = (p_{X} − p_{Y}) / √(p₀(1 − p₀)(1/n_{X} + 1/n_{Y}))', '=NORM.S.DIST(z, TRUE)'],
                  ['F-test, two variances', 'F = s_{X}² / s_{Y}²,  v_{1} = n_{X} − 1,  v_{2} = n_{Y} − 1', '=F.INV.RT(α, v₁, v₂), =F.DIST.RT(F, v₁, v₂)']],
         'widths': [120, 210, 138], 'center': (), 'boldcol0': True},
}
FIGURES = {}
