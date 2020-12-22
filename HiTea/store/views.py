from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect(request.path_info + '#contact')
    else:
        c_form = ContactForm
        
    context = {
        'c_form': c_form,
    }
    return render(request, 'store/home.html', context)


def error_404_view(request, exception):
    return render(request, 'store/404.html')


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "",
        "Sitemap: http://hiteato.ca/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")