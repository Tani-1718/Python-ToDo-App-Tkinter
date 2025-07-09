def writeFile():
    with open("notes.txt" , 'w') as f:
        f.write("python is powerfull\n")
        f.write("file handling is easy")
writeFile()
def readFile():
    with open("notes.txt" , 'r') as f:
        ob1 = f.read()
        print(ob1)
readFile()
def appendFile():
    with open("notes.txt" , 'a') as f:
        f.write("\nappending some new content in the file")

def countLines():
    count = 0
    with open("notes.txt" , 'r') as f:
        for line in f:
            print(line)
            count += 1
            print(count)
    print(count , "is the number of lines in notes")

def countWord():
    word_count = {}
    with open("notes.txt" ,'r') as f:
        for lines in f:
            words = lines.strip().lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    for word , count in word_count.items():
        print(word , " : " , count)

#Reverse content line-wise and save to new file
def reverseFile():
    with open("notes.txt" , 'r') as f:
        lines = f.readlines()

    with open("reverseNotes.txt" , 'w') as f:
        for line in reversed(lines):
            f.write(line)
    print("file content reversed and saved to reverseNotes.txt file")


#Count total characters in file
def countChar():
    with open("notes.txt" , 'r') as f:
        text = f.read()
        print("total chars in notes.txt file is " , len(text))

 
#Copy one file to another
def copyFile():
    with open("notes.txt" , 'r') as f:
        lines = f.readlines()

    with open("notes2.txt" , 'w') as f:
        for line in lines:
            f.write(line)

#Search Word in File
def searchWord():
    word = input("find the word to be found : ").lower()
    found = False
    with open("notes.txt" , 'r') as f:
        for line in f:
            if word in line.lower():
                print("->" , line.strip())
                found = True
    if not found:
        print("the word does not exist")

# Replace and Save to New File

def replaceWord():
    with open("notes.txt" , 'r') as f:
        content = f.read()

    newContent = content.replace("pyhton" , "javascript")

    with open("updatedNotes.txt" , 'w') as f:
        f.write(newContent)
    
    print("word are successfully replaced")

#replaceWord()


