#reading the file
file = open("data.txt", 'r')
fileLines = file.readlines()
print(fileLines)
file.close()

#writting
file = open("data.txt", 'w')
file.write("My name is jaiyantan")
file.close()

#append
file = open("data.txt", 'a')
file.write("I am 15 yrs old")
file.close()

#read
file = open("data.txt", 'r')
count = 0
for i in file:
    print(i)
    word = i.split()
    count = count + len(word)
print('No of words in the file = ' + count)
file.close()
