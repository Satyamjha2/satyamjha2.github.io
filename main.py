from flask import Flask, render_template, url_for, request
from randomwalk import PolarRWForm, polarRW
from random import randint

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config[""] = ""


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/randomwalk", methods=["GET"])
def randomwalkGET():
    form = PolarRWForm.PRWForm()
    return render_template("randomwalk.html", form=form)


@app.route("/randomwalk", methods=["POST"])
def randomwalkPOST():
    form = PolarRWForm.PRWForm()
    if form.validate_on_submit():
        print("success")
        polarRW.gen_polar_picture(float(form.dtheta.data), int(form.nsteps.data))
    return render_template("randomwalk.html", form=form)


def redirect_url(default="home"):
    return request.args.get("next") or request.referrer or url_for(default)


if __name__ == "__main__":
    app.run(debug=True)
