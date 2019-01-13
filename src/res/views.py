from django.shortcuts import render, redirect
from .models import Table, Reserved, User
import datetime

post_date = None
delta = datetime.timedelta(days=1)


def home_view(request):
	global post_date
	today = datetime.date.today()
	post_date = today if not post_date else post_date
	if request.method == 'POST':
		post_date = request.POST.get('party')
		
	tables = Table.objects.all()
	reserved = Reserved.objects.filter(date=post_date)
	context = {'tables': tables, 'reserved': reserved, 'post_date': str(post_date)}
	return render(request, 'base.html', context)


def reserve_form(request, id):
	global post_date
	if request.method == "POST":
		user_name = request.POST.get('user_name', None)
		user_email = request.POST.get('user_email', None)
		
		table = Table(id=id)
		if not User.objects.filter(user_name=user_name):
			user = User(user_name=user_name, user_email=user_email)
			user.save()

		user = User.objects.filter(user_name=user_name).first()
		
		form = Reserved(table=table, date=str(post_date), is_reserved=True, user=user)
		form.save()
		return redirect('home')
		
	tables = Table.objects.all()
	reserved = Reserved.objects.filter(date=post_date)
	context = {'tables': tables, 'reserved': reserved, 'post_date': str(post_date)}	
	return render(request, 'form.html', context)


def prev_view(request):
	global post_date
	global delta
	today = datetime.date.today()
	if post_date is None:
		post_date = today
		return redirect('home')

	if post_date == today:
		return redirect('home')
	
	post_date -= delta
	return redirect('home')


def today_view(request):
	global post_date
	today = datetime.date.today()
	post_date = today
	return redirect('home')


def next_view(request):
	global post_date
	global delta
	
	post_date += delta
	return redirect('home')
	