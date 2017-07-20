from django import forms
from django.forms import ModelForm, ValidationError
from .models import COLOUser

#SEARCH DATABASE
class SearchForm(forms.Form):
	searchName= forms.CharField(required=True)
	
#FORM TO UPDATE EMPLOYEE IMPROVAL
class ApprovalForm(ModelForm):
	approve= forms.BooleanField(required= True)
	
	class Meta:
		model = COLOUser
		fields= ['man_approved']
		#user= COLOUser.objects.get(pk='d904d4953fe74f958f84fddad76e862d')
		#user.supervisor_approve()

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
		email= self.cleaned_data['email']
		man_email= self.cleaned_data['man_email']
		phone= self.cleaned_data['phone']
		id= self.cleaned_data['UCard_ID']
		
		#ENSURE UMASS EMAIL
		if '.edu' not in email or '.edu' not in man_email:
			raise forms.ValidationError('Please submit a valid UMass Email with an ".edu" extension')
			
		#ENSURE VALID EMPLOYEE PHONE NUMBER
		if phone > 19999999999 or phone < 100000000:
			raise forms.ValidationError('Please submit a valid 10 digit phone number')
		
		#ENSURE VALID UMASS ID	
		if id > 99999999:
			raise forms.ValidationError('UMass ID numbers are 8 digits long')

#NOT IMPLEMENTED		
class LoginForm(forms.Form):
	user= forms.CharField(required= True)
	password= forms.CharField(widget = forms.PasswordInput())
	
	def clean_message(self):
		username= self.cleaned_data.get('user')		
		if username == 'test':
			return forms.ValidationError("No access")
		return username
