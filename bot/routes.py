from flask import request, jsonify, render_template
from bot import app, db
from bot.functions import send_message
from bot.models import Enzyme
from bot.forms import AddForm


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
        return jsonify(r)
    return render_template("index.html")


@app.route("/info/")
def db_info():
    all_data = db.session.query(Enzyme).all()
    return render_template("db_info.html", all_data=all_data)


@app.route("/addition/", methods=["GET", "POST"])
def addition():
    form = AddForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        catalogue_number = form.catalogue_number.data
        quantity = form.quantity.data
        enzyme = Enzyme(name=name, catalogue_number=catalogue_number, quantity=quantity)
        db.session.add(enzyme)
        db.session.commit()
        return f"Enzyme {name} was successfully added"
    else:
        return render_template("addition.html", form=form)
