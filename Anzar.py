# List = [1,2,3,4]
# List.append(9)
# print(List)
# b=List.copy()
# print(b) 
# set = (1,2,3,4,5)
# list=list(set)
# print(list)
# List.clear
# print(list)

# List = [1,2,3,4,5]
# List.sort(reverse=True)
# print(list)

# list = [5,9,15]
# List2 = [1,2,3]
# List.extend(List2)
# x = list.index(9)
# print(x)


# list = [x for x in range (2,9) if x!=8]
# print (list )

# y = int(input("enter value"))
# list = [x*x for x in range(2,30,2)]
# print(list)


def classroom():
    list=[]
    for i in range(10):
        n=int(input("Enter age : "))
        list.append(n)
    list=sum(list)
    avg=list/10
    print("avg is",avg)

classroom()
    

