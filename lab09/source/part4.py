# -*- coding: utf-8 -*-
BLOCKS = [
 ('h1', 'Part 6. Tasks'),
 ('p', 'Each task uses a real-size data set, so the main tool is **Excel**: enter the data, draw a scatter plot with a trendline, and run Data → Data Analysis → Regression. The sums given under each table let you also check b₁ and b₀ **by hand**, using the formulas from Part 3. Tasks 6–8 are extra practice for students who finish early. The tasks you do not finish in class can be completed at home.'),

 ('h2', 'Task 1. Is Experience Worth the Money?'),
 ('p', 'A career platform for software developers wants to show its users how much their salary can grow with experience. It collected the annual salaries (in thousands of dollars) and the years of experience of **15 software developers**, from juniors with one year of experience to seniors with almost ten (Table 10). The question is simple: **is experience a significant factor in predicting salary, and how much is one extra year worth?** Use **α = 0.05**.'),
 ('cap', 'Table 10. Years of experience and annual salary of 15 software developers.'),
 ('table', 'T10'),
 ('p', '**Sums for the calculation by hand:** x̄ = 5.453, ȳ = 61.753, Σ(x − x̄)² = 134.04, Σ(x − x̄)(y − ȳ) = 804.95, SST = Σ(y − ȳ)² = 5046.71.'),
 ('al', ['Which variable is X and which is Y? Draw a scatter plot in Excel and add a linear trendline with the equation and R². Describe the pattern you see.',
         'Using the sums above, calculate b₁ and b₀ by hand and write the regression equation. Check your result with =SLOPE(…) and =INTERCEPT(…).',
         'Interpret the slope and the intercept in context. Does the intercept make sense for this data?',
         'Calculate SSR = b₁ · Σ(x − x̄)(y − ȳ) and R² = SSR / SST. What share of the variation in salaries is explained by experience?',
         'Run Data → Data Analysis → Regression. Use the p-value and the 95% confidence interval of the slope to decide whether experience has a significant effect on salary.',
         'Predict the salary of a developer with 5 years of experience. Why would it be wrong to use the model for a developer with 40 years of experience?']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =FORECAST.LINEAR(5, y, x); Data → Data Analysis → Regression for the p-value and the confidence interval.'),
]
_X = ['4.4', '9.6', '7.6', '6.4', '2.4', '2.4', '1.5', '8.8', '6.4', '7.4', '1.2', '9.7', '8.5', '2.9', '2.6']
_Y = ['54.69', '84.83', '67.76', '71.25', '46.85', '39.83', '37.72', '80.57', '66.29', '67.98', '35.31', '89.99', '88.68', '48.58', '45.97']
TABLES = {
 'T10': {'rows': [['Developer', 'Years of experience (X)', 'Salary, $1000s (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
