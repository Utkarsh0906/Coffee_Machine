def sufficient_resource(Resources,coffee):
    if(Resources['water']<coffee['water'] or Resources['milk']<coffee['milk'] or Resources['coffee']<coffee['coffee']):
        print("Sorry Insufficient Resources")
        return False