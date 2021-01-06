from flask import request, jsonify
from bot import app, db
from bot.functions import send_message
from bot.models import Enzyme


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        r = request.get_json()
        chat_id = r["message"]["chat"]["id"]
        message = r["message"]["text"]
        input_data = message.split()
        if len(input_data) == 2:
            cat_id, amount = input_data
            data = db.session.query(Enzyme).filter(Enzyme.catalogue_number==cat_id).first()
            if data:
                data.quantity -= int(amount)
                db.session.commit()
                send_message(chat_id, text=f"Current amount is {data.quantity}")
            else:
                send_message(chat_id, "Wrong cat_id")
        else:
            send_message(chat_id, "Wrong data format")
        # if "Инга" in message:
        #     send_message(chat_id, text="Хрюня")
        # elif "Алексей" in message:
        #     send_message(chat_id, "зайчонок")
        return jsonify(r)
    return "<h1>Hello bot!</h1>"
