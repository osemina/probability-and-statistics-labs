# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 2. How Fast Does a Car Lose Value?'),
 ('p', 'You want to buy a used car and you are browsing an online marketplace. To know whether an ad is a good deal, you collect the age and the asking price (in thousands of KM) of **15 used cars of the same model** (Table 11). How much value does this car lose every year, and can the age alone predict the price? Use **α = 0.05**.'),
 ('cap', 'Table 11. Age and asking price of 15 used cars of the same model.'),
 ('table', 'T11'),
 ('p', '**Sums for the calculation by hand:** x̄ = 8.267, ȳ = 19.107, Σ(x − x̄)² = 238.93, Σ(x − x̄)(y − ȳ) = −483.13, SST = Σ(y − ȳ)² = 1035.15.'),
 ('al', ['Which variable is X and which is Y? Draw a scatter plot with a linear trendline. Is the relationship positive or negative?',
         'Calculate b₁ and b₀ by hand and write the regression equation. Check your result with =SLOPE(…) and =INTERCEPT(…).',
         'Interpret the slope in context: how many KM does the car lose per year? What does the intercept represent, and is it realistic?',
         'Calculate R². What share of the variation in prices is explained by the age of the car? What else could explain the rest?',
         'Run Data → Data Analysis → Regression. Use the F-test (Significance F) and the p-value of the slope to decide whether age has a significant effect on price.',
         'A 6-year-old car of this model is offered for 20,000 KM. Is it cheaper or more expensive than the model predicts? What price does the model give for a 20-year-old car, and why is this result impossible?']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =FORECAST.LINEAR(6, y, x); Data → Data Analysis → Regression for Significance F and the p-value.'),
]
_X = ['2', '3', '4', '5', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
_Y = ['35.3', '28.7', '28.6', '23.3', '24.7', '21.3', '22.8', '18.4', '19.7', '17.3', '14.5', '7.3', '9.5', '8.5', '6.7']
TABLES = {
 'T11': {'rows': [['Car', 'Age in years (X)', 'Price, 1000 KM (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
