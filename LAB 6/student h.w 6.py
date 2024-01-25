import os
# function to insert data.
def add(name , age , major , avg):
    try:
        file = open("first.txt", "a")
        file.write(name+'\n')
        file.write(str(age)+'\n')
        file.write(major+'\n')
        file.write(str(avg)+'\n')
        print('		Added Successfully ... !')
        print('----------------------')
        file.close()
    except:
        print('		error')
        print('----------------------')

# function to update data.
def read():
    f = open("first.txt", "r")
    for i in f :
        print('Name    : ', i)
        i = f.readline()
        print('Age     : ', i)
        i = f.readline()
        print('Major   : ', i)
        i = f.readline()
        print('Average : ', i)
        print('----------   -----------')
    f.close()



def search(n):
    f = open('first.txt','r')
    for i in f :
        if i==n+'\n':
            print('Name    : ',i)
            i = f.readline()
            print('Age     : ',i)
            i = f.readline()
            print('Major   : ',i)
            i = f.readline()
            print('Average : ',i)
            print('----------------------')
    f.close()
def update(name):
 with open("first.txt", "w") as file:
    file.write(name+'\n')
    file.write(str(age)+'\n')
    file.write(major+'\n')
    file.write(str(avg)+'\n')
    print('		update Successfully ... !')
    print('----------------------')


while True :
    c = int(input('''
1 ) Add Student.
2 ) Read Student Data.
3 ) exit.
4 ) update.
'''))
    print('===============================')
    if c==1:
        name = input('Enter the name : ')
        age = int(input('Enter the age : '))
        major = input('Enter the major : ')
        avg = int(input('Enter the average : '))
        add(name,age,major,avg)
    elif c==2:
        read()
    elif c==3:
        print('exit....')
        break
    elif c == 4:
        print("Current data:")
        read()
        name = input('Enter the  new name : ')
        age = int(input('Enter the new  age : '))
        major = input('Enter the  new major : ')
        avg = int(input('Enter the new  average : '))
        update(name)

    else:
        print('error')
