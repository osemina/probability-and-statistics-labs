# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 8. Phone A or Phone B: Which Battery Really Lasts Longer?'),
 ('p', 'Two popular phone models in the same price range both advertise an “all-day battery”. A tech YouTuber wants to find out which one really lasts longer, so she runs the same video-streaming test (same brightness, same Wi-Fi, same video) on **25 units of each phone** and records how many minutes each phone lasts until the battery is empty (Table 16). Battery life is approximately normally distributed and the population variances are unknown. At **α = 0.05**, is there a **difference** in the average battery life of the two phones?'),
 ('cap', 'Table 16. Battery life in the streaming test (minutes).'),
 ('table', 'T16'),
 ('al', ['Write H₀ and H₁. Which type of test is this? Compare the two sample variances: should you use the pooled t-test or Welch’s t-test?',
         'Calculate the pooled variance s_{p}², the t statistic and the degrees of freedom.',
         'Find the critical value and the p-value, make a decision and write the conclusion in words. Can the YouTuber say that one phone has a better battery?']),
 ('p', '**Excel:** =T.INV.2T(0.05, 48) gives the critical value, and =T.DIST.2T(ABS(t), 48) gives the p-value.'),
]
TABLES = {
 'T16': [['', 'Phone A (X)', 'Phone B (Y)'],
         ['Number of phones tested n', '25', '25'],
         ['Mean battery life', '412 min', '438 min'],
         ['Standard deviation s', '48 min', '55 min']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
