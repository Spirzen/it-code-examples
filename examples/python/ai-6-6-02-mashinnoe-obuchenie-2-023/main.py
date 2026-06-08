
import numpy as np
import random

class GeneticAlgorithm:
    def __init__(self, population_size=100, chromosome_length=20, 
                 mutation_rate=0.01, crossover_rate=0.8, generations=50):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
    
    def create_individual(self):
        return np.random.randint(0, 2, self.chromosome_length)
    
    def create_population(self):
        return [self.create_individual() for _ in range(self.population_size)]
    
    def fitness_function(self, individual):
        target = np.ones(self.chromosome_length)
        return np.sum(individual == target)
    
    def selection(self, population, fitnesses):
        total_fitness = sum(fitnesses)
        probabilities = [f / total_fitness for f in fitnesses]
        selected = random.choices(population, weights=probabilities, k=2)
        return selected[0], selected[1]
    
    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            point = random.randint(1, self.chromosome_length - 1)
            child1 = np.concatenate([parent1[:point], parent2[point:]])
            child2 = np.concatenate([parent2[:point], parent1[point:]])
            return child1, child2
        return parent1.copy(), parent2.copy()
    
    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual
    
    def evolve(self):
        population = self.create_population()
        
        for generation in range(self.generations):
            fitnesses = [self.fitness_function(ind) for ind in population]
            best_fitness = max(fitnesses)
            best_individual = population[fitnesses.index(best_fitness)]
            
            print(f"Поколение {generation}: лучшая приспособленность = {best_fitness}")
            
            if best_fitness == self.chromosome_length:
                print("Найдено оптимальное решение!")
                return best_individual
            
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection(population, fitnesses)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                if len(new_population) < self.population_size:
                    new_population.append(self.mutate(child2))
            
            population = new_population
        
        fitnesses = [self.fitness_function(ind) for ind in population]
        best_individual = population[fitnesses.index(max(fitnesses))]
        return best_individual

# Запуск алгоритма
ga = GeneticAlgorithm(
    population_size=200,
    chromosome_length=30,
    mutation_rate=0.02,
    crossover_rate=0.9,
    generations=100
)
solution = ga.evolve()
print("Полученное решение:", solution)
