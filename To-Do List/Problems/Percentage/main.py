def get_percentage(number_v, round_digit = None):
    if round_digit == None:
        gg = round(number_v*100)
    else:
        gg = round(number_v*100, round_digit)
    return str(gg)+'%'
