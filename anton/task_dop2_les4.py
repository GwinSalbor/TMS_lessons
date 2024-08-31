some_text = """English texts for beginners to practice reading 
and comprehension online and for free. Practicing your comprehension 
of written English will both improve your vocabulary and understanding 
of grammar and word order."""

sorted_text = sorted(some_text.lower())

empty_dict = {}

empty_list = []

for i in sorted_text:
    if i.isalpha():
        i_count = sorted_text.count(i)
        empty_dict.update({i : i_count})

for i in empty_dict:
    if empty_dict[i] == max(empty_dict.values()):
        empty_list.append(i)

end_list = sorted(empty_list)

print(end_list[0])

#нужно спросить про append в конце