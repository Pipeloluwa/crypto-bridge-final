from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from django.conf import settings
from django.contrib import messages
import urllib

#from .forms import ProForm, LogForm

from .models import Student,All_Course,User_Course,Payment,Message,Popular_Course,Certificate,Success_Storie
from .forms import CreateUserForm, StudentForm, TeacherForm, CourseForm,Pdf_Form,Video_Form
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

trueprofile= False




def register(request):
    # to restrict users to login page
    if request.user.is_authenticated:
        return redirect("my-dashboard")
    # restrict users ended

    else:
        form = CreateUserForm()
        form2= StudentForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            form2 = StudentForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get("email")
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for" + user)

                if form2.is_valid():
                    form2.save()
                return redirect("login")
        return render(request, "register.html", {"form": form})


def loginPage(request):
    verify=True
    # to restrict users to login page
    if request.user.is_authenticated:
        return redirect("my-dashboard")
    # restrict users ended

    else:
        if request.method == "POST":
            username = request.POST.get("username")  # the username in the html input
            password = request.POST.get("password")
            print(username,"/n",password)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # the login in function here was imported from django above
                # return redirect ("register") one can actually put return and redirect together like this
                return redirect("my-dashboard")
            else:
                messages.info(request, "Username Or Password is incorrect")
                return render(request, "login.html",{"trueprofile": trueprofile,"verify": False})
        context = {}
        return render(request, "login.html", {"verify": verify})


global r1,r2,once
r1 = []
r2 = []
once = 0

global stp,lim,numb
stp=0
lim=0
numb=1

global chkno
chkno = 0
global no
no = 0
def index(request):
    try:
        counter_cs=Student.objects.all()
        counter_cs2 = All_Course.objects.all()
        ap_cs= Popular_Course.objects.all()

        count_cs=(len(counter_cs)-1)
        if count_cs==-1:
            count_cs=0
        counter_cs2 = (len(counter_cs2))
        try:
            if request.method=="POST":
                tok=request.POST.get("s_result")
                return redirect("search_course1",tok)
        except:
            return HttpResponse("Your Search input is Empty")
    except:
        return redirect("index")


    return render(request, "index1.html",{"trueprofile": trueprofile, "count_cs":count_cs,"count2":counter_cs2,"ap_cs":ap_cs})

def search_course4(request,tok):
    try:
        p_course=  Popular_Course.objects.get(title=tok)
        return render(request, "admin/search_course4.html",{"p_course":p_course,"four":4})
    except:
        try:
            tok = None
            return render(request, "admin/search_course4.html")
        except:
            return HttpResponse("Your Search input is Empty")



def teachers_login(request):
    verify = True
    # to restrict users to login page
    if request.user.is_authenticated:
        cpl_st = []
        std_or_tch = Student.objects.all()
        for i in std_or_tch:
            cpl_st.append(i.username)
        if (str(request.user)) in cpl_st:
            return HttpResponse(
                "You are Not a Teacher, please click on the appropriate Login Button which is at the TOP in the Homepage")

        return redirect("my-dashboard")
    # restrict users ended

    else:
        cpl_st = []
        std_or_tch = Student.objects.all()
        for i in std_or_tch:
            cpl_st.append(i.username)
        if (str(request.user)) in cpl_st:
            return HttpResponse(
                "You are Not a Teacher, please click on the appropriate Login Button which is at the TOP in the Homepage")
        if request.method == "POST":
            username = request.POST.get("username")  # the username in the html input
            password = request.POST.get("password")
            print(username, "/n", password)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                sf=StudentForm(request.POST)
                if sf.is_valid():
                    sf.save()
                else:
                    pass
                login(request, user)  # the login in function here was imported from django above
                # return redirect ("register") one can actually put return and redirect together like this
                return redirect("teachers-dashboard")
            else:
                messages.info(request, "Username Or Password is incorrect")
                return render(request, "teacher's-login.html", {"trueprofile": trueprofile,"verify": False})
        context = {}
        return render(request, "teacher's-login.html", {"verify": verify})







