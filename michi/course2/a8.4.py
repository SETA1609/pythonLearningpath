fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("There is no such file")
    quit()
lst = list()

for line in fh:
    crrt_list:list=line.split(" ")
    for word in crrt_list:
        if word not in lst and word !="\n":
            lst.append(word.strip())
        else:
            continue
lst.sort()
print(lst)

#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']