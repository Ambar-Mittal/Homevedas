from django.db.models import query
from django.http import response
from django.shortcuts import render, HttpResponse
from .models import Product
import json
# Create your views here.
def index(request):
    if request.method == "POST":
        query=(request.POST.get('search', ''))
        try:
            obj=Product.objects.filter(product_name=query)
            objects=[]
            for item in obj:
                objects.append({'name':item.product_name, 'fat':item.fat, 'protein':item.protein, 'carbohydrate':item.carbohydrate, 'energy':item.energy, 'desc':item.desc})
                response=json.dumps(objects, default=str)
            return HttpResponse(response)
        except Exception as e:
            return HttpResponse('{}')    
        # params={'obj':obj}
    return render(request, 'nutrition/index.html')

def about(request):
    return render(request, 'nutrition/about.html')

def fruit(request):
    return render(request, 'nutrition/fruits.html')

def vegetables(request):
    return render(request, 'nutrition/vegetables.html')

def dairy(request):
    return render(request, 'nutrition/dairy.html')

def spices(request):
    return render(request, 'nutrition/spices.html')

# def searchmatch(query, item):
#     if query in item.desc or query in item.product_name or query in item.category:
#         return True
#     else:
#         return False

def search(request):
    query=(request.POST.get('search', ''))
    # catprods = Product.objects.values('category')
    # print(catprods)
    # cats = {item["category"] for item in catprods} 
    # for cat in cats:
    obj=Product.objects.get(product_name=query)
    params={'obj':obj}
    return render(request, "nutrition/index.html", params)






            