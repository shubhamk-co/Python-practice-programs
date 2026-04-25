# file=open("data.bin","wb")
# file.write(b"hello")
# file.close()

# file=open("data.bin","rb")
# print(file.read())
# file.close()



# with open("data.bin","wb") as file:
#     file.write(b"hello")


# with open("data.bin","rb") as file:
#     print(file.read())




# f=open("tea.txt","r")
# print(f.readline())
# print(f.readline().strip())
# print(f.readline().strip())


import csv
# file=open("cancer.csv","r")
# print(file.read())
# file.close()

with open("cancer.csv","r") as file:
    read=csv.reader(file)
    next(read)
    
    for i in read:
        print(i[0])