import markdown2
import html

from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from django.urls import reverse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request,title):
    markdown_text=util.get_entry(title)

    if(markdown_text is not None):
        html_text=markdown2.markdown(markdown_text) #Convert markdown text to HTML
        notfound=False
    else:
        html_text=""
        notfound=True

    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": html_text,
        "notfound": notfound
    })

def search(request):
    if request.method=='POST':
        search_title=request.POST.get('q','')
        if util.get_entry(search_title) is not None:
            redirect_url=reverse('encyclopedia:title',args=[search_title])
            return HttpResponseRedirect(redirect_url)
        else:
            entries=util.list_entries()
            filtered_entries=[x for x in entries if search_title.lower() in x.lower() ]
            return render(request, "encyclopedia/index.html", {
                "entries": filtered_entries
            })
