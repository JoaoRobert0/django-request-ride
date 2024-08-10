from django.shortcuts import render
from . import business

# Create your views here.
def home(request):
    return render(request, 'home.html')

def request_ride(request):
    ride_value = 0

    if request.method == 'POST':
        ride_type = request.POST.get('ride-type')
        distance_in_km = float(request.POST.get('distance-in-km'))
        
        if ride_type == 'x':
            ride_value = business.CalculateRaceX(distance_in_km).getValue()
        elif ride_type == 'motocycle':
            ride_value = business.CalculateRaceMotocycle(distance_in_km).getValue()
        elif ride_type == 'black':
            ride_value = business.CalculateRaceBlack(distance_in_km).getValue()
           
    ride_value = f"{ride_value:.2f}"
    context = {'ride_value': ride_value}
    return render(request, 'request-ride.html', context)