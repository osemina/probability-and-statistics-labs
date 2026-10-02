import random
import statistics

random.seed(14)
population = [round(random.gauss(9.97, 0.04), 4) for _ in range(2440)]

for n in (5, 50, 500):
    means = [statistics.mean(random.sample(population, n)) for _ in range(1000)]
    print("n =", n, " smallest:", round(min(means), 4),
          " largest:", round(max(means), 4),
          " st. dev.:", round(statistics.stdev(means), 4))
