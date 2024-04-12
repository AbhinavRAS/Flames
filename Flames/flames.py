def boyname(name1):
    list1 = []
    names = name1.lower().split()
    for name in names:
        for i in range(len(name)):
            if name[i] != ' ':
                list1.append(name[i])
    return sorted(list1)

def girlname(name2):
    list2 = []
    names = name2.lower().split()
    for name in names:
        for i in range(len(name)):
            if name[i] != ' ':
                list2.append(name[i])
    return sorted(list2)

def match(name1, name2):
    list1 = boyname(name1)
    list2 = girlname(name2)
    if list1 is None or list2 is None or name1[0] == ' ' or name2[0] == ' ':
        return None
    count = 0
    for i in list1:
        if i in list2:
            count += 1
            list2.remove(i)
    return count % 6

def flames():
    count1 = match(name1, name2)
    if count1 is not None:
        list3 = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        output = list3[count1 - 1]
        print("\033[1;34mYour relationship is\033[0m", "\033[1;31m",output,"\033[0m")
        print(count1,"\n")

for i in range(int(input("Enter the number of test cases: "))):
    name1 = input("Enter the boy's name: ")
    name2 = input("Enter the girl's name: ")
    flames()
