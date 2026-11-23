# -*- coding: utf-8 -*-
BLOCKS = [
 ('h2', 'Task 9. Your First Car: Is a Hybrid Really Worth It?'),
 ('p', 'You have just got your driving licence and your parents offer to help you buy your first car. You like a cheaper **petrol** model, but your parents insist on the **hybrid** version of the same car: “It will save you a fortune on fuel!” You decide to settle the argument with statistics.'),
 ('p', 'A transport research institute has tested thousands of cars, so the **population variances of fuel consumption are known**: σ² = 0.49 for hybrids and σ² = 1.00 for petrol cars. In a new test, **60 hybrids** and **55 petrol cars** were driven on the same route (Table 17). At **α = 0.01**, is there a **difference** in average fuel consumption?'),
 ('cap', 'Table 17. Fuel consumption (L/100 km).'),
 ('table', 'T17'),
 ('al', ['Write H₀ and H₁. Which type of test is this, and why do we use z?',
         'Calculate the standard error and the z statistic.',
         'Find the critical value for α = 0.01 and the p-value, make a decision and write the conclusion in words. Would your decision change at α = 0.05? If you drive 15,000 km per year and fuel costs 1.60 € per litre, how much would the hybrid save you per year? Who wins the argument?']),
 ('p', '**Excel:** =NORM.S.INV(0.995) gives the critical value, and =2*NORM.S.DIST(z, TRUE) gives the p-value (here z is negative).'),
]
TABLES = {
 'T17': [['', 'Hybrid (X)', 'Petrol (Y)'],
         ['Population variance σ²', '0.49', '1.00'],
         ['Sample size n', '60', '55'],
         ['Sample mean', '4.6 L/100 km', '5.0 L/100 km']],
}
TABLES = {k: {'rows': v, 'widths': [190, 130, 130], 'center': (1, 2), 'boldcol0': True} for k, v in TABLES.items()}
