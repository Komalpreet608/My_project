from django.shortcuts import render,redirect  
import datetime 

from django.http import HttpRequest
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.template import RequestContext

from django.core.mail import EmailMessage

from django.views.decorators.csrf import csrf_exempt
from system1.forms import *
#from models  import *
from system1.models import *





# Create your views here.
def home(request):
    return render(request,"system1/index.html")
def UploadG(request):
    return render(request,"system1/UploadG.html")

def about(request):
    return render(request,"system1/about.html")
def civil(request):
    return render(request,"system1/civil.html")
def detcse(request):
    return render(request,"system1/detcse.html")
def ece(request):
    return render(request,"system1/ece.html")
def me(request):
    return render(request,"system1/me.html")
def admin(request):
    return render(request,"system1/admin.html")
        
def forget(request):
    
    return render(request,"system1/forget.html")
def user(request):
    return render(request,"system1/user.html")

def Teacher(request):
    return render(request,"system1/Teacher.html")
   
def login1(request):
    return render(request,"system1/login.html")



@csrf_exempt
def login(request):
    
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        userid = request.POST.get('userid')
        request.session['myuser'] =userid
                  
        password = request.POST.get('password')
        op = request.POST.get('op')
        
     
     
        
            #adding the values in a context variable 
        '''context = {
            'userid': userid,
            'password': password
            
        }'''
        #getting our showdata template
  
        #data = Student.objects.all().values()
        
        #student_dict = {'students': data}
          
        #template = loader.get_template('app/showdata.html');
        
        if KStudent2.objects.filter(userid=userid,password=password).exists():    
                # message='Logged in successfully.'  
                #return render(request,"system/login.html",{'message':message})
                #return render(request,"system1/admin.html")
                template = loader.get_template('system1/admin.html')
                return HttpResponse(template.render())


        
        # elif op=='Student':
        elif AddU2.objects.filter(userid=userid,password=password).exists(): 
                # message="not record found"  
                #return render(request,"system1/Teacher.html",)
                username=request.session['myuser'];
                template = loader.get_template('system1/user.html')
                return HttpResponse(template.render())

        #elif op=='Teacher':
        elif TeacherA.objects.filter(userid=userid,password=password).exists(): 
                       
                # message="not record found"  
                #return render(request,"system1/Teacher.html",)
                         username=request.session['myuser'];               
                         #template = loader.get_template('system1/Teacher.html')
                         #return HttpResponse(template.render())
                         return render(request, 'system1/Teacher.html',{"username" : username})

                        
        else:
               message='Incorrect Password'  
               return render(request,"system1/login.html",{'message':message})
               #return render(request,"system1/login.html")
         

                #au=MStudent()
                #au.userid= userid
                #au.password= password
                #au.save()
                #students = MStudent.objects.all()
                #template = loader.get_template('system/login.html')
                #context = {'students': students}
                #output = template.render(context)
                #return HttpResponse(output)
       

        #returing the template 
        #return HttpResponse(template.render(context, request))
        #context = RequestContext(request)
        #return render_to_response('app/showdata.html', student_dict, context)
    else:
    
        #if post request is not true 
        #returing the form template 
        #template = loader.get_template('system1/login.html')
        #return HttpResponse(template.render())
        return render(request,"system1/login.html")
@csrf_exempt
def adduser1(request):
        #if post request came 
    if request.method == 'POST':
        #getting values from post
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        fn = request.POST.get('fn')
        rno = request.POST.get('rno')
        ln= request.POST.get('ln')
        email = request.POST.get('email')
        br= request.POST.get('hbr')
        batch = request.POST.get('batch')
        sem= request.POST.get('sem')
        DD= request.POST.get('DD')
        
        
        
        
     
        
            #adding the values in a context variable 
        context = {
            'userid': userid,
            'password': password,
            'fn':fn,
            'ln': ln,
            'rno': rno,
            'email':email,
            'sem': sem,
            'DD':DD,
            'br':br,
            'batch':batch
            
            
        }
        #getting our showdata template
  
        #data = MStudent.objects.all().values()
        
        #student_dict = {'students': data}
          
        #template = loader.get_template('app/showdata.html');
        
        '''au=MStudent()
        au.userid= userid
        au.password= password
        au.save()
        students = Student.objects.all()
        
        template = loader.get_template('system/showdata.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)'''
       
        
       
        rno= request.POST.get('rno')
        if AddU2.objects.filter(rno=rno).exists():    
                     #messages.add_message(request, messages.SUCCESS, 'Record already exist!')
                     message='Record already exist.'
                     return render(request,"system1/adduser.html",{'message':message})
         
         #if MStudent.objects.filter(rno=rno).exists():
                  #message="not record found"  
                  #return render(request,"app/showdata.html",{'message':message})
                   
                         
                        
        
                #message='Incorrect Password'  
                #return render(request,"system/login.html",{'message':message})
         
        else:
            au=AddU2()
            au.userid= userid
            au.password= password
            au.rno= rno
            au.ln= ln
            au.fn= fn
            au.sem= sem
            au.batch= batch
            au.DD= DD
            au.br= br
            au.email= email      
            au.save()
            message='Record Successfully Added!.'
            return render(request,"system1/adduser.html",{'message':message})
         
            #students = AddU2.objects.all()
            
            #template = loader.get_template('system1/adduser.html')
            #context = {'students': students}
            #output = template.render(context)
            #return HttpResponse(output)
       

        #returing the template 
        #return HttpResponse(template.render(context, request))
        #context = RequestContext(request)
        #return render_to_response('app/showdata.html', student_dict, context)
    else:
    
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('system1/adduser.html')
        return HttpResponse(template.render())

@csrf_exempt
def edit(request, rno):
        students = AddU2.objects.get(rno=rno) 
        return render(request,"system1/update.html",{'Useradd':students})
        
        #template = loader.get_template('system/update.html',)
  
