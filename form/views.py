from django.shortcuts import render, redirect
from .models import UserInfo
import re

#insert data
def user_form(request):

    error = {}
    # Holds submitted values so the form can be re-populated on error
    form_data = {'name': '', 'email': '', 'phone': '', 'gender': ''}

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        gender = request.POST.get('gender', '').strip()

        # Keep whatever the user typed so we can redisplay it on error
        form_data = {'name': name, 'email': email, 'phone': phone, 'gender': gender}

        # Name validation
        if not name:
            error['name'] = 'Name is required.'
        elif len(name) < 3:
            error['name'] = 'Name must be at least 3 characters long.'
        elif len(name) > 50:
            error['name'] = 'Name must be at most 50 characters long.'

        # Email validation
        if not email:
            error['email'] = 'Email is required.'
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            error['email'] = 'Invalid email format.'

        # Phone validation
        if not phone:
            error['phone'] = 'Phone number is required.'
        elif not phone.isdigit():
            error['phone'] = 'Phone number must contain only numbers.'
        elif len(phone) != 10:
            error['phone'] = 'Phone number must be exactly 10 digits long.'

        # Gender validation
        # FIX: radio values are lowercase ('male'/'female'/'other') below,
        # so this comparison now actually matches what gets submitted.
        if gender not in ['male', 'female', 'other']:
            error['gender'] = 'Select a gender.'

        if not error:

            UserInfo.objects.create(
                name=name,
                email=email,
                phone=phone,
                gender=gender
            )

            # Clear the form after a successful save
            return render(request, 'user_form.html', {
                'success': 'Registration successful!'
            })

    return render(request, 'user_form.html', {
        'error': error,
        'form_data': form_data,
    })

#select data
def user_list(request):
    users = UserInfo.objects.all()

    return render(request, 'user_list.html', {
        'users': users
    })

#update data
def user_update(request, id):

    user = UserInfo.objects.get(id=id)

    if request.method == 'POST':

        user.name = request.POST.get('name', '').strip()
        user.email = request.POST.get('email', '').strip()
        user.phone = request.POST.get('phone', '').strip()
        user.gender = request.POST.get('gender', '').strip()

        user.save()

        return redirect('user_list')

    return render(request, 'user_update.html', {
        'user': user
    })

#delete data

def user_delete(request, id):

    user = UserInfo.objects.get(id=id)

    if request.method == 'POST':
        user.delete()

    return redirect('user_list')