def npage(request):
    global chkno
    chkno += 1
    return redirect(courses)
def ppage(request):
    global r1, r2
    global chkno
    chkno -= 1
    return redirect(courses)

global former
former= None
def courses(request):
    global r1, r2, once,stp, lim, numb,no,chkno,former
    if len (All_Course.objects.all()) != former:
        chkno = 0
        no = 0
        stp = 0
        lim = 0
        numb = 1

        r2 = []
        r1 = []
        once = 0

    if request.method=="POST":
        nametok=request.POST.get("dzName")
        print("It is a Post: ",nametok)
        return redirect("search_course11", nametok)
    else:
        all_c = All_Course.objects.all()
        former=len(all_c)
        enablepage=False
        if chkno>=1:
            print("thisi sthe len: ",len(r2),chkno)
            try:
                if len(r2) != 0:
                    lenpages=len(r2)
                    if len(r2) >= 1:
                        enablepage = True
                    if chkno <= lenpages:
                        kp_stp = []
                        for i in range(stp):
                            kp_stp.append(i)

                        hlt=None
                        if no==0:
                            hlt=stp
                        return render(request, "courses.html", {"trueprofile": trueprofile, "r2": r2[chkno], "lim":lim,
                                        "stp":kp_stp,"halt":hlt, "numb":numb,"chkno":chkno+1,"enablepage":enablepage})
            except:
                if no != 0:
                    stp+=1
                    hlt=stp
                    kp_stp = []
                    print(stp)
                    print(lim)
                    for i in range(stp):
                        kp_stp.append(i)
                    return render(request, "courses.html",
                                  {"trueprofile": trueprofile, "r2": r1,"stp":kp_stp,"halt":hlt,"numb":numb,
                                   "chkno":chkno+1,"enablepage": enablepage, "lim":lim})

                # else:
                #     kp_stp = []
                #     for i in range(stp):
                #         kp_stp.append(i)
                #     enablepage = False
                #     return render(request, "courses.html", {"trueprofile": trueprofile,"chkno":chkno+1,"stp":kp_stp})



        else:
            if once==0:
                limt=0
                for i in all_c:
                    limt+=1
                    once=1
                    no += 1
                    #if no<=9:
                    r1.append(i.title)
                    if no==9:
                        stp+=1
                        r2.append(r1)
                        r1 = []
                        no=0
                if limt % 9 !=0:
                    lim= (limt // 9) + 1
                if limt % 9 ==0:
                    lim= limt // 9

            if len(r2) > 1:
                kp_stp = []
                for i in range(stp):
                    kp_stp.append(i)
                enablepage = True
                return render(request, "courses.html", {"trueprofile": trueprofile, "r2": r2[0],"stp":kp_stp,
                                                    "numb": numb, "enablepage": enablepage,"chkno":chkno+1, "lim":lim})
            if len(r2) != 0:
                kp_stp = []
                for i in range(stp):
                    kp_stp.append(i)
                enablepage=True
                return render(request, "courses.html", {"trueprofile": trueprofile,"r2":r2[0],"stp":kp_stp,
                                            "numb":numb,"enablepage":enablepage,"chkno":chkno+1, "lim":lim})
            if len(r1) != 0:
                kp_stp = []
                for i in range(stp):
                    kp_stp.append(i)
                enablepage=False
                return render(request, "courses.html", {"trueprofile": trueprofile,"r2":r1,"stp":kp_stp,
                                                    "numb":numb,"enablepage":enablepage,"chkno":chkno+1, "lim":lim})
            else:
                kp_stp=[]
                for i in range (stp):
                    kp_stp.append(i)
                enablepage=False
                return render(request, "courses.html", {"trueprofile": trueprofile,"stp":kp_stp,"chkno":chkno+1,
                                                        "numb":numb,"lim":lim})

def about(request):
    return render(request, "about-2.html", {"trueprofile": trueprofile})


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Message.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
        return render(request, "contact-1.html", {"trueprofile": trueprofile,"sent":True})
    else:
        return render(request, "contact-1.html", {"trueprofile": trueprofile,"sent":False})


def testimony(request):
    succ=Success_Storie.objects.all()
    return render(request, "testimony.html", {"trueprofile": trueprofile,"succ":succ})

@login_required(login_url="login")  # to restrict anonymous user if the user is not logged in
def my_dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            tok = request.POST.get("qq")
            return redirect("search_course3",tok)
        else:
            courses= All_Course.objects.all()
            uc = User_Course.objects.all()
            course_picture = 'CB/ourapp/static/assets/images/courses/pic.jpg'
            userv = request.user
            userv = str(userv)

            no = 0
            tno1 = []
            for i in courses:
                tno1.append(i.identification_code)
                no += 1

            nop = 0
            for i in uc:
                if userv== i.username:
                    if i.course_id_title in tno1:
                        nop += 1
            return render(request, "admin/index1.html", {"trueprofile": trueprofile,"nop":nop,"no":no,
                                                         "courses": courses, "course_picture": course_picture,
                                                         "userv": userv, "uc":uc
                                                         })

    else:
        return redirect("login")

def signout(request):
    logout(request)
    return redirect("index")


def add_courses(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            tok = request.POST.get("qq")
            return redirect("search_course2",tok)

        else:
            courses = All_Course.objects.all()
            uc = User_Course.objects.all()
            course_picture = 'CB/ourapp/static/assets/images/courses/pic.jpg'
            userv = request.user
            userv = str(userv)
            ctrace = []
            utrace= []

            no = 0
            tno1 = []
            for i in courses:
                tno1.append(i.identification_code)
                no += 1

            for i in uc:
                ctrace.append(i.course_id_title)
                utrace.append(i.username)
            print(ctrace,utrace)
            print(userv)

            from django.contrib.auth.models import User
            all_us = User.objects.all()
            save_email= None
            for i in all_us:
                if userv == i.username:
                    save_email=i.email

            return render(request, "admin/add-courses.html", {"trueprofile": trueprofile,"utrace":utrace,"ctrace":ctrace,
                                                                   "courses": courses, "course_picture": course_picture,
                                                                   "userv": userv,"no":no,"save_email":save_email})
    else:
        return redirect("index")


def course_action(request,id,us):
    if request.user.is_authenticated:
        try:
            User_Course.objects.create(username=us,course_id_title=id)
            return redirect("add-courses")
        except:
            return HttpResponse("Your course could not be added")

    else:
        return redirect("index")

def course_action2(request,id2):
    if request.user.is_authenticated:
        try:
            dlt= User_Course.objects.get(course_id_title=id2)
            print(dlt)
            dlt.delete()
            return redirect("my-dashboard")
        except:
            return HttpResponse("Your course could not be deleted")

    else:
        return redirect("index")


def course_action3(request,id3):
    if request.user.is_authenticated:
        try:
            dlt2= All_Course.objects.get(identification_code=id3)
            print(dlt2)
            dlt2.delete()
            return redirect("teachers-courses")
        except:
            return HttpResponse("Your course could not be deleted")

    else:
        return redirect("index")

def certificates(request):
    if request.user.is_authenticated:
        try:
            All_Cert= Certificate.objects.get(username=(str(request.user)))
            return render(request, "admin/certificates.html", {"trueprofile": trueprofile,
                                                "file":All_Cert.certificate_pdf.url,"ct":True,"name":All_Cert})
        except:
            return render(request, "admin/certificates.html", {"trueprofile": trueprofile,"ct":False})
    else:
        return redirect("index")


import mimetypes
from pathlib import Path
def ct_download(request):
    if request.user.is_authenticated:
        try:
            secr = Certificate.objects.get(username=(str(request.user)))
            filename = f"{secr}.pdf"
            BASE_DIR = Path(__file__).resolve().parent.parent
            filepath = BASE_DIR / "media/certificates"/ f"{secr.username}.pdf"
            path = open(filepath, "rb")
            mimetype, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mimetype)
            response["Content-Disposition"] = "attachment; filename=%s" % filename
            return response
        except:
            return HttpResponse("It's either you want to scam us or you have tampered with the Url path")

    else:
        return redirect("index")







#Teachers dashboard
def teachers_dashboard(request):
    if request.user.is_authenticated:
        cpl_st = []
        std_or_tch = Student.objects.all()
        for i in std_or_tch:
            cpl_st.append(i.username)
        if (str(request.user)) in cpl_st:
            return HttpResponse(
                "You are Not a Teacher, please click on the appropriate Login Button which is at the TOP in the Homepage")
        else:
            userc = All_Course.objects.all()
            userv=request.user
            userv=str(userv)
            no1 = User_Course.objects.all()
            tno1 = []
            for i in no1:
                tno1.append(i.course_id_title)

            no = 0
            nop = 0
            for i in userc:
                if userv == i.username:
                    nop += 1
                    if i.identification_code in tno1:
                        no += 1
            return render(request, "admin/teachers-dashboard.html", {"trueprofile": trueprofile,"id": request.user,
                                                                     "no":no,"nop":nop,})
    else:
        return redirect("index")





def teachers_add_courses(request):
    if request.user.is_authenticated:
        courseform = CourseForm()
        pdfform= Pdf_Form()
        videoform= Video_Form()
        if request.method == "POST":

            courseform = CourseForm(request.POST)
            pdfform = Pdf_Form(data=request.POST, files=request.FILES)
            videoform = Video_Form(data=request.POST, files=request.FILES)

            if courseform.is_valid() and pdfform.is_valid() and videoform.is_valid():
                user1 = courseform.cleaned_data["identification_code"]
                user11 = courseform.cleaned_data["title"]
                user111 = courseform.cleaned_data["description"]
                user1111 = courseform.cleaned_data["price"]
                user2 = pdfform.cleaned_data["pdf_file"]
                user3 = videoform.cleaned_data["video_file"]

                unm = str(request.user)
                from django.contrib.auth.models import User
                getUser = User.objects.get(username=unm)
                getEmail= getUser.email
                All_Course.objects.create(identification_code=user1,title=user11,username=getUser,
                                          description=user111,price=user1111,email=getEmail)

                user4 = All_Course.objects.get(identification_code=user1)

                user4.pdf_file.save(f"{user1}.pdf", user2)
                if user3 is not None:
                    user4.video_file.save(f"{user1}.mp4", user3)
                success= "The Course has been Uploaded successfully, It should now be in your dashboard"

                return render(request, "admin/teachers-add-courses.html",
                              {"trueprofile": trueprofile, "courseform": courseform,
                               "pdfform": pdfform, "videoform": videoform, "msg": True,"success":success})

        return render(request, "admin/teachers-add-courses.html", { "trueprofile": trueprofile,"courseform":courseform,
                             "pdfform":pdfform,"videoform":videoform,"msg":False})
    else:
        return redirect("index")

def teachers_courses(request):
    if request.user.is_authenticated:
        userc = All_Course.objects.all()
        course_picture =  'CB/ourapp/static/assets/images/courses/pic.jpg'
        userv=request.user
        userv=str(userv)
        return render(request, "admin/teachers-courses.html", {"trueprofile": trueprofile,
                                "userc":userc,"course_picture": course_picture,"userv":userv})
    else:
        return redirect("index")

def student_action(request,id4):
    if request.user.is_authenticated:
        try:
            dlt2= User_Course.objects.get(identification_code=id4)
            print(dlt2.size)
            return redirect("teachers-courses")
        except:
            return HttpResponse("Your course could not be deleted")

    else:
        return redirect("index")

def teachers_signout(request):
    logout(request)
    return redirect("index")



def search_course11(request,tok):
        try:
            if request.method=="POST":
                tok=request.POST.get("qq")
                cont = All_Course.objects.all()
                tok = tok.upper()
                try:
                    for i in cont:
                        toU=str(i.title)
                        if tok == toU.upper():
                            got = All_Course.objects.get(title=i.title)
                            return render(request, "search_course11.html", {"tok": tok, "got": got,"ck":True})
                    return render(request, "search_course11.html", {"tok": tok, "cont": cont, "ck": False})
                except:
                    return render(request, "search_course11.html", {"tok": tok, "cont": cont, "ck": False})
            else:
                cont=All_Course.objects.all()
                tok = tok.upper()
                try:
                    for i in cont:
                        toU = str(i.title)
                        if tok == toU.upper():
                            got = All_Course.objects.get(title=i.title)
                            return render(request, "search_course11.html", {"tok": tok, "got": got, "ck": True})
                    return render(request, "search_course11.html", {"tok": tok, "cont": cont,"ck":False})
                except:
                    return render(request, "search_course11.html", {"tok": tok, "cont": cont,"ck":False})
        except:
            try:
                tok=None
                return render(request, "search_course11.html", {"tok": tok, "cont": cont, "ck": False})
            except:
                return HttpResponse("Your Search input is Empty")



def search_course1(request,tok):
    try:
        if request.method=="POST":
            tok=request.POST.get("qq")
            cont = All_Course.objects.all()
            tok = tok.upper()
            try:
                for i in cont:
                    toU=str(i.title)
                    if tok == toU.upper():
                        got = All_Course.objects.get(title=i.title)
                        return render(request, "search_course.html", {"tok": tok, "got": got,"ck":True})
                return render(request, "search_course.html", {"tok": tok, "cont": cont, "ck": False})
            except:
                return render(request, "search_course.html", {"tok": tok, "cont": cont, "ck": False})
        else:
            cont=All_Course.objects.all()
            tok = tok.upper()
            try:
                for i in cont:
                    toU = str(i.title)
                    if tok == toU.upper():
                        got = All_Course.objects.get(title=i.title)
                        return render(request, "search_course.html", {"tok": tok, "got": got, "ck": True})
                return render(request, "search_course.html", {"tok": tok, "cont": cont,"ck":False})
            except:
                return render(request, "search_course.html", {"tok": tok, "cont": cont,"ck":False})
    except:
        try:
            tok=None
            return render(request, "search_course.html", {"tok": tok, "cont": cont, "ck": False})
        except:
            return redirect("index")



def search_course2(request,tok):
    try:
        if request.user.is_authenticated:
            try:
                courses = All_Course.objects.all()
                uc = User_Course.objects.all()
                course_picture = 'CB/ourapp/static/assets/images/courses/pic.jpg'
                userv = request.user
                userv = str(userv)
                ctrace = []
                utrace= []

                no = 0
                tno1 = []
                for i in courses:
                    tno1.append(i.identification_code)
                    no += 1

                for i in uc:
                    ctrace.append(i.course_id_title)
                    utrace.append(i.username)
                print(ctrace,utrace)
                print(userv)

                from django.contrib.auth.models import User
                all_us = User.objects.all()
                save_email= None
                for i in all_us:
                    if userv == i.username:
                        save_email=i.email

                check_UC=User_Course.objects.all()
                save_CUH=[]
                for i in check_UC:
                    save_CUH.append(i.course_id_title)
                if request.method == "POST":
                    tok = request.POST.get("qq")
                    cont = All_Course.objects.all()
                    tok = tok.upper()
                    try:
                        print("Trial: ",tok)
                        for i in cont:
                            toU = str(i.title)
                            if tok == toU.upper():
                                got = All_Course.objects.get(title=i.title)
                                return render(request, "admin/search_course2.html", {"tok": tok, "got": got, "ck": True,
                                                                                     "trueprofile": trueprofile,
                                                                                     "utrace": utrace, "ctrace": ctrace,
                                                                                     "courses": courses,
                                                                                     "course_picture": course_picture,
                                                                                     "userv": userv, "no": no,
                                                                                     "save_email": save_email,"save_CUH":save_CUH
                                                                                     })
                        return render(request, "admin/search_course2.html", {"tok": tok, "cont": cont, "ck": False,"save_CUH":save_CUH})
                    except:
                        print("Except: ",tok)
                        return render(request, "admin/search_course2.html", {"tok": tok, "cont": cont, "ck": False,"save_CUH":save_CUH})
                else:
                    cont = All_Course.objects.all()
                    tok = tok.upper()
                    try:
                        for i in cont:
                            toU = str(i.title)
                            if tok == toU.upper():
                                got = All_Course.objects.get(title=i.title)
                                return render(request, "admin/search_course2.html", {"tok": tok, "got": got, "ck": True,
                                                                                     "trueprofile": trueprofile,
                                                                                     "utrace": utrace, "ctrace": ctrace,
                                                                                     "courses": courses,
                                                                                     "course_picture": course_picture,
                                                                                     "userv": userv, "no": no,
                                                                                     "save_email": save_email,"save_CUH":save_CUH
                                                                                     })
                        return render(request, "admin/search_course2.html", {"tok": tok, "cont": cont, "ck": False,"save_CUH":save_CUH})
                    except:
                        return render(request, "admin/search_course2.html", {"tok": tok, "cont": cont, "ck": False,"save_CUH":save_CUH})
            except:
                try:
                    tok = None
                    return render(request, "admin/search_course2.html", {"tok": tok, "cont": cont, "ck": False,"save_CUH":save_CUH})
                except:
                    return HttpResponse("Your Search input is Empty")
        else:
            return redirect("index")
    except:
        return HttpResponse("Your Search input is Empty")




def search_course3(request,tok):
    try:
        if request.user.is_authenticated:
            try:
                courses = All_Course.objects.all()
                uc = User_Course.objects.all()
                course_picture = 'CB/ourapp/static/assets/images/courses/pic.jpg'
                userv = request.user
                userv = str(userv)
                ctrace = []
                utrace= []

                no = 0
                tno1 = []
                for i in courses:
                    tno1.append(i.identification_code)
                    no += 1

                for i in uc:
                    ctrace.append(i.course_id_title)
                    utrace.append(i.username)


                print(ctrace,utrace)
                print(userv)

                from django.contrib.auth.models import User
                all_us = User.objects.all()
                save_email= None
                for i in all_us:
                    if userv == i.username:
                        save_email=i.email
                        break

                if request.method == "POST":
                    tok = request.POST.get("qq")
                    tok = tok.upper()
                    cont = All_Course.objects.all()
                    pamb = User_Course.objects.all()
                    cpamb = []
                    for i in pamb:
                        cpamb.append(i.course_id_title)
                    try:
                        for i in cont:
                            toU = str(i.title)
                            if tok == toU.upper():
                                if i.identification_code in cpamb:
                                    got = All_Course.objects.get(title=i.title)
                                    if i.identification_code in ctrace:
                                        trace=i.identification_code
                                    return render(request, "admin/search_course3.html", {"tok": tok, "got": got, "ck": True,
                                                                                         "trueprofile": trueprofile,
                                                                                         "utrace": utrace, "ctrace": ctrace,
                                                                                         "courses": courses,"trace":trace,
                                                                                         "course_picture": course_picture,
                                                                                         "userv": userv, "no": no,
                                                                                         "save_email": save_email
                                                                                         })
                        return render(request, "admin/search_course3.html", {"tok": tok, "cont": cont, "ck": False})
                    except:
                        print("Except: ",tok)
                        return render(request, "admin/search_course3.html", {"tok": tok, "cont": cont, "ck": False})
                else:
                    cont = All_Course.objects.all()
                    tok = tok.upper()
                    pamb= User_Course.objects.all()
                    cpamb= []
                    for i in pamb:
                        cpamb.append(i.course_id_title)
                    try:
                        for i in cont:
                            toU = str(i.title)
                            if tok == toU.upper():
                                if i.identification_code in cpamb:
                                    got = All_Course.objects.get(title=i.title)
                                    if i.identification_code in ctrace:
                                        trace=i.identification_code
                                    return render(request, "admin/search_course3.html", {"tok": tok, "got": got, "ck": True,
                                                                                         "trueprofile": trueprofile,
                                                                                         "utrace": utrace, "ctrace": ctrace,
                                                                                         "courses": courses,"trace":trace,
                                                                                         "course_picture": course_picture,
                                                                                         "userv": userv, "no": no,
                                                                                         "save_email": save_email
                                                                                         })
                        return render(request, "admin/search_course3.html", {"tok": tok, "cont": cont, "ck": False})
                    except:
                        return render(request, "admin/search_course3.html", {"tok": tok, "cont": cont, "ck": False})
            except:
                try:
                    tok = None
                    return render(request, "admin/search_course3.html", {"tok": tok, "cont": cont, "ck": False})
                except:
                    return HttpResponse("Your Search input is Empty")
        else:
            return redirect("search_course3")
    except:
        return HttpResponse("Your Search input is Empty")




import os
import mimetypes
from pathlib import Path
def download(request,title, id):
    try:
        if request.user.is_authenticated:
            secr=User_Course.objects.all()
            for i in secr:
                if (str(request.user))== i.username:
                    if id== i.course_id_title:
                        filename = f"{title}.pdf"
                        print(title)
                        BASE_DIR = Path(__file__).resolve().parent.parent
                        filepath=BASE_DIR / "media/pdf" / f"{id}.pdf"
                        #filepath = "C:/Users/PAPIC/P1/uploads/Songs/" + filename
                        path = open(filepath, "rb")
                        mimetype, _ = mimetypes.guess_type(filepath)
                        response = HttpResponse(path, content_type=mimetype)
                        response["Content-Disposition"] = "attachment; filename=%s" % filename
                        return response
                    return HttpResponse("It's either you want to scam us or you have tampered with the Url path")
                return HttpResponse("It's either you want to scam us or you are not logged currently logged in")
        else:
            return redirect("index")
    except:
        return HttpResponse("Could Not Download")

def download2(request,title, id):
    try:
        if request.user.is_authenticated:
            secr = User_Course.objects.all()
            for i in secr:
                if (str(request.user)) == i.username:
                    if id == i.course_id_title:
                        filename = f"{title}.mp4"
                        print(title)
                        BASE_DIR = Path(__file__).resolve().parent.parent
                        filepath = BASE_DIR / "media/video" / f"{id}.mp4"
                        # filepath = "C:/Users/PAPIC/P1/uploads/Songs/" + filename
                        path = open(filepath, "rb")
                        mimetype, _ = mimetypes.guess_type(filepath)
                        response = HttpResponse(path, content_type=mimetype)
                        response["Content-Disposition"] = "attachment; filename=%s" % filename
                        return response
                    return HttpResponse("It's either you want to scam us or you have tampered with the Url path")
                return HttpResponse("It's either you want to scam us or you are not logged currently logged in")
        else:
            return redirect("index")
    except:
        return HttpResponse("Could not dowmload")










from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . import forms
from django.conf import settings
from .models import Payment
from django.contrib import messages


def initiate_payment(request: HttpResponse, id) -> HttpResponse:
    try:
        if request.user.is_authenticated:
            c_values=All_Course.objects.get(identification_code=id)
            c_values_amount=c_values.price
            from django.contrib.auth.models import User
            userv=request.user
            userv=str(userv)
            all_us = User.objects.all()
            save_email=""
            for i in all_us:
                if userv == i.username:
                    save_email = i.email
            amt= int(c_values_amount)
            Payment.objects.create(amount=amt,email=save_email)
            pay= Payment.objects.first()
            return render(request, "paystack/make_payment.html", {"amount": amt ,"email":save_email,"id":id,"us":userv,"payment":pay,
                         "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY})
        else:
            return redirect("index")
    except:
        return HttpResponse("Payment could not be initiated")


def verify_payment(request: HttpRequest, ref: str,id,us) -> HttpResponse: #the hypen and greater than means return
    try:
        if request.user.is_authenticated:
            payment= get_object_or_404(Payment, ref=ref)
            verified= payment.verify_payment()
            if verified:
                messages.success(request, "Verification Successfull")
            else:
                messages.error(request, "Verification Failed.")
            return redirect("course-action",id=id,us=us)
        else:
            return redirect("index")
    except:
        return HttpResponse("Payment Failed")