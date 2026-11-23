"""Lab 8 Excel workbooks (Students + Solutions), same layout as Labs 6 and 7 (excel_builder.py, steps.py).
The formula typed into each yellow cell is given once (TYPED); its value is evaluated here with scipy."""
import os, re, sys, types, math
from scipy import stats as S
import xl_images as XI

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'excel')
os.makedirs(OUT, exist_ok=True)
NAME = 'Lab 8 – Two Population Hypothesis Test'

D = [6, 1, 7, 6, -1, 8, 5, 5]   # Task 1 differences d = y − x


def xl_eval(f):
    """Evaluate the simple Excel formulas used here (numbers, + − * / ^, statistical functions) with scipy."""
    e = f.lstrip('=')
    e = e.replace('^', '**').replace('TRUE', 'True')
    e = re.sub(r'AVERAGE\([^)]*\)', 'AVG', e)
    e = re.sub(r'STDEV\.S\([^)]*\)', 'SD', e)
    env = dict(AVG=sum(D) / len(D), SD=(sum((d - sum(D) / len(D)) ** 2 for d in D) / (len(D) - 1)) ** 0.5,
               SQRT=math.sqrt, ABS=abs,
               NORM_S_INV=S.norm.ppf, NORM_S_DIST=lambda x, c: S.norm.cdf(x),
               T_INV=lambda p, df: S.t.ppf(p, int(df)), T_INV_2T=lambda a, df: S.t.ppf(1 - a / 2, int(df)),
               T_DIST_RT=lambda x, df: S.t.sf(x, int(df)), T_DIST_2T=lambda x, df: 2 * S.t.sf(abs(x), int(df)),
               T_DIST=lambda x, df, c: S.t.cdf(x, int(df)),
               F_INV_RT=lambda a, d1, d2: S.f.isf(a, d1, d2), F_INV=lambda p, d1, d2: S.f.ppf(p, d1, d2),
               F_DIST_RT=lambda x, d1, d2: S.f.sf(x, d1, d2), F_DIST=lambda x, d1, d2, c: S.f.cdf(x, d1, d2))
    for fn in ('NORM.S.INV', 'NORM.S.DIST', 'T.INV.2T', 'T.DIST.RT', 'T.DIST.2T', 'T.INV', 'T.DIST', 'F.INV.RT', 'F.INV', 'F.DIST.RT', 'F.DIST'):
        e = e.replace(fn + '(', fn.replace('.', '_') + '(')
    return float(eval(e, {}, env))


def task(k, title, focus, text, params, answers, data=None):
    blocks = [('params', params, None)]
    if data:
        blocks.append(data)
    blocks.append(('answers', [(a[0], a[1], None, xl_eval(a[2]), a[3]) for a in answers], None))
    TYPED[k] = {a[0]: a[2] for a in answers}
    return dict(sheet=f'Task {k}', title=title, fig=k, focus=focus, task=text, blocks=blocks)


