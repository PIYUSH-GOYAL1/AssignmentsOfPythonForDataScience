# COUNT THE NUMBER OF TIMES THE GIVEN SENTENCE CONTAINS THE WORD "DOG"

input_string = str(input("Enter a sentence: "))

def get_dog(input_string):
    
    words = input_string.split(" ")
    count_dog = 0

    for i in words:
        i = i.capitalize()
        if i == "Dog":
            count_dog += 1
        else:
            continue
    
    print("The given sentence contains {count} times the word dog".format(count = count_dog))
        
get_dog(input_string)