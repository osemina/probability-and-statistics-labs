# -*- coding: utf-8 -*-
BLOCKS = [
 ('h1', 'Part 2. Paired Samples'),
 ('h2', 'What Are Dependent (Paired) Samples?'),
 ('p', 'Sometimes we are not comparing two different groups, but looking at the **same sample** before and after something. We call these **dependent (paired) samples**, because they are connected: the same people or the same places, just in two different situations (for example before vs. after). Examples:'),
 ('ul', ['Students take a test before and after additional classes.',
         'We measure a person’s weight before and after a diet.',
         'We count the number of mistakes at work before and after a training.']),
 ('h2', 'The Differences d'),
 ('p', 'With dependent samples, we always look at the **difference for each person (pair)**: the difference between the first and the second measurement for the same individual.'),
 ('eq', r'$$d_i = x_i - y_i$$'),
 ('p', '**Assumption:** the differences come from a normally distributed population.'),
 ('p', 'The goal of the test is to see whether there is a **real change**. Once we have the differences d_{i}, we ask: is the average difference large enough to say that something really changed, or could it be just a coincidence? To answer this, we use the **t-test for dependent samples (paired t-test)**.'),
 ('h2', 'The Test Statistic'),
 ('p', 'The test statistic for the mean difference is a t value with **n − 1 degrees of freedom**:'),
 ('eq', r'$$t = \frac{\bar{d} - D_0}{s_d / \sqrt{n}}, \qquad df = n - 1$$'),
 ('p', 'where:'),
 ('ul', [r'$$\bar{d} = \frac{\sum d_i}{n}$$ is the mean of the differences;',
         's_{d} is the sample standard deviation of the differences;',
         'n is the sample size (the number of pairs);',
         'D_{0} is the hypothesized mean difference; under H₀ it is usually **D_{0} = 0** (“no change”).']),
 ('p', 'This formula converts the data into a t value, which we then compare with the critical values from the t-distribution (Table 3).'),
 ('cap', 'Table 3. Decision rules for paired samples (μ_{d} is the population mean difference).'),
 ('table', 'T3'),
 ('box', 'tip', '**Tip:** Always subtract in the same order for every pair (for example before − after). The sign of d̄ then tells you the direction: if before − after > 0, the values went down.'),
 ('box', 'mistake', '**Common mistake:** Treating paired data as two independent samples. If the same people are measured twice, compute the differences first and use the paired t-test.'),
]
TABLES = {
 'T3': [['Test type', 'H₀', 'H₁', 'Reject H₀ if'],
        ['Left-tailed', 'μ_{d} ≥ 0', 'μ_{d} < 0', 't < −t_{n−1, α}'],
        ['Right-tailed', 'μ_{d} ≤ 0', 'μ_{d} > 0', 't > t_{n−1, α}'],
        ['Two-tailed', 'μ_{d} = 0', 'μ_{d} ≠ 0', 't < −t_{n−1, α/2} or t > t_{n−1, α/2}']],
}
_W = {'T3': ([100, 90, 90, 188], (1, 2, 3))}
TABLES = {k: {'rows': v, 'widths': _W[k][0], 'center': _W[k][1], 'boldcol0': True} for k, v in TABLES.items()}
FIGURES = {}
