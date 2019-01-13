from django.db import models

class Table(models.Model):
	TABLE_FORM = (
		('OVAL', 'Oval'),
		('SQUERE', 'Squere'),
	)
	places = models.IntegerField(default=True)
	shape = models.CharField(max_length=20, choices=TABLE_FORM, default=True)
	#width = models.FloatField(blank=True, null=True)
	#length = models.FloatField(blank=True, null=True)
	#x = models.FloatField(blank=True, null=True)
	#y = models.FloatField(blank=True, null=True)

	def __str__(self):
		return f'Table №{self.id}'


class User(models.Model):
	user_name = models.CharField(max_length=50)
	user_email = models.EmailField(max_length=50)

	def __str__(self):
		return self.user_name


class Reserved(models.Model):
	table = models.ForeignKey(Table, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_reserved = models.BooleanField(default=False)
	date = models.DateField(blank=True, null=True)

	def __str__(self):
		return f'{self.table} reserved for {self.user} at {self.date}'
