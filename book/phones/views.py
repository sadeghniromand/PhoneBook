from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .forms import CreatPhone
from . import models, serializers
from django.views.generic import ListView


class CreatPhoneNumber(LoginRequiredMixin, CreateView):
    model = models.PhoneBook
    form_class = CreatPhone
    template_name = 'phones/creat_phone.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return JsonResponse(data={'message': "save phone number", 'success': True, }, status=200)

    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse(data={'success': False}, status=400)


class ListPhoneBookView(LoginRequiredMixin, ListView):
    model = models.PhoneBook
    template_name = "phones/phone_book.html"
    context_object_name = "object"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class SearchPhoneNumber(LoginRequiredMixin, ListView):
    template_name = "phones/search_phone.html"
    context_object_name = "object"

    def get(self, request, *args, **kwargs):
        if request.GET.get("phone", None):
            data = self.get_queryset()
            return JsonResponse(status=200, data={"success": True, "results": list(data.values())})
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = models.PhoneBook.objects.all()
        qs = qs.filter(user=self.request.user)
        if self.request.GET.get("phone", None):
            phone = self.request.GET.get("phone")
            typ = self.request.GET.get("type")
            if typ == "exact":
                qs = qs.filter(phone_number__exact=phone)
            elif typ == "first":
                qs = qs.filter(phone_number__startswith=phone)
            elif typ == "end":
                qs = qs.filter(phone_number__endswith=phone)
            elif typ == "cont":
                qs = qs.filter(phone_number__contains=phone)
        return qs


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = models.PhoneBook.objects.all()
    serializer_class = serializers.PhoneSerializers

    # def create(self, request, *args, **kwargs):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class ReadPhoneViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing phones.
    """
    queryset = models.PhoneBook.objects.all()
    serializer_class = serializers.ReadPhoneSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^phone_number', '=phone_number']

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
