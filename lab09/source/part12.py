# -*- coding: utf-8 -*-
MC = [
 ('In a study of how the number of hours studied affects the exam score, the dependent variable (Y) is:', ['the number of hours studied', 'the exam score', 'the number of students', 'the slope']),
 ('In the regression equation ŷ = 46.2 + 5.6x, the number 5.6 tells us:', ['the predicted Y when x = 0', 'how much ŷ changes when x increases by 1', 'the correlation between x and y', 'the residual of the first student']),
 ('The least squares method chooses b₀ and b₁ so that:', ['the sum of the residuals is as large as possible', 'the sum of squared errors SSE is as small as possible', 'R² is equal to 1', 'the line passes through the origin']),
 ('The least squares regression line always passes through the point:', ['(0, 0)', '(0, b₀)', '(x̄, ȳ)', '(1, b₁)']),
 ('A student studied 4 hours and scored 70 points; the line predicts 68.6 points. The residual is:', ['−1.4', '1.4', '68.6', '138.6']),
 ('A regression has R² = 0.81 and a negative slope. The correlation coefficient is:', ['0.81', '0.9', '−0.9', '−0.81']),
 ('In simple linear regression with n = 15 observations, the t-test for the slope has:', ['15 degrees of freedom', '14 degrees of freedom', '13 degrees of freedom', '1 degree of freedom']),
 ('In the Excel coefficients table, the t Stat of the slope is calculated as:', ['Coefficient / Standard Error', 'Standard Error / Coefficient', 'Coefficient × Standard Error', 'R Square / Standard Error']),
 ('In simple linear regression, Significance F in the ANOVA table is:', ['always 0.05', 'equal to the P-value of the slope', 'equal to R Square', 'equal to the P-value of the intercept']),
 ('The Standard Error s in the Regression Statistics measures:', ['the typical size of a residual', 'the standard deviation of X', 'the error of the slope only', 'the share of explained variation']),
 ('The residual plot shows residuals that are negative at both ends and positive in the middle (an arch). This means that:', ['the model is perfect', 'the relationship is not linear', 'the variance is constant', 'the sample is too large']),
 ('A data point has a standardized residual of 3.1. This point is:', ['the best point in the data', 'a possible outlier', 'the intercept', 'always a typing mistake']),
 ('The data on X go from 1 to 10. Using the regression line to predict Y for x = 50 is called:', ['interpolation', 'extrapolation', 'regression to the mean', 'least squares']),
]
TF = [
 'A strong correlation between X and Y proves that X causes Y.',
 'A high R² always means that the linear model is the right model for the data.',
 'Excel shows Multiple R with the same sign as the slope.',
 'Ticking “Constant is Zero” always gives a better model.',
 'For the least squares line, the sum of all residuals is always 0.',
 'For a one-tailed test of the slope, we divide the two-tailed P-value from Excel by 2 (if b₁ has the expected sign).',
]

BLOCKS = [('h1', 'Test Yourself'), ('h2', 'Multiple Choice')]
for i, (q, opts) in enumerate(MC, 1):
    BLOCKS += [('p', f'**9.{i}.** {q}'), ('al', opts)]
BLOCKS.append(('p', '**9.14.** A regression with n = 20 observations gives b₁ = 3 and a standard error of the slope SE(b₁) = 1.2. The test statistic is t = ________ with df = ________.'))
BLOCKS.append(('h2', 'True or False'))
for i, s in enumerate(TF, 15):
    BLOCKS.append(('p', f'**9.{i}.** {s}'))

BLOCKS += [
 ('h1', 'Lab Summary'),
 ('ul', ['**Simple linear regression** describes how a dependent variable Y changes with an independent variable X using a straight line: ŷ = b₀ + b₁x. Always start with a **scatter plot**.',
         'The **least squares** method chooses b₁ = Σ(x − x̄)(y − ȳ) / Σ(x − x̄)² and b₀ = ȳ − b₁x̄, which make the sum of squared residuals SSE as small as possible. The line always passes through (x̄, ȳ).',
         '**b₁** is the change in ŷ when X increases by 1 unit; **b₀** is the predicted Y when X = 0, which makes sense only if X = 0 is realistic.',
         '**R² = SSR / SST** is the share of the variation in Y explained by X (0 ≤ R² ≤ 1). In simple regression R² = r², and r takes the sign of b₁.',
         'The **t-test for the slope** (H₀: β₁ = 0, df = n − 2) and the **F-test** give the same p-value. If the 95% confidence interval for β₁ does not contain 0, the slope is significant.',
         '**Residuals** and the **residual plot** help you check the assumptions: a random cloud around 0 is good; a curve or a growing spread is a warning. Standardized residuals larger than 2 in absolute value point to possible outliers.',
         'Do not **extrapolate** far outside the range of X, and remember that **correlation is not causation**.']),
 ('p', 'Table 18 collects the key formulas and Excel functions from this lab, and Table 19 explains every option of the Excel Regression dialog.'),
 ('cap', 'Table 18. Key formulas and Excel functions from this lab.'),
 ('table', 'T18'),
 ('cap', 'Table 19. Regression dialog checklist: what each option in Data → Data Analysis → Regression does.'),
 ('table', 'T19'),
]

TABLES = {
 'T18': {'rows': [['Quantity', 'Formula', 'In Excel'],
                  ['Slope b₁', 'b₁ = Σ(x − x̄)(y − ȳ) / Σ(x − x̄)²', '=SLOPE(y, x)'],
                  ['Intercept b₀', 'b₀ = ȳ − b₁x̄', '=INTERCEPT(y, x)'],
                  ['Correlation r', 'r = b₁ · s_{x} / s_{y}', '=CORREL(x, y)'],
                  ['Coefficient of determination', 'R² = SSR / SST = 1 − SSE / SST', '=RSQ(y, x)'],
                  ['Standard error of the estimate', 's = √(SSE / (n − 2))', '=STEYX(y, x)'],
                  ['t-test for the slope', 't = b₁ / SE(b₁),  df = n − 2', 'Regression output: t Stat, P-value'],
                  ['Prediction', 'ŷ = b₀ + b₁x', '=FORECAST.LINEAR(x, y, x)'],
                  ['Line through the origin', 'ŷ = b₁x', '=LINEST(y, x, FALSE)']],
         'widths': [130, 190, 148], 'center': (), 'boldcol0': True},
 'T19': {'rows': [['Option', 'What it does', 'Used in'],
                  ['Labels', 'the first row of the selected ranges contains the column headers', 'Task 7'],
                  ['Confidence Level', 'adds confidence intervals at a level other than 95% (for example 99%)', 'Task 6'],
                  ['Constant is Zero', 'forces the line through the origin (b₀ = 0)', 'Task 8'],
                  ['Residuals', 'lists the predicted value ŷ and the residual e for every observation', 'Tasks 4, 6'],
                  ['Standardized Residuals', 'residuals divided by their standard deviation; |value| > 2 means a possible outlier', 'Task 6'],
                  ['Residual Plots', 'a chart of the residuals against X, to check the assumptions', 'Task 4'],
                  ['Line Fit Plots', 'a chart of the observed and the predicted values of Y against X', 'Task 6']],
         'widths': [120, 268, 80], 'center': (2,), 'boldcol0': True},
}
FIGURES = {}
