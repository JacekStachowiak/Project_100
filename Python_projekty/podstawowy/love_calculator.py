
print('Welcome to the Love Calculator !!!')

name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

string_combo = name1 + name2
lower_name = string_combo.lower()
# TRUE LOVE
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t+r+u+e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))
print(f'Your total point is: {love_score}')

if (love_score < 10) or (love_score >= 90):
    print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score  >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are allright together')
else:
    print(f'Your score is {love_score}')    
    
      