from django.shortcuts import render
from django.http import HttpResponse


#HTTPRESPONSE




#RENDERS

def home(request):
	return render(request, 'accounts/home.html')

def shop(request):
	return render(request, 'accounts/shop.html')

def orders(request):
	return render(request, 'accounts/orders.html')




