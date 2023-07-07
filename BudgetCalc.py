from flask import Flask, request, Response  # ,jsonify
from flask_restful import abort
from interest_calc import interest

app = Flask(__name__)

# data = {90001: [20000, "monthly", 180],
#         90002: [5000, "weekly", 90],
#         90003: [3000, "daily", 180],
#         90004: [50000, "monthly", 270],
#         90005: [10000, "weekly", 150]
#         }

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

    # if request.method == 'POST':
    #     new_contribution = request.form["contribution"]
    #     new_frequency = request.form["frequency"]
    #     new_timeframe = request.form["timeframe"]
    #
    #     my_interest = interest(int(new_contribution), int(new_frequency), int(new_timeframe))
    #
    #     return {
    #         "interest": my_interest[0],
    #         "total": my_interest[1]
    #     }


if __name__ == "__main__":
    app.run(debug=True)
