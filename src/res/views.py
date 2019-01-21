from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Table, Reserved, User
import datetime
from django.urls import reverse


post_date = datetime.date.today()
check_table_date = str(datetime.date.today())
delta = datetime.timedelta(days=1)
idt = None
table_for_check = None
if_form = False

def home_view(request):
	global post_date
	global idt
	global table_for_check
	global if_form
	
	today = datetime.date.today()
	post_date = today if not post_date else post_date

	if request.method == 'POST':
		post_date = request.POST.get('party')

	tables = Table.objects.all()
	tables_dict = {}
	for table in tables:
		reserved = Reserved.objects.filter(date=str(post_date), 
										table=table).first()
		tables_dict[f'{table}'] = {'table':table, 
									'reserved': reserved
								}

	context = {'tables': tables,
			 	'post_date': str(post_date), 'idt': idt,
			 	'check_table_date': str(check_table_date),
			 	'table_for_check': table_for_check,
			 	'tables_dict': tables_dict,
			 	'if_form': if_form,
			}
	return render(request, 'base.html', context)

def get_tables(request):
	global post_date
		
	tables = Table.objects.all()
	tables_dict = {}
	for table in tables:
		link = reverse('reserve', args=[table.id])
		reserved = Reserved.objects.filter(date=str(post_date), 
										table=table).first()
		tables_dict[f'{table}'] = {'places':table.places, 
									'shape':table.shape,
									'link': link,
									'width':table.width,
									'length': table.length,
									'x': table.x,
									'y': table.y,
									'reserved': reserved.is_reserved if reserved else False}
	return JsonResponse(tables_dict)
	

def reserve_form(request, id):
	global post_date
	global idt
	global table_for_check
	global if_form

	if request.method == "POST":
		user_name = request.POST.get('user_name', None)
		user_email = request.POST.get('user_email', None)
		print(user_name, user_email)

		# table = Table(id=id)
		# if not User.objects.filter(user_name=user_name):
		# 	user = User(user_name=user_name, user_email=user_email)
		# 	user.save()

		# user = User.objects.filter(user_name=user_name).first()
		
		# if not Reserved.objects.filter(date=post_date, table=table):
		# 	form = Reserved(table=table, date=str(post_date), is_reserved=True, user=user)
		# 	form.save()
		# 	send_mail(subject='Book a table', 
		# 			message=f'Table{table.id} booked for {user.user_name} on {form.date}', 
		# 			from_email='this-comp@somemail.com', recipient_list=[user.user_email],
		# 			fail_silently=False)
		# table_for_check = None
		# if_form = False
		return redirect('home')
		
	# tables = Table.objects.all()
	# reserved = Reserved.objects.filter(date=post_date)
	# context = {'tables': tables, 'reserved': reserved, 
	# 				'post_date': str(post_date),
	# 				'check_table_date': check_table_date,
	# 				'table_for_check': table_for_check,
	# 				'idt': idt}	

	# return render(request, 'form.html', context)
	if_form = True
	return redirect('home')


def check_table(request):
	global idt
	global check_table_date
	global table_for_check

	if request.method == 'POST':
		print(request.POST)
		table_id = request.POST.get('table_choice')
		check_date = request.POST.get('check_date')
		check_table_date = check_date
		try:
			table_for_check = Table.objects.filter(id=int(table_id)).first()
			idt = Reserved.objects.filter(table=table_for_check, date=check_date).first()
		except:
			table_for_check = None
		return redirect('home')


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
	