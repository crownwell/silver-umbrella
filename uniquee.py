# silver-umbrella
#a function to determine the uniqueness of a list
def unique(list):
    for i in range(0,len(list)-1):
        if list[i] in list[i+1:]:
                return False

    return True

lis=[9,5,4,3,2,1,8,8]
print(unique(lis))
