from flask import Flask, request

app = Flask(__name__)

account_balance = 0


@app.get("/balance", endpoint='balance')
def get_countries():
    return {"Account balance": account_balance}, 200


@app.post("/addMoney", endpoint='addMoney')
def add_money():
    if request.is_json:
        json = request.get_json()
        value = json["value"]
        global account_balance
        account_balance = account_balance + value

        return {"New account balance": account_balance}, 200
    return {"error": "Request must be JSON"}, 415


@app.post("/withdraw", endpoint='withdraw')
def add_money():
    if request.is_json:
        json = request.get_json()
        value = json["value"]
        global account_balance
        account_balance = account_balance - value

        return {"New account balance: ": account_balance}, 200
    return {"error": "Request must be JSON"}, 415
