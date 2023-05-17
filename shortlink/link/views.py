from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import LinkForm
from .models import Link




class HomePage(ListView):
    model = Link
    template_name = 'link/home.html'
    context_object_name = 'link'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'

        return ctx

# user = request.user
class LinksPage(FormMixin, ListView):
    model =Link
    template_name = 'link/links.html'
    form_class = LinkForm

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LinksPage, self).get_context_data(**kwargs)

        links = Link.objects.all()

        ctx['links'] = links
        return ctx

    def post(self, request, *args, **kwargs):

        post = request.POST.copy()
        post['avtor'] = request.user

        request.POST = post
        form = LinkForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('links')


