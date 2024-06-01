from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        api_url = 'http://starc009.pythonanywhere.com/'
        response = requests.get(api_url)
        data = response.json()
        cost = None
        for item in data:
            if item['name'].lower() == name.lower():
                cost = item['cost']
                break
        return render(request, 'result.html', {'name': name, 'cost': cost})
    return render(request, 'index.html')
