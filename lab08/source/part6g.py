# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Extra Practice (If You Have Time Left)'),
 ('p', 'Tasks 7–10 practise the same tests in new situations: a left-tailed F-test, a two-tailed comparison of means with unknown variances, a z-test with known variances and a comparison of two proportions.'),

 ('h2', 'Task 7. Is AI a Fairer Grader Than Humans?'),
 ('p', 'A professor wants to find out whether an AI tool could help with grading. **25 student essays** are graded twice: once by the AI tool and once by a team of human teaching assistants. Everybody knows that human graders are sometimes “strict” and sometimes “generous”, depending on the day and on who is grading. The professor wants to know whether the AI scores are **more consistent**, that is, whether they have a **smaller variance** (Table 15). Assume that the scores are approximately normally distributed and use **α = 0.05**.'),
 ('cap', 'Table 15. Variance of essay scores (points out of 100).'),
 ('table', 'T15'),
 ('al', ['Write H₀ and H₁. Which type of test is this?',
         'Calculate the F statistic and the degrees of freedom v_{1} and v_{2}.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words. If the AI scores are more consistent, does that also mean that they are more correct?']),
 ('p', '**Excel:** =F.INV(0.05, 24, 24) gives the (lower) critical value, and =F.DIST(F, 24, 24, TRUE) gives the p-value.'),
]
TABLES = {
 'T15': [['', 'AI tool (X)', 'Human graders (Y)'],
         ['Number of essays n', '25', '25'],
         ['Sample variance s² (points²)', '6.5', '14.0']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
