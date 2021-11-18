def ADD(k,v):
    global d
    box = bool(d)
    while(True):
        if box == False :
            d = {k:v}
            return d
        else:
            box2 =d.keys()
            if k in box2:
                print("this key,there is in dictionary")
                break
            else:
                d[k] = v
                return d
def REMOVE(k,v):
    box3 = d.keys()
    if k in box3:
        for i in d.items():
            if (k,v) in d.items():
                del d[k]
                print("successfully")
                break
            else:
                print("Error")
                break



d = {}
print("first you must 5 item to add: ")
for i in range(5):

    kilid = input("Enter key: ")
    value = int(input("Enter value: "))
    ADD(kilid, value)
print(d)
kilid = input("Enter key: ")
value = int(input("Enter value: "))
action = input("Enter action: ")
if action == "ADD":
    ADD(kilid, value)
    print("added successfully")
    #print(d)
else:
    REMOVE(kilid,value)
    print("removed successfully")
    #print(d)


