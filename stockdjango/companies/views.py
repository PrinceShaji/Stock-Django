from django.shortcuts import render
from django.http import HttpResponse

def companies(request):
    return render(request, 'companies/companies.html')