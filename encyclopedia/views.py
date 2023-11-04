import markdown2, html,random

from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from . import util
from .forms import NewPageForm,EditPageForm

def custom_404_view(request,undefinedpath):
    return render(request,'encyclopedia/custom_404.html',status=404)


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

def create(request):
    errormsg=""
    iserror=False

    if request.method=="POST":
        form=NewPageForm(request.POST)
      
        if form.is_valid():
            title=form.cleaned_data['title_field']
            content=form.cleaned_data['content_field']

            if util.get_entry(title) is None:
                try:
                    util.save_entry(title,content)
                    form=NewPageForm()
                except Exception as e:
                    errormsg="File save operation failed."
                    iserror=True
            else:
                errormsg="The article is already exists."
                iserror=True
        else:
            errormsg="The submitted data is invalid."
            iserror=True
    else:
        form=NewPageForm()

        
    return render(request, "encyclopedia/newpage.html", {
        "form": form,
        "errormessage": errormsg,
        'iserror': iserror
    })

def edit(request,title):
    errormsg=""
    iserror=False

    if request.method=="POST":
        form=EditPageForm(request.POST)
    
        if form.is_valid():
            title=form.cleaned_data['title_field']
            content=form.cleaned_data['content_field']

            if util.get_entry(title) is not None:
                try:
                    util.save_entry(title,content)
                    return HttpResponseRedirect(reverse("encyclopedia:create"))
                except Exception as e:
                    errormsg="File save operation failed."
                    iserror=True
            else:
                errormsg="The article not exists in our repository."
                iserror=True
        else:
            errormsg="The submitted data is invalid."
            iserror=True

    else:
        content=util.get_entry(title)
        if(content is None):
            iserror=True
            errormsg="The article not exists in our repository."

        form=EditPageForm(initial={'title_field': title,'content_field':content})

    return render(request, "encyclopedia/editpage.html", {
        "title":'test',
        "form": form,
        "errormessage": errormsg,
        'iserror': iserror
    })

def randompage(request):
    entries= util.list_entries()
    title=entries[random.randint(0, len(entries))]

    return HttpResponseRedirect(reverse("encyclopedia:title",args=[title]))
