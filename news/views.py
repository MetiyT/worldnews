from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'news/home.html')

def article(request, article_id):
    return render(request, 'news/article.html', {'article_id': article_id})