@csrf_exempt
def update(request, rno):
    
    Useradd = AddU2.objects.get(rno=rno)   
    form = AddForm(request.POST, instance=Useradd)  
    if form.is_valid():  
        form.save()  
        students = AddU2.objects.all()
        template = loader.get_template('system1/userinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)  

    return render(request, 'system1/update.html', {'Useradd': Useradd})  
@csrf_exempt
def DeleteU(request):
         
        if request.method == 'POST':
        
                #addu = AddU.objects.all()
                abc = int(request.POST.get('abc'))  
                item = AddU2.objects.get(rno=abc)       
                item.delete()
                students = AddU2.objects.all()
                template = loader.get_template('system1/userinfo.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
                #return redirect("/userinfo")
                '''instance = AddU.objects.get(rno=id)
                instance.delete()'''
        else:  
              template = loader.get_template('system1/userinfo.html')
              return HttpResponse(template.render())

def userinfo(request):
        students = AddU2.objects.all()
        template = loader.get_template('system1/userinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)
@csrf_exempt
def addteach(request):
    if request.method == 'POST':
        #getting values from post
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        fn = request.POST.get('fn')
        ph = request.POST.get('ph')
        ln= request.POST.get('ln')
       
        
        email = request.POST.get('email')
        gen= request.POST.get('gen')
        
  
        context = {
            'userid': userid,
            'password': password,
            'fn':fn,
            'ln': ln,
            'ph': ph,
            'email':email,
            'gen':gen 
            
        }
       
        userid= request.POST.get('userid')
        if TeacherA.objects.filter(userid=userid).exists():    
                     message='Record already exist.'  
                     return render(request,"system1/addteach.html",{'message':message})
         
         
        else:
            au=TeacherA()
            au.userid= userid
            au.password= password
            au.ph= ph
            au.ln= ln
            au.fn= fn
            au.gen= gen
            au.email= email      
            au.save()
            #students = TeacherA.objects.all()
            
            #template = loader.get_template('system1/addteach.html')
            #context = {'students': students}
            #output = template.render(context)
            #return HttpResponse(output)
            message='Record Successfully Added!.'
            return render(request,"system1/addteach.html",{'message':message})
         

        #returing the template 
        #return HttpResponse(template.render(context, request))
        #context = RequestContext(request)
        #return render_to_response('app/showdata.html', student_dict, context)
    else:
    
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('system1/addteach.html')
        return HttpResponse(template.render())

        
    
    return render(request,"system1/addteach.html")

@csrf_exempt
def edit1(request, userid):
        students = TeacherA.objects.get(userid=userid) 
        return render(request,"system1/updateTeach.html",{'Useradd':students})
        
        #template = loader.get_template('system/update.html',)
  
@csrf_exempt
def updateTeach(request, userid):
    
    Useradd = TeacherA.objects.get(userid=userid)   
    form = TeachForm(request.POST, instance=Useradd)  
    if form.is_valid():  
        form.save()  
        students = TeacherA.objects.all()
        template = loader.get_template('system1/teachinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)  

    return render(request, 'system1/updateTeach.html', {'Useradd': Useradd}) 
@csrf_exempt
def delete1(request, userid):  
    students = TeacherA.objects.get(userid=userid)  
    students.delete()  
    template = loader.get_template('system1/teachinfo.html')

    students = TeacherA.objects.all()
    template = loader.get_template('system1/teachinfo.html')
    context = {'students': students}
    output = template.render(context)
    return HttpResponse(output)

def teachinfo(request):
        students = TeacherA.objects.all()
        template = loader.get_template('system1/teachinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)
@csrf_exempt
def subject(request):
    if request.method == 'POST':
        #getting values from post
        code = request.POST.get('code')
        sub = request.POST.get('sub')
        context = {
            'code': code,
            'sub': sub
            
        }
       
        
       
        au=Subject1()
        au.code= code
        au.sub= sub
        au.save()
        students = Subject1.objects.all()
            
        template = loader.get_template('system1/subject.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)
       

        #returing the template 
        #return HttpResponse(template.render(context, request))
        #context = RequestContext(request)
        #return render_to_response('app/showdata.html', student_dict, context)
    else:
    
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('system1/subject.html')
        return HttpResponse(template.render())

def showsub(request):

        students = Subject1.objects.all()
        template = loader.get_template('system1/showsub.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)
def Showsub2(request):

        students = Subject1.objects.all()
        template = loader.get_template('system1/Showsub2.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)

csrf_exempt
def delsub(request, code):  
    students = Subject1.objects.get(code=code)  
    students.delete()  
    template = loader.get_template('system1/showsub.html')

    students = Subject1.objects.all()
    template = loader.get_template('system1/showsub.html')
    context = {'students': students}
    output = template.render(context)
    return HttpResponse(output)


@csrf_exempt
def Attend(request):
    username=request.session['myuser'];               
                        
    if request.method == 'POST':
        #getting values from post
        br = request.POST.get('hbr')
        sub = request.POST.get('sub')
        sem = request.POST.get('sem')
        userid = request.POST.get('userid')
        
        
        context = {
            'sem': sem,
            'sub': sub,
            'br': br,
            'userid': userid
              
            
        }
       
        '''rno= request.POST.get('rno')
        if Attend1.objects.filter(rno=rno).exists():    
                     message='Record already exist.'  
                     return render(request,"system1/Attendance.html",{'message':message})'''
         
         
       # else:
        au=Attend1()
        au.sem= sem
        au.sub= sub
        au.br= br
        au.userid= userid
        
           
           
        au.save()
        students = Attend1.objects.all()
        #template = loader.get_template('system1/Attendance.html')
        #context = {'students': students}
        #output = template.render(context)
        return render(request, 'system1/Attendance.html',{'students': students,'message':'Record successfully Added!'})    
        
        return HttpResponse(output)
       

        #returing the template 
        #return HttpResponse(template.render(context, request))
        #context = RequestContext(request)
        #return render_to_response('app/showdata.html', student_dict, context)
    else:
    
        #if post request is not true 
        #returing the form template 
        #template = loader.get_template('system1/Attendance.html')
        #return HttpResponse(template.render())
         return render(request, 'system1/Attendance.html',{"username" : username})
@csrf_exempt
def editA(request):
     if request.method == 'POST':
        #getting values from post
        Alec = request.POST.get('Alec')
        students=Attend1()
       
        students.save()
            
   
        students = Attend1.objects.all()
        template = loader.get_template('system1/AttendR.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)  
     return render(request, 'system1/AttendR.html')  

@csrf_exempt
def showAttend(request):
    username=request.session['myuser']; 
         
    if request.method == 'POST':
        #getting values from post
        userid = request.POST.get('userid')
        if Attend1.objects.filter(userid=userid).exists(): 
                  
                students= Attend1.objects.filter(userid=userid)
                return render(request, 'system1/AttendR.html',{'students': students})

                #template = loader.get_template('system1/AttendR.html')
                #context = {'students': students}
                #output = template.render(context)
                #return HttpResponse(output)
        else:
             message='Not found!'  
             return render(request,"system1/AttendR.html",{'message':message})
    else:
         return render(request,"system1/AttendR.html",{'username':username})

def AttendR(request):
        
        username=request.session['myuser']; 
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
                #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/AttendR.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/AttendR.html',{'message':'Not Found Record'})



def AttendR1(request):
        
        username=request.session['myuser']; 
        
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
        
        #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/AttendR1.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/AttendR1.html',{'message':'Not Found Record'})



def Attend3(request):
        
        username=request.session['myuser']; 
        
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
        
        #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/Attend3.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/Attend3.html',{'message':'Not Found Record'})

def Addnotes(request):
        
        username=request.session['myuser']; 
        
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
        
        #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/Addnotes.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/Addnotes.html',{'message':'Not Found Record'})





def Attend4(request):
        
        username=request.session['myuser']; 
        
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
        
                #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/Attend4.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/Attend4.html',{'message':'Not Found Record'})

   

def Attend5(request):
        
        username=request.session['myuser']; 
        
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
        
                #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/Attend5.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/Attend5.html',{'message':'Not Found Record'})




@csrf_exempt
def Attedit1(request,br,sub,sem):
        if Assgin2.objects.filter(stream=br,sub=sub,des=sem).exists(): 
                students = Assgin2.objects.filter(stream=br).filter(sub=sub).filter(des=sem)
        
                return render(request, 'system1/showdata.html',{"pro" : students})

                #template = loader.get_template('system1/showdata.html')
                #context = {'students': students}
                #output = template.render(context)
                #return HttpResponse(output)
        else:
            return render(request, 'system1/Attend4.html')
@csrf_exempt
def Attedit2(request,br,sub,sem):
        if AddU2.objects.filter(br=br).filter(sem=sem).exists():
                aa1= AddU2.objects.filter(br=br).filter(sem=sem)
                
        
             
                request.session['subject']=sub;
                subject=request.session['subject'];
                return render(request,"system1/MstReport.html",{"students" : aa1,'ex':'MST-1'})
        else:
            return render(request, 'system1/MstReport.html')

 

        
        #return render(request,"system1/editAttend.html",{'Useradd':students})
        
        #students = Attend1.objects.get(br=br,sem=sem,sub=sub) 
        #return render(request,"system1/MstReport.html",{'Useradd':students})
@csrf_exempt
def Attedit3(request,br,sub,sem):
        if AddU2.objects.filter(br=br).filter(sem=sem).exists():
                aa1= AddU2.objects.filter(br=br).filter(sem=sem)
                
        
             
                request.session['subject']=sub;
                subject=request.session['subject'];
                return render(request,"system1/MstReport1.html",{"students" : aa1,'ex':'MST-2'})
        else:
            return render(request, 'system1/MstReport1.html')

 

@csrf_exempt
def Attedit(request,br,sub,sem):
        students = Attend1.objects.get(br=br,sem=sem,sub=sub) 
        return render(request,"system1/assign.html",{'Useradd':students})

@csrf_exempt
def notes(request,br,sub,sem):
        students = Attend1.objects.get(br=br,sem=sem,sub=sub) 
        return render(request,"system1/notes1.html",{'Useradd':students})



@csrf_exempt
def editAttend1(request,sub):
              aa1= EditA.objects.filter(sub=sub)
             
                  
              return render(request,"system1/editAttend1.html",{'students':aa1,'dd':datetime.datetime.now().date()})
@csrf_exempt
def editAttend(request,sem,br,sub):
        #sem=Attend1.objects.get(sem=sem)
        #students=Attend1.objects.get(sub=sub)  
        #ss=Attend1.objects.filter(sub=sub) 
        #students = Attend1.objects.get(sub=sub) 
        if AddU2.objects.filter(br=br).filter(sem=sem).exists():
                aa1= AddU2.objects.filter(br=br).filter(sem=sem)
                
        
             
                #template = loader.get_template('system1/editAttend.html')
        
                #students = {'students':aa1}
                #output = template.render(context)
                #return HttpResponse(output)
                request.session['subject']=sub;
                subject=request.session['subject'];
                return render(request,"system1/editAttend.html",{"students" : aa1,'dd':datetime.datetime.now().date()})
        #return render(request,"system1/editAttend.html",{'Useradd':students})
        
        #template = loader.get_template('system/update.html',)
        else:
            return render(request, 'system1/editAttend.html',{'message':'Not found!'})

@csrf_exempt
def edit22(request):
       if request.method == 'POST':
            
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            Alec = request.POST.getlist('Alec')
            Dlec = request.POST.getlist('Dlec')
            per = request.POST.getlist('per')
            dd = request.POST.getlist('dd')

            context={
                    'rno' : rno,
                    'sub' : sub,
                    'Alec': Alec,
                    'Dlec': Dlec,
                    'per' : per,
                    'dd' : dd 
                       
                   
            }     
            c = min([len(rno), len(sub), len(Alec), len(Dlec),len(per) , len(dd)])
        
            for i in range(c):
                per[i]=int(Alec[i])*100/int(Dlec[i]) 
                res = EditA()
                res.rno=rno[i]
                res.sub=sub[i]
                res.Alec=Alec[i] 
                res.Dlec=Dlec[i]
                res.per=float(per[i])
                res.dd=dd[i]
                res.save() 
         
            
            return render(request, 'system1/editAttend.html',{'message':'Records are successfully submitted.'})
           
             
       else:
            return render(request, 'system1/editAttend.html',{'message':'Not found!'})
@csrf_exempt
def delAttend(request, sub):  
    students = Attend1.objects.get(sub=sub)  
    students.delete()  
    template = loader.get_template('system1/AttendR.html')

    students = Attend1.objects.all()
    template = loader.get_template('system1/AttendR.html')
    context = {'students': students}
    output = template.render(context)
    return HttpResponse(output)



@csrf_exempt
def UpdateAttend(request):
       if request.method == 'POST':
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            Alec = request.POST.getlist('Alec')
            Dlec = request.POST.getlist('Dlec')
            per = request.POST.getlist('per')
            dd = request.POST.getlist('dd')
            
            c = min([len(rno), len(sub), len(Alec), len(Dlec), len(per), len(dd)])
            for i in range(c):
                per[i]=int(Alec[i])*100/int(Dlec[i]) 
               
                res = EditA.objects.get(rno=rno[i],sub=sub[i])
                res.Alec=Alec[i] 
                res.Dlec=Dlec[i]
                res.per=float(per[i])
                res.save() 
           # pro = EditA.objects.all()
           # template = loader.get_template('system1/AttendShow.html')
           # context = {'students': pro}
           # output = template.render(context)
           # return HttpResponse(output)
 
            
            return render(request, 'system1/AttendShow.html',{'message':'Record Successfully Updated!'})
           
             
       else:
         return render(request, 'system1/editAttend1.html',{'message':'Not found!'})
@csrf_exempt
def Mstupdate(request):
       if request.method == 'POST':
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            sem = request.POST.getlist('sem')
            ex = request.POST.getlist('ex')
            mo = request.POST.getlist('mo')
            max = request.POST.getlist('max')
            br = request.POST.getlist('br')

               
            c = min([len(rno), len(sub), len(sem), len(br),len(max) , len(mo), len(ex)])
        
            for i in range(c):
                #per[i]=int(Alec[i])*100/int(Dlec[i]) 
               
                res = Mst1.objects.get(rno=rno[i],ex=ex[i])
                res.max=max[i] 
                #res.ex=ex[i]
                res.mo=mo[i]
               # res.per=float(per[i])
                res.save() 
            pro = EditA.objects.all()
            #template = loader.get_template('system1/Mstupdate.html')
            #context = {'students': pro}
            #output = template.render(context)
            #return HttpResponse(output)
 
            
            return render(request, 'system1/Mstupdate.html',{'students': pro,'message':'Record Successfully Updated!'})
           
             
       else:
         return render(request, 'system1/Mstupdate.html',{'message':'Not found!'})
@csrf_exempt
def Mstupdate2(request):
       if request.method == 'POST':
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            sem = request.POST.getlist('sem')
            ex = request.POST.getlist('ex')
            mo = request.POST.getlist('mo')
            max = request.POST.getlist('max')
            br = request.POST.getlist('br')

               
            c = min([len(rno), len(sub), len(sem), len(br),len(max) , len(mo), len(ex)])
        
            for i in range(c):
                #per[i]=int(Alec[i])*100/int(Dlec[i]) 
               
                res = Mst2.objects.get(rno=rno[i],ex=ex[i])
                res.max=max[i] 
                #res.ex=ex[i]
                res.mo=mo[i]
               # res.per=float(per[i])
                res.save() 
            pro = EditA.objects.all()
            #template = loader.get_template('system1/Mstupdate.html')
            #context = {'students': pro}
            #output = template.render(context)
            #return HttpResponse(output)
 
            
            return render(request, 'system1/Mstupdate2.html',{'students': pro,'message':'Record Successfully Updated!'})
           
             
       else:
         return render(request, 'system1/Mstupdate2.html',{'message':'Not found!'})




@csrf_exempt
def ShowAttend(request):
    username=request.session['myuser'];               
    
    if EditA.objects.filter(rno=username).exists(): 
                  
            pro = EditA.objects.filter(rno=username)
            template = loader.get_template('system1/ShowAttend.html')
            context = {'students': pro}
            output = template.render(context)
            return HttpResponse(output)
    else:
            message='Not found!'  
            return render(request,"system1/ShowAttend.html",{'message':message})
 
@csrf_exempt
def MstR(request):
    username=request.session['myuser'];               
    if Mst1.objects.filter(rno=username).exists(): 
                  
            pro = Mst1.objects.filter(rno=username).filter(ex='MST-1')
            pro1 = Mst2.objects.filter(rno=username).filter(ex='MST-2') 
            #template = loader.get_template('system1/showAssign.html')
            #context = {'students': pro}
            #output = template.render(context)
            #return HttpResponse(output)
            return render(request,"system1/showAssign.html",{'students':pro,'students1':pro1})
    else:
            message='Not found!'  
            return render(request,"system1/showAssign.html",{'message':message})
   
def showAssign(request):
        pro = Mst1.objects.all()
        template = loader.get_template('system1/showAssign.html')
        context = {'pro': pro}
        output = template.render(context)
        return HttpResponse(output)


@csrf_exempt
def manoj(request):
     MyProfileForm = ProForm(request.POST, request.FILES)
     return render(request, 'system1/assign.html', {'MyProfileForm':MyProfileForm})

@csrf_exempt
def assign(request):
   saved = False
   if request.method == "POST":
      MyProfileForm = ProForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         assign = Assgin2()
         assign.sub = MyProfileForm.cleaned_data["sub"]
         assign.dd = MyProfileForm.cleaned_data["dd"]
         assign.title = MyProfileForm.cleaned_data["title"]
         assign.stream = MyProfileForm.cleaned_data["stream"]
         assign.des = MyProfileForm.cleaned_data["des"]
         assign.picture = MyProfileForm.cleaned_data["picture"]
         saved = True
         assign.save()
         
         pro = Assgin2.objects.all()
         #context ={'pro': pro}
         return render(request, 'system1/assign.html',{'message':'Record successfully Submitted!'})
   else:

      MyProfileForm = ProForm()
   return render(request, 'system1/showdata.html', locals())

@csrf_exempt
def notes2(request):
     MyProfileForm = NotesForm(request.POST, request.FILES)
     return render(request, 'system1/notes1.html', {'MyProfileForm':MyProfileForm})


# Create your views here.
@csrf_exempt
def notesadd(request):
   saved = False
   if request.method == "POST":
      MyProfileForm = NotesForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         assign = Notes()
         assign.sub = MyProfileForm.cleaned_data["sub"]
         assign.title = MyProfileForm.cleaned_data["title"]
         assign.stream = MyProfileForm.cleaned_data["stream"]
         assign.des = MyProfileForm.cleaned_data["des"]
         assign.picture = MyProfileForm.cleaned_data["picture"]
         saved = True
         assign.save()
         
         pro = Notes.objects.all()
         #context ={'pro': pro}
         return render(request, 'system1/notes1.html',{'message':'Record successfully Submitted!'})
   else:

      MyProfileForm = NotesForm()
   return render(request, 'system1/showdata.html', locals())

# Create your views here.


def showdata(request):
        
        pro = Assgin2.objects.all()
        template = loader.get_template('system1/showdata.html')
        context = {'pro': pro}
        output = template.render(context)
        return HttpResponse(output)
@csrf_exempt
def showA(request):
    if request.method == 'POST':
        #getting values from post
        stream = request.POST.get('hbr')
        des = request.POST.get('des')
        if Assgin2.objects.filter(stream=stream,des=des).exists(): 
                  
                pro = Assgin2.objects.filter(stream=stream).filter(des=des)
                template = loader.get_template('system1/WebPage1.html')
                context = {'pro': pro}
                output = template.render(context)
                return HttpResponse(output)
        else:
             message='Not found!'  
             return render(request,"system1/WebPage1.html",{'message':message})
    else:
         return render(request,"system1/WebPage1.html")



@csrf_exempt
def MstRep(request):
     if request.method == 'POST':
            
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            sem = request.POST.getlist('sem')
            ex = request.POST.getlist('ex')
            mo = request.POST.getlist('mo')
            max = request.POST.getlist('max')
            br = request.POST.getlist('br')

            context={
                    'rno' : rno,
                    'sub' : sub,
                    'sem': sem,
                    'br': br,
                    'max' : max,
                    'mo' : mo, 
                    'ex' : ex  
                   
            }     
            c = min([len(rno), len(sub), len(sem), len(br),len(max) , len(mo), len(ex)])
        
            for i in range(c):
                res = Mst1()
                res.rno=rno[i]
                res.sub=sub[i]
                res.br=br[i] 
                res.sem=sem[i]
                res.ex=ex[i]
                res.max=max[i]
                res.mo=mo[i]
                res.save() 
         
            return render(request, 'system1/MstReport.html', {'message':'Record Successfully Added!'})

            #return render(request, 'system1/editAttend.html',{'message':'Records are successfully submitted.'})
           
             
     else:
           template = loader.get_template('system1/MstReport.html')
           return HttpResponse(template.render())

@csrf_exempt
def MstRep1(request):
     if request.method == 'POST':
            
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            sem = request.POST.getlist('sem')
            ex = request.POST.getlist('ex')
            mo = request.POST.getlist('mo')
            max = request.POST.getlist('max')
            br = request.POST.getlist('br')

            context={
                    'rno' : rno,
                    'sub' : sub,
                    'sem': sem,
                    'br': br,
                    'max' : max,
                    'mo' : mo, 
                    'ex' : ex  
                   
            }     
            c = min([len(rno), len(sub), len(sem), len(br),len(max) , len(mo), len(ex)])
        
            for i in range(c):
                res = Mst2()
                res.rno=rno[i]
                res.sub=sub[i]
                res.br=br[i] 
                res.sem=sem[i]
                res.ex=ex[i]
                res.max=max[i]
                res.mo=mo[i]
                res.save() 
         
            return render(request, 'system1/MstReport1.html', {'message':'Record Successfully Added!'})

            #return render(request, 'system1/editAttend.html',{'message':'Records are successfully submitted.'})
           
             
     else:
           template = loader.get_template('system1/MstReport1.html')
           return HttpResponse(template.render())
 

 
     
    
@csrf_exempt
def DeleteM1(request,rno):
               
                students = Mst1.objects.get(rno=rno)      
                students.delete()

                template = loader.get_template('system1/mstinfo.html')
           
                students = Mst1.objects.all()
           
                template = loader.get_template('system1/mstinfo.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)

@csrf_exempt
def editM(request, rno):
     students = Mst1.objects.get(rno=rno)
     return render(request, 'system1/updateM.html', {'Useradd': students})


@csrf_exempt
def updateM(request, rno):
    Useradd = Mst1.objects.get(rno=rno)
    form = MstForm(request.POST, instance=Useradd)
    if form.is_valid():
        form.save()
        #students = Mst1.objects.all()
        #template = loader.get_template('system1/mstinfo.html')
        #context = {'students': students}
        #output = template.render(context)
        #return HttpResponse(output)
        return render(request, 'system1/updateM.html', {'Useradd': Useradd,'message':'Record Successfully Updated!'})

@csrf_exempt
def mstinfo(request,br,sem,sub):
         if Mst1.objects.filter(br=br,sub=sub,sem=sem).exists():    
                students=Mst1.objects.filter(br=br).filter(sub=sub).filter(sem=sem).filter(ex='MST-1')    
                
                #students = Mst1.objects.all()
                template = loader.get_template('system1/Mstupdate.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
                #render(request, 'system1/Mstupdate.html', {'students': students,'message':'Record successfully updated!'})

         else:
            template = loader.get_template('system1/Attend5.html')
            return HttpResponse(template.render())
 
           # render(request, 'system1/ms.html', {'message':'Not Found!'})
@csrf_exempt
def mstinfo2(request,br,sem,sub):
         if Mst2.objects.filter(br=br,sub=sub,sem=sem).exists():    
                students=Mst2.objects.filter(br=br).filter(sub=sub).filter(sem=sem).filter(ex='MST-2')    
                #render(request, 'system1/Mstupdate.html', {'students': students,'message':'Record successfully updated!'})
                template = loader.get_template('system1/Mstupdate.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
               
         else:
             render(request, 'system1/Attend5.html')

     
@csrf_exempt
def change(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        password1= request.POST.get('password1')
        password2 = request.POST.get('password2')
       
        password3 = request.POST.get('password3')
        if not password2==password3:
                    return render(request,"system1/change.html",{'message':"Not match"})
        
        elif KStudent2.objects.filter(userid=password1).exists():
           
                    students = KStudent2.objects.get(userid=password1)
            
                    students.password= password2
            
                    students.save()
           
       
                    return render(request,"system1/change.html",{'message':"Password Successfully Changed!"})
        elif TeacherA.objects.filter(userid=password1).exists():
           
                    students = TeacherA.objects.get(userid=password1)
            
                    students.password= password2
            
                    students.save()
           
       
                    return render(request,"system1/change.html",{'message':"Record Successfully Updated!"})

        elif AddU2.objects.filter(userid=password1).exists():
           
                    students = AddU2.objects.get(userid=password1)
            
                    students.password= password2
            
                    students.save()
           
       
                    return render(request,"system1/change.html",{'message':"Record Successfully Updated!"})
           
        
        else:
             return render(request,"system1/change.html",{'message':"Incorrect Password!"})
      
    else:
         
        return render(request,"system1/change.html")

@csrf_exempt
def ForgetP(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
          
        form = ForForm(request.POST)  
       
       
        if form.is_valid():  
                email = form.cleaned_data['email']
                email = request.POST.get('email')
                if AddU2.objects.filter(email=email).exists():
                        
                        #password =AddU2.objects.get( 'password')
                
                       # students=AddU2.objects.filter(email=email)
                        #id=students.userid
                        #pas=students.password
                        students=AddU2.objects.get(email=email)
                       
                        use=students.userid
                        pas=students.password
                        
                        email1=EmailMessage('Your UserID and Password Is:',"Userid="+use+"  "+"Password="+pas,to=[email])
                        email1.send()
                        message='Record already exist' 
                        response = render(request, 'system1/forget.html',{"username" : message})
                         
                        
    else:  
         form = ForForm()  
       
    return render(request, 'system1/forget.html')

def manoj1(request):
     MyProfileForm = ProfileForm(request.POST, request.FILES)
     return render(request, 'system1/UploadG.html', {'MyProfileForm':MyProfileForm})

def SaveProfile(request):
   saved = False
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      if MyProfileForm.is_valid():
         profile = Profile1()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
         pro = Profile1.objects.all()
         
       
         return render(request, 'system1/UploadG.html',{'message':'File upload successfully!'})
         
       
   else:
      MyProfileForm = ProfileForm()
   return render(request, 'system1/UploadG.html', locals())

def saved(request):
     pro = Profile1.objects.all()
         
     return render(request, 'system1/saved.html',{'pro': pro})

@csrf_exempt
def box1(request):
     if request.method == 'POST':
            #getting values from post
            co = request.POST.get('co')
            com = request.POST.get('com')
            context = {
                'co': co,
                'com': com
            }

            au=Compbox()
            au.co= co
            au.com= com  
            au.save()
            #students = Attend1.objects.all()
            #template = loader.get_template('system1/Attendance.html')
            #context = {'students': students}
            #output = template.render(context)
            return render(request, 'system1/Box.html',{'message':'Successfully Post Complain!'})    
        
            return HttpResponse(output)
       
     else:
        
          return render(request, 'system1/Box.html')

def box(request):
      return render(request, 'system1/Box.html')

@csrf_exempt
def contact1(request):
     if request.method == 'POST':
            #getting values from post
            na = request.POST.get('na')
            message = request.POST.get('message')
            mail = request.POST.get('mail')
            
            context = {
                'na': na,
                'message': message,
                'mail':mail
            }

            au=Contactus()
            au.na= na
            au.message= message 
            au.mail=mail
            au.save()
            students = Contactus.objects.all()
            template = loader.get_template('system1/contact.html')
            context = {'students': students}
            output = template.render(context)
           # return render(request, 'system1/contact.html',{'message':'Message successfully submitted!'})    
        
            return HttpResponse(output)
       
     else:
        
          return render(request, 'system1/contact.html',{'message':'Message successfully submitted!'})

@csrf_exempt
def contact(request):
        return render(request, 'system1/contact.html')

def showcom(request):


        students = Compbox.objects.all()
        template = loader.get_template('system1/showcom.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)

def time(request):
     MyProfileForm = TimeForm(request.POST, request.FILES)
     return render(request, 'system1/time.html', {'MyProfileForm':MyProfileForm})

def saveT(request):
   saved = False
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = TimeForm(request.POST, request.FILES)
      if MyProfileForm.is_valid():
         profile = Time()
         profile.userid = MyProfileForm.cleaned_data["userid"]
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
         pro = Time.objects.all()
         
       
         return render(request, 'system1/time.html',{'message':'Time table upload successfully!'})
         
       
   else:
      MyProfileForm = TimeForm()
   return render(request, 'system1/time.html', locals())

def ShowTime(request):
        pro = Time.objects.all()
        template = loader.get_template('system1/ShowTime.html')
        context = {'pro': pro}
        output = template.render(context)
        return HttpResponse(output)

csrf_exempt
def deltime(request,userid):  
    pro = Time.objects.get(userid=userid)  
    pro.delete()  
    template = loader.get_template('system1/ShowTime.html')

    pro = Time.objects.all()
    template = loader.get_template('system1/ShowTime.html')
    context = {'pro': pro}
    output = template.render(context)
    return HttpResponse(output)

csrf_exempt
def Techtime(request):
        username=request.session['myuser'];
        if Time.objects.filter(userid=username).exists(): 
                  
                pro= Time.objects.filter(userid=username)
                return render(request, 'system1/Techtime.html',{'pro': pro})

                #template = loader.get_template('system1/AttendR.html')
                #context = {'students': students}
                #output = template.render(context)
                #return HttpResponse(output)
        else:
             message='Not found!'  
             return render(request,"system1/Techtime.html",{'message':message})

def timestudent(request):
     MyProfileForm = StimeForm(request.POST, request.FILES)
     return render(request, 'system1/timestudent.html', {'MyProfileForm':MyProfileForm})

def studentT(request):
   saved = False
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = StimeForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
           
         profile = STime()
         profile.br = request.POST.get('hbr')
         profile.sem = MyProfileForm.cleaned_data["sem"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
         pro = STime.objects.all()
         
       
         return render(request, 'system1/timestudent.html',{'message':'Time table upload successfully!'})
         
       
   else:
      MyProfileForm = StimeForm()
   return render(request, 'system1/timestudent.html', locals())

def showStime(request):
        pro = STime.objects.all()
        template = loader.get_template('system1/showStime.html')
        context = {'pro': pro}
        output = template.render(context)
        return HttpResponse(output)

csrf_exempt
def delStime(request,br,sem):  
    pro = STime.objects.get(br=br,sem=sem)  
    pro.delete()  
    template = loader.get_template('system1/showStime.html')

    pro = STime.objects.all()
    template = loader.get_template('system1/showStime.html')
    context = {'pro': pro}
    output = template.render(context)
    return HttpResponse(output)

@csrf_exempt
def showtimet(request):
    if request.method == 'POST':
        #getting values from post
        br = request.POST.get('hbr')
        sem = request.POST.get('sem')
        if STime.objects.filter(br=br,sem=sem).exists(): 
                  
                pro = STime.objects.filter(br=br).filter(sem=sem)
                template = loader.get_template('system1/timetable.html')
                context = {'pro': pro}
                output = template.render(context)
                return HttpResponse(output)
        else:
             message='Not found!'  
             return render(request,"system1/timetable.html",{'message':message})
    else:
         return render(request,"system1/timetable.html")

def Noticeb(request):
     MyProfileForm = NoticeForm(request.POST, request.FILES)
     return render(request, 'system1/Noticeb.html', {'MyProfileForm':MyProfileForm})

def SaveNotice(request):
   saved = False
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = NoticeForm(request.POST, request.FILES)
      if MyProfileForm.is_valid():
         profile = Notice1()
         
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
         pro = Notice1.objects.all()
         
       
         return render(request, 'system1/Noticeb.html',{'message':'File upload successfully!'})
         
       
   else:
      MyProfileForm = NoticeForm()
   return render(request, 'system1/Noticeb.html', locals())

def showNotice(request):
     pro = Notice1.objects.all()
         
     return render(request, 'system1/showNotice.html',{'pro': pro})

@csrf_exempt
def register(request):
        #if post request came
    if request.method == 'POST':
        #getting values from post
       
        password = request.POST.get('password')
        fn = request.POST.get('fn')
        collegename=request.POST.get('collegename')
        ln= request.POST.get('ln')
        email = request.POST.get('email')
        br= request.POST.get('br')
        eventname = request.POST.get('eventname')
        eventcategory = request.POST.get('eventcategory')
        mno = request.POST.get('mno')
        gender = request.POST.get('gender')
        fathern = request.POST.get('fathern')
        sem= request.POST.get('sem')
        DD= request.POST.get('DD')
       
       
       
       
     
       
            #adding the values in a context variable
        context = {
           
            'password': password,
            'fn':fn,
            'ln': ln,
            'collegename':collegename,
            'email':email,
            'sem': sem,
            'DD':DD,
            'br':br,
            'eventname':eventname,
            'eventcategory':eventcategory,
            'gender':gender,
            'mno':mno,
            'fathern':fathern
           
           
        }
        #getting our showdata template
 
        #data = MStudent.objects.all().values()
       
        #student_dict = {'students': data}
         
        #template = loader.get_template('app/showdata.html');
       
        '''au=MStudent()
        au.userid= userid
        au.password= password
        au.save()
        students = Student.objects.all()
       
        template = loader.get_template('system/showdata.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)'''
       
       
       
        email= request.POST.get('email')
        if RegisterU2.objects.filter(email=email).exists():    
                     #messages.add_message(request, messages.SUCCESS, 'Record already exist!')
                     message='Email Id already Registered'
                     return render(request,"system1/register.html",{'message':message})
         
         #if MStudent.objects.filter(rno=rno).exists():
                  #message="not record found"  
                  #return render(request,"app/showdata.html",{'message':message})
                   
                         
                       
       
                #message='Incorrect Password'  
                #return render(request,"system/login.html",{'message':message})
         
        else:
            au=RegisterU2()
           
            au.password= password
           
            au.ln= ln
            au.fn= fn
            au.sem= sem
            au.collegename=collegename
            au.DD= DD
            au.br= br
            au.email= email
            au.fathern= fathern
            au.mno= mno
            au.gender=gender
            au.eventcategory= eventcategory
            au.eventname= eventname                  
     
            au.save()
            message='Registered Successfully!.'
            return render(request,"system1/register.html",{'message':message})
         
            #students = AddU2.objects.all()
           
            #template = loader.get_template('system1/adduser.html')
            #context = {'students': students}
            #output = template.render(context)
            #return HttpResponse(output)
       

        #returing the template
        #return HttpResponse(template.render(context, request))
        #context = RequestContext(request)
        #return render_to_response('app/showdata.html', student_dict, context)
    else:
   
        #if post request is not true
        #returing the form template
        template = loader.get_template('system1/register.html')
        return HttpResponse(template.render())

def registerinfo(request):
        students = RegisterU2.objects.all()
        template = loader.get_template('system1/registerinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)

@csrf_exempt
def delreg(request, email):  
    students = RegisterU2.objects.get(email=email)  
    students.delete()  
    template = loader.get_template('system1/registerinfo.html')

    students = RegisterU2.objects.all()
    template = loader.get_template('system1/registerinfo.html')
    context = {'students': students}
    output = template.render(context)
    return HttpResponse(output)


def notesinfo(request):
        students = Notes.objects.all()
        template = loader.get_template('system1/notesinfo.html')
        context = {'students': students}
        output = template.render(context)
        return HttpResponse(output)

@csrf_exempt
def delnotes(request,stream,sub,des):  
    students = Notes.objects.get(stream=stream,sub=sub,des=des)  
    students.delete()  
    template = loader.get_template('system1/notesinfo.html')

    students = Notes.objects.all()
    template = loader.get_template('system1/notesinfo.html')
    context = {'students': students}
    output = template.render(context)
    return HttpResponse(output)

@csrf_exempt
def showNotes(request):
    if request.method == 'POST':
        #getting values from post
        br = request.POST.get('hbr')
        sem = request.POST.get('sem')
        if Notes.objects.filter(stream=br,des=sem).exists(): 
                  
                pro = Notes.objects.filter(stream=br).filter(des=sem)
                template = loader.get_template('system1/showNotes.html')
                context = {'students': pro}
                output = template.render(context)
                return HttpResponse(output)
        else:
             message='Not found!'  
             return render(request,"system1/showNotes.html",{'message':message})
    else:
         return render(request,"system1/showNotes.html")

@csrf_exempt
def Assign1marks(request,br,sub,sem):
        if AddU2.objects.filter(br=br).filter(sem=sem).exists():
                aa1= AddU2.objects.filter(br=br).filter(sem=sem)
                
        
             
                request.session['subject']=sub;
                subject=request.session['subject'];
                return render(request,"system1/Assignmarks1.html",{"students" : aa1,'ex':'ASSIGNMENT-1'})


        #return render(request,"system1/editAttend.html",{'Useradd':students})
        

@csrf_exempt
def Addmarks1(request):
     if request.method == 'POST':
            
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            sem = request.POST.getlist('sem')
            ex = request.POST.getlist('ex')
            mo = request.POST.getlist('mo')
            max = request.POST.getlist('max')
            br = request.POST.getlist('br')

            context={
                    'rno' : rno,
                    'sub' : sub,
                    'sem': sem,
                    'br': br,
                    'max' : max,
                    'mo' : mo, 
                    'ex' : ex  
                   
            }     
            c = min([len(rno), len(sub), len(sem), len(br),len(max) , len(mo), len(ex)])
        
            for i in range(c):
                res = marks1()
                res.rno=rno[i]
                res.sub=sub[i]
                res.br=br[i] 
                res.sem=sem[i]
                res.ex=ex[i]
                res.max=max[i]
                res.mo=mo[i]
                res.save() 
         
            return render(request, 'system1/Assignmarks1.html', {'message':'Record Successfully Added!'})

            #return render(request, 'system1/editAttend.html',{'message':'Records are successfully submitted.'})
           
             
     else:
           template = loader.get_template('system1/Assignmarks1.html')
           return HttpResponse(template.render())
 
@csrf_exempt
def Assign2marks(request,br,sub,sem):
        if AddU2.objects.filter(br=br).filter(sem=sem).exists():
                aa1= AddU2.objects.filter(br=br).filter(sem=sem)
                
        
             
                request.session['subject']=sub;
                subject=request.session['subject'];
                return render(request,"system1/Assignmarks2.html",{"students" : aa1,'ex':'ASSIGNMENT-2'})


        #return render(request,"system1/editAttend.html",{'Useradd':students})
        

@csrf_exempt
def Addmarks2(request):
     if request.method == 'POST':
            
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            sem = request.POST.getlist('sem')
            ex = request.POST.getlist('ex')
            mo = request.POST.getlist('mo')
            max = request.POST.getlist('max')
            br = request.POST.getlist('br')

            context={
                    'rno' : rno,
                    'sub' : sub,
                    'sem': sem,
                    'br': br,
                    'max' : max,
                    'mo' : mo, 
                    'ex' : ex  
                   
            }     
            c = min([len(rno), len(sub), len(sem), len(br),len(max) , len(mo), len(ex)])
        
            for i in range(c):
                res = marks2()
                res.rno=rno[i]
                res.sub=sub[i]
                res.br=br[i] 
                res.sem=sem[i]
                res.ex=ex[i]
                res.max=max[i]
                res.mo=mo[i]
                res.save() 
         
            return render(request, 'system1/Assignmarks2.html', {'message':'Record Successfully Added!'})

            #return render(request, 'system1/editAttend.html',{'message':'Records are successfully submitted.'})
           
             
     else:
           template = loader.get_template('system1/Assignmarks2.html')
           return HttpResponse(template.render())

@csrf_exempt
def assign1info(request,br,sem,sub):
         if marks1.objects.filter(br=br,sub=sub,sem=sem).exists():    
                students=marks1.objects.filter(br=br).filter(sub=sub).filter(sem=sem).filter(ex='ASSIGNMENT-1')    
                
                #students = Mst1.objects.all()
                template = loader.get_template('system1/assign1info.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
                #render(request, 'system1/Mstupdate.html', {'students': students,'message':'Record successfully updated!'})

         else:
            template = loader.get_template('system1/assign1info.html')
            return HttpResponse(template.render())
 
           # render(request, 'system1/ms.html', {'message':'Not Found!'})
@csrf_exempt
def assign2info(request,br,sem,sub):
         if marks2.objects.filter(br=br,sub=sub,sem=sem).exists():    
                students=marks2.objects.filter(br=br).filter(sub=sub).filter(sem=sem).filter(ex='ASSIGNMENT-2')    
                
                #students = Mst1.objects.all()
                template = loader.get_template('system1/assign2info.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
                #render(request, 'system1/Mstupdate.html', {'students': students,'message':'Record successfully updated!'})

         else:
            template = loader.get_template('system1/assign2info.html')
            return HttpResponse(template.render())
 

@csrf_exempt
def studentassginmarks(request):
    username=request.session['myuser'];               
    
    if marks1.objects.filter(rno=username).exists(): 
                  
            pro = marks1.objects.filter(rno=username).filter(ex='ASSIGNMENT-1') 
            pro1= marks2.objects.filter(rno=username).filter(ex='ASSIGNMENT-2')
            #template = loader.get_template('system1/studentassginmarks.html')
            #context = {'students': pro}
            #output = template.render(context)
            #return HttpResponse(output)
            return render(request,"system1/studentassginmarks.html",{"students" :pro,"students1":pro1})
    else:
            message='Not found!'  
            return render(request,"system1/studentassginmarks.html",{'message':message})

def Internalform(request):
        
        username=request.session['myuser']; 
        if Attend1.objects.filter(userid=username).exists(): 
                students = Attend1.objects.filter(userid=username)
                #return render(request, 'system1/AttendR.html',{"username" : username})

                template = loader.get_template('system1/internalform.html')
                context = {'students': students}
                output = template.render(context)
                return HttpResponse(output)
        else:
              return render(request, 'system1/internalform.html',{'message':'Not Found Record'})

@csrf_exempt
def addInternal(request,sem,br,sub):
          
                 
                  aa1= Mst1.objects.filter(br=br).filter(sem=sem).filter(sub=sub)
                  aa2=marks1.objects.filter(br=br).filter(sem=sem).filter(sub=sub)
                  aa3= EditA.objects.filter(sub=sub)
                  aa4=marks2.objects.filter(br=br).filter(sem=sem).filter(sub=sub)
                  aa5= Mst2.objects.filter(br=br).filter(sem=sem).filter(sub=sub)
                  
                  return render(request,"system1/addinternal.html",{"students" : aa1,"students1":aa2,"students3" : aa3,"students2":aa4,"students4":aa5})

@csrf_exempt
def submitInternal(request):
          
                 
      if request.method == 'POST':
            
            rno = request.POST.getlist('rno')
            sub = request.POST.getlist('sub')
            mst1 = request.POST.getlist('mst1')
            mst2 = request.POST.getlist('mst2')
            assgin1 = request.POST.getlist('assgin1')
            assgin2= request.POST.getlist('assgin2')
            attend= request.POST.getlist('attend')
            internal= request.POST.getlist('internal')

            context={
                    'rno' : rno,
                    'sub' : sub,
                    'mst1': mst1,
                    'mst2': mst2,
                    'assgin1' : assgin1,
                    'assgin2' : assgin2, 
                    'attend': attend,
                    'internal': internal
                       
                   
            }     
            c = min([len(rno), len(sub), len(mst1), len(mst2),len(assgin1) , len(assgin2),len(attend),len(internal)])
        
            for i in range(c):
                if float(attend[i])>=95:
                     attend[i]=6
                elif float(attend[i])<95 and float(attend[i])>=90:
                     attend[i]=5 
                elif float(attend[i])<90 and float(attend[i])>=85:
                     attend[i]=4 
                elif float(attend[i])<85 and float(attend[i])>=80:
                     attend[i]=3 
                elif float(attend[i])<80 and float(attend[i])>=75:
                     attend[i]=2
                else:
                     attend[i]=1
                   
                
                internal[i]=int(mst1[i])*12/45+int(mst2[i])*12/45+int(assgin1[i])*5/10+int(assgin2[i])*5/10+float(attend[i]) 
                res = Internal()
                res.rno=rno[i]
                res.sub=sub[i]
                res.mst1=mst1[i] 
                res.mst2=mst2[i]
                res.internal=int(internal[i])
                res.assgin1=assgin1[i]
                res.assgin2=assgin2[i]
                res.attend=attend[i]
                res.save() 
         
            
            return render(request, 'system1/addinternal.html',{'message':'Records are successfully submitted.'})
           
             
      else:
            return render(request, 'system1/addinternal.html',{'message':'Not found!'})

@csrf_exempt
def ViewInternal(request,sub):
              aa1= Internal.objects.filter(sub=sub)
             
                  
              return render(request,"system1/ViewInternal.html",{'students':aa1})

@csrf_exempt
def showInternal(request):
    username=request.session['myuser'];               
    
    if Internal.objects.filter(rno=username).exists(): 
                  
            pro = Internal.objects.filter(rno=username)
            template = loader.get_template('system1/ViewInternal.html')
            context = {'students': pro}
            output = template.render(context)
            return HttpResponse(output)
    else:
            message='Not found!'  
            return render(request,"system1/ViewInternal.html",{'message':message})

def event(request):
     MyProfileForm = EventForm(request.POST, request.FILES)
     return render(request, 'system1/event.html', {'MyProfileForm':MyProfileForm})

def saveevent(request):
   saved = False
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = EventForm(request.POST, request.FILES)
      if MyProfileForm.is_valid():
         profile = eventdetails()
         
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
         pro = eventdetails.objects.all()
         
       
         return render(request, 'system1/event.html',{'message':'Event details uploaded successfully!'})
         
       
   else:
      MyProfileForm = EventForm()
   return render(request, 'system1/event.html', locals())

def ShowEvent(request):
        pro =eventdetails.objects.all()
        template = loader.get_template('system1/showevent.html')
        context = {'pro': pro}
        output = template.render(context)
        return HttpResponse(output)

def showeventdetails(request):
     pro = eventdetails.objects.all()
         
     return render(request, 'system1/showeventdetails.html',{'pro': pro})


 












    





        

        

 
    