from tsp import *


total_fit = 0
final_order = []

# best_ever =2e9+10

# Calculates the fitness for every order
# Fitness = (1/(d+1))
# Also saves the order with best fitness till now
def calc_fitness(population: list,cities,fitness):
    global best_ever
    global min_distance
    global final_order
    best_order = 0  
    for x in population:
        d  =calc_distance(cities,x)
        fitness.append(1/(d+1))
        # min_distance  = min(min_distance,d)
        if(min_distance>d):
            min_distance = d
            best_order = x
    # best_ever = min(min_distance,best_ever)
    print("best order is 1 ")
    print(best_order)
    if(best_ever>min_distance):
        
        best_ever = min_distance
        final_order = best_order
    return

# Mutates the given order

def mutate(order1,mutation_rate =1):

    for i in range(mutation_rate):
     
        ind_a = randint(0,len(order1)-1)
        ind_b = randint(0,len(order1)-1)

        swap(order1,ind_a,ind_b)

# Normalizes the fitness of every order in current population
def Normalize(fitness):
    sum =0 
    for x in fitness:
        sum+=x

    for i in range(len(fitness)):

        fitness[i] = fitness[i]/sum

# return a random index from the fitness list
# The probabilty of an indexed being chosed increases with its fitness value

def pick_one(fitness):

    rt = uniform(0,total_fit)

    j =0 
    while(j<len(fitness)):

        if(rt<=0):
            return j
        
        rt-=fitness[j]
        j+=1
    
    return len(fitness)

# Performs crossover between 2 orders

def crossOver(orderA:list,orderB : list):

    # print(type(orderA))

    na = len(orderA)

    st = randint (0,na-1)
    try:
        en = randint(st+1,na-1)
    except:
        en = na-1
    neworder = orderA[st:en+1]

    for x in orderB:
        if not (x in neworder):
            neworder.append(x)
    return neworder

# Generates new generation ie new population of orders

def new_generation(population,fitness):

    new_population = []
    for i in range(len(population)):
        
        random_fitness_index  =pick_one(fitness)-1
        temp_order  = population[random_fitness_index]
        random_fitness_index  =pick_one(fitness)-1
        temp_order2  = population[random_fitness_index]
        temp_order = crossOver(temp_order,temp_order2)
        mutate(temp_order,3)
        new_population.append([])
        new_population[-1].extend(temp_order)
    return new_population


# calc_fitness()
# Normalize()
# new_generation()
cities = []

# Generating random cities coordinates in a given range
for i in range(num_cities):
    cities.append([randint(0,height),randint(0,width)])
order_c = []
for i in range(num_cities):
    order_c.append(i)



population  = []

for i in range(population_size):
    population.append([])
    population[-1].extend(order_c)
    # population.append(order_c)

for x in population:
    shuffle_1(x,10)

# print(population)

fitness  = []


for i in range(10000):
    fitness = []
    min_distance = 2e9
    calc_fitness(population,cities,fitness)
    for x in fitness:
        total_fit+=x

    Normalize(fitness)
    population = new_generation(population,fitness)

    print("best ever is ",best_ever)

    vec_x = [0]
    vec_y = [0]

    if len(final_order) == 0:
        continue

 

print("Final best order is ")


print(final_order)

# displays the best obtained route

for j in final_order:
    vec_x.append(cities[j][0])
    vec_y.append(cities[j][1])
    # clear_output(wait=True)

# plt.plot(vec_x,vec_y,scatter)
plt.scatter(vec_x,vec_y,color = 'black')
plt.show()
plt.scatter(vec_x,vec_y,color = 'black')
plt.plot(vec_x,vec_y)
plt.title("Optimal Path")
plt.show(block = True)
# plt.pause()

plt.close()