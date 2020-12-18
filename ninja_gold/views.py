from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Dictionary For Gold - >>DRY!!<<
gold_map = {
    'farm': (10,20),
    'cave': (5,10),
    'house': (2,5),
    'casino': (0,50),
}

def gold_home(request):
    context = {
        'page_title' : 'Ninja Gold!'
    }
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'gold/index.html', context)

def reset(request):
    request.session.flush()
    return redirect('/')

def process_gold(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        building = gold_map[location] # Access the correct values...
        building_name_upper = location[0].upper() + location[1:]  # Capitalize the building name for the text string
        gold_prize = random.randrange(building[0], building[1]) # Make the gold prize!
        now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p") # Date/Time string for the text string
        result = 'success' # CSS message color class!
        message = f"Earned {gold_prize} gold from the {building_name_upper}! ({now_formatted})" 
        if location == "casino":
            win_or_lose = round(random.random())
            if win_or_lose == 0:
                message = f"Entered a Casino and lost {gold_prize} gold... Ouch... ({now_formatted})"
                result = 'danger'
                gold_prize = gold_prize * -1
        request.session['gold'] += gold_prize
        request.session['activities'].append({"message": message, "result": result})
        return redirect('/')
    if request.method == 'POST':
        location = request.POST["gold_location"]
        building = gold_map[location] # Access the correct values...
        building_name_upper = location[0].upper() + location[1:]  # Capitalize the building name for the text string
        gold_prize = random.randrange(building[0], building[1]) # Make the gold prize!
        now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p") # Date/Time string for the text string
        result = 'success' # CSS message color class!
        message = f"Earned {gold_prize} gold from the {building_name_upper}! ({now_formatted})" 
        if location == "casino":
            win_or_lose = round(random.random())
            if win_or_lose == 0:
                message = f"Entered a Casino and lost {gold_prize} gold... Ouch... ({now_formatted})"
                result = 'danger'
                gold_prize = gold_prize * -1
        request.session['gold'] += gold_prize
        request.session['activities'].append({"message": message, "result": result})
        return redirect('/')





# Code I removed for the sake of not repeating myself!
        # if location == "farm":
        #     gold_prize = random.randrange(10,20)
        #     request.session['gold'] += gold_prize
        # if location == "cave":
        #     gold_prize = random.randrange(5,10)
        #     request.session['gold'] += gold_prize
        # if location == "house":
        #     gold_prize = random.randrange(2,5)
        #     request.session['gold'] += gold_prize