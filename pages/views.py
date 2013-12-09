from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView


from pages.models import Page

# Create your views here.

def index(request):
    latest_page_list = Page.objects.order_by('-word')
    context = { 'latest_page_list': latest_page_list }
    return render(request, 'pages/index.html', context)

def text(request, word):
    page = get_object_or_404(Page, pk=word)
#     page_text = as_html(word)
    return render(request, 'pages/word.html', {'page': page})


# def as_html(word):
#     page = get_object_or_404(Page, pk=word)
#     page_text = page.word_text.lower().split()
#     return page_text

class PageUpdate(UpdateView):
    model = Page
    fields = ['word_text']
    template_name_suffix = '_update_form'
    
class PageCreate(CreateView):
    model = Page
    fields = ['word_text']
    