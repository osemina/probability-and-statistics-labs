# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 2. Do Students in the Front Rows Get Better Grades?'),
 ('p', 'A statistics professor has noticed that students who always sit in the front rows seem to do better on exams. From many years of exam records, the **population standard deviation** of exam scores is known: **σ = 12 points** for both groups. This semester, the professor compares the final exam scores of **36 students** who always sit in the front rows with **42 students** who always sit at the back (Table 10). At **α = 0.05**, do front-row students score **higher** on average?'),
 ('cap', 'Table 10. Final exam scores of front-row and back-row students.'),
 ('table', 'T10'),
 ('al', ['Write H₀ and H₁. Which type of test is this, and why do we use z?',
         'Calculate the standard error and the z statistic.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words. Does this prove that sitting in the front rows **causes** better grades?']),
 ('p', '**Excel:** =NORM.S.INV(0.95) gives the critical value, and =1-NORM.S.DIST(z, TRUE) gives the p-value.'),
]
TABLES = {
 'T10': [['', 'Front rows (X)', 'Back rows (Y)'],
         ['Population standard deviation σ', '12 points', '12 points'],
         ['Sample size n', '36', '42'],
         ['Sample mean', '74.5 points', '68.9 points']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
