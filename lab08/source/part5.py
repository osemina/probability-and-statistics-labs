# -*- coding: utf-8 -*-
BLOCKS = [
 ('h1', 'Part 5. Two Variances (F-test)'),
 ('h2', 'Why an F-test?'),
 ('p', 'The goal of the F-test is to test whether the **variances of two independent populations are equal**. This is useful when you want to check:'),
 ('ul', ['Are the data from one group more spread out than the data from the other group?',
         'Can I assume equal variances when I apply the pooled t-test (Part 3)?']),
 ('p', 'As always, the type of test depends on the alternative hypothesis (Table 7).'),
 ('cap', 'Table 7. Types of F-tests.'),
 ('table', 'T7'),
 ('h2', 'The F Statistic'),
 ('p', 'We calculate the **F statistic** as the ratio of the two sample variances:'),
 ('eq', r'$$F = \frac{s_X^2}{s_Y^2}$$'),
 ('p', 'where s_{X}² and s_{Y}² are the sample variances of group X and group Y. This statistic follows an **F-distribution** with two numbers of degrees of freedom:'),
 ('ul', ['v_{1} = n_{X} − 1 degrees of freedom (numerator);',
         'v_{2} = n_{Y} − 1 degrees of freedom (denominator).']),
 ('p', 'We write the critical value as F_{v1, v2, α}: the value of the F-distribution with an area α **to its right** (this is also what the F-table and Excel’s F.INV.RT give). Unlike z and t, the F-distribution is **not symmetric**: it is skewed to the right and never negative (Figure 2).'),
 ('figure', 'F2'),
 ('cap', 'Figure 2. A right-tailed F-test with v₁ = 10, v₂ = 15 and α = 0.05. The critical value 2.54 cuts off an area of 0.05 in the right tail. F = 3.10 falls in the rejection region, so we reject H₀.'),
 ('box', 'tip', '**Tip:** Put the larger sample variance in the numerator, so that F ≥ 1. This is especially helpful in two-tailed tests: then you only need to compare F with the upper critical value F_{v1, v2, α/2}.'),
 ('h2', 'Decision Rules'),
 ('cap', 'Table 8. Decision rules for the F-test.'),
 ('table', 'T8'),
 ('box', 'note', '**Always think this way:** (1) **Why do we use the F-test?** To compare the spread (variability) of two independent groups. (2) **What is the formula?** F = s_{X}² / s_{Y}². (3) **What do we compare it to?** A critical F value from the F-table, based on v_{1} and v_{2}. (4) **When do we reject H₀?** If the calculated F falls into the rejection region.'),
 ('box', 'mistake', '**Common mistake:** Comparing standard deviations instead of variances. The F statistic uses s², so square the standard deviations first.'),
]
TABLES = {
 'T7': [['Test type', 'H₀', 'H₁', 'Use when you want to know if…'],
        ['Left-tailed', 'σ_{X}² ≥ σ_{Y}²', 'σ_{X}² < σ_{Y}²', 'the variance in group X is less than in group Y'],
        ['Right-tailed', 'σ_{X}² ≤ σ_{Y}²', 'σ_{X}² > σ_{Y}²', 'the variance in group X is greater than in group Y'],
        ['Two-tailed', 'σ_{X}² = σ_{Y}²', 'σ_{X}² ≠ σ_{Y}²', 'the variances are not equal']],
 'T8': [['Test type', 'Reject H₀ if'],
        ['Right-tailed', 'F > F_{v1, v2, α}'],
        ['Left-tailed', 'F < F_{v1, v2, 1−α}'],
        ['Two-tailed', 'F < F_{v1, v2, 1−α/2} or F > F_{v1, v2, α/2}']],
}
_W = {'T7': ([90, 90, 90, 198], (1, 2)), 'T8': ([150, 318], (1,))}
TABLES = {k: {'rows': v, 'widths': _W[k][0], 'center': _W[k][1], 'boldcol0': True} for k, v in TABLES.items()}
FIGURES = {'F2': ('fig2_f_distribution.gif', 468, 211)}
