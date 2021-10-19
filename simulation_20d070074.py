import random as rnd        ## For generating random choices/numbers
import matplotlib.pyplot as plt         ## For plotting the graphs     
import seaborn as sns           ## For data visualization and analysis
import sys
from people_20d070074 import *                #Importing the people module

def on_press(event):
    """
    Close sim on pressing any key
    """
    sys.exit(0)

#Initializing the people 
population = []
for i in range(100):
    population.append(people())
for i in range(10):
    population.append(coder())
for i in range(10):
    population.append(dancer())
    
## Loop runs for each day in a month and each day the activities array is emptied
fig, ax = plt.subplots()

for days in range(30):
    activities = [[]]*120
    for hours in range(24):
        for i in range(120):
            person = population[i]
            if(hours >= rnd.randint(8, 8+person.laziness*4) or hours <= 17): #Depending on how lazy the person is, it decides when the person starts his day

                ## Randomly choosing between study, hobby and relax according to their weights defined earlier

                work = rnd.choices(['s', 'h', 'r'], person.probs)
                if work == ["s"]:
                    activities[i].append("studied")
                    person.study()
                elif work == ["h"]:
                    activities[i].append("hobby")
                    person.hobby()
                else:
                    activities[i].append("relaxed")
                    person.relax()
            elif((hours > 4 and hours <= 7) or (hours < 20 and hours > 17)):
                # For exercising in morning or evening, depends on the laziness of the person
                e = rnd.choices(['e', 'ne'], [1-person.laziness, person.laziness])[0]
                if e == "e":
                    person.exercise()
            if hours == 23 and (activities[i].count("studied")/len(activities[i])) > 0.4:
                #Studying above a certain limit in a day can cause some amount of mental health detrioration
                person.mental_health -= 1
         
            person.academics -= 0.02 #To simulate forgetfullnes, each day you tend to a forget a few things from days back
    
    ## Appending the arrays according to the activities and the choices in a day

    acads = []
    for person in population:
        acads.append(person.academics)
    extracurs = []
    for person in population:
        extracurs.append(person.extracur)

    mental_healths = []
    for person in population:
        mental_healths.append(person.mental_health)

    physical_healths = []
    for person in population:
        physical_healths.append(person.fitness)

    ## Plotting the results

    plt.subplot(4, 1, 1)
    plt.plot(range(120), acads)
    plt.xlabel("Person")
    plt.ylabel("Academic Level")
    plt.subplot(4, 1, 2)
    plt.plot(range(120), extracurs)
    plt.xlabel("Person")
    plt.ylabel("Extracurricular Level")
    plt.subplot(4, 1, 3)
    plt.plot(range(120), mental_healths)
    plt.xlabel("Person")
    plt.ylabel("Mental Health")
    plt.subplot(4, 1, 4)
    plt.plot(range(120), physical_healths)
    plt.xlabel("Person")
    plt.ylabel("Physical Fitness")
    plt.tight_layout()
    fig.canvas.mpl_connect("key_press_event", on_press) #Detect key press
    plt.draw()
    plt.pause(1)
    fig.clf()

## Compile data and draw the final graph at the end of the month

acads = []
for person in population:
    acads.append(person.academics)
extracurs = []
for person in population:
    extracurs.append(person.extracur)

mental_healths = []
for person in population:
    mental_healths.append(person.mental_health)

physical_healths = []
for person in population:
    physical_healths.append(person.fitness)

## Plotting the results


plt.subplot(4, 1, 1)
plt.plot(range(100), acads)
plt.xlabel("Person")
plt.ylabel("Academic Level")
plt.subplot(4, 1, 2)
plt.plot(range(100), extracurs)
plt.xlabel("Person")
plt.ylabel("Extracurricular Level")
plt.subplot(4, 1, 3)
plt.plot(range(100), mental_healths)
plt.xlabel("Person")
plt.ylabel("Mental Health")
plt.subplot(4, 1, 4)
plt.plot(range(100), physical_healths)
plt.xlabel("Person")
plt.ylabel("Physical Fitness")
plt.tight_layout()
fig.canvas.mpl_connect("key_press_event", on_press) #Detect key press
plt.show()