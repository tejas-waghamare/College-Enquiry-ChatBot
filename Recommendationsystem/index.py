from django.shortcuts import render, redirect
import random
from django.core.cache import cache
from .models import User
import pymysql

# Only needed for non-ORM tables
mydb = pymysql.connect(host="localhost", user="root", password="root", database="college")

def admindashboard(request):
    return render(request, "admindashboard.html")

def addquestion(request):
    q1 = request.POST.get('q1')
    ans = request.POST.get('ans')
    sql = "INSERT INTO question(Question,Answer) VALUES (%s,%s)"
    values = (q1, ans)
    c1 = mydb.cursor()
    c1.execute(sql, values)
    mydb.commit()
    return render(request, "index.html")

def subanswer(request):
    q1 = request.GET.get('q1')
    request.session['question'] = q1
    return render(request, "subanswer.html")

def subanswer1(request):
    q1 = request.session['question']
    ans = request.POST.get('ans1')
    
    sql = "INSERT INTO question(Question,Answer) VALUES (%s,%s)"
    values = (q1, ans)
    c1 = mydb.cursor()
    c1.execute(sql, values)

    c2 = mydb.cursor()
    q2 = "DELETE FROM unanswer WHERE question=%s"
    c2.execute(q2, (q1,))
    mydb.commit()
    
    return render(request, "subanswer.html")

def page1(request):
    return render(request, "index.html")

def userhome(request):
    return render(request, "userdashboard.html")

def aboutus(request):
    return render(request, "aboutus.html")

def login(request):
    return render(request, "index.html")

def logout(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def ourteam(request):
    return render(request, "ourteam.html")

def contact(request):
    return render(request, "contact.html")

def adminhome(request):
    return render(request, "admindashboard.html")

def doregister(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    password = request.POST.get('password')

    User.objects.create(name=name, contact=contact, email=email, password=password)
    return render(request, "index.html")

def viewuser(request):
    users = User.objects.all()
    payload = [{'name': u.name, 'contact': u.contact, 'email': u.email, 'uid': u.id} for u in users]
    return render(request, "viewuser.html", {'list': {'items': payload}})

def doremove(request):
    uid = request.GET.get("uid")
    User.objects.filter(id=uid).delete()
    return viewuser(request)

def unanswer(request):
    content = {}
    payload = []
    q1 = "SELECT * FROM unanswer"
    cur = mydb.cursor()
    cur.execute(q1)
    res = cur.fetchall()
    for x in res:
        content = {'question': x[0]}
        payload.append(content)
        content = {}
    return render(request, "unanswer.html", {'list': {'items': payload}})

def viewpredicadmin(request):
    users = User.objects.all()
    payload = [{'name': u.name, 'contact': u.contact, 'email': u.email, 'uid': u.id} for u in users]
    return render(request, "prevpredadmin.html", {'list': {'items': payload}})

def analyze(request):
    return render(request, 'analyze.html')

def calculate(request):
    return render(request, "calculate.html")

def recommend(request):
    return render(request)

def index(request):
    return render(request, 'userdashboard2.html')

def temp(request):
    return render(request, 'analyze.html')

def dologin(request):
    email = request.POST.get('username')
    password = request.POST.get('password')
    isfound = "0"

    if email == "admin" and password == "admin":
        return render(request, "admindashboard.html")

    users = User.objects.all()
    for u in users:
        if u.email == email and u.password == password:
            request.session['uid'] = u.id
            request.session['name'] = u.name
            request.session['email'] = u.email
            request.session['contact'] = u.contact
            request.session['pass'] = u.password
            isfound = "1"
            break

    if isfound == "1":
        return render(request, "userdashboard.html")
    else:
        return render(request, "error.html")

def chat(request):
    user_input = request.POST.get('user_input')
    content = {}
    payload = []
    isfound = 0

    q1 = "SELECT * FROM question"
    cur = mydb.cursor()
    cur.execute(q1)
    res = cur.fetchall()

    for x in res:
        if x[0] == user_input:
            content = {'ans': x[1]}
            payload.append(content)
            isfound = 1
            break

    if isfound == 0:
        content = {'ans': "Answer Not Found"}
        payload.append(content)
        sql = "INSERT INTO unanswer VALUES (%s)"
        cur.execute(sql, (user_input,))
        mydb.commit()

    return render(request, 'userdashboard.html', {'list': {'items': payload}})
