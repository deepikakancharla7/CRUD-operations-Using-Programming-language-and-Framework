from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Registration

# Create operation
def create_registration(request):
    if request.method == 'POST':
        data = request.POST
        registration = Registration(name=data['name'], email=data['email'], date_of_birth=data['date_of_birth'])
        registration.save()
        return JsonResponse({'message': 'Registration created successfully.'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

# Read operation
def get_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    return JsonResponse(registration.serialize())

# Update operation
def update_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    if request.method == 'PUT':
        data = request.PUT
        registration.name = data.get('name', registration.name)
        registration.email = data.get('email', registration.email)
        registration.date_of_birth = data.get('date_of_birth', registration.date_of_birth)
        registration.save()
        return JsonResponse({'message': 'Registration updated successfully.'})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

# Delete operation
def delete_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    if request.method == 'DELETE':
        registration.delete()
        return JsonResponse({'message': 'Registration deleted successfully.'})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
