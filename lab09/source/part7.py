# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 4. Does Coffee Make You Productive?'),
 ('p', 'A tech start-up has just installed a free espresso machine in its office, and the coffee bill is growing fast. Before the next budget meeting, the HR manager wants to know whether the coffee is at least worth it. For one week, **15 employees** recorded how many cups of coffee they drank per day and rated their own productivity on a scale from 0 to 100 (Table 13). Use **α = 0.05**.'),
 ('cap', 'Table 13. Cups of coffee per day and self-reported productivity score of 15 employees.'),
 ('table', 'T13'),
 ('p', '**Sums for the calculation by hand:** x̄ = 4.667, ȳ = 71.373, Σ(x − x̄)² = 141.33, Σ(x − x̄)(y − ȳ) = 389.37, SST = Σ(y − ȳ)² = 1293.79.'),
 ('al', ['Which variable is X and which is Y? Draw a scatter plot with a linear trendline.',
         'Calculate b₁ and b₀ by hand, write the regression equation and interpret the slope: how many productivity points does one extra cup bring?',
         'Run Data → Data Analysis → Regression and tick **Residuals** and **Residual Plots**. In the **Residual Output**, find the predicted productivity and the residual of employee 2. Which employee is the furthest above the line, and which is the furthest below? What is the sum of all residuals, and why?',
         'Look at the **residual plot** (residuals against cups of coffee). Do the points form a random cloud around 0, or can you see a pattern (a curve, or a spread that grows with X)? Which assumptions from Part 2 does this plot help you check?',
         'In the **ANOVA** table, explain where the degrees of freedom 1, 13 and 14 come from. Calculate MS = SS / df for the Regression and the Residual rows, then F = MS Regression / MS Residual, and compare your results with Excel. Check that MS Residual is equal to the square of the Standard Error s.',
         'Calculate and interpret R². Is the relationship significant (use Significance F)?',
         'The HR manager wants to write in the report: “Every extra cup of coffee increases productivity by almost 3 points.” Name at least two limitations of this study (think about how productivity was measured and what else could explain the relationship), and explain why the model should not be used for 15 cups per day.']),
 ('p', '**Excel:** =SLOPE(y, x), =INTERCEPT(y, x), =RSQ(y, x), =STEYX(y, x); Data → Data Analysis → Regression with Residuals and Residual Plots ticked.'),
]
_X = ['2', '4', '2', '0', '4', '9', '6', '6', '8', '9', '9', '2', '6', '0', '3']
_Y = ['58.3', '77.2', '67.3', '61.2', '65.9', '76.8', '75.8', '75.5', '82.4', '85.3', '83.9', '59.1', '78.6', '59.6', '63.7']
TABLES = {
 'T13': {'rows': [['Employee', 'Cups of coffee per day (X)', 'Productivity score (Y)']] + [[str(i + 1), a, b] for i, (a, b) in enumerate(zip(_X, _Y))],
         'widths': [90, 160, 160], 'center': (0, 1, 2)},
}
FIGURES = {}
