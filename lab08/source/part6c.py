# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 3. Who Drinks More Coffee: Engineers or Economists?'),
 ('p', 'There is a popular belief on campus that engineering students “run on coffee”. To test it, a student club runs a short survey and asks students how many **cups of coffee they drink per week**. The results for a random sample of **20 engineering students** and **24 economics students** are shown in Table 11. Assume that both populations are approximately normal with **equal variances**. At **α = 0.05**, is there a **difference** in the average weekly coffee consumption of the two groups?'),
 ('cap', 'Table 11. Cups of coffee per week.'),
 ('table', 'T11'),
 ('al', ['Write H₀ and H₁. Which type of test is this? Why is it reasonable to assume equal variances here?',
         'Calculate the pooled variance s_{p}², the t statistic and the degrees of freedom.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words.']),
 ('p', '**Excel:** =T.INV.2T(0.05, 42) gives the critical value, and =T.DIST.2T(ABS(t), 42) gives the p-value.'),
]
TABLES = {
 'T11': [['', 'Engineering (X)', 'Economics (Y)'],
         ['Sample size n', '20', '24'],
         ['Sample mean (cups per week)', '9.4', '7.1'],
         ['Sample standard deviation s', '3.2', '2.9']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
