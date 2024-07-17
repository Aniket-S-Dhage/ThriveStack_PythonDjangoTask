from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import RegisterForm

class ListOrdersView(View):

    def get(self, request):
        template_name = 'listorders.html'
        orders = Task.objects.all()
        context = {"orders": orders}
        return render(request, template_name, context)


class AddOrderView(View):

    def get(self, request):
        template_name = 'AddOrder.html'
        context = {"form": RegisterForm}
        return render(request, template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        template_name = 'AddOrder.html'
        context = {"form": RegisterForm}
        if form.is_valid():
            form.save()
            return redirect('/orderapp/showlist/')
        return render(request, template_name, context)

