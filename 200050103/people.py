## Class for people defining various parameters such as acads, extracurriculars, tech, cult etc
## Various member functions are defined indicating the effect of a particular activity
import random
import math
types_of_people = 2 #change this variable with more number of people
class people():
    def __init__(self):
        self.academics = 20
        self.extracur = 15
        self.technical = 15
        self.cult = 15
        self.fitness = 75
        self.mental_health = 75
        self.happiness = 80
        self.probs = [0.6, 0.2, 0.2]
        self.laziness = 0.5

        #max and min:essentially, ranges for the attribute values
        self.technical_max = 100
        self.fitness_min = 0
        self.fitness_max = 200
        self.laziness_max = 3
        self.academics_max = 100
        self.academics_min = 0

    def adjust(self):
        if self.technical>self.technical_max:
            self.technical = self.technical_max
        if self.fitness < self.fitness_min:
            self.fitness = self.fitness_min
        if self.fitness > self.fitness_max:
            self.fitness = self.fitness_max
        if self.laziness > self.laziness_max:
            self.laziness = self.laziness_max
        if self.academics < self.academics_min:
            self.academics = self.academics_min
        if self.academics > self.academics_max:
            self.academics = self.academics_max

    def choose(self,min,max,parameter):           #selects value increment or decrement as per tanh function's slope
        #parameter = (max-min)tanh(x)+min
        dx = 0.5
        return (max-min)*(1-math.tanh(parameter))*dx

    def study(self):
        self.academics += self.choose(0,self.academics_max,self.academics)
        self.fitness -= self.choose(self.fitness_min,self.fitness_max,self.fitness)
        self.adjust()

    def hobby(self):
        self.extracur += 0.5
        self.mental_health += 0.7
        self.adjust()

    def relax(self):
        self.mental_health += 0.7
        self.fitness -= self.choose(self.fitness_min,self.fitness_max,self.fitness)
        self.adjust()

    def exercise(self):
        self.fitness -= self.choose(self.fitness_min,self.fitness_max,self.fitness)
        self.mental_health += 0.5
        self.adjust()

class coder(people):
    def __init__(self):
        super().__init__()
        self.academics += 5
        self.extracur += 2
        self.technical += 15
        self.cult -= 5
        self.fitness -= 20
        self.mental_health -= 5
        self.happiness += 5
        self.laziness += 1  # ;)
        self.probs = [0.5, 0.1, 0.2, 0.05, 0.1, 0.05]
    
    def coding_practice(self):
        self.extracur += 0.5
        self.fitness -= self.choose(self.fitness_min,self.fitness_max,self.fitness)
        self.adjust()
    
    def comp_coding(self):
        self.extracur += 0.5
        self.fitness -= 0.5

        success = (random.randint(0,10000) <= (self.technical*100))  #success on  based on technical skill
        if success:
            self.happiness += 1
            self.mental_health += 0.25
        else:
            self.happiness -= 1
            self.mental_health -= 1.25
            self.laziness += 0.05
        self.adjust()
    
    def contributive_coding(self):
        self.extracur += 0.5
        self.technical += self.choose(0,self.technical_max,self.technical)
        self.fitness -= self.choose(self.fitness_min,self.fitness_max,self.fitness)

        pr_accept = (random.randint(0,10000) <= ((self.technical+self.extracur)*100))  #success on  based on technical skill and extracur
        if pr_accept:
            self.happiness += 1.25
            self.mental_health += 0.25
        else:
            self.happiness -= 1
            self.mental_health -= 1.25
        self.adjust()
