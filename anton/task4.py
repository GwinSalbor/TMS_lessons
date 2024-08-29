input_string = str(input())

list_string = list(input_string)

def func_frequency(list_st):

    for i in list_st:
        i_count = list_st.count(i)
        print(dict({i_count : i}))

func_frequency(list_string)
    


