# Write a function, it will convert a list to a dictionary. The dictionary will contain key value pairs. The keys are the items in the list, the values are the number of times they appear in the list. Only items that occur more than once should be included in the dictionary.
# e.g
# [1,6,6,0,3,1,6,4,] =>> {1:2 , 6:3}

list = [2,3,5,3,2,2,2,5,6,6,8,9,7,7]
def List2Dict(list):
    dict = {}
    print("List =",list)
    for i in list:
        #print(i)
        if (i in dict):
            #print(dict)
            dict[i] += 1
        else:
            dict[i] = 1
    #print(dict)
    dict = {k:v for k, v in dict.items() if v!=1}
    print("Dictionary =",dict)
List2Dict(list)
