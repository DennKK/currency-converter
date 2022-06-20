from django.shortcuts import render
from django.views import View
import requests

class Converter(View):
    api_response = requests.get('https://api.exchangerate-api.com/v4/latest/usd').json()
    currencies = api_response.get('rates')

    def get(self, request):
        context = {'currencies': currencies}
        return render(request, 'app/index.html', context)

    def post(self, request):
        curr1 = request.POST['currencies_option1']
        curr2 = request.POST['currencies_option2']
        amount = request.POST['amount']
        price = round(currencies[curr2] / currencies[curr1] * float(amount), 2)
        context = {'currencies': currencies, 'price': price, 'curr1': curr1, 'curr2': curr2, 'amount': amount}
        return render(request, 'app/index.html', context)