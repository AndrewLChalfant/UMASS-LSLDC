from django import forms
from django.forms import ModelForm, ValidationError, CharField
from .models import COLOUser
from django.shortcuts import render, redirect, get_object_or_404

#SEARCH DATABASE
class SearchForm(forms.Form):
	searchName= forms.CharField(required=True)
	
#COMPLETE ACCESS
class COLOApprovalForm(forms.Form):	
	app_input= forms.CharField(label= '', required= True, widget=forms.TextInput(attrs={'placeholder': 'Please enter the tracking number of the request you wish to approve'}))
	
    #CUSTOM VALIDATION	
	#def clean(self):
		#input= self.cleaned_data['app_input']
		#if len(input) < 35:
			#raise forms.ValidationError('Please enter a valid tracking number')

#COMPLETE ACCESS
class COLODeletionForm(forms.Form):	
	del_input= forms.CharField(label= '', required= True, widget=forms.TextInput(attrs={'placeholder': 'Please enter the tracking number of the request you wish to delete'}))
	
    #CUSTOM VALIDATION	
	#def clean(self):
		#input= self.cleaned_data['del_input']
		#if len(input) < 35:
			#raise forms.ValidationError('Please enter a valid tracking number')
			            
#FORM TO UPDATE EMPLOYEE IMPROVAL
class ApprovalForm(forms.Form):
	approved= forms.BooleanField(label= 'This information is correct', required= True)


#FORM TO REQUEST USER DATA	
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
		name= self.cleaned_data['name']
		email= self.cleaned_data['email']
		man_email= self.cleaned_data['man_email']
		phone= self.cleaned_data['phone']
		id= self.cleaned_data['UCard_ID']
		
		#ENSURE FIRST AND LAST NAME
		if len(name) < 4 or len(name) > 20:
			raise forms.ValidationError('Please enter your first and last name')
			
		#ENSURE UMASS EMAIL
		if '.edu' not in email or '.edu' not in man_email:
			raise forms.ValidationError('Please submit a valid UMass Email with an ".edu" extension')
			
		#ENSURE VALID EMPLOYEE PHONE NUMBER
		if phone > 19999999999 or phone < 100000000:
			raise forms.ValidationError('Please submit a valid 10 digit phone number')
		
		#ENSURE VALID UMASS ID	
		if id > 99999999:
			raise forms.ValidationError('Please submit a valid 8 digit UMass ID number')

