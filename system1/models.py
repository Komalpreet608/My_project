from django.db import models



# Create your models here.
class KStudent2(models.Model):
      userid=models.CharField(max_length=50)
      password=models.CharField(max_length=50)
      op=models.CharField(max_length=50)
      
class AddU2(models.Model):
     
      userid=models.CharField(max_length=50)
      password=models.CharField(max_length=50)
      fn=models.CharField(max_length=50)
      ln=models.CharField(max_length=50)
      rno=models.CharField(max_length=50)
      email=models.EmailField(max_length=50)
      br=models.CharField(max_length=50)
      batch=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      DD=models.CharField(max_length=50)
      class Meta:
           db_table = "AddU2"

           

class Assgin2(models.Model):
      sub=models.CharField(max_length=50)
      dd=models.CharField(max_length=50)
      title=models.CharField(max_length=50)
      stream=models.CharField(max_length=50)
      des=models.CharField(max_length=50)
      picture= models.FileField(upload_to = 'pdf')
      class Meta:
         db_table = "Assgin2"

class Notes(models.Model):
      sub=models.CharField(max_length=50)
      title=models.CharField(max_length=50)
      stream=models.CharField(max_length=50)
      des=models.CharField(max_length=50)
      picture= models.FileField(upload_to = 'pdf')
      class Meta:
         db_table = "Notes"

class Profile1(models.Model):
      name=models.CharField(max_length=150)
      #des=models.CharField(max_length=50)
      picture= models.FileField(upload_to = 'gallery')
      class Meta:
         db_table = "Profile1"

class TeacherA(models.Model):
      userid=models.CharField(max_length=50)
      password=models.CharField(max_length=50)
      fn=models.CharField(max_length=50)
      ln=models.CharField(max_length=50)
      ph=models.CharField(max_length=50)
      email=models.EmailField(max_length=50)
      gen=models.CharField(max_length=50)

class Subject1(models.Model):
      code=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)

class Mst1(models.Model):
      rno=models.CharField(max_length=50)
      ex=models.CharField(max_length=50)
      br=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)
      max=models.CharField(max_length=50)
      mo= models.CharField(max_length=50)
      class Meta:
         db_table = "Mst1"

class Mst2(models.Model):
      rno=models.CharField(max_length=50)
      ex=models.CharField(max_length=50)
      br=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)
      max=models.CharField(max_length=50)
      mo= models.CharField(max_length=50)
      class Meta:
         db_table = "Mst2"

class Attend1(models.Model):
      br=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      sub=models.CharField(max_length=100)
      userid=models.CharField(max_length=50)
      class Meta:
         db_table = "Attend1"

class EditA(models.Model):
      rno=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)
      Alec=models.CharField(max_length=50)
      Dlec=models.CharField(max_length=50)
      per=models.CharField(max_length=50)
      dd=models.CharField(max_length=50)
      
      class Meta:
         db_table = "EditA"

class Compbox(models.Model):
      com=models.CharField(max_length=60)
      co=models.CharField(max_length=250)
        
      class Meta:
         db_table = "Compbox"

class Contactus(models.Model):
      na=models.CharField(max_length=50)
      mail=models.EmailField(max_length=50)
      message=models.CharField(max_length=200)
        
      class Meta:
         db_table = "Contactus"

class Time(models.Model):
      name=models.CharField(max_length=50)
      userid=models.CharField(max_length=50)
      picture= models.FileField(upload_to = 'gallery')
      
        
      class Meta:
         db_table = "Time"

class eventdetails(models.Model):
     
      picture= models.FileField(upload_to = 'pdf')
     
       
      class Meta:
         db_table = "eventdetails"


class STime(models.Model):
      br=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      picture= models.FileField(upload_to = 'gallery')
      
        
      class Meta:
         db_table = "STime"

class Notice1(models.Model):
       picture= models.FileField(upload_to = 'gallery')
     
       class Meta:
         db_table = "Notice1"

class RegisterU2(models.Model):
     
     
      password=models.CharField(max_length=50)
      fn=models.CharField(max_length=50)
      ln=models.CharField(max_length=50)
      fathern=models.CharField(max_length=50)
      collegename=models.CharField(max_length=50)
      mno=models.CharField(max_length=50)
      gender=models.CharField(max_length=50)
      email=models.EmailField(max_length=50)
      br=models.CharField(max_length=50)
      eventcategory=models.CharField(max_length=50)
      eventname=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      DD=models.CharField(max_length=50)
      class Meta:
           db_table = "RegisterU2"

class marks1(models.Model):

      rno=models.CharField(max_length=50)
      ex=models.CharField(max_length=50)
      br=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)
      max=models.CharField(max_length=50)
      mo= models.CharField(max_length=50)
      class Meta:
         db_table = "marks1"

class marks2(models.Model):

      rno=models.CharField(max_length=50)
      ex=models.CharField(max_length=50)
      br=models.CharField(max_length=50)
      sem=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)
      max=models.CharField(max_length=50)
      mo= models.CharField(max_length=50)
      class Meta:
         db_table = "marks2"

class Internal(models.Model):
      rno=models.CharField(max_length=50)
      sub=models.CharField(max_length=50)
      mst1=models.CharField(max_length=50)
      mst2= models.CharField(max_length=50)
      assgin1=models.CharField(max_length=50)
      assgin2= models.CharField(max_length=50)
      attend= models.CharField(max_length=50)
      internal= models.CharField(max_length=50)
      class Meta:
         db_table = "Internal"






   
      
      
      
      
