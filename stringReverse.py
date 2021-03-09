# definition of the reverse function 
def reverse(string): 
  #crete an empty string
  str = "" 
  #looping fromthe end of the string's array
  for i in string: 
    #adding the current characte to the empty string
    str = i + str
  return str

myString = input("Enter a string : ")
print(reverse(myString))