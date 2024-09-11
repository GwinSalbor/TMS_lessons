# Additional task1: Find a unique value in the given list
num_list = [1, 5, 2, 9, 2, 9, 1]

for i in num_list:
    if num_list.count(i) == 1:
        print(f"Unique value in the given array:", i)


# Additional task2: Find the most frequently used symbol. In case more than one value match, use alphabetical order
def most_frequent_char(text):

    char_count = {}

    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    max_frequency = 0
    most_frequently_used_char = None

    for item, count in char_count.items():
        if count > max_frequency or (count == max_frequency and item < most_frequently_used_char):
            max_frequency = count
            most_frequently_used_char = item
    print(most_frequently_used_char)

most_frequent_char("a-z")
most_frequent_char("Hello World!")
most_frequent_char("How do you do?")
most_frequent_char("One")
most_frequent_char("Oops!")
most_frequent_char("AAaooo!!!!")
most_frequent_char("a" * 9000 + "b" * 1000)