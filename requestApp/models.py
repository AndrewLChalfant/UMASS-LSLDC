from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
import uuid
from datetime import datetime
#EMPLOYEES REQUESTING ACCESS WILL HAVE THEIR INFORMATION STORED AS A 'COLOUSER' Model

#COLO CONSTRUCTOR
class COLOUserManager(models.Manager):
	def create_user(self, name, email, phone, reason, UCard_ID, manager, manager_email):
		user= self.create(
		name=name, 
		email=email,
		phone=phone, 
		reason=reason,
		UCard_ID= UCard_ID,
		manager= manager,
		man_email= manager_email,)
		
		return user

#MODEL TO STORE USER DATA
class COLOUser(models.Model):
	objects = COLOUserManager()
	
	#FIELDS NOT EDITABLE BY USER 
	man_approved= models.BooleanField('Manager Approved', blank= 'False', default='False')
	COLO_approved= models.BooleanField('COLO Manager Approved', default='False')
	time= models.DateTimeField("Timestamp", auto_now_add= True, editable= 'False')
	tracker= models.UUIDField(default= uuid.uuid4, primary_key= True, unique= True)
	
	#FIELDS EDITABLE BY USER
	name= models.CharField('Employee Name', max_length=30)
	email= models.EmailField('Employee Email', max_length=40)
	phone= models.PositiveIntegerField('Employee Phone Number')
	REASONS= (
	('COLO Area Access', 'COLO Area Access'),
	('LSLDC Card Access', 'LSLDC Card Access'),
	)
	reason= models.CharField('Reason for request', max_length=20, choices= REASONS, default='', )
	UCard_ID= models.PositiveIntegerField()
	manager= models.CharField('Manager Name', max_length=30)	
	man_email= models.EmailField('Manager Email', max_length=40)
	DEPARTMENTS= (
	('UMass Amherst', 'UMass Amherst'),
	('UMass Boston', 'UMass Boston'),
	("UMass President's Office", " UMass President's Office"),
	("UMass Medical School", "UMass Medical School"),
	)
	dep= models.CharField('Campus', max_length=20, choices= DEPARTMENTS, default='', )
	
	def __str__(self):
		return self.name
