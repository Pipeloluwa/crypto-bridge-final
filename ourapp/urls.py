from django.urls import path
from django import urls
from . import views

urlpatterns= [
    path("crypto-bridge/", views.index, name="index"),
    path("crypto-bridge/login", views.loginPage, name="login"),
    path("crypto-bridge/register", views.register, name="register"),
    path("crypto-bridge/courses", views.courses, name="courses"),
    path("crypto-bridge/courses/next-page", views.npage, name="npage"),
    path("crypto-bridge/courses/previous-page", views.ppage, name="ppage"),

    path("crypto-bridge/about", views.about, name="about"),
    path("crypto-bridge/contact", views.contact, name="contact"),
    path("crypto-bridge/success-stories", views.testimony, name="testimony"),
    path("crypto-bridge/teachers-login", views.teachers_login, name="teachers-login"),
    #Dashboard
    path("crypto-bridge/my-dashboard", views.my_dashboard, name="my-dashboard"),

    path("crypto-bridge/certificates", views.certificates, name="certificates"),
    path("crypto-bridge/certificates/download", views.ct_download, name="ct_download"),

    path("crypto-bridge/add-courses", views.add_courses, name="add-courses"),
    path("crypto-bridge/signout", views.signout, name="signout"),

    #Teachersdashboard
    path("crypto-bridge/teachers-dashboard", views.teachers_dashboard, name="teachers-dashboard"),
    path("crypto-bridge/teachers-courses", views.teachers_courses, name="teachers-courses"),
    path("crypto-bridge/teachers-add-courses>", views.teachers_add_courses, name="teachers-add-courses"),
    path("crypto-bridge/teachers-signout", views.teachers_signout, name="teachers-signout"),

    path("crypto-bridge/add/<str:id>/<str:us>", views.course_action, name="course-action"),
    path("crypto-bridge/delete/<str:id2>", views.course_action2, name="course-action2"),
    path("crypto-bridge/teacher-delete/<str:id3>", views.course_action3, name="course-action3"),

    path("crypto-bridge/search-course1/<str:tok>", views.search_course1, name="search_course1"),
    path("crypto-bridge/search-course11/<str:tok>", views.search_course11, name="search_course11"),
    path("crypto-bridge/search-course2/<str:tok>", views.search_course2, name="search_course2"),
    path("crypto-bridge/search-course3/<str:tok>", views.search_course3, name="search_course3"),
    path("crypto-bridge/search-course4/<str:tok>", views.search_course4, name="search_course4"),


    path("crypto-bridge/download-link/<str:title>/<str:id>", views.download, name="download"),
    path("crypto-bridge/download-link2/<str:title>/<str:id>", views.download2, name="download2"),


    path("crypto-bridge/make-payment/<str:id>",views.initiate_payment, name="initiate-payment"),
    path("crypto-bridge/<str:ref>/<str:id>/<str:us>", views.verify_payment, name="verify-payment"),
]


