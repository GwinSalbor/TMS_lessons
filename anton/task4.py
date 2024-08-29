input_string = str(input())

list_string = list(input_string)

def func_frequency(list_st):

    list_b = []

    for i in list_st:
        i_count = list_st.count(i)
        list_b.append(dict({i_count : i}))
    return list_b

print(func_frequency(list_string))
    


