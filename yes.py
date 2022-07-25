


print("welcome to my sports quiz!")      
answer_yes = input('do you want to play?').lower()
#here we tell the system that if the answer to "do you want to play", is yes, to continue. If not the program will quit
if answer_yes == 'yes':
     print ("Okay, Lets Play!")
else :
    if answer_yes == 'no':
        quit()
score = 0
if answer_yes == 'yes':
  print("lets play")
answer = 'random'  
   
#we state that if answer_yes = 'yes', to show the questions. this is because when you first start this program, 
# if you type yes the program continues. we repeat this every question
if answer_yes == 'yes':
  answer = input(" What team did Tom Brady play the most years for?").lower()
  if answer == 'patriots':
    print("correct")
    score = score + 1 
else: 
    if answer_yes == 'yes':
     print("not correct")
     score = score + 0

if answer_yes == 'yes':
 answer = input("Q:2, which nba player of old times is considered the best of all time?").lower()
if answer == 'micheal jordan':
    print("correct")
    score = score + 1
else:
    if answer_yes == 'yes':
        print("not correct")  
        score = score + 0
    

if answer_yes == 'yes':    
 answer = input('What sport did Jackie Robinson play? ').lower()
if answer == 'baseball':
    print("correct")
    score = score + 1
else:
     if answer_yes == 'yes':
      print("not correct")   
      score = score + 0

if answer_yes == 'yes':
 answer = input("who is considered the best player of all time in the NFL?").lower()
if answer == 'tom brady':
 print("correct")
 score = score + 1
else:
    if answer_yes == 'yes':
     print('not correct')
     score = score + 0


if answer_yes == 'yes':
 print( " Welcome to the end of the quiz! You got", score, "points out of 4!" )
