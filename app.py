"""
This is entrypoint of our application
"""
from re import I
from dotenv import dotenv_values, load_dotenv
from os import path
from flask import Flask, render_template, request
from scrapper.currency_scrapper import get_currency_rate, currency_calculate


app = Flask(__name__)

# This is the file where we pass the environment variables.
dotenv_path = path.join(path.dirname(__file__), ".env")
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", request_type="clean_input")
    else:
        # user input
        requested_amount: float = float(request.form["currency_from"])
        # user selection base currency
        currency_from = request.form.get("currency_from_select")
        # user selection target currency
        currency_to = request.form.get("currency_to_select")
        # target currency scrapped rate
        rate: float = get_currency_rate(
            currency_from=currency_from, currency_to=currency_to
        )
        # calculated amount
        calculated_amount = currency_calculate(
            rate_of_currency=rate, amount_of_money=requested_amount
        )
        # return answer
        return render_template(
            "index.html",
            calculated_amount=calculated_amount,
            request_type="set_value",
            currency_to_amount=str(requested_amount),
        )


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
