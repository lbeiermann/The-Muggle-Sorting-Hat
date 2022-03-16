#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import webbrowser as wb 
points = 0

#Question 1
tvshow = input("Choose your favorite tvshow from this list looney toons cartoons, scooby doo or art attack")
print("Your favorite show is" +  tvshow)

if tvshow == "looney toons cartoons":
    print("Thank you for your Answer Muggle")
    points += 1

elif tvshow == "scooby doo":
    print("Thank you for your Answer Muggle")
    points += 2

elif tvshow == "art attack":
    print ("Thank you for your Answer Muggle")
    points += 1
wb.open("https://www.denofgeek.com/wp-content/uploads/2020/03/UK-Kids-streaming.jpg?resize=768%2C432")


#Question 2
food = input ("Choose your favorite food from this list sushi, hamburger or salad")
print ("Your favorite food is" +  food)

if food == "sushi":
    print("Thank you for your Answer Muggle")
    points += 2

elif food == "hamburger":
    print("Thank you for your Answer Muggle")
    points += 1

elif food == "salad":
    print ("Thank you for your Answer Muggle")
    points += 1

wb.open("https://www.eufic.org/de/images/uploads/images/1_Jan_Plant-basedDiets_Website.png")

#Question 3
sport = input ("Choose your favorite sport from this list fotball, yoga or swimming")
print("Your favorite sport is" +  sport)

if sport == "fotball":
    print("Thank you for your Answer Muggle")
    points += 3

elif sport == "yoga":
    print("Thank you for your Answer Muggle")
    points += 2

elif sport == "swimming":
    print("thank you for your Answer Muggle")
    points += 1

wb.open("https://post-sv.de/wp-content/uploads/2021/02/sports-tools-e1617284629329.jpg")

#Question 4
color = input ("Choose your favorite color from this list blue, green, yellow or red")
print ("Your favorite color is" +  color)

if color == "blue":
    print ("Thank you for your Answer Muggle")
    points += 2

elif color == "green":
    print ("Thank you for your Answer Muggle")
    points += 1

elif color == "yellow":
    print("Thank you for your Answer Muggle")
    points += 1

elif color == "red":
    print("Thank you for your Answer Muggle")
    points += 3

wb.open("https://neilpatel.com/wp-content/uploads/2017/08/colors.jpg")

#Question 5
assignment = input ("Choose your favorite assignment from this list mathematics,german or sports ")
print("Your favorite assignment is" + assignment)

if assignment == "mathematics":
    print ("Thank you for your Answer Muggle")
    points += 2

elif assignment == "german":
    print("Thank you for your Answer Muggle")
    points += 1

elif assignment == "sports":
    print ("Thank you for your Answer Muggle")
    points += 1

wb.open ("https://smallstuffcounts.com/wp-content/uploads/2018/07/free-printable-assignment-tracker_lri-6.jpg")

#Question 6
new_people = input ("Do you like to meet new people?")
print("Your Answer is" + new_people)

if new_people == "yes":
    print("Thank you for your Answer Muggle")
    points += 2

elif new_people == "no":
    print("Thank you for your Answer Muggle")
    points += 1

wb.open("https://www.youtube.com/watch?v=nMN4JZ8crVY")

#Question 7
feel= input ("Do you feel you today happy?")
print("Today you feel happy" + feel )

if feel == "yes":
    print("Thank you for your Answer Muggle")
    points += 2

elif feel == "no":
    print("Thank you for your Answer Muggle")
    points += 1

#Question 8
travel = input ("How often do you travel? Choose one of the following options: 1-2 times per year, 2-4 times per year or None")
print("Your Answer is" + travel)

if travel == "1-2 times per year":
    print("Thank you for your Answer Muggle")
    points += 1

elif travel == "2-4 times per year":
    print ("Thank you for your Answer Muggle")
    points += 2

elif travel == "none":
    print ("Thank you for your Answer Muggle")
    points += 0

#Question 9

problems = input ("Do you like to solve problems")
print ("Your Answer is" + problems)

if problems == "yes": 
    print ("Thank you for your Answer Muggle")
    points += 2

elif problems == "no":
    print ("Thank you for your Answer Muggle")
    points += 1

#Question 10 

overwhelmed = input ("Do you some times tend to feel overwhelmed? ")
print ("Your Answer is" + overwhelmed)

if overwhelmed == "yes":
    print("Thank you for your Answer Muggle")
    points += 1

