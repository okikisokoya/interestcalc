# Determining the interest rate based on the time frame (months) and principle at maturity
def ratecalc(time_months, principle):
    rate = 0.0
    time = time_months * 30

    if 90 <= time < 180:
        if principle < 1000000:
            rate = 0.085
        elif principle > 5000000:
            rate = 0.095
        else:
            rate = 0.115

    elif 180 <= time < 270:
        if principle < 1000000:
            rate = 0.095
        elif principle > 5000000:
            rate = 0.105
        else:
            rate = 0.125

    elif 270 <= time < 360:
        if principle < 1000000:
            rate = 0.105
        elif principle > 5000000:
            rate = 0.115
        else:
            rate = 0.135

    elif time >= 360:
        if principle < 1000000:
            rate = 0.11
        elif principle > 5000000:
            rate = 0.125
        else:
            rate = 0.15

    else:
        print("Duration cannot be less than 3 months \n")

    return rate


# Method calculating interest
def interest(contribution, frequency, time_months):
    #rate = ratecalc(time, contribution)

    multiplier = 1
    if frequency == "daily":
        multiplier = 30
    elif frequency == "weekly":
        multiplier = 4

    # finding out the principle at maturity
    principle = contribution * multiplier * time_months

    # calculating rate
    rate = ratecalc(time_months, principle)
    time = time_months * 30
    interestValue = (principle * (rate * (time / 360)))
    amount = principle + interestValue

    #print("If i save NGN" + str(contribution) + " " + frequency + " for " + str(time_months) + " months, I will have a balance of NGN" + str(amount) + "and would have accured an interest of NGN" + str(interest))
    return [interestValue, amount]