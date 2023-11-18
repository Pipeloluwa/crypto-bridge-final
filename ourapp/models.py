from django.db import models


# Create your models here.
class Certificate(models.Model):
    username= models.CharField(max_length=100,unique=True)
    certificate_pdf= models.FileField(upload_to="certificates")


class Success_Storie(models.Model):
    stories=models.TextField(max_length=500)


class Student(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email= models.EmailField()


    def __str__(self):
        return f"{self.username}-{self.email}"

class Teacher(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email= models.EmailField()

    def __str__(self):
        return f"{self.username}-{self.email}"

class All_Course(models.Model):
    username = models.CharField(max_length=100)
    email= models.EmailField()
    identification_code= models.CharField(max_length=30,unique=True)
    title= models.CharField(max_length=30)
    description= models.TextField(max_length=300)
    price= models.PositiveIntegerField()
    pdf_file= models.FileField(upload_to="pdf")
    video_file= models.FileField(upload_to="video",blank=True, null=True)

    def __str__(self):
        return f"{self.username}-{self.email}-{self.title}-{self.description}-{self.pdf_file}-{self.video_file}"

class User_Course(models.Model):
    username = models.CharField(max_length=100)
    course_id_title= models.CharField(max_length=30)

    def __str__(self):
        return f"{self.course_id_title}"

class Message(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField(max_length=150)
    phone= models.CharField(max_length=150)
    subject= models.CharField(max_length=150)
    message= models.TextField(max_length=700)

    def __str__(self):
        return f"{self.name}-{self.email}-{self.phone}-{self.subject}-{self.message}"

class Popular_Course(models.Model):
    title= models.CharField(max_length=71,unique=True)
    description= models.TextField(max_length=500)

    def __str__(self):
        return f"{self.title}-{self.description}"








import secrets
from django.db import models
from .paystack import PayStack



class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)


    def __str__(self) -> str:
        # return f"Payment: {self.amount}"
        return f"{self.email} - {self.amount} - {self.ref} - {self.date_created}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)  # secrets model is used to generate a safe api key
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
                print("This is the original ref: ",self.ref)
        super().save(*args, **kwargs)


    def amount_value(self) -> int:  # a work around for a decimal part in amount
        return self.amount * 100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False