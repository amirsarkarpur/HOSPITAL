from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class doctor (models.Model):

    CHOICES = [
        ('single', ' single'),
        ('married', ' married'),
    ]

    CHOICES2 = [
        ('man', ' man'),
        ('woman', ' woman'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="",max_length=50,null=False,blank=False)
    last_name = models.CharField(default="",max_length=50,null=False,blank=False)
    full_name = models.CharField(default="",max_length=50,null=False,blank=False)
    Medical_license_number = models.CharField(default="",max_length=5,null=False,blank=False)
    Expertise = models.CharField(default="",max_length=50,null=False,blank=False)
    phone_number = models.CharField(default="",max_length=11,null=False,blank=False)
    marital_status = models.CharField(default="",max_length=20, choices=CHOICES,null=False,blank=False)
    gender = models.CharField(default="",max_length=20, choices=CHOICES2,null=False,blank=False)
    def __str__(self) :
        return self.full_name



  


class Patient (models.Model):

    CHOICES = [
        ('single', ' single'),
        ('married', ' married'),
    ]

    CHOICES2 = [
        ('man', ' man'),
        ('woman', ' woman'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="",max_length=50,null=False,blank=False)
    last_name = models.CharField(default="",max_length=50,null=False,blank=False)
    full_name = models.CharField(default="",max_length=50,null=False,blank=False)
    National_code = models.CharField(default="",max_length=10,null=False,blank=False)
    underlying_disease = models.CharField(default="",max_length=50,null=False,blank=False)
    phone_number = models.CharField(default="",max_length=11,null=False,blank=False)
    marital_status = models.CharField(default="",max_length=20, choices=CHOICES,null=False,blank=False)
    gender = models.CharField(default="",max_length=20, choices=CHOICES2,null=False,blank=False)
    
    def __str__(self) :
        return self.full_name
    


class Medication (models.Model):

    CHOICES = [
    ('pill', ' pill'),
    ('Sherbet', ' Sherbet'),
    ('serum', ' serum'),
    ('ampoule', ' ampoule'),
    ('powder', ' powder'),
    ]


    name = models.CharField(default="",max_length=50,null=False,blank=False)
    description = models.TextField(default="",max_length=50,null=False,blank=False)
    Complications = models.TextField(default="",max_length=50,null=False,blank=False)
    How_to_use = models.CharField(default="",max_length=50,null=False,blank=False)
    expiration_date = models.DateTimeField ()
    Production_date = models.DateTimeField ()
    number = models.IntegerField()
    Medication_type = models.CharField(default="",max_length=20, choices=CHOICES,null=False,blank=False)


    def __str__(self):
        return self.name
    



class Prescription(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    upload = models.DateField(auto_now_add=True)
    type_of_disease = models.CharField(max_length=50)

    def __str__(self):
        return f"Patient: {self.patient}, Doctor: {self.doctor}, Disease: {self.type_of_disease}"


class AddPrescription(models.Model):
    medication = models.ForeignKey('Medication', on_delete=models.CASCADE)
    description = models.TextField()
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.medication)
    



class Appointment(models.Model):
    Doctor = models.ForeignKey('doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    time = models.CharField(max_length=30,default="",blank=False,null=False)
    disease = models.CharField(max_length=30,default="",blank=False,null=False)
    descriptien = models.CharField(max_length=30,default="",blank=False,null=False)
    status = models.BooleanField(default=False)
    end = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient: {self.patient}, Doctor: {self.Doctor}, time: {self.time}"
        


class superuser(models.Model):
    CHOICES = [
        ('single', ' single'),
        ('married', ' married'),
    ]

    CHOICES2 = [
        ('man', ' man'),
        ('woman', ' woman'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="",max_length=50,null=False,blank=False)
    last_name = models.CharField(default="",max_length=50,null=False,blank=False)
    full_name = models.CharField(default="",max_length=50,null=False,blank=False)
    Medical_license_number = models.CharField(default="",max_length=5,null=False,blank=False)
    Expertise = models.CharField(default="",max_length=50,null=False,blank=False)
    phone_number = models.CharField(default="",max_length=11,null=False,blank=False)
    marital_status = models.CharField(default="",max_length=20, choices=CHOICES,null=False,blank=False)
    gender = models.CharField(default="",max_length=20, choices=CHOICES2,null=False,blank=False)

    def __str__(self) :
        return self.full_name