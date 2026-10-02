import random
import statistics

random.seed(14)
population = [round(random.gauss(9.97, 0.04), 4) for _ in range(2440)]
mu = statistics.mean(population)
print("Population size N =", len(population))
print("Population mean  mu =", round(mu, 4))

for i in range(1, 6):
    sample = random.sample(population, 50)
    x_bar = statistics.mean(sample)
    print("Sample", i, " x_bar =", round(x_bar, 4))
