from django.shortcuts import render
import requests


def converter(request):
    api_response = requests.get('https://api.exchangerate-api.com/v4/latest/usd').json()
    currencies = api_response.get('rates')

    if request.method == "POST":

        curr1 = request.POST['currencies_option1']
        curr2 = request.POST['currencies_option2']
        amount = request.POST['amount']
        price = round(currencies[curr2] / currencies[curr1] * float(amount), 2)
        context = {'currencies': currencies, 'price': price, 'curr1': curr1, 'curr2': curr2, 'amount': amount}

        return render(request, 'app/index.html', context)

    context = {'currencies': currencies}
    return render(request, 'app/index.html', context)

