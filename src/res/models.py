from django.db import models

class Table(models.Model):
	TABLE_FORM = (
		('OVAL', 'oval'),
		('SQUERE', 'squere'),
	)

	places = models.PositiveIntegerField(default=2)
	shape = models.CharField(max_length=20, choices=TABLE_FORM, default=TABLE_FORM[0][1])
	width = models.PositiveIntegerField(blank=False, null=False, default=10)
	length = models.PositiveIntegerField(blank=False, null=False, default=20)
	x = models.PositiveIntegerField(blank=False, null=False, default=0)
	y = models.PositiveIntegerField(blank=False, null=False, default=0)

	def __str__(self):
		return f'Table{self.id}'


class User(models.Model):
	user_name = models.CharField(max_length=50, unique=True)
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
		
		