# UISNG LAMBDA AND FILTER FUNCTION TO FILTER OUT PARTICULAR ELEMENTS FROM THE GIVEN LIST

seq = ["soup" , "dog" , "salad" , "cat" , "great"]

result = list(filter(lambda element : (element[0] != 's') , seq))

print(result)