TYPED = {}
T = [
 task(1, 'Task 1. Does Gaming Before Bed Keep You Awake?', 'paired t-test  ·  differences d = y − x  ·  df = n − 1  ·  AVERAGE  ·  STDEV.S  ·  T.INV  ·  T.DIST.RT',
      "A group of 8 university students wanted to find out whether playing video games just before bedtime affects their sleep. Each student tracked how many minutes they stayed awake in bed before falling asleep "
      "on two different nights: one night they did not play any games before sleep, and another night they played video games just before going to bed. The students believe that gaming keeps them awake longer. "
      "Test this claim at α = 0.05 (data below).\n\n"
      "a) Why are these samples dependent? Write H₀ and H₁. Which type of test is this?\nb) Calculate the differences d = y − x, the mean difference d̄ and the standard deviation sd.\n"
      "c) Calculate the t statistic, find the critical value and the p-value, make a decision and write the conclusion in words.",
      [('n', 'n (pairs of measurements)', 8, '0'), ('a', 'α', 0.05, '0.00')],
      [('dbar', 'mean difference d̄', '=AVERAGE({d})', '0.000'), ('sd', 'standard deviation of d, sd', '=STDEV.S({d})', '0.000'),
       ('df', 'degrees of freedom df = n − 1', '=8-1', '0'), ('tc', 'critical value tα, df', '=T.INV(0.95,7)', '0.000'),
       ('se', 'standard error sd/√n', '=3.068/SQRT(8)', '0.0000'), ('t', 'test statistic t', '=4.625/(3.068/SQRT(8))', '0.000'),
       ('p', 'p-value (right-tailed)', '=T.DIST.RT(4.264,7)', '0.0000')],
      data=('data', ['Student', 'No gaming x', 'With gaming y', 'd = y − x'],
            [[i + 1, x, y, y - x] for i, (x, y) in enumerate(zip([12, 8, 15, 5, 10, 20, 7, 9], [18, 9, 22, 11, 9, 28, 12, 14]))],
            ['0', '0', '0', '0'], ['s', 'x', 'y', 'd'])),
 task(2, 'Task 2. Do Students in the Front Rows Get Better Grades?', 'z-test for two means (σ known)  ·  right-tailed  ·  NORM.S.INV  ·  NORM.S.DIST',
      "A statistics professor has noticed that students who always sit in the front rows seem to do better on exams. From many years of exam records, the population standard deviation of exam scores is known: "
      "σ = 12 points for both groups. This semester, the professor compares the final exam scores of 36 students who always sit in the front rows (mean 74.5 points) with 42 students who always sit at the back "
      "(mean 68.9 points). At α = 0.05, do front-row students score higher on average?\n\n"
      "a) Write H₀ and H₁. Which type of test is this, and why do we use z?\nb) Calculate the standard error and the z statistic.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words. Does this prove that sitting in the front rows causes better grades?",
      [('sx', 'σX = σY (known, points)', 12, '0'), ('nx', 'nX (front rows)', 36, '0'), ('mx', 'x̄ (front rows)', 74.5, '0.0'),
       ('ny', 'nY (back rows)', 42, '0'), ('my', 'ȳ (back rows)', 68.9, '0.0'), ('a', 'α', 0.05, '0.00')],
      [('zc', 'critical value zα', '=NORM.S.INV(0.95)', '0.000'), ('se', 'standard error √(σX²/nX + σY²/nY)', '=SQRT(12^2/36+12^2/42)', '0.0000'),
       ('z', 'test statistic z', '=(74.5-68.9)/SQRT(12^2/36+12^2/42)', '0.000'), ('p', 'p-value (right-tailed)', '=1-NORM.S.DIST(2.055,TRUE)', '0.0000')]),
 task(3, 'Task 3. Who Drinks More Coffee: Engineers or Economists?', 'pooled t-test  ·  sp²  ·  df = nX + nY − 2  ·  T.INV.2T  ·  T.DIST.2T',
      "There is a popular belief on campus that engineering students “run on coffee”. A student club asks students how many cups of coffee they drink per week. A random sample of 20 engineering students "
      "has a mean of 9.4 cups (s = 3.2), and a random sample of 24 economics students has a mean of 7.1 cups (s = 2.9). Assume that both populations are approximately normal with equal variances. "
      "At α = 0.05, is there a difference in the average weekly coffee consumption of the two groups?\n\n"
      "a) Write H₀ and H₁. Which type of test is this? Why is it reasonable to assume equal variances here?\nb) Calculate the pooled variance sp², the t statistic and the degrees of freedom.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words.",
      [('nx', 'nX (engineering)', 20, '0'), ('mx', 'x̄ (engineering)', 9.4, '0.0'), ('sx', 'sX', 3.2, '0.0'),
       ('ny', 'nY (economics)', 24, '0'), ('my', 'ȳ (economics)', 7.1, '0.0'), ('sy', 'sY', 2.9, '0.0'), ('a', 'α', 0.05, '0.00')],
      [('sp2', 'pooled variance sp²', '=(19*3.2^2+23*2.9^2)/42', '0.000'), ('df', 'degrees of freedom nX + nY − 2', '=20+24-2', '0'),
       ('tc', 'critical value tα/2, df', '=T.INV.2T(0.05,42)', '0.000'), ('se', 'standard error √(sp²/nX + sp²/nY)', '=SQRT(9.238/20+9.238/24)', '0.0000'),
       ('t', 'test statistic t', '=(9.4-7.1)/SQRT(9.238/20+9.238/24)', '0.000'), ('p', 'p-value (two-tailed)', '=T.DIST.2T(2.499,42)', '0.0000')]),
 task(4, 'Task 4. E-scooter or Tram: Which Gets You to Campus Faster?', 'Welch’s t-test  ·  unequal variances  ·  degrees of freedom ν  ·  T.INV  ·  T.DIST',
      "A group of students who live in the same part of the city cannot agree on the fastest way to get to campus. For a month, they recorded their door-to-door travel times: 15 trips by e-scooter "
      "(mean 38.5 min, s = 6.2 min) and 25 trips by tram (mean 52.0 min, s = 15.4 min). The tram times vary much more because of traffic jams and waiting at the stops, so the population variances are unknown "
      "and clearly different. At α = 0.05, is the e-scooter faster on average?\n\n"
      "a) Write H₀ and H₁. Which type of test is this? Why do we use Welch’s t-test and not the pooled t-test?\nb) Calculate the t statistic and the degrees of freedom ν with the Welch–Satterthwaite formula.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words.",
      [('nx', 'nX (e-scooter trips)', 15, '0'), ('mx', 'x̄ (e-scooter, min)', 38.5, '0.0'), ('sx', 'sX (min)', 6.2, '0.0'),
       ('ny', 'nY (tram trips)', 25, '0'), ('my', 'ȳ (tram, min)', 52.0, '0.0'), ('sy', 'sY (min)', 15.4, '0.0'), ('a', 'α', 0.05, '0.00')],
      [('ratio', 'variance ratio sY² / sX²', '=15.4^2/6.2^2', '0.00'), ('v1', 'sX² / nX', '=6.2^2/15', '0.000'), ('v2', 'sY² / nY', '=15.4^2/25', '0.000'),
       ('se', 'standard error √(sX²/nX + sY²/nY)', '=SQRT(6.2^2/15+15.4^2/25)', '0.0000'), ('t', 'test statistic t', '=(38.5-52)/SQRT(6.2^2/15+15.4^2/25)', '0.000'),
       ('nu', 'Welch degrees of freedom ν', '=(2.563+9.486)^2/(2.563^2/14+9.486^2/24)', '0.00'),
       ('tc', 'critical value −tα, 34', '=T.INV(0.05,34)', '0.000'), ('p', 'p-value (left-tailed)', '=T.DIST(-3.889,34,TRUE)', '0.0000')]),
 task(5, 'Task 5. Do Students Fall for Phishing More Often Than Staff?', 'z-test for two proportions  ·  pooled proportion p₀  ·  NORM.S.INV  ·  NORM.S.DIST',
      "As part of a cybersecurity awareness week, the university IT department sends a fake phishing email (“Your account will be blocked – click here to confirm your password”) to a random sample of students "
      "and staff. Nobody’s password is collected: the IT department only records who clicked the link. 46 of 200 students and 27 of 210 staff members clicked. At α = 0.05, do students click the phishing link "
      "more often than staff?\n\n"
      "a) Calculate the two sample proportions and check that both samples are large enough. Write H₀ and H₁. Which type of test is this?\nb) Calculate the pooled proportion p₀ and the z statistic.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words. What would you recommend to the IT department?",
      [('nx', 'nX (students)', 200, '0'), ('xx', 'xX (students who clicked)', 46, '0'), ('ny', 'nY (staff)', 210, '0'),
       ('xy', 'xY (staff who clicked)', 27, '0'), ('a', 'α', 0.05, '0.00')],
      [('p1', 'pX = xX / nX', '=46/200', '0.000'), ('p2', 'pY = xY / nY', '=27/210', '0.0000'), ('zc', 'critical value zα', '=NORM.S.INV(0.95)', '0.000'),
       ('p0', 'pooled proportion p₀', '=(46+27)/(200+210)', '0.0000'), ('se', 'standard error √(p₀(1 − p₀)(1/nX + 1/nY))', '=SQRT(0.178*(1-0.178)*(1/200+1/210))', '0.0000'),
       ('z', 'test statistic z', '=(0.23-27/210)/SQRT(0.178*(1-0.178)*(1/200+1/210))', '0.000'), ('p', 'p-value (right-tailed)', '=1-NORM.S.DIST(2.68,TRUE)', '0.0000')]),
 task(6, 'Task 6. iPhone vs Android: Whose Screen Time Is More Unpredictable?', 'F-test for two variances  ·  right-tailed  ·  F.INV.RT  ·  F.DIST.RT',
      "You are part of a student team building “Unplug”, a digital wellbeing app that sends smart reminders when someone has been on their phone for too long. If one group of users has very unpredictable "
      "screen time, fixed daily limits will not work for them. You suspect that iPhone users have more variable screen time than Android users. From 14 days of screen-time reports, the sample variance is "
      "2.25 hours² for 25 iPhone users and 1.20 hours² for 21 Android users. Test your suspicion at α = 0.05.\n\n"
      "a) Write H₀ and H₁. Which type of test is this?\nb) Calculate the F statistic and the degrees of freedom v₁ and v₂.\n"
      "c) Find the critical value and the p-value, and make a decision. What should the UX designer do: one rule for everyone, or separate settings for iPhone users?",
      [('nx', 'nX (iPhone users)', 25, '0'), ('vx', 'sX² (hours²)', 2.25, '0.00'), ('ny', 'nY (Android users)', 21, '0'), ('vy', 'sY² (hours²)', 1.20, '0.00'), ('a', 'α', 0.05, '0.00')],
      [('v1', 'v₁ = nX − 1', '=25-1', '0'), ('v2', 'v₂ = nY − 1', '=21-1', '0'), ('fc', 'critical value F(v₁, v₂, α)', '=F.INV.RT(0.05,24,20)', '0.000'),
       ('F', 'test statistic F = sX² / sY²', '=2.25/1.2', '0.000'), ('p', 'p-value (right-tailed)', '=F.DIST.RT(1.875,24,20)', '0.0000')]),
 task(7, 'Task 7. Is AI a Fairer Grader Than Humans? (Extra Practice)', 'F-test for two variances  ·  left-tailed  ·  F.INV  ·  F.DIST',
      "A professor wants to find out whether an AI tool could help with grading. 25 student essays are graded twice: once by the AI tool and once by a team of human teaching assistants. "
      "The variance of the AI scores is 6.5 points² and the variance of the human scores is 14.0 points². The professor wants to know whether the AI scores are more consistent (have a smaller variance). "
      "Assume normal scores and use α = 0.05.\n\n"
      "a) Write H₀ and H₁. Which type of test is this?\nb) Calculate the F statistic and the degrees of freedom v₁ and v₂.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words. If the AI scores are more consistent, does that also mean that they are more correct?",
      [('nx', 'nX (essays, AI)', 25, '0'), ('vx', 'sX² (AI, points²)', 6.5, '0.0'), ('ny', 'nY (essays, humans)', 25, '0'), ('vy', 'sY² (humans, points²)', 14.0, '0.0'), ('a', 'α', 0.05, '0.00')],
      [('v1', 'v₁ = nX − 1', '=25-1', '0'), ('v2', 'v₂ = nY − 1', '=25-1', '0'), ('fc', 'lower critical value F(v₁, v₂, 1 − α)', '=F.INV(0.05,24,24)', '0.000'),
       ('F', 'test statistic F = sX² / sY²', '=6.5/14', '0.000'), ('p', 'p-value (left-tailed)', '=F.DIST(0.464,24,24,TRUE)', '0.0000')]),
 task(8, 'Task 8. Phone A or Phone B: Which Battery Really Lasts Longer? (Extra Practice)', 'variance check  ·  pooled t-test  ·  two-tailed  ·  T.INV.2T  ·  T.DIST.2T',
      "Two popular phone models in the same price range both advertise an “all-day battery”. A tech YouTuber runs the same video-streaming test on 25 units of each phone: Phone A lasts 412 minutes on average "
      "(s = 48 min) and Phone B lasts 438 minutes on average (s = 55 min). Battery life is approximately normal and the population variances are unknown. At α = 0.05, is there a difference in the average battery life?\n\n"
      "a) Write H₀ and H₁. Which type of test is this? Compare the two sample variances: should you use the pooled t-test or Welch’s t-test?\nb) Calculate the pooled variance sp², the t statistic and the degrees of freedom.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words. Can the YouTuber say that one phone has a better battery?",
      [('nx', 'nX (Phone A)', 25, '0'), ('mx', 'x̄ (Phone A, min)', 412, '0'), ('sx', 'sX (min)', 48, '0'),
       ('ny', 'nY (Phone B)', 25, '0'), ('my', 'ȳ (Phone B, min)', 438, '0'), ('sy', 'sY (min)', 55, '0'), ('a', 'α', 0.05, '0.00')],
      [('ratio', 'variance ratio sY² / sX²', '=55^2/48^2', '0.00'), ('sp2', 'pooled variance sp²', '=(24*48^2+24*55^2)/48', '0.0'),
       ('df', 'degrees of freedom nX + nY − 2', '=25+25-2', '0'), ('tc', 'critical value tα/2, df', '=T.INV.2T(0.05,48)', '0.000'),
       ('se', 'standard error √(sp²/nX + sp²/nY)', '=SQRT(2664.5/25+2664.5/25)', '0.000'), ('t', 'test statistic t', '=(412-438)/SQRT(2664.5/25+2664.5/25)', '0.000'),
       ('p', 'p-value (two-tailed)', '=T.DIST.2T(1.781,48)', '0.0000')]),
 task(9, 'Task 9. Your First Car: Is a Hybrid Really Worth It? (Extra Practice)', 'z-test for two means (σ known)  ·  α = 0.01  ·  NORM.S.INV  ·  NORM.S.DIST',
      "You like a cheaper petrol car, but your parents insist on the hybrid version of the same car. A transport research institute knows the population variances of fuel consumption: 0.49 for hybrids and "
      "1.00 for petrol cars. In a new test, 60 hybrids averaged 4.6 L/100 km and 55 petrol cars averaged 5.0 L/100 km. At α = 0.01, is there a difference in average fuel consumption?\n\n"
      "a) Write H₀ and H₁. Which type of test is this, and why do we use z?\nb) Calculate the standard error and the z statistic.\n"
      "c) Find the critical value for α = 0.01 and the p-value, make a decision and write the conclusion in words. Would your decision change at α = 0.05? If you drive 15,000 km per year and fuel costs "
      "1.60 € per litre, how much would the hybrid save you per year? Who wins the argument?",
      [('vx', 'σX² (hybrid, known)', 0.49, '0.00'), ('nx', 'nX (hybrids)', 60, '0'), ('mx', 'x̄ (hybrid, L/100 km)', 4.6, '0.0'),
       ('vy', 'σY² (petrol, known)', 1.00, '0.00'), ('ny', 'nY (petrol cars)', 55, '0'), ('my', 'ȳ (petrol, L/100 km)', 5.0, '0.0'), ('a', 'α', 0.01, '0.00')],
      [('zc', 'critical value zα/2 (α = 0.01)', '=NORM.S.INV(0.995)', '0.000'), ('se', 'standard error √(σX²/nX + σY²/nY)', '=SQRT(0.49/60+1/55)', '0.0000'),
       ('z', 'test statistic z', '=(4.6-5)/SQRT(0.49/60+1/55)', '0.000'), ('p', 'p-value (two-tailed)', '=2*NORM.S.DIST(-2.464,TRUE)', '0.0000'),
       ('save', 'yearly saving with the hybrid (€)', '=0.4/100*15000*1.6', '0')]),
 task(10, 'Task 10. Flu Season on Campus: Does the Flu Shot Really Work? (Extra Practice)', 'z-test for two proportions  ·  pooled proportion p₀  ·  NORM.S.INV  ·  NORM.S.DIST',
      "It is December and half of your class is coughing. The university health centre offered free flu shots in October, and now it wants to know whether they were worth it. At the end of the flu season, "
      "96 of 480 unvaccinated students and 45 of 500 vaccinated students got the flu. At α = 0.05, are unvaccinated students more likely to get the flu than vaccinated students?\n\n"
      "a) Calculate the two sample proportions and check that both samples are large enough. Write H₀ and H₁. Which type of test is this?\nb) Calculate the pooled proportion p₀ and the z statistic.\n"
      "c) Find the critical value and the p-value, make a decision and write the conclusion in words. How many times higher is the flu rate among unvaccinated students?",
      [('nx', 'nX (unvaccinated)', 480, '0'), ('xx', 'xX (got the flu)', 96, '0'), ('ny', 'nY (vaccinated)', 500, '0'), ('xy', 'xY (got the flu)', 45, '0'), ('a', 'α', 0.05, '0.00')],
      [('p1', 'pX = xX / nX', '=96/480', '0.000'), ('p2', 'pY = xY / nY', '=45/500', '0.000'), ('zc', 'critical value zα', '=NORM.S.INV(0.95)', '0.000'),
       ('p0', 'pooled proportion p₀', '=(96+45)/(480+500)', '0.0000'), ('se', 'standard error √(p₀(1 − p₀)(1/nX + 1/nY))', '=SQRT(0.1439*(1-0.1439)*(1/480+1/500))', '0.0000'),
       ('z', 'test statistic z', '=(0.2-0.09)/SQRT(0.1439*(1-0.1439)*(1/480+1/500))', '0.000'), ('p', 'p-value (right-tailed)', '=1-NORM.S.DIST(4.905,TRUE)', '0.00E+00'),
       ('ratio', 'how many times higher: pX / pY', '=0.2/0.09', '0.00')]),
]

