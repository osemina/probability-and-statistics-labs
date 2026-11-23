# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 8 (Extra). How Much Does Another Roommate Cost?'),
 ('p', 'You are moving into a shared flat and you want to plan the monthly budget for groceries. How much more do you spend for every new roommate? A local economic research team collected the household size and the monthly grocery spending (in dollars) of **15 households** (Table 17). Use **α = 0.05**.'),
 ('cap', 'Table 17. Household size and monthly grocery spending of 15 households.'),
 ('table', 'T17'),
 ('p', '**Sums for the calculation by hand:** x̄ = 4.267, ȳ = 696.72, Σ(x − x̄)² = 50.933, Σ(x − x̄)(y − ȳ) = 4752.44, SST = Σ(y − ȳ)² = 456,339.57.'),
 ('al', ['Draw a scatter plot with a linear trendline. Calculate b₁ and b₀ by hand and write the regression equation.',
         'Interpret the slope: how much additional spending is expected per additional household member? What does the intercept represent, if a household with 0 members does not exist?',
         'A classmate says: “With 0 people there is no spending, so the line must go through the origin.” Run Data → Data Analysis → Regression twice: once as usual, and once with **Constant is Zero** ticked. Write both regression equations. How much does the slope change?',
         'Use both models to predict the spending of a one-person household and compare the predictions with the two one-person households in Table 17. Which model describes the data better?',
         'With Constant is Zero, Excel still shows an R Square, but it is calculated around 0 instead of around ȳ, so the two R² values **cannot be compared**. Which parts of the output (coefficients, residuals, predictions) are better for choosing between the two models?',
         'When is it justified to tick Constant is Zero? Give one example where the line really must pass through the origin, and explain why grocery spending is not such a case.',
         'Using the better model, predict the monthly grocery cost for a household of 2 people and a household of 6 people. What factors (other than household size) might influence the accuracy of these predictions?']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =FORECAST.LINEAR(2, y, x); =LINEST(y, x, FALSE) gives the slope of the line through the origin; Data → Data Analysis → Regression with and without Constant is Zero.'),
]
_X = ['3', '4', '2', '3', '5', '6', '1', '5', '6', '4', '5', '7', '1', '6', '6']
_Y = ['533.52', '682.90', '513.39', '535.05', '740.27', '865.74', '445.61', '752.52', '879.18', '696.33', '760.32', '977.79', '368.24', '880.98', '818.97']
TABLES = {
 'T17': {'rows': [['Household', 'Household size (X)', 'Grocery spending, $ (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
