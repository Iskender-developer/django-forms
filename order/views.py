
from django.shortcuts import render, redirect
from .forms import OrderForm


def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            p = data['product']
            q = data['quantity']
            d = data['delivery']

            prices = {
                'laptop': 5000000,
                'phone': 3000000,
                'headphones': 200000,
            }

            result = prices[p] * q

            if d == 'courier':
                result += 30000

            request.session['order'] = {
                'name': data['name'],
                'phone': data['phone'],
                'product': p,
                'quantity': q,
                'delivery': d,
                'address': data['address'],
                'total': result,
            }

            return redirect('oresult')

    else:
        form = OrderForm()

    return render(request, 'order/home.html', {'form': form})


def result(request):
    order = request.session.get('order')

    if not order:
        return redirect('home')

    return render(request, 'order/result.html', {'order': order})
