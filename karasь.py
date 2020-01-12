import random
mylist = ["top","karasь","krasava","kibersport","#ВNaviНеЗвали?"]
mylist2 = ["best of the best","god","#КиберспортСкучает","pashalka"]
name =input("Введи своё имя для авторизации")
if name =="Maksim":
    print(random.choice(mylist))
else:
    print(random.choice(mylist2))
    
    
    
