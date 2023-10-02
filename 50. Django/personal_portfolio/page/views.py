from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request):
    page = Page.objects.order_by('-date')
    return render(request, 'page/page.html', {'pages': page})

def more(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    # pk - это ключ, Blog - модель 
    # return render(request, 'blog/detail.html', {'blog_id': blog_id}) было только это 
    return render(request, 'page/more.html', {'page': page})
