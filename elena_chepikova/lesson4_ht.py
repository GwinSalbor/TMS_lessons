# HT4.1 Create chatbot based on user input with if and elif operators
# HT4.2 Add a couple of conditions with startswith
zodiac_dict = {"december": "Sagittarius", "january": "Capricorn", "february": "Aquarius",
               "march": "Pisces", "april": "Aries", "may": "Taurus",
               "june": "Gemini", "july": "Cancer", "august": "Leo",
               "september": "Virgo", "october": "Libra", "november": "Scorpio"}

user_input1 = input("Hello! I am an astrological chat bot. Would you like to know your Zodiac sign: ").lower()
if user_input1.startswith("y"):
    user_input2 = input("Please write the month of your birth: ").lower()
    if user_input2 in zodiac_dict:
        print(f"Most likely your Zodiac sign is {zodiac_dict[user_input2]}.")
    else:
        print("The month you have entered does not exist. Please start over.")
elif user_input1.startswith("n"):
    print("What a pity! Come back later when you are ready!")
else:
    print('Please write "yes" if you would like to learn more about your Zodiac sign.')


# HT4.3 Make an array out of the string
def text_split(text):
    print(text.split())

text_split("Robin Singh")
text_split("I love arrays they are my favorite")


# HT4.4 Write text with given list and strings
array1 = ['Ivan', 'Ivanou']
str1 = 'Minsk'
str2 = 'Belarus'

print(f"Hello {array1[0]} {array1[1]}! Welcome to {str1} {str2}!")


# HT4.5 Make a string from a given list
array2 = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
print(' '.join(array2))


# HT4.6 Create a list,add a new value to the 3d position, remove an element using index
array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array3.insert(2, "i")
print(array3)
array3.pop(5)
print(array3)


# HT4.7 Create a loop for 10 inputs and sort the list
array4 = []
for i in range(10):
    array4.append(int(input(f"Add a numeric value {i+1}: ")))

print(sorted(array4))