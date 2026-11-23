"""Lab 7 Excel workbooks (Students + Solutions), same layout as Lab 6 (excel_builder.py, steps.py, typed.py)."""
import os
import xl_images as XI
from excel_builder import build

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'excel')
os.makedirs(OUT, exist_ok=True)
NAME = 'Lab 7 – Hypothesis Test of a Single Population'

FIG = {
    1: XI.test_curve('t1', -2.108, [1.96], 'two', 'z-test for μ, α = 0.05: z = −2.11', pval=0.0350),
    2: XI.test_curve('t2', 0.88, [1.2816], 'right', 'z-test for μ, α = 0.10: z = 0.88', pval=0.1894),
    3: XI.test_curve('t3', -2.25, [1.96], 'two', 'z-test for μ, α = 0.05: z = −2.25', pval=0.0244),
    4: XI.test_curve('t4', 1.461, [2.0639], 'two', 't-test for μ, α = 0.05: t = 1.46', df=24, pval=0.157, label='t'),
    5: XI.test_curve('t5', 2.138, [1.6449], 'right', 'z-test for π, α = 0.05: z = 2.14', pval=0.0163),
    6: XI.test_curve('t6', -2.167, [-1.6449], 'left', 'z-test for μ, α = 0.05: z = −2.17', pval=0.0151),
    7: XI.test_curve('t7', 1.303, [2.3263], 'right', 'z-test for π, α = 0.01: z = 1.30', pval=0.0963),
    8: XI.test_curve('t8', 2.222, [1.7109], 'two', 't-test for μ, α = 0.10: t = 2.22', df=24, pval=0.036, label='t'),
}


def task(k, title, focus, text, params, answers):
    return dict(sheet=f'Task {k}', title=title, fig=k, focus=focus, task=text,
                blocks=[('params', params, None), ('answers', [(a[0], a[1], None, a[2], a[3]) for a in answers], None)])


