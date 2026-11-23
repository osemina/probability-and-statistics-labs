# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 6 (Extra). When Does the Server Slow Down?'),
 ('p', 'The DevOps team of an online shop is preparing for Black Friday. Their contract with clients (SLA) says that the server must answer every request in **less than 300 ms**. To see how the server behaves under pressure, they run a load test: they simulate from 50 to 750 users at the same time and measure the average **response time** in milliseconds (Table 15). Use **α = 0.05**.'),
 ('cap', 'Table 15. Number of simultaneous users and average server response time in a load test.'),
 ('table', 'T15'),
 ('p', '**Sums for the calculation by hand:** x̄ = 400, ȳ = 251.13, Σ(x − x̄)² = 700,000, Σ(x − x̄)(y − ȳ) = 277,350, SST = Σ(y − ȳ)² = 120,593.73.'),
 ('al', ['Draw a scatter plot with a linear trendline. Calculate b₁ and b₀ by hand and write the regression equation. Interpret the slope (per 100 extra users) and the intercept (an “empty” server).',
         'Run Data → Data Analysis → Regression and tick **Residuals**, **Standardized Residuals** and **Line Fit Plots**. Also tick **Confidence Level** and set it to **99%**. In the Line Fit Plot, which measurement lies furthest from its predicted value?',
         'In the Residual Output, find the measurement with a **standardized residual** larger than 2 in absolute value. Such a point is a possible **outlier**. The server logs show that a nightly database backup started during this measurement. Should the point be removed? Run the regression again without it: how do b₁ and R² change?',
         'Compare the 95% and the 99% confidence intervals of the slope in the output. Why is the 99% interval wider? Does either interval contain 0?',
         'Using the regression equation, find the largest number of users for which the predicted response time stays below the SLA limit of 300 ms.',
         'On Black Friday the shop expects 5000 users at the same time. What response time does the model predict? Explain why the DevOps team should not trust this number.']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =FORECAST.LINEAR(5000, y, x); Data → Data Analysis → Regression with Residuals, Standardized Residuals, Line Fit Plots and Confidence Level 99%.'),
]
_X = ['50', '100', '150', '200', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750']
_Y = ['103', '120', '155', '166', '175', '213', '250', '265', '256', '377', '300', '333', '311', '370', '373']
TABLES = {
 'T15': {'rows': [['Test', 'Simultaneous users (X)', 'Response time, ms (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
