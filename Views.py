from django.shortcuts import render, get_object_or_404, redirect
from .models import Registration
from .forms import RegistrationForm

def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registration_list.html', {'registrations': registrations})

def registration_create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

def registration_update(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'registration_form.html', {'form': form})

def registration_delete(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('registration_list')
    return render(request, 'registration_confirm_delete.html', {'object': registration})
