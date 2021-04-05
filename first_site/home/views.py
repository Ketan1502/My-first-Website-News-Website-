from django.shortcuts import render,HttpResponse
from datetime import date
from home.models import Contact
from django.contrib import messages
from newsapi import NewsApiClient
# Create your views here.
def home(request):
    return render (request,'home.html')
    
    
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('number')
        area=request.POST.get('area')
        contact=Contact(name=name,email=email,phone=phone,area=area,date=date.today())
        contact.save()
        messages.success(request,"Your form has been submitted")
    return render (request,'contact.html')

def newssource(request):
    newsapi=NewsApiClient(api_key='9abbc50e95b04fea94addd0c7fee19ed')
    headlines=newsapi.get_top_headlines(sources='bbc-news')
    articles=headlines['articles']
    title=[]
    desc=[]
    img=[]
    for i in range(len(articles)):
        article=articles[i]
        title.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
    mylist=zip(title,desc,img)
    return render (request,'news.html',context={'mylist': mylist})