FIG = {
    1: XI.test_curve('t1', 4.264, [1.8946], 'right', 'paired t-test, α = 0.05: t = 4.26', df=7, pval=0.0019, label='t'),
    2: XI.test_curve('t2', 2.055, [1.6449], 'right', 'z-test for two means, α = 0.05: z = 2.05', pval=0.0200),
    3: XI.test_curve('t3', 2.499, [2.0181], 'two', 'pooled t-test, α = 0.05: t = 2.50', df=42, pval=0.0164, label='t'),
    4: XI.test_curve('t4', -3.889, [-1.6909], 'left', 'Welch’s t-test, α = 0.05: t = −3.89', df=34, pval=0.0002, label='t'),
    5: XI.test_curve('t5', 2.684, [1.6449], 'right', 'z-test for two proportions, α = 0.05: z = 2.68', pval=0.0036),
    6: XI.f_curve('t6', 1.875, 2.0825, 'right', 'F-test, α = 0.05: F = 1.875', (24, 20), pval=0.0787),
    7: XI.f_curve('t7', 0.4643, 0.5041, 'left', 'F-test (left-tailed), α = 0.05: F = 0.464', (24, 24), pval=0.0330),
    8: XI.test_curve('t8', -1.781, [2.0106], 'two', 'pooled t-test, α = 0.05: t = −1.78', df=48, pval=0.0813, label='t'),
    9: XI.test_curve('t9', -2.464, [2.5758], 'two', 'z-test for two means, α = 0.01: z = −2.46', pval=0.0137),
    10: XI.test_curve('t10', 4.905, [1.6449], 'right', 'z-test for two proportions, α = 0.05: z = 4.90', pval=0.0000005),
}

sys.modules['typed'] = types.SimpleNamespace(TYPED=TYPED)
from excel_builder import build

if __name__ == '__main__':
    for k_, t_ in enumerate(T, 1):
        for a in t_['blocks'][-1][1]:
            print(k_, a[0], round(a[3], 4))
    for s_ in (False, True):
        print(build(s_, T, FIG, NAME, OUT))
