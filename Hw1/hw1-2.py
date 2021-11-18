def time_display(v1,v2):
    v1 = [int(i) for i in t1.split(':')]
    v2 = [int(i) for i in t2.split(':')]
    box1_h = v1[2]+v2[2] +(v1[1]+v2[1]+(v1[0]+v2[0])//60)//60
    box_m = (v1[1]+v2[1]+(v1[0]+v2[0])//60)%60
    box_s = (v1[0]+v2[0])%60
    return f'Time is {box1_h} hour(s) and {box_m} minute(s) and {box_s} second(s)'


t1=input("enter first time: ")
t2=input("enter second time: ")

print(time_display(t1,t2))