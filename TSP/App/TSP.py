print("Starting the TSP optimization program...\n\n")

import numpy as np
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
import os

'''
### Generating n random cities and distances between them
n = 10
dist = np.array([random.sample(range(n**2), n**2)])
dist = dist.reshape(n, n)

for i in range(n):
    dist[i][i] = 0
   
for i in range(n):
    for j in range(n):
        if j<i:
            dist[i][j] = dist[j][i]

print("Printing the distance matrix:\n")
print(dist)

### Declaring cities indexed from 0 to n-1
cities = [ i for i in range(n) ]

### POPULATION_SIZE is the number of random solutions samples we
### want our solution to start with.
POPULATION_SIZE = 300
'''

class Individual():
	
	def __init__(self, chromosome, dist):
		self.chromosome = chromosome
		self.path_length = self.cal_path_length(dist)
		self.fitness = self.cal_fitness()

	@classmethod
	def create_gnome(self, cities):
		gnome = []
		temp = [ i for i in cities ]
		for i in cities:
			x = random.choice(temp)
			gnome.append(x)
			temp.remove(x)
		return(gnome)

	
	def mate(self, par2, n, dist):
		#Replace the hard-coded values here with something generic
		x_part = 3
		y_part = 6
		t1 = self.chromosome[x_part:y_part]
		t2 = par2.chromosome[x_part:y_part]
		child1 = []
		
		for i, j in zip(self.chromosome[0:x_part], par2.chromosome[0:x_part]):
			if i not in t2:
				child1.append(i)
			else:
				temp1 = random.choice(t1)
				while (temp1 in t2) or (temp1 in child1):
					temp1 = random.choice(t1)
				child1.append(temp1)

		child1 = child1 + t2

		for i, j in zip(self.chromosome[y_part:n], par2.chromosome[y_part:n]):
			if (i not in t2):
				child1.append(i)
			else:
				temp1 = random.choice(t1)
				while temp1 in t2 or temp1 in child1:
					temp1 = random.choice(t1)
				child1.append(temp1)
		return (Individual(child1, dist))

	def mutation(self, cities):
		prob = random.random()
		mutation_rate = 0.4
		if prob < mutation_rate:
			x = random.choice(cities)
			y = random.choice(cities)
			temp = self.chromosome[x]
			self.chromosome[x] = self.chromosome[y]
			self.chromosome[y] = temp

	def cal_fitness(self):
		return (self.path_length)**2

	def cal_path_length(self, dist):
		path = 0
		length = len(self.chromosome)
		for i in range(length-1):
			path = path + dist[self.chromosome[i], self.chromosome[i+1]]
		
		path = path + dist[self.chromosome[length-1], self.chromosome[0]]

		return path


	@classmethod
	def selection(self, population):
		while True:
			max_fitness = 10**12
			par = random.choice(population)
			prob = random.randint(0, max_fitness)

			if( prob > par.fitness ):
				return par



def main(n, cities, POPULATION_SIZE, dist):
		'''
		global POPULATION_SIZE
		global cities
		'''
		generation = 1
		found = False

		population = [ Individual(Individual.create_gnome(cities), dist) for _ in range(POPULATION_SIZE)]
	
		while not found:
				population = sorted(population, key = lambda x : x.fitness)

				if population[0].path_length <= 200 or generation == 100:
						found = True
						break

				new_generation = []
				s = int((10*POPULATION_SIZE)/100)
				new_generation.extend(population[:s])

				s = int((90*POPULATION_SIZE)/100)
				for _ in range(s):
						par1, par2 = Individual.selection(population), Individual.selection(population)
						child = par1.mate(par2, n, dist)
						child.mutation(cities)
						new_generation.append(child)

				population = new_generation

				#print("Generation: {}\tPath: {}\tPath_Length: {}".format(generation, population[0].chromosome, population[0].path_length))
				generation +=1
				
		print("\n\n\nResults : \n")

		print("Generation: {}\tPath: {}\tPath_length: {}".format(generation, population[0].chromosome, population[0].path_length))

		generation +=1
		
		results = {"path":population[0].chromosome, "generation":generation, "path_length": population[0].path_length}
		
		return results
		
def run(n):
		dist = np.array([random.sample(range(n**2), n**2)])
		dist = dist.reshape(n, n)

		for i in range(n):
				dist[i][i] = 0
			 
		for i in range(n):
				for j in range(n):
				    if j<i:
				        dist[i][j] = dist[j][i]

		print("Printing the distance matrix:\n")
		print(dist)

		### Declaring cities indexed from 0 to n-1
		cities = [ i for i in range(n) ]

		### POPULATION_SIZE is the number of random solutions samples we
		### want our solution to start with.
		POPULATION_SIZE = 300


		average_time = []
		s = time.clock()
		results = main(n, cities, POPULATION_SIZE, dist)
		average_time.append(time.clock()-s)
		
		G = nx.Graph()
		for i in range(n):
				for j in range(i+1, n):
						G.add_edge(i, j)
						G[i][j]['weight'] = dist[i][j]
						
						
		
		nx.draw(G, with_labels=True, font_weight='bold', font_size='large', font_color="yellow", node_color="blue")
		plt.savefig("static/graph.jpg")
		plt.clf()
		
		
		print("Time taken: {}".format(round(sum(average_time)/len(average_time), 3)))
		
		results["time_taken"] = round(sum(average_time)/len(average_time), 3)
		
		return results
		


'''average_time = []

if __name__ == "__main__":
		s = time.clock()
		main()
		average_time.append(time.clock()-s)
		print(time.clock()-s)

		print("Time taken: ",sum(average_time)/len(average_time))
'''








































