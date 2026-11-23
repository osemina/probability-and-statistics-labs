# -*- coding: utf-8 -*-
BLOCKS = [
 ('h1', 'Lab Objectives'),
 ('p', 'By the end of this lab, students will be able to:'),
 ('ol', ['decide whether two samples are **dependent (paired)** or **independent**;',
         'test the **mean difference** of paired samples with the **paired t-test**;',
         'compare two independent means with the **z-test** (σ known), the **pooled t-test** (equal variances) and **Welch’s t-test** (unequal variances);',
         'compare two **population proportions** with the z-test and the **pooled proportion**;',
         'compare two **population variances** with the **F-test**;',
         'choose the right two-sample test for a real problem and write the conclusion in words.']),
 ('cap', 'Table 1. Plan for the 90-minute session.'),
 ('table', 'T1'),
 ('box', 'tip', '**Before you start:** You need a calculator, the Z-, t- and F-tables and Excel. Every test in this lab follows the same five steps as in Lab 7: hypotheses, α and the critical value, test statistic, p-value, decision. Only the formula for the test statistic changes.'),

 ('h1', 'Part 1. Comparing Two Populations'),
 ('h2', 'Why Do We Compare Two Groups?'),
 ('p', 'In the previous lab, we learned how to test hypotheses about **one population**, for example whether the average height of students is greater than 170 cm. However, in real life we often have to **compare two groups**. For example:'),
 ('ul', ['Does the new therapy really lower blood pressure (before vs. after)?',
         'Are iOS users more satisfied than Android users?',
         'Did students from two different groups achieve different results on the test?']),
 ('p', 'When we have two groups, we use **two-sample tests**: statistical tests that compare two groups in some respect, their **mean**, **proportion** or **variance**.'),
 ('h2', 'Four Types of Two-Sample Tests'),
 ('p', 'There are four main types of two-sample tests (Table 2):'),
 ('ol', ['**Population means, dependent samples.** Two measurements within the same group are compared, for example before and after a treatment. **Example:** a fitness trainer measures the resting heart rate of clients before and after a 6-week exercise program and wants to test whether the program lowered their heart rate.',
         '**Population means, independent samples.** The averages of two separate, unrelated groups are compared. There is no overlap between the groups. **Example:** the average height of men vs. women.',
         '**Population proportions.** Percentages or proportions of two groups are compared. **Example:** in a survey, 60% of city residents vs. 45% of rural residents support a new environmental policy. Is the proportion of support significantly different?',
         '**Population variances.** The variability of two groups is compared: not the averages, but how consistent or scattered the results are. **Example:** a school administrator wants to know whether student grades vary more in morning classes or in evening classes.']),
 ('cap', 'Table 2. The four types of two-sample tests.'),
 ('table', 'T2'),
 ('p', 'Figure 1 shows how to choose the right test, step by step.'),
 ('figure', 'F1'),
 ('cap', 'Figure 1. Which two-sample test? First decide what you compare (mean, proportion or variance). For means, decide whether the samples are paired or independent, and for independent samples whether σ is known and whether the variances are equal.'),
 ('box', 'note', '**Key question:** When choosing a test, first ask: are the groups **dependent or independent**, and what are we measuring: a **mean**, a **proportion** or a **variance**?'),
]

TABLES = {
 'T1': [['Part', 'Activity', 'Time'],
        ['1', 'Comparing two populations', '5 min'],
        ['2', 'Paired samples', '10 min'],
        ['3', 'Two independent means', '15 min'],
        ['4', 'Two proportions', '5 min'],
        ['5', 'Two variances (F-test)', '5 min'],
        ['6', 'Tasks 1–6, by hand, with the tables and in Excel (Tasks 7–10 if you have time left)', '50 min']],
 'T2': [['Type of test', 'What we compare', 'Example', 'Test statistic'],
        ['Means, dependent (paired) samples', 'the mean difference of pairs', 'heart rate before vs. after a program', 't (paired t-test)'],
        ['Means, independent samples', 'μ_{X} vs. μ_{Y}', 'height of men vs. women', 'z (σ known), pooled t or Welch t'],
        ['Proportions', 'π_{X} vs. π_{Y}', 'support in the city vs. in rural areas', 'z'],
        ['Variances', 'σ_{X}² vs. σ_{Y}²', 'grades in morning vs. evening classes', 'F']],
}
_W = {'T1': ([50, 340, 78], (0, 2)), 'T2': ([118, 110, 130, 110], ())}
TABLES = {k: {'rows': v, 'widths': _W[k][0], 'center': _W[k][1]} for k, v in TABLES.items()}
TABLES['T2']['boldcol0'] = True
FIGURES = {'F1': ('fig1_which_test.gif', 468, 211)}
