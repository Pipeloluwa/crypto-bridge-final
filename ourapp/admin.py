from django.contrib import admin

# Register your models here.
from .models import Student,Teacher,All_Course,User_Course,Message,Popular_Course,Certificate,Success_Storie

class us(admin.ModelAdmin):
    list_display = ("username", "email",)
    list_filter = ("username",)


class tc(admin.ModelAdmin):
    list_display = ("username", "email",)
    list_filter = ("username",)

class tc2(admin.ModelAdmin):
    list_display = ("identification_code","username", "email","title","description","price","pdf_file","video_file")
    list_filter = ("username",)

class tc3(admin.ModelAdmin):
    list_display = ("username", "course_id_title",)
    list_filter = ("username",)

class tc4(admin.ModelAdmin):
    list_display = ("name","email","phone","subject","message")
    list_filter = ("name",)

class tc5(admin.ModelAdmin):
    list_display = ("title","description",)


class tc6(admin.ModelAdmin):
    list_display = ("username","certificate_pdf",)


class tc7(admin.ModelAdmin):
    list_display = ("stories",)


admin.site.register(Student,us)
admin.site.register(Teacher,tc)
admin.site.register(All_Course,tc2)
admin.site.register(User_Course,tc3)
admin.site.register(Message,tc4)
admin.site.register(Popular_Course,tc5)
admin.site.register(Certificate,tc6)
admin.site.register(Success_Storie,tc7)



from .models import Payment

# Register your models here.

class show(admin.ModelAdmin):
     list_display=("verified","email","amount","ref","date_created",)
     list_filter=("email",)

admin.site.register(Payment, show)