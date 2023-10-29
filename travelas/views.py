from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import RequestContext
from travelas.models import Car
from travelas.models import Page
from travelas.forms import CarForm
from travelas.forms import PageForm
#from travelas.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from travelas.forms import UserForm, UserProfileForm

# Create your views here.

def index(request):

    context = RequestContext(request)

    car_list = Car.objects.order_by('-name')[:10]
    context_dict = {'cars' : car_list}

    for car in car_list:
        car.url = car.name.replace(' ', '_')

    return render(request, 'travelas/index.html', context_dict)

def car(request, car_name_url):

    # Request context from the request passed .
    context = RequestContext(request)

    # Replacing the underscores with spaces again to get the name.
    car_name = car_name_url.replace('_', ' ')

    # Containing the name of the car passed by the user.
    context_dict = {'car_name': car_name}

    try:
         
        car = Car.objects.get(name=car_name)

        pages = Page.objects.filter(car=car)

        context_dict['pages'] = pages

        # Use this in the template to check that the car exists.
        context_dict['car'] = car
    except Car.DoesNotExist:
        
        pass

    #  Render response and return it to the client.
    return render(request, 'travelas/car.html', context_dict)


def add_car(request):

    # Get the context from the request.
    context = RequestContext(request)

    # HTTP POST
    if request.method == 'POST':
        form = CarForm(request.POST)

        # Checking if the form is valid
        if form.is_valid():

            # Save the new car to database
            form.save(commit = True)

            # Calling the index() view to display homepage
            return index(request)

        else:
            print(form.errors)

    else:
        form = CarForm()

    # If form is bad neither details are good render the form with error
    return render(request, 'travelas/add_car.html', {'form': form},)                


def add_page(request, car_name_url):
    context = RequestContext(request)

    car_name = decode_url(car_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit = False)

            try:

                cat = Car.objects.get(name = car_name)
                page.car = vehicles_cat
            except Car.DoesNotExist:
                return render(request, 'travelas/add_car.html', {}, context)

            page.views = 0
            
            page.save()

            return car(request, car_name_url)

        else:
            print(form.errors)
    else:
        form = PageForm()

    return render(request, 'travelas/add_page.html', {'car_name_url': car_name_url, 'car_name' : car_name, 'form' : form}, context) 
    

 

def register(request):
    
    context = RequestContext(request)

    
    registered = False

    # If it's a HTTP POST,  process form data.
    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

             
            user.set_password(user.password)
            user.save()

            
            profile = profile_form.save(commit=False)
            profile.user = user

             
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

             
            profile.save()

             
            registered = True

         
        else:
            print (user_form.errors, profile_form.errors)

     
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'travelas/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},)                               