from pyclbr import Class
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, DeleteView, TemplateView,DetailView)
from django.db import connections
from django.db.models import Count
from random import randint


def home(request):
    return render(request, 'home.html')


def internal_delay(request):
    return render(request,'internal_delay.html')


def sales_overview(request):
    return render(request,'sales_overview.html')


def invoices_missing(request):
    return render(request,'invoices_missing.html')


def delivery_chain_problem(request):
    return render(request,'delivery_chain_problem.html')


def external_delay(request):
    return render(request,'external_delay.html')


def offer_missing(request):
    return render(request,'offer_missing.html')


def example(request):
    return render(request,'example.html')