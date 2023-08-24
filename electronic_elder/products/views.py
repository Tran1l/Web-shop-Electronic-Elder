from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Electronic Elder', 
    }
    return render(request, 'products/index.html', context=context)

def contacts(request):
    return render(request, 'products/contacts.html')