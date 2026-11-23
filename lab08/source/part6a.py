# -*- coding: utf-8 -*-
BLOCKS = [
 ('h1', 'Part 6. Tasks'),
 ('p', 'Solve each task by hand, following the five steps (hypotheses, α and the critical value, test statistic, p-value, decision) and using the Z-, t- or F-table, and then check your answers in Excel with the functions given under the task. Tasks 7–10 are extra practice for students who finish early. The tasks you do not finish in class can be completed at home.'),

 ('h2', 'Task 1. Does Gaming Before Bed Keep You Awake?'),
 ('p', 'A group of **8 university students** wanted to find out whether playing video games just before bedtime affects their sleep. Each student tracked how many minutes they stayed awake in bed before falling asleep on two different nights:'),
 ('ul', ['one night they did **not** play any games before sleep;',
         'another night they played video games **just before** going to bed.']),
 ('p', 'The students believe that gaming keeps them awake longer. Test this claim at **α = 0.05** (Table 9).'),
 ('cap', 'Table 9. Minutes awake before falling asleep.'),
 ('table', 'T9'),
 ('al', ['Why are these samples **dependent**? Write H₀ and H₁. Which type of test is this?',
         'Calculate the differences d = y − x, the mean difference d̄ and the standard deviation s_{d}.',
         'Calculate the t statistic, find the critical value and the p-value, make a decision and write the conclusion in words.']),
 ('p', '**Excel:** =T.INV(0.95, 7) gives the critical value, and =T.DIST.RT(t, 7) gives the p-value. =AVERAGE(…) and =STDEV.S(…) of the differences give d̄ and s_{d}.'),
]
TABLES = {
 'T9': [['Student', 'No gaming (X)', 'With gaming (Y)'],
        ['1', '12', '18'], ['2', '8', '9'], ['3', '15', '22'], ['4', '5', '11'],
        ['5', '10', '9'], ['6', '20', '28'], ['7', '7', '12'], ['8', '9', '14']],
}
TABLES = {k: {'rows': v, 'widths': [90, 130, 130], 'center': (0, 1, 2)} for k, v in TABLES.items()}
