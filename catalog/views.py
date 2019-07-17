from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from catalog import models 
from catalog import forms

class Index(TemplateView) :
    template_name = 'catalog/index.html'

    def get(self, request, *args, **kwargs) :
        websites = models.Website.objects.filter(approved = 'True')
        tag_form = forms.FilterByTagForm()
        return render(request, self.template_name, {'tag_form' : tag_form, 'websites' : websites})

    def post(self, request, *args, **kwargs) :
        tag_form = forms.FilterByTagForm(request.POST)
        if tag_form.is_valid() :
            if tag_form.cleaned_data['tag'] == None :
                websites = models.Website.objects.filter(approved = 'True')
                return render(request, self.template_name, {'tag_form': tag_form, 'websites': websites})
            else :
                tag_id = tag_form.cleaned_data['tag'].id
                websites = models.Website.objects.filter(approved = 'True').filter(tag_id = tag_id)
                return render(request, self.template_name, {'tag_form': tag_form, 'websites': websites})
