# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 10. Flu Season on Campus: Does the Flu Shot Really Work?'),
 ('p', 'It is December and half of your class is coughing. The university health centre offered free flu shots in October, and now it wants to know whether they were worth it. At the end of the flu season, the centre checks the records of **500 vaccinated** and **480 unvaccinated** students (Table 18). At **α = 0.05**, are unvaccinated students **more likely** to get the flu than vaccinated students?'),
 ('cap', 'Table 18. Flu cases during the flu season.'),
 ('table', 'T18'),
 ('al', ['Calculate the two sample proportions and check that both samples are large enough. Write H₀ and H₁. Which type of test is this?',
         'Calculate the pooled proportion p₀ and the z statistic.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words. How many times higher is the flu rate among unvaccinated students?']),
 ('p', '**Excel:** =NORM.S.INV(0.95) gives the critical value, and =1-NORM.S.DIST(z, TRUE) gives the p-value.'),
]
TABLES = {
 'T18': [['', 'Unvaccinated (X)', 'Vaccinated (Y)'],
         ['Number of students n', '480', '500'],
         ['Number who got the flu x', '96', '45']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
