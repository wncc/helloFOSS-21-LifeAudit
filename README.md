# Hello-FOSS-LifeAudit
This project is a part of HELLO-FOSS: Celebration of Open Source by the Web and Coding Club. In this project we will be seeing the application of python in
developing an interesting, statistical simulation of our life in an online semester

### Guidelines
To contribute to this project there are not many prerequisites just that you should have  a basic grasp over Python.You can go through [these resources](https://github.com/wncc/TSS-2021/tree/main/Python%20%26%20its%20Applications/Week-1) if you want to revise or learn Python.  
**NOTE: before sending any pull request, rename your file to include your initials as - filename_RollNum.extension**.

## LifeAudit: Simulation Of Your Life In An Online Semester


Online semeseter has been sucking the joy out of our college life since the past 1-2 years for many of us. We all must have felt depressed, demotivated many times during this period. Overburdened by academics, running behind deadlines, mental and physical fitness going down the drain, we have all struggled to surrvive in this situation. 

This simulation is an attempt to analyze if we managed our time well, set better priorities could we utilize this any better?. Its an interesting way to explore and see what works best for us even in such a situation. 

### Problem Statement

#### The Code

There are 2 files here. One is [people.py](https://github.com/Karrthik-Arya/Hello-FOSS-LifeAudit/blob/main/people.py), this contains the code to describe the people class. This class contains the factors and characteristics describing a person such as his priorities, laziness, academic level, mental health etc. as well as the functions describes activities that the person does such as studying, exercising, relaxing etc.   

The other file is [simulation.py](https://github.com/Karrthik-Arya/Hello-FOSS-LifeAudit/blob/main/simulation.py), this contains the code in which people are instantiatied, they perform various daily activities by calling the appropriate functions etc. Right now the simulation contains 100 people with exactly the same initial characteristics. The simulation runs and it plots some simple graphs from the results. The graphs contain the academic level, physical fitness, extracurricular development and mental health plotted daily for each person. 

#### The Tasks
1. **Diversity**: Right now the model considers all the people have similar interests which is far from true. Add more classes of people for different types of people with different characteristics, different interests(see task-4) like coders, fitness freaks, maggus etc. These can inherit functions and attributes from the people class or can be altogether different classes. You can watch [this](https://www.youtube.com/watch?v=H2SQrZK2nvM&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=6) short video on inheritance if you don't know about it. 


2. **Variation of Factors**: In the python file, change the variation of the factors so that the value remains between 0 and 100. The variation shouldn't just increment or decrement the value by a constant and it should depend on the current level as well. Consider the scenerio for academics for instance, initially you might study a lot but then you reach your saturation point and then the rate would decrease. Don't forget to model this situation! You can use the Gaussian function to model this or even simple if eles commands or whatever function you think would be suitable. 


3. **Breaking the Monotonous Routine**: No one can work monotonically and everyone needs a break from their routine at some point of time. So in this task try adding some features which help you to relax from your packed schedule. For instance, you have worked hard for 3-4 days continuously( that would mean the no. of hours that you study have been above a certain threshold for these few days) and now you want to take a break, relax and do minimal work.

 
4. **Individual Interests**: Each individual has a particular interest or an inclination towards a specific activity. Depending upon the interests, probability to attend a certain event can change drastically. The field of extracurricular activities can also be expanded accordingly. So instead of having the field of extracurricular level you can have fields for different kinds of activities like culturals, sports, tech etc. Also the activity "hobby" will also now change according to your interest. Depending on the interest other factors may get affected as well, like having sports as an hobby will automatically help push your physical fitness.  


5.  **Monthly Events**: A lot of events are conducted by  the Institute Technical, Cultural and the Academic Council each month(unfortunately, online events for the 'COVID Batch'). Depending upon your interests, some of these events can affect the time spent on your daily activities. Major and the minor quizes also play a major role in the time distribution. So mainly there will be 2 types of events quizzes or events of clubs(Choose any 3 clubs you like). Now for quizzes one important factor to consider would be how the earlier academic level impacts and how the schedule changes when the quiz is just round the corner(A threshold of academic level might be needed to do well in the quiz and what can be observed is how people who are well prepared react differently to those who are not in the few days before the quiz). As for the events of the clubs you can use the interests described in task-4 to see in which events a person is likely to participate. Consider these situations and try to model them by showing how these events/quizes affect each person.

6. **External Factors**: You can try to incorporate the effect of weather and how it affects one's efficiency for eg.  On a sunny day people don't exercise or on a rainy day (which is literally everyday here) the person feels sulky and doesn't feel like studying. On a rainy day, you might need to cancel your plan of playing outdoor sports which affects the physical fitness metric in the simulation. 

7. **Representing the results**: As you can see in the code right now it simply plots graphs of each factor for each person everyday. However its hard to draw any kind of conclusions from such graphs. So you should try and improve the ways results are being represented. Try drawing scatter plots between factors to see correlatons between them. You can draw these plots considering weekly averages of people instead of daily. After task 5 you can compare the plots specifically of the days close to the event to see its impact.      

### Note: The above mentioned tasks are not hard guidelines and are just to give you a nudge to think in the right direction. So feel free to put your creativity & critical thinking to the work and make some awesome simulations! 

Join our [Discord server](https://discord.gg/Rkh6e6F2) for discussing your doubts.
***

<p align="center">Created with :heart: by <a href="https://wncc-iitb.org/">WnCC</a></p>

