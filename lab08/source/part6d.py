# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 4. E-scooter or Tram: Which Gets You to Campus Faster?'),
 ('p', 'A group of students who live in the same part of the city cannot agree on the fastest way to get to campus. Some take an **e-scooter**, others take the **tram**. For a month, they recorded their door-to-door travel times (Table 12). The tram times vary much more than the scooter times, because of traffic jams and waiting at the stops, so the population variances are **unknown and clearly different**. At **α = 0.05**, is the e-scooter **faster** on average?'),
 ('cap', 'Table 12. Travel times to campus (minutes).'),
 ('table', 'T12'),
 ('al', ['Write H₀ and H₁. Which type of test is this? Why do we use Welch’s t-test and not the pooled t-test?',
         'Calculate the t statistic and the degrees of freedom ν with the Welch–Satterthwaite formula.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words.']),
 ('p', '**Excel:** =T.INV(0.05, 34) gives the (negative) critical value, and =T.DIST(t, 34, TRUE) gives the p-value (ν rounded down to 34).'),
]
TABLES = {
 'T12': [['', 'E-scooter (X)', 'Tram (Y)'],
         ['Number of trips n', '15', '25'],
         ['Mean travel time', '38.5 min', '52.0 min'],
         ['Standard deviation s', '6.2 min', '15.4 min']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
