from rest_framework import viewsets
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, 'accounts/home.html')

class AccountListView(ListView):
    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/account_detail.html'

class AccountCreateView(CreateView):
    model = Account
    template_name = 'accounts/account_form.html'
    fields = ['name', 'email', 'app_secret_token']
    success_url = reverse_lazy('account-list')

class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'accounts/account_form.html'
    fields = ['name', 'email', 'app_secret_token']
    success_url = reverse_lazy('account-list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('account-list')

# Destination views
class DestinationListView(ListView):
    model = Destination
    template_name = 'accounts/destination_list.html'
    context_object_name = 'destinations'

class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'accounts/destination_detail.html'

class DestinationCreateView(CreateView):
    model = Destination
    template_name = 'accounts/destination_form.html'
    fields = ['account', 'url', 'name']
    success_url = reverse_lazy('destination-list')

class DestinationUpdateView(UpdateView):
    model = Destination
    template_name = 'accounts/destination_form.html'
    fields = ['account', 'url', 'name']
    success_url = reverse_lazy('destination-list')

class DestinationDeleteView(DeleteView):
    model = Destination
    template_name = 'accounts/destination_confirm_delete.html'
    success_url = reverse_lazy('destination-list')
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['GET'])
def get_account_destinations(request,account_id):
    print(request.get,"request")
    try:
        account = Account.objects.get(id=account_id)
        destinations = account.destinations.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=404)

@csrf_exempt
@require_http_methods(["POST", "GET"])
def incoming_data(request):
    if request.method == 'POST':
        app_secret_token = request.POST['secretToken']
        if not app_secret_token:
            return JsonResponse({"error": "Un Authenticate"}, status=401)
        account = validate_token_and_get_account(app_secret_token)
        if not account:
            return JsonResponse({"error": "Un Authenticate"}, status=401)

        try:
            data = json.loads(account)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid Data"}, status=400)

        
        send_to_destinations(account, data)

        return JsonResponse({"message": "Data received and processed successfully"}, status=200)
    else:
        return render(request, 'accounts/form.html')
        
def validate_token_and_get_account(token):
    account = Account.objects.get(app_secret_token=token)
    if account:
        queryset = Destination.objects.filter(id=account.id) 
        json_data = serializers.serialize('json', queryset)
        return json_data

def send_to_destinations(account, data):
    print(f"Sending data to destinations for account: {account}")
    print(f"Data: {data}")
