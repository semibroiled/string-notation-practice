import random
myNum = 5.123 #this is a float data type
print(int(myNum)) #this converts my variable to int data type

print(random.randrange(1,100))

myString = 'gloria borger'
print(len(myString))

print(myString.split())

comment = 'thanks, Mykull. what you did at the 36:20 ish mark helped me overcome an obstacle in my coding. Im fairly new to coding, just started with python, and I was trying to make a script to respond to certain things containing keywords. And the bit where you can find words in a string and set that variable to a boolean really helped!'
print('cute' in comment)

comment2withquotes = 'thanks, Mykull. what you did at the 36:20 ish mark helped me overcome an obstacle in my coding. I\'m fairly new to coding, just started with python, and I was trying to make a script to respond to certain things containing keywords. And the bit where you can find words in a string and set that variable to a boolean really helped!'
#shift + alt + 7 gives a backslah. using that with the 
#quotation mark, and i could include it in the 
#str without fucking it up

print(comment2withquotes[2])

commentSplit = comment2withquotes.split()
print(commentSplit[2])

print(comment[0:random.randrange(0,len(comment2withquotes))])


