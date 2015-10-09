from django.shortcuts import render
from django.http import HttpResponse
from .models import article

# Create your views here.
def content(request):									#returns the corresponding values when template content.html is been called.
	total_rows = article.objects.all() 
	context = {'rows':total_rows}
	return render(request,'content.html',context)

def detail(request, art_id):							#returns the corresponding values when template detail.html is been called.
	row_detail = article.objects.get(pk=art_id)
	context = {'rows': row_detail}
	return render(request, 'detail.html',context)
def navbar(request):									##returns the corresponding values when template navbar.html is been called.
	total_rows = article.objects.all() 
	context = {'row':total_rows}
	return render(request,'navbar.html',context)

def whereto(request):									##returns the corresponding values when template whereto.html is been called.
	total_rows = article.objects.all() 
	context = {'row':total_rows}
	return render(request,'whereto.html',context)
	