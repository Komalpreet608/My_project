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

    url(r'^admin1/', admin.site.urls),
    url(r'^$', system1.views.home, name='home'),
    url(r'^about/$', system1.views.about, name='about'),
    url(r'^box/$', system1.views.box, name='box'),
    url(r'^contact1/', system1.views.contact1, name='contact1'),
    url(r'^cbox/$', system1.views.box1, name='box1'),
    url(r'^showcom/$', system1.views.showcom, name='showcom'),
    url(r'^Mstupdate/$', system1.views.Mstupdate, name='Mstupdate'),
    url(r'^Mstupdate2/$', system1.views.Mstupdate2, name='Mstupdate2'), 
    url(r'^time/$', system1.views.time, name='time'),
    url(r'^saveT/$', system1.views.saveT, name='saveT'),
    url(r'^ShowTime/$', system1.views.ShowTime, name='ShowTime'),
    url(r'^deltime/(?P<userid>[\w-]+)/$',system1.views.deltime,name='deltime'),
    url(r'^Techtime/$', system1.views.Techtime, name='Techtime'),
    url(r'^internal/$', system1.views.submitInternal, name='submitInternal'),
     
    url(r'^Addnotes/$', system1.views.Addnotes, name='Addnotes'),
    url(r'^notes/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.notes, name='notes'),

    url(r'^Noticeb/$', system1.views.Noticeb, name='Noticeb'),
    url(r'^SaveNotice', system1.views.SaveNotice, name='SaveNotice'),
    url(r'^showNotice/$', system1.views.showNotice, name='showNotice'),
    url(r'^getregisterdata/$', system1.views.register, name='register'),


    url(r'^timestudent/$', system1.views.timestudent, name='timestudent'),
    url(r'^studentT/$', system1.views.studentT, name='studentT'),
    url(r'^showStime/$', system1.views.showStime, name='showStime'),
    url(r'^delStime/(?P<br>[\w-]+)/(?P<sem>[\w-]+)/$', system1.views.delStime, name='delStime'),
     url(r'^showtimet/$', system1.views.showtimet, name='showtimet'),
   
   
    url(r'^admin/$', system1.views.admin, name='admin'),
    url(r'^contact/', system1.views.contact, name='contact'),
    url(r'^login1/$', system1.views.login1, name='login1'),
    url(r'^addteach/$', system1.views.addteach, name='addteach'),
    url(r'^showsub/$', system1.views.showsub, name='showsub'),
    url(r'^Showsub2/$', system1.views.Showsub2, name='Showsub2'),
   
    url(r'^civil/$', system1.views.civil, name='civil'),
    url(r'^detcse/$', system1.views.detcse, name='detcse'),
    url(r'^me/$', system1.views.me, name='me'),
    url(r'^ece/$', system1.views.ece, name='ece'),
    url(r'^subject/$', system1.views.subject, name='subject'),
    url(r'^Attend/$', system1.views.Attend, name='Attend'),
    url(r'^showA/$', system1.views.showA, name='showA'),
    url(r'^editA/$',system1.views.editA,name='editA'),
    url(r'^AttendR/$',system1.views.AttendR,name='AttendR'),
    url(r'^AttendR1/$',system1.views.AttendR1,name='AttendR1'),
    url(r'^UpdateAttend/$', system1.views.UpdateAttend, name='UpdateAttend'),
    url(r'^ShowAttend/$', system1.views.ShowAttend, name='ShowAttend'),
    url(r'^Attend3/$',system1.views.Attend3,name='Attend3'),
    url(r'^studentassginmarks/$',system1.views.studentassginmarks,name='studentassginmarks'),
    
    url(r'^Attedit/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit, name='Attedit'),
    url(r'^Attedit/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)$', system1.views.Attedit, name='Attedit'),
    
    url(r'^Attend4/$',system1.views.Attend4,name='Attend4'),
    url(r'^Attedit1/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit1, name='Attedit1'),
    url(r'^Attend5/$',system1.views.Attend5,name='Attend5'),
    url(r'^Attedit2/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit2, name='Attedit2'),
    url(r'^Attedit3/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)$', system1.views.Attedit3, name='Attedit3'),
    
    url(r'^showAttend/$', system1.views.showAttend, name='showAttend'),
    url(r'^editAt1/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)/$', system1.views.editAttend, name='editAt1'),
    url(r'^editAt1/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.editAttend, name='editAt1'),
    url(r'^editAttend1/(?P<sub>[\w-]+)/$', system1.views.editAttend1, name='editAtttend1'),
    url(r'^addInternal/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.addInternal, name='addInternal'),
   
    url(r'^editAt/$', system1.views.edit22, name='editAt'),
    url(r'^delsub/(?P<code>[\w-]+)/$',system1.views.delsub,name='delsub'),
    
     
 

    url(r'^edit1/(?P<userid>\w+)',system1.views.edit1,name='edit1'),
    url(r'^updateTeach/(?P<userid>\w+)', system1.views.updateTeach, name='updateTeach'),
    url(r'^teachinfo/$', system1.views.teachinfo, name='teachinfo'),
    url(r'^delete1/(?P<userid>\w+)',system1.views.delete1,name='delete1'),
     
    url(r'^komal/$', system1.views.login, name='login'),
    url(r'^change/$', system1.views.change, name='change'),
    url(r'^forget/$', system1.views.forget, name='forget'),
    url(r'^ForgetP/$', system1.views.ForgetP, name='ForgetP'),
    url(r'^delAttend/(?P<sub>[\w-]+)/$',system1.views.delAttend,name='delAttend'),
    url(r'^UploadG/$', system1.views.UploadG, name='UploadG'),
    url(r'^manoj1/$', system1.views.manoj1, name='manoj1'),
    url(r'^saverecord/$', system1.views.SaveProfile, name='SaveProfile'),
    url(r'^saved/$', system1.views.saved, name='saved'),
    url(r'^showdata/$', system1.views.showdata, name='showdata'),
    url(r'^getdata/$', system1.views.adduser1, name='add'),
    url(r'^userinfo/$', system1.views.userinfo, name='info'),
    url(r'^DeleteU/$',system1.views.DeleteU,name='DeleteU'),
    url(r'^edit/(?P<rno>\w+)',system1.views.edit,name='edit'),
    url(r'^update/(?P<rno>\w+)', system1.views.update, name='update'),
    url(r'^Teacher/$', system1.views.Teacher, name='Teacher'),
    url(r'^manoj/$',system1.views.manoj,name='manoj'), 
    url(r'^assign/',system1.views.assign,name='assign'),
    url(r'^notes2/$',system1.views.notes2,name='notes2'), 
    url(r'^notes/',system1.views.notesadd,name='notesadd'),
    url(r'^registerinfo/$', system1.views.registerinfo, name='registerinfo'),
    url(r'^notesinfo/$', system1.views.notesinfo, name='notesinfo'),
    url(r'^delreg/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',system1.views.delreg,name='delreg'),
    url(r'^user/',system1.views.user,name='user'),
    url(r'^shownotes/',system1.views.showNotes,name='showNotes'), 
    url(r'^DeleteM1/(?P<rno>\w+)',system1.views.DeleteM1,name='DeleteM1'),
    url(r'^editM/(?P<rno>\w+)',system1.views.editM,name='editM'),
    url(r'^updateM/(?P<rno>\w+)', system1.views.updateM, name='updateM'),
    url(r'^MstRep/$', system1.views.MstRep, name='MstRep'),
    url(r'^MstRep1/$', system1.views.MstRep1, name='MstRep1'),
    url(r'^showInternal/$', system1.views.showInternal, name='showInternal'),
    url(r'^ViewInternal/(?P<sub>[\w-]+)/$', system1.views.ViewInternal, name='ViewInternal'),


    url(r'^event/$', system1.views.event, name='event'),
    url(r'^saveE/$', system1.views.saveevent, name='saveE'),
    url(r'^ShowEvent/$', system1.views.ShowEvent, name='ShowEvent'),
   
    url(r'^showeventdetails/$', system1.views.showeventdetails, name='eventdetails'),


    
    url(r'^mstinfo/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)/$', system1.views.mstinfo, name='mstinfo1'),
    url(r'^mstinfo/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.mstinfo, name='mstinfo1'),
    url(r'^mstinfo2/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.mstinfo2, name='mstinfo2'),
    url(r'^mstinfo2/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>\w+)/$', system1.views.mstinfo2, name='mstinfo2'),
    url(r'^delnotes/(?P<des>[\w-]+)/(?P<stream>\w+)/(?P<sub>[\w-]+)/$', system1.views.delnotes, name='delnotes'),
    url(r'^Assign1marks/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.Assign1marks, name='assign1marks'),
    url(r'^assign2info/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.assign2info, name='assign2info'),
    
    url(r'^Addmarks1/$', system1.views.Addmarks1, name='Addmarks1'),
    url(r'^Assign2marks/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.Assign2marks, name='assign2marks'),
    url(r'^Addmarks2/$', system1.views.Addmarks2, name='Addmarks2'),
   
   
    url(r'^MstR/$', system1.views.MstR, name='MstR'),
    url(r'^Internalform/$', system1.views.Internalform, name='Internalform'),
   
   
    url(r'^showAssign/$', system1.views.showAssign, name='showAssign'),
    

    url(r'^assign1info/(?P<sem>[\w-]+)/(?P<br>\w+)/(?P<sub>[\w-]+)/$', system1.views.assign1info, name='assign1info'),
    
    
    #url(r'^Erp2/', include('Erp2.Erp2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

