import markdown
import html

from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request,title):
    markdown_text=util.get_entry(title)

    if(markdown_text is not None):
        html_text=markdown.markdown(markdown_text) #Conver markdown text to HTML
        notfound=False
    else:
        html_text=""
        notfound=True

    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": html_text,
        "notfound": notfound
    })


