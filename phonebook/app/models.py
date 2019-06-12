from django.db import models

class PersonManager(models.Manager):
	def get_by_natural_key(self, name,surname):
		return self.get(name=name,surname=surname)

class EmailManager(models.Manager):
	def get_by_natural_key(self,email):
		return self.get(email=email)

class Person(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	objects = PersonManager()


class Phone(models.Model):
	person = models.ForeignKey(Person,editable=False,on_delete=models.CASCADE,related_name="phones")
	phone = models.CharField(max_length=11)

	def __str__(self):
		return self.phone

class Email(models.Model):
	person = models.ForeignKey(Person,editable=False,on_delete=models.CASCADE,related_name="emails")
	email = models.EmailField()
	objects = EmailManager()

	def __str__(self):
		return self.email