from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

#IMPORT MODELS AND FORMS
from requestApp.models import COLOUser
from requestApp.forms import PostForm, ApprovalForm, LoginForm, SearchForm

#REQUIRE EMPLOYEE FORM FIELDS AND SEND TWO EMAILS
def home(request):
	if request.method == 'GET':
		form= PostForm()
		
	else:
		form= PostForm(request.POST)
		if form.is_valid():
			#CREATE NEW MODEL
			newUser= form.save()
			#PASS EMPLOYEE FORM DATA TO BE COMPOSED AS EMAIL TO HTML OUTLINE
			employee_content= render_to_string('requestApp/email_account_act.html', {
				'user': newUser,
			})
							
			#SEND EMAIL RECEIPT TO EMPLOYEE
			try:
				send_mail(
					'LSLDC COLO Request Confirmation', 
					employee_content,
					'noReply@umass.edu',
					[newUser.email])
			except BadHeaderError:
				return HttpResponse('ERROR')
			
			#PASS EMPLOYEE FORM DATA TO BE COMPOSED AS EMAIL TO HTML OUTLINE
			man_content= render_to_string('requestApp/email_manager_approve.html', {
				'user': newUser,
			})

			#SEND EMAIL TO EMPLOYEE MANAGER
			try:
				send_mail(
					'LSLDC COLO Employee Request Notification', 
					man_content,
					'noReply@umass.edu',
					[newUser.man_email])
			except BadHeaderError:
				return HttpResponse('ERROR')
			#REDIRECT TO COMPLETE PAGE
			return render(request, 'requestApp/employee_complete.html', {'user': newUser})
			
	return render(request, 'requestApp/request_home.html', {'form': form})

def employee_info(request):
	return render(request, 'requestApp/employee_second.html')
		
def complete(request):
	return render(request, 'requestApp/employee_complete.html')
	
def manager(request):
	if request.method == 'GET':
		form= ApprovalForm()
	else:
		form= ApprovalForm(request.POST)
		#approved= form.cleaned_data['man_approved']
		if form.approved == True:
			boolean= form.cleaned_data['man_approved']
			COLOUser.objects.supervisor_approve()
			colo_content= 'A new request has been submitted. Please visit the COLO Approval Site to grant access. LINK'
			#email script
			try:
				send_mail(
				'LSLDC COLO Request', 
				colo_content,
				'noReply@umass.edu',
				['colo@lsldc.umass.edu'])
			except BadHeaderError:
				return HttpResponse('ERROR')
			return redirect('complete')
			return redirect('supervisor_approved')
		else:
			return redirect('home')
			#denied
	return render(request, 'requestApp/supervisor_confirm.html', {'form': form})
	
def supervisor_complete(request):
	return render(request, 'requestApp/supervisor_complete.html')

#COLOMANAGER
def COLO(request):
	if request.method == 'GET':
		form= SearchForm()
	else:
		form= SearchForm(request.POST)
		#if form.is_valid():
			#name= form.cleaned_data['searchName']
			#COLOUser.objects.filter(name_contains= name)
	request_list= list(COLOUser.objects.all())
	full_list= {'requests' : request_list}
	return render(request, 'requestApp/colo.html', full_list)#, {'form': form})
	
def login(request):
	username= 'error'
	if request.method == "GET":
		form= LoginForm()
		
	else:
		form= LoginForm(request.POST)
		if form.is_valid():
			username= form.cleaned_data['username']
			password= form.cleaned_data['password']
			user= authenticate(request, username= username, password= password)
			if user:
				login(request, user)
				return HttpResponseRedirectt('/colo/')
			else:
				return HttpResponse('False')
				
	return render(request, 'requestApp/login.html', {'form': form})