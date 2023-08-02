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

    #print("If I save NGN" + str(contribution) + " " + frequency + " for " + str(time_months) +
    # " months, I will have a balance of NGN" + str(amount) +
    # "and would have received an interest of NGN" + str(interest))
    return [interestValue, amount]


def standard_budget(monthly_income):
    needs = 0.5 * monthly_income
    wants = 0.3 * monthly_income
    savings = 0.2 * monthly_income

    return [needs, wants, savings]


def custom_budget(monthly_income, needs_percent, want_percentage, savings_percentage):
    needs = (needs_percent/100) * monthly_income
    wants = (want_percentage/100) * monthly_income
    savings = (savings_percentage/100) * monthly_income

    return [needs, wants, savings]


def essential_expenses(monthly_income, transportation, data_airtime,
                       groceries, utilities, rent_contribution, debt_repayment=0,
                       custom_budget_select=False, needs_percent=50, want_percentage=30, savings_percentage=20):

    if custom_budget_select:
        needs = custom_budget(monthly_income, needs_percent, want_percentage, savings_percentage)[0]
    else:
        needs = standard_budget(monthly_income)[0]

    total = transportation + data_airtime + groceries + utilities + rent_contribution + debt_repayment

    over = False

    if needs - total < 0:
        over = True

    return [total, over, needs-total]
