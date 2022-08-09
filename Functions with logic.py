def even_check(number):
    return number % 2 == 0
print(even_check(20))
my_list= [1,2,3,4,56,7,8,9]
listtwo = [1,3,5,7]
evennumber=[]
def even_check_list(list):
    for number in list:
        if number %2 == 0:
            evennumber.append(number)

    else:
        pass
    return evennumber
print(even_check_list(my_list))
print(even_check_list(listtwo))
