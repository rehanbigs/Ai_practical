import random
population_size=50
fitnessarr=[]
def generatestates():
    stateboard=[]
    for i in range(0,8):
        stateboard.append(random.randint(0,8))
    return stateboard

def fitness(arr):
    fitnessscore=0;
    for i in range(0,8):
        for j in range(i,8):
            if(arr[i]!=arr[j] and j-i != abs(arr[j]-arr[i])):
                fitnessscore=fitnessscore+1
    return fitnessscore

def crossover(arr1,arr2):
    crossoverpoint=3
    newarr1=arr1[:crossoverpoint]+arr2[crossoverpoint:]
    newarr2=arr2[:crossoverpoint]+arr1[crossoverpoint:]
    return newarr1,newarr2

def mutation(arr):
    arr[random.randint(0,7)]=arr[random.randint(0,7)]
    return arr
generation=0;
maxgenerations=200
mutation_rate=0.9
population=[]
for i in range(0,population_size):
    population.append(generatestates())
    
    fitnessarr.append([i,fitness(population[i])])

fitnessarr=sorted(fitnessarr,key=lambda x:x[1],reverse=True)
while(generation<maxgenerations):
  

  
  for i in range(0,population_size//10,2):
    parent1index=fitnessarr[i][0]
    parent2index=fitnessarr[i+1][0]
    offspring1,offspring2=crossover(population[parent1index],population[parent2index])
    if(random.random()<mutation_rate):
        offspring1=mutation(offspring1)
        offspring2=mutation(offspring2)
    population[fitnessarr[population_size-1][0]]=offspring1
    population[fitnessarr[population_size-2][0]]=offspring2
    fitnessarr[fitnessarr[population_size-1][0]][1]=fitness(offspring1)
    fitnessarr[fitnessarr[population_size-2][0]][1]=fitness(offspring2)
  fitnessarr=sorted(fitnessarr,key=lambda x:x[1],reverse=True)
  
  print (fitnessarr)
  generation=generation+1
  print(generation)
  print(fitnessarr[0][1])





                

