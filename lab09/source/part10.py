# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 7 (Extra). Every Second Costs Money'),
 ('p', 'Large online shops say that every extra second of loading time costs them customers. The e-commerce team of a local online shop wants to check this with their own data. For **15 weeks** they recorded the average page **loading time** (in seconds) and the **conversion rate**: the percentage of visitors who actually bought something (Table 16). The team believes that slower pages **reduce** the conversion rate. Use **α = 0.05**.'),
 ('cap', 'Table 16. Average page loading time and conversion rate over 15 weeks.'),
 ('table', 'T16'),
 ('p', '**Sums for the calculation by hand:** x̄ = 3.233, ȳ = 3.047, Σ(x − x̄)² = 43.593, Σ(x − x̄)(y − ȳ) = −20.613, SST = Σ(y − ȳ)² = 11.014.'),
 ('al', ['The team’s claim is directional (“slower pages **reduce** conversion”). Write H₀ and H₁ for the slope β₁. Is this a one-tailed or a two-tailed test?',
         'Draw a scatter plot with a linear trendline. Calculate b₁ and b₀ by hand, write the regression equation and interpret the slope.',
         'Run Data → Data Analysis → Regression. This time select the data **together with the column headers** and tick **Labels**: what changes in the output? Excel shows **Multiple R** = 0.941. What is the correlation coefficient r, and why do you have to add the sign yourself?',
         'Excel always gives a **two-tailed** P-value for the slope. Calculate the one-tailed p-value (P-value / 2) and compare the t Stat with the critical value t₀.₀₅,₁₃ = 1.771. What is your decision?',
         'Calculate and interpret R².',
         'Marketing needs a conversion rate of **at least 3%**. Using the regression equation, find the longest loading time that still meets this target.',
         'The shop has about 10,000 visitors per day. How many orders per day does it lose if the loading time grows from 2 to 4 seconds? What does the model predict for a loading time of 12 seconds, and why is this impossible?']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =CORREL(x, y), =RSQ(y, x), =T.INV(0.95, 13); Data → Data Analysis → Regression with Labels ticked.'),
]
_X = ['0.8', '1.1', '1.4', '1.7', '2.0', '2.3', '2.6', '3.0', '3.4', '3.8', '4.2', '4.7', '5.2', '5.8', '6.5']
_Y = ['4.27', '3.92', '3.80', '3.05', '4.18', '3.84', '3.25', '3.39', '3.05', '2.61', '2.88', '2.25', '2.01', '1.58', '1.62']
TABLES = {
 'T16': {'rows': [['Week', 'Loading time, s (X)', 'Conversion rate, % (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
