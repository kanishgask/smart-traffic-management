def signal_control(vehicle_count):

    if vehicle_count < 5:
        return "GREEN 15 sec"

    elif vehicle_count < 15:
        return "GREEN 30 sec"

    else:
        return "GREEN 60 sec"
