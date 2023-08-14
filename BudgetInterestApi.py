from flask import Flask, request, Response
from BudgetInterestCode import standard_budget, custom_budget, essential_expenses, interest
from moneyPersonalitiesCode import money_personality
from flask_restful import abort


app = Flask(__name__)


def abort_contribution(contribution):
    if contribution < 0:
        abort(400, message="Value is invalid - cannot use negative value")


def abort_frequency(frequency):
    if frequency not in ["daily", "weekly", "monthly"] or len(frequency.strip()) == 0:
        abort(400, message="Select a valid frequency.")


def abort_time(timeframe):
    if timeframe < 3:
        abort(400, message="Time cannot be less than 90 days! (3 months)")


@app.route('/', methods=['GET'])
def default():
    if request.method == 'GET':
        return {
            'contribution': 0,
            'frequency': "daily",
            'time frame': 90,
        }


@app.route('/<int:contribution>/<frequency>/<int:timeframe>', methods=['GET'])
def calculation(contribution, frequency, timeframe):
    if request.method == 'GET':

        # abort_frequency(frequency)
        # abort_contribution(contribution)
        # abort_time(timeframe)
        if contribution < 0:
            return Response('Contribution cannot be negative', 400)

        if frequency not in ["daily", "weekly", "monthly"] or len(frequency.strip()) == 0:
            return Response('Please enter a valid time frame', 400)

        if timeframe < 3:
            return Response('Time frame cannot be less than 3 months (90 days)', 400)

        my_interest = interest(int(contribution), frequency, int(timeframe))
        return {
            "interest": round(my_interest[0], 2),
            "total": round(my_interest[1], 2),
        }


@app.route('/<int:monthly_income>/<custom_budget_select>', methods=['GET'])
def calculation(monthly_income, custom_budget_select, needs=50, wants=30, savings=20):
    if request.method == 'GET':

        if monthly_income < 0:
            return Response('Income cannot be negative!', 400)
        if needs+wants+savings != 100:
            return Response('Percentages must add up to 100!', 400)

        budget = [0, 0, 0]
        if custom_budget_select:
            budget = custom_budget(monthly_income, 50, 15, 35)
        else:
            budget = standard_budget(monthly_income)

        return{
            "Essential Needs": budget[0],
            "Wants": budget[1],
            "Savings/Investments/Debt Contribution": budget[2]
        }


@app.route('/essential-spending-limit-reached', methods=['GET'])
def essential_limit():
    if request.method == 'GET':
        monthly_income = int(request.args.get('monthly_income'))
        transportation = int(request.args.get('transportation'))
        data_airtime = int(request.args.get('data_airtime'))
        groceries = int(request.args.get('groceries'))
        utilities = int(request.args.get('utilities'))
        rent_contribution = int(request.args.get('rent_contribution'))
        debt_repayment = int(request.args.get('debt_repayment'))
        custom_budget_select = bool(request.args.get('custom_budget_select'))
        needs_percentage = int(request.args.get('needs_percentage'))
        want_percentage = int(request.args.get('want_percentage'))
        savings_percentage = int(request.args.get('savings_percentage'))

        result = essential_expenses(monthly_income, transportation,
                                    data_airtime, groceries, utilities,
                                    rent_contribution, debt_repayment,
                                    custom_budget_select, needs_percentage,
                                    want_percentage, savings_percentage)

        return {
            "Total spending on essential needs": result[0],
            "Are we over budget?": result[1],
            "Remaining left of essential needs budget": result[2]
        }

@app.route('/my-money-personality/<given_responses>', methods=['GET'])
def processing_money_personality(given_responses):
    if request.method == 'GET':
        if len(given_responses) < 13:
            return Response('Responses are incomplete!', 400)
        else:
            return money_personality(given_responses)

if __name__ == "__main__":
    app.run(debug=True)
