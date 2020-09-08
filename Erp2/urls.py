"""
Definition of urls for FileUploadDjango.
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import django.contrib.auth.views

import system1.views
#from . import views

urlpatterns = [
    # Examples:
    #url('admin/', admin.site.urls),

    url('admin1/', admin.site.urls),
    url('', system1.views.home, name='home'),
    url('about/', system1.views.about, name='about'),
    url('box/', system1.views.box, name='box'),
    url('contact1/', system1.views.contact1, name='contact1'),
    url('cbox/', system1.views.box1, name='box1'),
    url('showcom/', system1.views.showcom, name='showcom'),
    url('Mstupdate/', system1.views.Mstupdate, name='Mstupdate'),
    url('Mstupdate2/', system1.views.Mstupdate2, name='Mstupdate2'), 
    url('time/', system1.views.time, name='time'),
    url('saveT/', system1.views.saveT, name='saveT'),
    url('ShowTime/', system1.views.ShowTime, name='ShowTime'),
    url('deltime/(?P<userid>[\w-]+)/',system1.views.deltime,name='deltime'),
    url('Techtime/', system1.views.Techtime, name='Techtime'),
    url('internal/', system1.views.submitInternal, name='submitInternal'),
     
    url('Addnotes/', system1.views.Addnotes, name='Addnotes'),
    url('notes/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.notes, name='notes'),

    url('Noticeb/', system1.views.Noticeb, name='Noticeb'),
    url('SaveNotice', system1.views.SaveNotice, name='SaveNotice'),
    url('showNotice/', system1.views.showNotice, name='showNotice'),
    url('getregisterdata/', system1.views.register, name='register'),


    url('timestudent/', system1.views.timestudent, name='timestudent'),
    url('studentT/', system1.views.studentT, name='studentT'),
    url('showStime/', system1.views.showStime, name='showStime'),
    url('delStime/(?P<br>[\w-]+)/(?P<sem>[\w-]+)/', system1.views.delStime, name='delStime'),
     url('showtimet/', system1.views.showtimet, name='showtimet'),
   
   
    url('admin/', system1.views.admin, name='admin'),
    url('contact/', system1.views.contact, name='contact'),
    url('login1/', system1.views.login1, name='login1'),
    url('addteach/', system1.views.addteach, name='addteach'),
    url('showsub/', system1.views.showsub, name='showsub'),
    url('Showsub2/', system1.views.Showsub2, name='Showsub2'),
   
    url('civil/', system1.views.civil, name='civil'),
    url('detcse/', system1.views.detcse, name='detcse'),
    url('me/', system1.views.me, name='me'),
    url('ece/', system1.views.ece, name='ece'),
    url('subject/', system1.views.subject, name='subject'),
    url('Attend/', system1.views.Attend, name='Attend'),
    url('showA/', system1.views.showA, name='showA'),
    url('editA/',system1.views.editA,name='editA'),
    url('AttendR/',system1.views.AttendR,name='AttendR'),
    url('AttendR1/',system1.views.AttendR1,name='AttendR1'),
    url('UpdateAttend/', system1.views.UpdateAttend, name='UpdateAttend'),
    url('ShowAttend/', system1.views.ShowAttend, name='ShowAttend'),
    url('Attend3/',system1.views.Attend3,name='Attend3'),
    url('studentassginmarks/',system1.views.studentassginmarks,name='studentassginmarks'),
    
    url('Attedit/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit, name='Attedit'),
    url('Attedit/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)$', system1.views.Attedit, name='Attedit'),
    
    url('Attend4/',system1.views.Attend4,name='Attend4'),
    url('Attedit1/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit1, name='Attedit1'),
    url('Attend5/',system1.views.Attend5,name='Attend5'),
    url('Attedit2/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit2, name='Attedit2'),
    url('Attedit3/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit3, name='Attedit3'),
    
    url('showAttend/', system1.views.showAttend, name='showAttend'),
    url('editAt1/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)/', system1.views.editAttend, name='editAt1'),
    url('editAt1/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.editAttend, name='editAt1'),
    url('editAttend1/(?P<sub>[\w-]+)/', system1.views.editAttend1, name='editAtttend1'),
    url('addInternal/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.addInternal, name='addInternal'),
   
    url('editAt/', system1.views.edit22, name='editAt'),
    url('delsub/(?P<code>[\w-]+)/',system1.views.delsub,name='delsub'),
    
     
 

    url('edit1/(?P<userid>\w+)',system1.views.edit1,name='edit1'),
    url('updateTeach/(?P<userid>\w+)', system1.views.updateTeach, name='updateTeach'),
    url('teachinfo/', system1.views.teachinfo, name='teachinfo'),
    url('delete1/(?P<userid>\w+)',system1.views.delete1,name='delete1'),
     
    url('komal/', system1.views.login, name='login'),
    url('change/', system1.views.change, name='change'),
    url('forget/', system1.views.forget, name='forget'),
    url('ForgetP/', system1.views.ForgetP, name='ForgetP'),
    url('delAttend/(?P<sub>[\w-]+)/',system1.views.delAttend,name='delAttend'),
    url('UploadG/', system1.views.UploadG, name='UploadG'),
    url('manoj1/', system1.views.manoj1, name='manoj1'),
    url('saverecord/', system1.views.SaveProfile, name='SaveProfile'),
    url('saved/', system1.views.saved, name='saved'),
    url('showdata/', system1.views.showdata, name='showdata'),
    url('getdata/', system1.views.adduser1, name='add'),
    url('userinfo/', system1.views.userinfo, name='info'),
    url('DeleteU/',system1.views.DeleteU,name='DeleteU'),
    url('edit/(?P<rno>\w+)',system1.views.edit,name='edit'),
    url('update/(?P<rno>\w+)', system1.views.update, name='update'),
    url('Teacher/', system1.views.Teacher, name='Teacher'),
    url('manoj/',system1.views.manoj,name='manoj'), 
    url('assign/',system1.views.assign,name='assign'),
    url('notes2/',system1.views.notes2,name='notes2'), 
    url('notes/',system1.views.notesadd,name='notesadd'),
    url('registerinfo/', system1.views.registerinfo, name='registerinfo'),
    url('notesinfo/', system1.views.notesinfo, name='notesinfo'),
    url('delreg/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',system1.views.delreg,name='delreg'),
    url('user/',system1.views.user,name='user'),
    url('shownotes/',system1.views.showNotes,name='showNotes'), 
    url('DeleteM1/(?P<rno>\w+)',system1.views.DeleteM1,name='DeleteM1'),
    url('editM/(?P<rno>\w+)',system1.views.editM,name='editM'),
    url('updateM/(?P<rno>\w+)', system1.views.updateM, name='updateM'),
    url('MstRep/', system1.views.MstRep, name='MstRep'),
    url('MstRep1/', system1.views.MstRep1, name='MstRep1'),
    url('showInternal/', system1.views.showInternal, name='showInternal'),
    url('ViewInternal/(?P<sub>[\w-]+)/', system1.views.ViewInternal, name='ViewInternal'),


    url('event/', system1.views.event, name='event'),
    url('saveE/', system1.views.saveevent, name='saveE'),
    url('ShowEvent/', system1.views.ShowEvent, name='ShowEvent'),
   
    url('showeventdetails/', system1.views.showeventdetails, name='eventdetails'),


    
    url('mstinfo/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)/', system1.views.mstinfo, name='mstinfo1'),
    url('mstinfo/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.mstinfo, name='mstinfo1'),
    url('mstinfo2/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.mstinfo2, name='mstinfo2'),
    url('mstinfo2/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)/', system1.views.mstinfo2, name='mstinfo2'),
    url('delnotes/(?P<des>[\w-]+)/(?P<stream>\w+)/(?P<sub>[\w-]+)/', system1.views.delnotes, name='delnotes'),
    url('Assign1marks/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.Assign1marks, name='assign1marks'),
    url('assign2info/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.assign2info, name='assign2info'),
    
    url('Addmarks1/', system1.views.Addmarks1, name='Addmarks1'),
    url('Assign2marks/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.Assign2marks, name='assign2marks'),
    url('Addmarks2/', system1.views.Addmarks2, name='Addmarks2'),
   
   
    url('MstR/', system1.views.MstR, name='MstR'),
    url('Internalform/', system1.views.Internalform, name='Internalform'),
   
   
    url('showAssign/', system1.views.showAssign, name='showAssign'),
    

    url('assign1info/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/', system1.views.assign1info, name='assign1info'),
    
    
    #url('Erp2/', include('Erp2.Erp2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

