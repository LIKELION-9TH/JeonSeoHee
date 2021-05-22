from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def detail(request):
    return render(request, 'detail.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    dictionary = {}

    for word in words:
        if word in dictionary:
            #increase
            dictionary[word] += 1
        else:
            #add to dictionary
            dictionary[word] = 1
            
    return render(request, 'result.html', {'full': text, 'total':len(words), 'dictionary':dictionary.items()}) 