ZM = 'z-test for a mean (σ known)  ·  critical value  ·  p-value  ·  NORM.S.INV  ·  NORM.S.DIST'
TM = 't-test for a mean (σ unknown)  ·  df = n − 1  ·  T.INV.2T  ·  T.DIST.2T'
ZP = 'z-test for a proportion  ·  π₀ in the standard error  ·  NORM.S.INV  ·  NORM.S.DIST'
T = [
 task(1, 'Task 1. Do Students Really Sleep 7 Hours?', ZM,
      "A university mental health advisor claims that students in Sarajevo sleep on average 7 hours per night. A research team wants to test this claim in order to introduce new measures to improve student life. "
      "They randomly select 40 students and ask them how many hours they sleep on average during a night. The sample mean is x̄ = 6.6 hours, and the population standard deviation is known: σ = 1.2 hours. "
      "Using α = 0.05, test the claim that students sleep a different amount than 7 hours per night.\n\n"
      "a) Write H₀ and H₁. Which type of test is this, and why do we use z?\nb) Calculate the test statistic and find the critical value.\nc) Find the p-value, make a decision and write a conclusion in words.",
      [('mu', 'μ₀ (claimed mean, hours)', 7, '0'), ('sg', 'σ (population SD, hours)', 1.2, '0.0'), ('n', 'n (students)', 40, '0'),
       ('xb', 'x̄ (sample mean, hours)', 6.6, '0.0'), ('a', 'α', 0.05, '0.00')],
      [('zc', 'critical value zα/2', 1.95996, '0.000'), ('se', 'standard error σ/√n', 0.18974, '0.0000'),
       ('z', 'test statistic z', -2.10819, '0.000'), ('p', 'p-value (two-tailed)', 0.03501, '0.0000')]),
 task(2, 'Task 2. Have Phone Bills Really Gone Up?', ZM,
      "A phone company manager thinks that customers’ monthly cell phone bills have increased and now average more than $52 per month. The company wants to test this claim. "
      "A random sample of 64 customers gives a sample mean of x̄ = $53.10. Assume that the population standard deviation is known, σ = $10, and use α = 0.10.\n\n"
      "a) Write H₀ and H₁. Which type of test is this?\nb) Calculate the test statistic and find the critical value z₀.₁₀.\nc) Make a decision. Do the data support the manager’s claim that the bills have increased?",
      [('mu', 'μ₀ (claimed mean, $)', 52, '0'), ('sg', 'σ (population SD, $)', 10, '0'), ('n', 'n (customers)', 64, '0'),
       ('xb', 'x̄ (sample mean, $)', 53.1, '0.00'), ('a', 'α', 0.10, '0.00')],
      [('zc', 'critical value zα', 1.28155, '0.000'), ('se', 'standard error σ/√n', 1.25, '0.00'),
       ('z', 'test statistic z', 0.88, '0.00'), ('p', 'p-value (right-tailed)', 0.18943, '0.0000')]),
 task(3, 'Task 3. Do Students Game More or Less?', ZM,
      "A gaming platform reports that its players aged 18–25 play 3 hours per day on average, with a standard deviation of σ = 0.8 hours. A student project team wants to know whether IBU students play a different amount, "
      "so they survey a random sample of 100 students. The sample mean is x̄ = 2.82 hours per day. Test at α = 0.05 whether IBU students play a different amount than the platform’s average.\n\n"
      "a) Write H₀ and H₁ and state the type of test.\nb) Calculate the test statistic and the p-value.\nc) Make a decision and write a conclusion in words.",
      [('mu', 'μ₀ (platform average, hours)', 3, '0'), ('sg', 'σ (population SD, hours)', 0.8, '0.0'), ('n', 'n (students)', 100, '0'),
       ('xb', 'x̄ (sample mean, hours)', 2.82, '0.00'), ('a', 'α', 0.05, '0.00')],
      [('zc', 'critical value zα/2', 1.95996, '0.000'), ('se', 'standard error σ/√n', 0.08, '0.00'),
       ('z', 'test statistic z', -2.25, '0.00'), ('p', 'p-value (two-tailed)', 0.02445, '0.0000')]),
 task(4, 'Task 4. Does the Battery Tool Really Work?', TM,
      "A group of computer science students found a free app that promises to “boost” laptop batteries during long coding sessions. According to the app’s website, a laptop running the app lasts 168 minutes on average while you code. "
      "The students are skeptical, so they write a small script that logs battery life and test the app on 25 different laptops during real programming sessions. They get a sample mean battery life of x̄ = 172.5 minutes "
      "and a sample standard deviation of s = 15.4 minutes. Battery life is approximately normally distributed. At α = 0.05, test whether the true average battery life with the app is different from the 168 minutes claimed on the website.\n\n"
      "a) Write H₀ and H₁. Which type of test is this, and why do we use t instead of z?\nb) Calculate the test statistic and find the critical value.\n"
      "c) Make a decision and write a conclusion in words. Can the students say that the website is wrong?",
      [('mu', 'μ₀ (claimed mean, minutes)', 168, '0'), ('n', 'n (laptops)', 25, '0'), ('xb', 'x̄ (sample mean, minutes)', 172.5, '0.0'),
       ('s', 's (sample SD, minutes)', 15.4, '0.0'), ('a', 'α', 0.05, '0.00')],
      [('df', 'degrees of freedom df = n − 1', 24, '0'), ('tc', 'critical value tα/2, df', 2.06390, '0.000'),
       ('se', 'standard error s/√n', 3.08, '0.00'), ('t', 'test statistic t', 1.46104, '0.000'), ('p', 'p-value (two-tailed)', 0.15697, '0.0000')]),
 task(5, 'Task 5. Do Students Use AI for Their Homework?', ZP,
      "The faculty claims that no more than 30% of students use AI tools (such as ChatGPT) to write their homework. A student newspaper doubts this and runs an anonymous survey of a random sample of 150 students: "
      "57 of them say that they use AI tools to write their homework.\n\n"
      "a) Find the sample proportion p, and check that the sample is large enough to use the normal approximation.\nb) Write H₀ and H₁ and test the faculty’s claim at α = 0.05.\n"
      "c) Find the p-value. What can the student newspaper write in its article?",
      [('pi', 'π₀ (claimed proportion)', 0.30, '0.00'), ('n', 'n (students)', 150, '0'), ('x', 'x (use AI tools)', 57, '0'), ('a', 'α', 0.05, '0.00')],
      [('p', 'sample proportion p = x/n', 0.38, '0.000'), ('c1', 'check n·π₀ (≥ 5)', 45, '0'), ('c2', 'check n·(1 − π₀) (≥ 5)', 105, '0'),
       ('zc', 'critical value zα', 1.64485, '0.000'), ('se', 'standard error σp', 0.037417, '0.0000'),
       ('z', 'test statistic z', 2.13809, '0.000'), ('pv', 'p-value (right-tailed)', 0.01626, '0.0000')]),
 task(6, 'Task 6. Does Your Smartwatch Keep You Moving? (Extra Practice)', ZM,
      "A smartwatch company claims that its users walk at least 8000 steps per day on average. The population standard deviation is known: σ = 1800 steps. "
      "A random sample of 36 students who wear the watch gives x̄ = 7350 steps per day. Use α = 0.05 to test the company’s claim.\n\n"
      "a) Write H₀ and H₁. Which type of test is this?\nb) Calculate the test statistic and the p-value.\nc) Make a decision. Do the data support the company’s claim?",
      [('mu', 'μ₀ (claimed mean, steps)', 8000, '0'), ('sg', 'σ (population SD, steps)', 1800, '0'), ('n', 'n (students)', 36, '0'),
       ('xb', 'x̄ (sample mean, steps)', 7350, '0'), ('a', 'α', 0.05, '0.00')],
      [('zc', 'critical value −zα', -1.64485, '0.000'), ('se', 'standard error σ/√n', 300, '0'),
       ('z', 'test statistic z', -2.16667, '0.000'), ('p', 'p-value (left-tailed)', 0.01513, '0.0000')]),
 task(7, 'Task 7. Are Code Deployments Too Buggy? (Extra Practice)', ZP,
      "An IT company claims that no more than 8% of its code deployments result in critical bugs. In a recent audit of 200 deployments, 21 were found to have critical bugs. "
      "Use α = 0.01 to test whether more than 8% of the deployments have critical bugs.\n\n"
      "a) Find the sample proportion p and check that the sample is large enough.\nb) Write H₀ and H₁, calculate the test statistic and make a decision at α = 0.01.\n"
      "c) Would the decision change at α = 0.10? Explain using the p-value.",
      [('pi', 'π₀ (claimed proportion)', 0.08, '0.00'), ('n', 'n (deployments)', 200, '0'), ('x', 'x (with critical bugs)', 21, '0'), ('a', 'α', 0.01, '0.00')],
      [('p', 'sample proportion p = x/n', 0.105, '0.000'), ('c1', 'check n·π₀ (≥ 5)', 16, '0'), ('c2', 'check n·(1 − π₀) (≥ 5)', 184, '0'),
       ('zc', 'critical value zα (α = 0.01)', 2.32635, '0.000'), ('se', 'standard error σp', 0.019183, '0.0000'),
       ('z', 'test statistic z', 1.30322, '0.000'), ('pv', 'p-value (right-tailed)', 0.09626, '0.0000'),
       ('zc10', 'c) critical value at α = 0.10', 1.28155, '0.000')]),
 task(8, 'Task 8. How Long Is a Hit Song? (Extra Practice)', TM,
      "A music blog claims that today’s hit songs last 3 minutes on average. A student picks a random sample of 25 songs from the Top 50 list of a streaming platform and finds a mean length of x̄ = 3.4 minutes "
      "with a sample standard deviation of s = 0.9 minutes. Song lengths are approximately normally distributed. Using α = 0.10, test whether the average length of hit songs is different from 3 minutes.\n\n"
      "a) Write H₀ and H₁. Why do we use t?\nb) Calculate the test statistic and find the critical value t₀.₀₅, ₂₄.\nc) Make a decision and write a conclusion in words.",
      [('mu', 'μ₀ (claimed mean, minutes)', 3, '0'), ('n', 'n (songs)', 25, '0'), ('xb', 'x̄ (sample mean, minutes)', 3.4, '0.0'),
       ('s', 's (sample SD, minutes)', 0.9, '0.0'), ('a', 'α', 0.10, '0.00')],
      [('df', 'degrees of freedom df = n − 1', 24, '0'), ('tc', 'critical value tα/2, df', 1.71088, '0.000'),
       ('se', 'standard error s/√n', 0.18, '0.00'), ('t', 'test statistic t', 2.22222, '0.000'), ('p', 'p-value (two-tailed)', 0.03595, '0.0000')]),
]

if __name__ == '__main__':
    for s_ in (False, True):
        print(build(s_, T, FIG, NAME, OUT))
