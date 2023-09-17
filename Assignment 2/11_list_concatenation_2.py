# LIST CONCATENATION

list_1 = ["Hello ","take "]
list_2 = ["Dear","Sir"]

list_3 = list()

for i in range (0 , len(list_1)):
    for j in range (0 , len(list_2)):
        list_3.append(list_1[i] + list_2[j])

print(list_3)
