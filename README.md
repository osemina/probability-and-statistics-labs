# IBU 014 Probability and Statistics: lab materials

Illustrations, animations and Python code used in the lab documents for
IBU 014 Probability and Statistics at International Burch University.

## Lab 1: Fundamentals of Statistics

| File | Used in |
|---|---|
| `lab01/images/fig1_population_sample.png` | Figure 1, population, sample and inference |
| `lab01/images/fig2_data_types.png` | Figure 2, types of data |
| `lab01/images/fig3_sampling_methods.png` | Figure 3, probability sampling methods |
| `lab01/images/fig5_bias_variability.gif` | Figure 4, bias and variability (animated) |
| `lab01/images/fig6_random_rectangles.png` | Figure 5, Task 9 random rectangles |
| `lab01/images/fig4_sampling_distribution.gif` | Figure 6, Task 10 sampling simulation (animated) |
| `lab01/code/` | Python programs for Tasks 9, 10 and Optional Task 1 |
| `lab01/source/make_images.py` | Script that generates all figures (matplotlib + Pillow) |

## Lab 1, improved version (FENMS 0021)

| File | Used in |
|---|---|
| `lab01-v2/images/fig1_population_to_inference_hf.gif` | Figure 1, from population to inference (HyperFrames animation, Problem 1) |
| `lab01-v2/images/fig2_types_of_data.png` | Figure 2, types of data |
| `lab01-v2/images/fig3_who_answered_hf.gif` | Figure 3, who answered the survey (HyperFrames animation, Problem 4) |
| `lab01-v2/hyperframes/` | HyperFrames compositions for Figures 1 and 3. Render with `npx hyperframes render`, then convert to GIF with ffmpeg; fonts (Montserrat, Open Sans) go in `assets/` |
| `lab01-v2/source/make_images_v2.py` | Script that generates these figures |

## Lab 1, improved version 2 (FENMS 0021, relatable scenarios)

| File | Used in |
|---|---|
| `lab01-v3/images/fig1_cafe_population_to_inference.gif` | Figure 1, café bottles: population, sample, statistic, inference (HyperFrames) |
| `lab01-v3/images/fig2_types_of_data.png` | Figure 2, types of data |
| `lab01-v3/images/fig3_who_answered.gif` | Figure 3, who answered the social-media survey (HyperFrames) |
| `lab01-v3/images/fig4_process_orders.gif` | Figure 4, delivery orders as a process (HyperFrames) |
| `lab01-v3/hyperframes/` | HyperFrames compositions; fonts (Montserrat, Open Sans) go in `assets/` before rendering |

## Lab 3: Fundamentals of Probability (FENMS 0021)

| File | Used in |
|---|---|
| `lab03/images/fig1_probability_scale.gif` | Figure 1, the probability scale from impossible to certain (HyperFrames) |
| `lab03/images/fig2_die_events.gif` | Figure 2, die roll: events A, B, the joint event and the complement (HyperFrames) |
| `lab03/images/fig3_venn_operations.gif` | Figure 3, union, intersection, complement, mutually exclusive (HyperFrames) |
| `lab03/images/fig4_red_or_king.gif` | Figure 4, addition rule: red card or King, subtract the overlap (HyperFrames) |
| `lab03/images/fig5_playlist_no_repeats.gif` | Figure 5, dependent events: shuffled playlist without repeats (HyperFrames) |
| `lab03/images/fig6_delivery_tree_bayes.gif` | Figure 6, delivery tree: total probability and Bayes' theorem (HyperFrames) |
| `lab03/images/fig7_given_spotify.gif` | Figure 7, conditional probability shrinks the sample space (HyperFrames) |
| `lab03/images/fig8_problem1_venn.png` | Figure 8, Problem 1 Venn diagram (HyperFrames still) |
| `lab03/hyperframes/` | HyperFrames compositions; fonts (Montserrat, Open Sans) go in `assets/` before rendering |
| `lab03/source/build_figs.py` | Script that writes the compositions (`common.py` holds the shared template) |
