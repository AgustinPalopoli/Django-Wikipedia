from django.shortcuts import render,redirect
from django.contrib import messages

from . import util
from markdown2 import markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def entry(request,title):
    content = util.get_entry(title.strip())
    error = 0
    if content == None:
        content = "Error! page was not found :("
        error = 1
    content = markdown(content)
    return render(request, "encyclopedia/entry.html", {'content': content, 'title': title,'error':error})

def search(request):
    q = request.GET.get('q').strip().upper()
    entrys = util.list_entries()
    entrysWS = []
    for i in range(0,len(entrys)):
        if q in entrys[i].upper():
            if q == entrys[i].upper():
                return redirect("encyclopedia:entry",title=entrys[i])
            else:
                entrysWS.append(entrys[i])
    return render(request, "encyclopedia/search.html", {'entries': entrysWS})

def newpage(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title == "" or content == "":
            messages.info(request, 'Error! You need to fill all the form')
            return redirect("encyclopedia:newpage")
        else:
            entrys = util.list_entries()
            for i in range(0,len(entrys)):
                if title.upper() in entrys[i].upper():
                    messages.info(request, 'Error! Encyclopedia entry already exists')
                    return redirect("encyclopedia:newpage")
            util.save_entry(title, content)
            return redirect("encyclopedia:entry",title=title)
    return render(request, "encyclopedia/newpage.html")

def editpage(request, title):
    content = util.get_entry(title)
    if request.method == "POST":
        contentE = request.POST.get('contentE').rstrip()
        if contentE != content:
            util.save_entry(title,contentE)
            return redirect("encyclopedia:entry",title)
    return render(request, "encyclopedia/editpage.html",{'title': title,'content':content})

def random_page(request):
    entries = util.list_entries()
    random_title = random.choices(entries)
    return redirect("encyclopedia:entry", title=random_title[0])