# Post a Python program that contains an array variable whose values are 
# [x] input by the user.
# [x] It should the perform some modification to each element of the array using a loop 
# [x] and then the modified array should be displayed. 
# [x] Include comments in your program that describe what the program does. 
# [x] Also post a screen shot of executing your program on at least one test case.
# ---description--- 
# BL-adder, adds BL to every word in an array

# ----CODE----

# request user to input a sentence
sentence = input("please enter a sentence:\n")
# define array[] as the individual words in the sentence.
array = sentence.split()
# define an empty array to append items to
blarray = []
# define vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# define commonly used digraphs
digraphs = ['ch', 'sh', 'th', 'ph', 'rh', 'sc', 'gh', 'wh', 'qu', 'wr', 'sp']
# define bl as a string
bl = 'bl'

# for every element in array
for i in array:
    # if the first letter is a vowel,
    if i[0].lower() in vowels:
        # then simply add 'bl' to the word
        i = bl + i
        # add the new word to the blarray 
        blarray.append(i)
    # otherwise if the first to letters are a digraph, both letters need to be replaced
    elif i[0:2].lower() in digraphs:
        # add bl in place of the digraphs
        i = bl + i[2:]
        # add the new word to the blarray 
        blarray.append(i)
    # otherwise, the word starts with a consonant which is the only thing that needs to be replaced. 
    else:
        # replace the first letter with bl
        i = bl + i[1:]
        # add the new word to the blarray 
        blarray.append(i)

# print the new sentence. 
print('your bl\'d sentence is:')
for i in blarray:
    print (i, end=' ')

