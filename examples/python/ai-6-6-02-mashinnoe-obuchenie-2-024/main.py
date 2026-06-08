from deap import base, creator, tools, algorithms

import random
import numpy as np

# Создание типов
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Генерация городов
np.random.seed(42)
cities = np.random.rand(20, 2)

def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(individual):
    total = 0
    for i in range(len(individual) - 1):
        total += distance(cities[individual[i]], cities[individual[i+1]])
    total += distance(cities[individual[-1]], cities[individual[0]])
    return total,

def create_individual():
    return random.sample(range(len(cities)), len(cities))

toolbox = base.Toolbox()
toolbox.register("indices", create_individual)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", total_distance)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Создание популяции и запуск алгоритма
population = toolbox.population(n=300)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)

algorithms.eaSimple(
    population, 
    toolbox, 
    cxpb=0.7, 
    mutpb=0.2, 
    ngen=400,
    stats=stats, 
    halloffame=hof,
    verbose=True
)

print("Лучший маршрут:", hof[0])
print("Длина маршрута:", total_distance(hof[0])[0])
