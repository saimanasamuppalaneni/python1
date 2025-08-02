# trip expenditure
def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Tampa":
        return 183
    elif city == "Charlotte":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los angeles":
        return 475
def rental_car_cost(days):
    if days > 7:
        return 40 * days - 50
    elif days >3:
        return 40 * days - 20
    else:
        return 40*days
def trip_cost(city,days,money_spent):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+money_spent
print(trip_cost("Pittsburgh",8,550))