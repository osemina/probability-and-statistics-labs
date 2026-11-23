# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 5. Is the Ad Budget Worth It?'),
 ('p', 'The marketing team of a fitness app spends money every month on Instagram and TikTok ads. The CFO asks a hard question: **“How many new users do we get for every 1000 dollars, and how many would we get without any ads at all?”** The team collects the monthly advertising budget (in thousands of dollars) and the number of new app sign-ups for **15 months** (Table 14). Use **α = 0.05**.'),
 ('cap', 'Table 14. Monthly advertising budget and number of new app sign-ups over 15 months.'),
 ('table', 'T14'),
 ('p', '**Sums for the calculation by hand:** x̄ = 30.78, ȳ = 1854.13, Σ(x − x̄)² = 1392.12, Σ(x − x̄)(y − ȳ) = 69,627.94, SST = Σ(y − ȳ)² = 3,664,268.'),
 ('al', ['Draw a scatter plot with a linear trendline and write the regression equation (by hand, using the sums above, and with =SLOPE and =INTERCEPT).',
         'Interpret the slope: how many new users does every extra 1000 dollars bring? How much does one new user cost the company?',
         'Run Data → Data Analysis → Regression. In the coefficients table, check that **t Stat = Coefficients / Standard Error** for both rows. Which t Stat is larger, and what does that tell you?',
         'Interpret the intercept in this context. Is it significant (P-value of the Intercept)? Read the **Lower 95% and Upper 95%** of the intercept and explain the interval in one sentence. Why does the intercept make sense here, while in Task 3 it did not?',
         'Read R² and the 95% confidence interval of the slope. Can the CFO be confident that every 1000 dollars brings at least 40 new users?',
         'Predict the number of sign-ups for a budget of 20,000 dollars and of 50,000 dollars (use =FORECAST.LINEAR). The data go from 15,400 to 49,100 dollars: which prediction is more reliable? What would the model say for a budget of 100,000 dollars, and why should the CFO not trust that number?']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =FORECAST.LINEAR(20, y, x); Data → Data Analysis → Regression for t Stat, P-values and the confidence intervals.'),
]
_X = ['29.4', '27.9', '33.6', '16.3', '31.5', '49.1', '26.9', '45.8', '24.5', '20.8', '34.0', '35.1', '43.9', '15.4', '27.5']
_Y = ['1880', '1843', '2020', '937', '1851', '2788', '1696', '2577', '1559', '1552', '2155', '1960', '2435', '1059', '1500']
TABLES = {
 'T14': {'rows': [['Month', 'Ad budget, $1000s (X)', 'New sign-ups (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
