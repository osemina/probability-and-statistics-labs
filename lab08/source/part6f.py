# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 6. iPhone vs Android: Whose Screen Time Is More Unpredictable?'),
 ('p', 'You are part of a student team building **“Unplug”**, a digital wellbeing app that sends smart reminders when someone has been on their phone for too long. Before the launch, your UX designer asks an important question: “Should the reminders work the same way for everyone?”'),
 ('p', 'If one group of users has very **unpredictable** screen time (2 hours one day, 7 hours the next), fixed daily limits will not work for them, and the app will need to learn each user’s habits instead. You suspect that **iPhone users have more variable screen time than Android users**. To check this, you take a random sample of users, read their screen-time reports for the past 14 days and calculate the variance of each group’s daily screen time (Table 14). Test your suspicion at **α = 0.05**.'),
 ('cap', 'Table 14. Variance of daily screen time.'),
 ('table', 'T14'),
 ('al', ['Write H₀ and H₁. Which type of test is this?',
         'Calculate the F statistic and the degrees of freedom v_{1} and v_{2}.',
         'Find the critical value and the p-value, and make a decision. What should the UX designer do: one rule for everyone, or separate settings for iPhone users?']),
 ('p', '**Excel:** =F.INV.RT(0.05, 24, 20) gives the critical value, and =F.DIST.RT(F, 24, 20) gives the p-value.'),
]
TABLES = {
 'T14': [['', 'iPhone users (X)', 'Android users (Y)'],
         ['Sample size n', '25', '21'],
         ['Sample variance s² (hours²)', '2.25', '1.20']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
