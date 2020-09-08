from django import forms  
from system1.models import *

class AddForm(forms.ModelForm):  
    class Meta:  
        model = AddU2  
        fields = "__all__"

class StimeForm(forms.ModelForm):  
    class Meta:  
        model = STime  
        fields = "__all__"

class AttendForm(forms.ModelForm):  
    class Meta:  
        model = Attend1
        fields = "__all__"

class Marks1Form(forms.ModelForm):  
    class Meta:  
        model = marks1  
        fields = "__all__"

class Marks2Form(forms.ModelForm):  
    class Meta:  
        model = marks2
        fields = "__all__"

class TeachForm(forms.ModelForm):  
    class Meta:  
        model = TeacherA  
        fields = "__all__"

class TimeForm(forms.ModelForm):  
    class Meta:  
        model = Time  
        fields = "__all__"


class ChangeForm(forms.ModelForm):  
    class Meta:  
        model = KStudent2  
        fields = "__all__"

class ProfileForm(forms.ModelForm):  
    class Meta:  
        model = Profile1 
        fields = "__all__"

class ProForm(forms.Form):
      sub = forms.CharField(max_length = 100)
      dd=forms.CharField(max_length=50)
      title=forms.CharField(max_length=50)
      stream=forms.CharField(max_length=50)
      des=forms.CharField(max_length=50)
      picture=forms.FileField()

class EventForm(forms.ModelForm):
      class Meta:  
        model = eventdetails  
        fields = "__all__"


class MstForm(forms.ModelForm):  
    class Meta:  
        model = Mst1  
        fields = "__all__"

class InternalForm(forms.ModelForm):  
    class Meta:  
        model = Internal  
        fields = "__all__"


class MstForm2(forms.ModelForm):  
    class Meta:  
        model = Mst2  
        fields = "__all__"

class NoticeForm(forms.ModelForm):  
    class Meta:  
        model = Notice1  
        fields = "__all__"

class ForForm(forms.Form):
      email = forms.EmailField(max_length = 100)

class NotesForm(forms.ModelForm):
      class Meta:  
        model = Notes  
        fields = "__all__"

  
   
    