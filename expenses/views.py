from django.shortcuts import render

# Create your views here.
# Contains logic for handling requests and responses

def index(request):
    return render(request, 'expenses/index.html')

def add_expense(request):
    return render(request, 'expenses/add_expense.html')

