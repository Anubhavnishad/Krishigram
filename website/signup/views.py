from django.shortcuts import render
import mysql.connector as sql

fn=''
mob=''
uid=''
mpass=''
cpass=''


# Create your views here.
def signaction(request):
    global fn,mob,uid,mpass,cpass
    if request.method=='POST':
        m=sql.connect(host="localhost",user="root",passwd="vivek",database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.item():
            if key=="name":
                fn=value
            if key=="mobno":
                mob=value
            if key=="userid":
                uid=value
            if key=="pass":
                mpass=value
            if key=="cpass":
                cpass=value
            print(fn,mob)
        
        c= "insert into users values({},{},{},{},{})".format(fn,mob,uid,mpass,cpass)
        cursor.execute(c)
        m.commit()
    

    return render(request,"signup.html")
