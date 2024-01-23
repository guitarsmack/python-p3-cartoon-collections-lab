def roll_call_dwarves(names):
    for name in names:
        print(f"{str(names.index(name) + 1 )}. {name.capitalize()}")
    pass

def summon_captain_planet(calls):
    return [ call.capitalize() + '!' for call in calls ]
    pass

def long_planeteer_calls(calls):
    while True:
        for call in calls:
            if len(call) > 4:
                return True
        return False

    pass

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None
    pass
