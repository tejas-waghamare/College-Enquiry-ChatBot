import pymysql
from django.shortcuts import render, redirect
import random
from django.core.cache import cache


mydb=pymysql.connect(host="localhost",user="root",password="root",database="college")

def admindashboard(request):
    return render(request,"admindashboard.html")
def addquestion(request):
    q1=request.POST.get('q1')
    ans=request.POST.get('ans')
    sql="INSERT INTO question(Question,Answer) VALUES (%s,%s)";
    values=(q1,ans)
    c1=mydb.cursor()
    c1.execute(sql,values)
    mydb.commit()
    return render(request,"index.html")

def subanswer(request):
    q1=request.GET.get('q1')
    print("question ",q1)
    request.session['question']=q1
    return render(request,"subanswer.html")
def subanswer1(request):
    q1=request.session['question']
    print("question ",q1)
    ans=request.POST.get('ans1')
    
    sql="INSERT INTO question(Question,Answer) VALUES (%s,%s)";
    values=(q1,ans)
    c1=mydb.cursor()
    c1.execute(sql,values)
   
    c2=mydb.cursor()
    q2="delete from unanswer where question='"+q1+"'"
    c2.execute(q2)
    mydb.commit()
    
    return render(request,"subanswer.html")
def page1(request):
    return render(request,"index.html")


def userhome(request):
    return render(request,"userdashboard.html")
def aboutus(request):
    return render(request,"aboutus.html")
def login(request):
    return render(request,"index.html")
def logout(request):
    return render(request,"index.html")
def register(request):
    return render(request,"register.html")
def ourteam(request):
    return render(request,"ourteam.html")
def contact(request):
    return render(request,"contact.html")
def adminhome(request):
    return render(request,"admindashboard.html")
def doregister(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    sql="INSERT INTO user_new(name,contact,email,password) VALUES (%s,%s,%s,%s)";
    values=(name,contact,email,password)
    cur=mydb.cursor()
    cur.execute(sql,values)
    mydb.commit()
    return render(request,"index.html")

def viewuser(request):
    content={}
    payload=[]
    q1="select * from user_new";
    cur=mydb.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    for x in res:
        content={'name':x[0],"contact":x[1],"email":x[2],"uid":x[4]}
        payload.append(content)
        content={}
    return render(request,"viewuser.html",{'list': {'items':payload}})


def doremove(request):

    uid= request.GET.get("uid")
    q1=" delete from user_new where uid=%s";
    values=(uid,)
    cur=mydb.cursor()
    cur.execute(q1,values)
    mydb.commit()
    return viewuser(request)





def unanswer(request):
    content={}
    payload=[]
    q1="select * from unanswer";
    cur=mydb.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    for x in res:
        content={'question':x[0]}
        payload.append(content)
        content={}
    return render(request,"unanswer.html",{'list': {'items':payload}})

def viewpredicadmin(request):
    content={}
    payload=[]
    q1="select * from user_new";
    cur=mydb.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    for x in res:
        content={'name':x[0],"contact":x[1],"email":x[2],"uid":x[4]}
        payload.append(content)
        content={}
    return render(request,"prevpredadmin.html",{'list': {'items':payload}})
    
def analyze(request):
    return render(request, 'analyze.html')

def calculate(request):
    return render(request,"calculate.html")

def recommend(request):
    return render(request)
def logout(request):
    return render(request,"index.html")

def index(request):
    return render(request, 'userdashboard2.html')

def temp(request):
    
    return render(request, 'analyze.html')




def dologin(request):
    sql="select * from user_new";
    cur=mydb.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    email=request.POST.get('username')
    password=request.POST.get('password')
    isfound="0";
    print(email)
    print(password)
    if(email=="admin" and password=="admin"):
        print("print")
        return render(request,"admindashboard.html")
    else:
        for x in data:
           if(x[2]==email and x[3]==password):
               request.session['uid']=x[4]
               request.session['name']=x[0]
               request.session['email']=x[1]
               request.session['contact']=x[2]
               request.session['pass']=x[3]
               isfound="1"
        if(isfound=="1"):
            return render(request,"userdashboard.html")
        else:
            return render(request,"error.html")




def chat(request):
    user_input = request.POST.get('user_input')
    content={}
    payload=[]
    answer=[]
    q1="select * from question"
    cur=mydb.cursor()
    cur.execute(q1)
    res=cur.fetchall()
    texts = []
    isfound=0
    for x in res:
        if(x[0]==user_input):
            content={'ans':x[1]}
            payload.append(content)
            content={}
            isfound=1
    print("Is Found",isfound)
    print(payload)
    if(isfound==0):
        str1="Wait a moment ,We will convey perfect answer to you (please skip this question for a couple of minutes)"
        content={'ans':str1}
        payload.append(content)
        sql="insert into unanswer values(%s)"
        values=(user_input)
        cur=mydb.cursor()
        cur.execute(sql,values)
        mydb.commit()
    
        
    
    return render(request, 'userdashboard.html', {'list': {'items':payload}}) 
