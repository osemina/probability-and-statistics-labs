# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 3. Do Five Stars Bring Downloads?'),
 ('p', 'You and two friends have just published a study-planner app on Google Play. Your first investor says: **“Get the rating up and the downloads will follow.”** Before you spend the next month answering every one-star review, you decide to check the claim with data. You collect the average rating (1.0 to 5.0) and the number of downloads of **15 apps** from the same category (Table 12). Use **α = 0.05**.'),
 ('cap', 'Table 12. Average rating and number of downloads of 15 apps from the same category.'),
 ('table', 'T12'),
 ('p', '**Sums for the calculation by hand:** x̄ = 3.847, ȳ = 17,847.87, Σ(x − x̄)² = 7.197, Σ(x − x̄)(y − ȳ) = 13,458.79, SST = Σ(y − ȳ)² = 63,547,318.'),
 ('al', ['Draw a scatter plot with a linear trendline. Compare it with the scatter plots from Tasks 1 and 2: how close are the points to the line now?',
         'Calculate b₁ and b₀ by hand, write the regression equation and interpret the slope: how many extra downloads does one extra star bring?',
         'Run Data → Data Analysis → Regression. Read **Multiple R** and **R Square** from the Regression Statistics. Why is Multiple R positive here? Then compare R Square with **Adjusted R Square**: why is the adjusted value smaller?',
         'Read the **Standard Error** (s) of the regression. What does it tell you about the typical error of a prediction? Predict the downloads of an app with a rating of 4.5 and give a rough range ŷ ± 2s.',
         'Use the p-value and the 95% confidence interval of the slope (Lower 95% and Upper 95%) to decide whether the rating has a significant effect on downloads. Why is the interval so wide?',
         'The p-value of the **Intercept** is also very small. Does this mean that b₀ (the downloads of an app with a rating of 0) has a practical meaning? Explain.',
         'Is your investor right? The slope is significant, but R² is only about 0.4: name at least three other factors that could influence the number of downloads, and explain why a higher rating does not necessarily **cause** more downloads.']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =STEYX(y, x) for the standard error s, =FORECAST.LINEAR(4.5, y, x); Data → Data Analysis → Regression for the full output.'),
]
_X = ['4.3', '3.3', '3.9', '3.8', '4.9', '4.6', '4.4', '3.8', '4.0', '4.9', '4.0', '3.2', '3.2', '2.9', '2.5']
_Y = ['15,786', '14,550', '18,754', '16,240', '20,514', '21,155', '19,117', '18,496', '16,655', '19,632', '20,203', '14,714', '17,825', '18,390', '15,687']
TABLES = {
 'T12': {'rows': [['App', 'Average rating (X)', 'Downloads (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
