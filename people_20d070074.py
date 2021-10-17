## Class for people defining various parameters such as acads, extracurriculars, tech, cult etc
## Various member functions are defined indicating the effect of a particular activity

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

    def study(self):
        self.academics += 0.5
        self.fitness -= 0.1

    def hobby(self):
        self.extracur += 0.5
        self.mental_health += 0.7

    def relax(self):
        self.mental_health += 0.7
        self.fitness -= 0.1

    def exercise(self):
        self.fitness += 1
        self.mental_health += 0.5

class coder(people):
    def __init__(self):
        super().__init__(self)
        self.extracur = 15
        self.technical = 20
        self.cult = 10
        self.fitness = 70

    def coding(self):
        self.fitness -= 0.1
        self.technical += 0.1

class dancer(people):
    def __init__(self):
        super().__init__(self)
        self.extracur = 20
        self.technical = 10
        self.cult = 20
        self.fitness = 80

    def dancing(self):
        self.fitness += 0.1
        self.cult += 0.1
        self.laziness -= 0.05