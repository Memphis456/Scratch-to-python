import random
import time

print("I am a magic 8 ball, you can ask me anything")

time.sleep(1)

name = input("First what is your name?: ").title()

time.sleep(1)

random1 = random.randint(1, 3)

if random1 == 1:
    print("Hi", name,)
    
elif random1 == 2:
    print("Hello", name, "I hope you're well today")
    
else:
    print("Its good to meet you", name)

time.sleep(1)

question = input("What would you like to ask me?: ")

random2 = random.randrange(19)

RandomQuestion = ["It is certain", "Reply hazy, try again", "Don’t count on it", "It is decidedly so", "Ask again later", "My reply is no", "Without a doubt", "Better not tell you now", "My sources say no", "Yes definitely", "Cannot predict now", "Outlook not so good", "You may rely on it", "Concentrate and ask again", "Very doubtful", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
print(f'{RandomQuestion[random2]} {name}')


##It is certain
##Reply hazy, try again
##Don’t count on it
##It is decidedly so
##Ask again later
##My reply is no
##Without a doubt
##Better not tell you now
##My sources say no
##Yes definitely
##Cannot predict now
##Outlook not so good
##You may rely on it
##Concentrate and ask again
##Very doubtful
##As I see it, yes
##Most likely		
##Outlook good
##Yes
##Signs point to yes

 




    
    

