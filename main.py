def Min():
    my_list=[4,6,27,15,31,22,30,29,8,16]
    min_value = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] < min_value:
            min_value = my_list[i]
    print(f'Minimum no is: {min_value}')

Min()
