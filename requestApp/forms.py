from django import forms
from django.forms import ModelForm, ValidationError, CharField
from .models import COLOUser
from django.shortcuts import render, redirect, get_object_or_404

#COLO OPS MANAGER COMPLETE ACCESS
class COLOApprovalForm(forms.Form):	
	app_input= forms.CharField(min_length= 36, max_length= 36, label= '', required= True, widget=forms.TextInput(attrs={'placeholder': 'Please enter the tracking number of the request you wish to approve'}))

#COLO OPS MANAGER REMOVE REQUEST
class COLODeletionForm(forms.Form):	
	del_input= forms.CharField(min_length= 36, max_length= 36, label= '', required= True, widget=forms.TextInput(attrs={'placeholder': 'Please enter the tracking number of the request you wish to delete'}))
			            
#FORM FOR MANAGER TO UPDATE EMPLOYEE IMPROVAL
class ApprovalForm(forms.Form):
	approved= forms.BooleanField(label= 'This information is correct', required= True)

#FORM TO REQUEST USER DATA ON HOME PAGE
class PostForm(ModelForm):
	class Meta:
		model = COLOUser
		fields = [
		'name', 
		'email', 
		'phone', 
		'reason', 
		'UCard_ID', 
		'manager', 
		'man_email',
		'dep'
		]
		
	#CUSTOM VALIDATION	
	def clean(self):
		error_css_class = 'error'
		name= self.cleaned_data['name']
		email= self.cleaned_data['email']
		manager= self.cleaned_data['manager']
		man_email= self.cleaned_data['man_email']
		phone= self.cleaned_data['phone']
		id= self.cleaned_data['UCard_ID']
		
		#ENSURE FIRST AND LAST NAME
		if len(name) < 4:
			raise forms.ValidationError('Please enter your first and last name')
		if len(manager) < 4:
			raise forms.ValidationError('Please enter your first and last name')	
			
		#ENSURE .EDU EMAIL
		if '.edu' not in email or '.edu' not in man_email:
			raise forms.ValidationError('Please submit a valid UMass Email with an ".edu" extension')
			
		#ENSURE VALID EMPLOYEE PHONE NUMBER
		if phone > 19999999999 or phone < 100000000:
			raise forms.ValidationError('Please submit a valid 10 digit phone number')
		
		#ENSURE VALID UMASS ID	
		if id > 99999999 or id < 1000000:
			raise forms.ValidationError('Please submit a valid 8 digit UMass ID number')

