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
