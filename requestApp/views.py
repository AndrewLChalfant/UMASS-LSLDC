from django.core.mail import send_mail
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from smtplib import SMTPException

#IMPORT MODELS AND FORMS
from requestApp.models import COLOUser
from requestApp.forms import PostForm, ApprovalForm, COLOApprovalForm, COLODeletionForm
from requestApp.tokens import account_activation_token

#REQUIRE EMPLOYEE FORM FIELDS AND SEND EMAILS TO EMPLOYEE AND MANAGER
def home(request):
        if request.method == 'GET':
                form= PostForm()

        else:
                form= PostForm(request.POST)
                if form.is_valid():
                        #CREATE NEW MODEL TO HOLD REQUESTER DATA
                        newUser= form.save()
                        #PASS EMPLOYEE FORM DATA TO BE COMPOSED AS EMAIL TO HTML OUTLINE
                        employee_content= render_to_string('requestApp/email_employee_complete.html',
                        {
                                'user': newUser,
                        })
                        #SEND EMAIL RECEIPT TO EMPLOYEE
                        send_mail(
                                'LSLDC COLO Request Confirmation',
                                employee_content,
                                'LSLDC-NoReply@umass.edu',
                                [newUser.email])

                        #PASS EMPLOYEE FORM DATA TO BE COMPOSED AS EMAIL TO HTML OUTLINE
                        man_content= render_to_string('requestApp/email_employee_comp_to_manager.html', {
                                'user': newUser,
                                'token': account_activation_token.make_token(newUser),
                        })

                        #SEND EMAIL TO EMPLOYEE MANAGER
                        send_mail(
                                'LSLDC COLO Employee Request Notification',
                                man_content,
                                'LSLDC-NoReply@umass.edu',
                                [newUser.man_email],)

                        #REDIRECT TO COMPLETE PAGE
                        return render(request, 'requestApp/employee_complete.html', {'user': newUser})

        return render(request, 'requestApp/request_home.html', {'form': form})

#SITE TO CONFIRM EMPLOYEE FORM COMPLETED, REACHABLE VIA MANAGER'S EMAIL
def complete(request):
        return render(request, 'requestApp/employee_complete.html')

#SITE FOR MANAGER TO CONFIRM EMPLOYEES REQUEST  
def manager(request, uuid4, token):
        user= get_object_or_404(COLOUser, pk= uuid4)
        #IF MANAGER HAS APPROVED USER REQUEST
        if "approve" in request.POST:
        	#UPDATE MODEL FIELDS
            user.man_approved= 'True'
            user.save()
            manager_content= render_to_string('requestApp/email_manager_approved.html', {
                'user': user,
           		    })
            colo_content= render_to_string('requestApp/email_colo_manager_new.html', {
                'user': user,
                    })

            #EMAIL RECEIPT TO MANAGER
            send_mail(
            'Confirmation Employee LSLDC COLO Approval',
            manager_content,
            'LSLDC-NoReply@umass.edu',
            [user.email])

            #EMAIL ALERTING LSLDC THERE IS A NEW REQUEST
            send_mail(
            'New LSLDC COLO Request',
            colo_content,
            'LSLDC-NoReply@umass.edu',
            #['jpkiernan@umass.edu'])
            ['chalfant@umass.edu'])
            return redirect('manager_approved')
			
		#IF MANAGER HAS DENIED REQUEST
        if "remove" in request.POST:
            user.delete()
            return redirect('manager_denied')
            
        return render(request, 'requestApp/manager_confirm.html', {'user':user})

#PAGE TO CONFIRM MANAGER FORM COMPLETED
def manager_complete(request):
        return render(request, 'requestApp/manager_complete.html')

#PAGE TO CONFIRM MANAGER FORM DENIED
def manager_denied(request):
        return render(request, 'requestApp/manager_denied.html')

#LSLDC OPS MANAGER CONTROL PANNEL SITE
def COLO(request):
        if request.method == 'GET':
                form= COLOApprovalForm()
                form2= COLODeletionForm()
        else:
                #GENERATE APPROVAL AND DELETION FORMS
                form= COLOApprovalForm(request.POST)
                form2= COLODeletionForm(request.POST)
                if form.is_valid():
                        if 'approve' in request.POST:
                                uuid4= form.cleaned_data['app_input']
                                user= get_object_or_404(COLOUser, pk= uuid4)
                                user.COLO_approved= 'True'
                                user.save()

                                colo_content= render_to_string('requestApp/email_colo_complete.html', {
                                'user': user,
                                })

                                iso_content= render_to_string('requestApp/email_iso_exchange.html', {
                                'user': user,
                                })

                                #SEND MAIL TO REQUEST NOTIFYING THEIR REQUEST HAS BEEN APPROVED                 
                                send_mail(
                                'New LSLDC COLO Request',
                                colo_content,
                                'LSLDC-NoReply@umass.edu',
                                [user.email])

                                #SEND MAIL TO MARK HARRISON TO APPROVE REQUEST FOR CCURE APPLICATION
                                send_mail(
                                'LSLDC Access Request',
                                iso_content,
                                'LSLDC-NoReply@umass.edu',
                                #['mharrison@facil.umass.edu'])
                                ['chalfant@umass.edu'])

                #IF COLO OPS MANAGER DELETES REQUEST
                if form2.is_valid():
                        if 'remove' in request.POST:
                                uuid4= form2.cleaned_data['del_input']
                                user= get_object_or_404(COLOUser, pk= uuid4).delete()
                return redirect('colo')

        #EXPORT LISTS TO BE USED IN COLO TABLES
        request_list= list(COLOUser.objects.all())

        if COLOUser.objects.exists():
                request_list= COLOUser.objects.all().order_by('-time')

        #SETTINGS FOR DISPLAYING AMOUNT OF PENDING AND TOTAL REQUESTS           
        half_list= COLOUser.objects.filter(COLO_approved= 'False')
        if len(request_list) -  len(half_list) == 0:
                approved_requests= False
        else:
                approved_requests= True

        return render(request, 'requestApp/colo.html', {'requests': request_list, 'new_requests': half_list, 'form':form, 'form2': form2, 'approved_requests': approved_requests})