elif overwhelmed == "no":
    print ("Thank you for your Answer Muggle")
    points += 2

#Question 11

pushy = input ("Do you like to be pushy?")
print ("Your Answer is" + pushy)

if pushy == "yes":
    print("Thank you for your Answer Muggle")
    points += 0

elif pushy == "no":
    print("Thank you for your Answer Muggle")
    points += 1

#Question 12 

goals = input("Do you like to set long term goals?")
print("Your Answer is" + goals)

if goals == "yes":
    print("Thank you for your Answer Muggle")
    points += 2

elif goals == "no":
    print("Thank you for your Answer Muggle")
    points += 1

#Question 13 
angry = input ("Do you get easly angry?")
print("Your Answer is"+ angry)

if angry == "yes":
    print("Thank you for your Answer Muggle")
    points += 1

elif angry == "no":
    print("Thank you for your Answer Muggle")
    points += 2


#Question 14 
helping = input ("Do you like helping other people?")
print("Your Answer is" + helping)

if helping == "yes":
    print("Thank you for your Answer Muggle")
    points += 2

elif helping == "no":
    print ("Thank you for your Answer Muggle")
    points += 1

#Question 15 
calm = input ("How much take you to be calm after a fight? Choose one of the following options: 1-5 hours, 24 hrs or weeks")
print("Your Answer is" + calm)

if calm == "1-5 hours":
    print("Thank you for your Answer Muggle")
    points += 3

elif calm == "24 hrs":
    print("Thank you for your Answer Muggle")
    points += 2

elif calm == "weeks":
    print("Thank you for your Answer Muggle")
    points += 1

#Question 16
busy = input("Are you always busy?")
print("Your Answer is" + busy)

if busy == "yes":
    print("Thank you for your Answer Muggle")
    points += 2

elif busy == "no":
    print("Thank you for your Answer Muggle")
    points += 3

#Question 17 
disappointed = input("Are you easily disappointed?") 
print("Your answer is" + disappointed)

if disappointed == "yes":
    print("Thank you for your Answer Muggle")
    points += 1

elif disappointed == "no":
    print("Thank you for your Answer Muggle")
    points += 2

#Question 18 

drink = input ("Which one is your favorite drink, please choose one from the following options: soda, water or tee ")
print("Your Answer is" + drink)

if drink == "soda":
    print("Thank you for your Answer Muggle")
    points += 1

elif drink == "water":
    print("Thank you for your Answer Muggle")
    points += 3

elif drink == "tee":
    print("Thank you for your Answer Muggle")
    points += 3

#Question 19 

movie = input ("What type of movie do you like the most, please choose one from the following options: comedy, cartoons or action ")
print("Your Answer is" + movie)

if movie == "comedy":
    print("Thank you for your Answer Muggle")
    points += 2

elif movie == "cartoons":
    print("Thank you for your Answer Muggle")
    points += 3

elif movie == "action":
    print("Thank you for your Answer Muggle")
    points += 1

#Question 20

dessert = input ("Which one is your favorite dessert, please choose one from the following options: chocolate cake, cookies, cheese")
print("Your Answer is" + dessert)

if dessert == "chocolate cake":
    print("Thank you for your Answer Muggle")
    points += 2

elif dessert == "cookies":
    print("Thank you for your Answer Muggle")
    points += 1

elif dessert == "Cheese":
    print("Thank you for your Answer Muggle")
    points += 3

#End of Personality survey 


if points == 10:
    print("You are Red")
    wb.open("https://static.wikia.nocookie.net/harrypotter/images/9/9b/Gryffindor_Banner.png/revision/latest?cb=20161129154826&path-prefix=de")
    
elif points == 15:
    print("You are Blue")
    wb.open("https://static.wikia.nocookie.net/harrypotter/images/7/71/Ravenclaw_ClearBG.png/revision/latest?cb=20161020182442")
    
elif points == 20: 
    print("You are Green")
    wb.open("https://static.wikia.nocookie.net/hpw/images/b/b2/ImagesSsl.jpeg/revision/latest?cb=20200716115840&path-prefix=de")
    
elif points == 25:
    print ("You are Yellow")
    wb.open("https://static.wikia.nocookie.net/harrypotterfanon/images/c/c9/Hufflepuff.png/revision/latest?cb=20160911200453&path-prefix=de")

    


# In[ ]:




