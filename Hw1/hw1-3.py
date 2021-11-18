def check_pas(pas):
    list1 =[]
    for i in pasword:
        specialsym = ['$', '@', '#', '%']
        val = True

        if len(i) < 6:
            val = False

        if len(i) > 12:
            val = False

        if not any(char.isdigit() for char in i):
            val = False

        if not any(char.isupper() for char in i):
            val = False

        if not any(char.islower() for char in i):
            val = False

        if not any(char in specialsym for char in i):
            val = False

        if val == True:
            list1.append(i)
    return list1

pasword = input("enter paswords:").split(',')
output = check_pas(pasword)
for i in output:
    print(i)