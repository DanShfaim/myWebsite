from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms


class AboutView(TemplateView):
    template_name = 'about.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'


def ContactFormView(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print('submitded')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['phone'])
            print(form.cleaned_data['subject'])
            print(form.cleaned_data['message'])

    return render(request, 'contact.html', {'form': form})