list_of_values = [1,5,2,9,9,2,1]

for i in list_of_values:
    i_count = list_of_values.count(i)
    if i_count == 1:
        print(i)
        break
