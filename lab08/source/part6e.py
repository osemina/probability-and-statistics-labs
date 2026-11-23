# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 5. Do Students Fall for Phishing More Often Than Staff?'),
 ('p', 'As part of a cybersecurity awareness week, the university IT department sends a **fake phishing email** (“Your account will be blocked – click here to confirm your password”) to a random sample of students and staff. Nobody’s password is collected: the IT department only records who clicked the link (Table 13). At **α = 0.05**, do students click the phishing link **more often** than staff?'),
 ('cap', 'Table 13. Results of the phishing test.'),
 ('table', 'T13'),
 ('al', ['Calculate the two sample proportions and check that both samples are large enough. Write H₀ and H₁. Which type of test is this?',
         'Calculate the pooled proportion p₀ and the z statistic.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words. What would you recommend to the IT department?']),
 ('p', '**Excel:** =NORM.S.INV(0.95) gives the critical value, and =1-NORM.S.DIST(z, TRUE) gives the p-value.'),
]
TABLES = {
 'T13': [['', 'Students (X)', 'Staff (Y)'],
         ['Number of people who received the email n', '200', '210'],
         ['Number who clicked the link x', '46', '27']],
}
TABLES = {k: {'rows': v, 'widths': [230, 110, 110], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
