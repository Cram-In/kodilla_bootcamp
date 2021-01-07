from flask import Flask, render_template, request, redirect, url_for, flash
from config import app
from model import Contacts, db


@app.route("/", methods=["GET"])
def homepage():
    movies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # movies_list = movies  # full view
    movies_list = movies[:4]  # restricted view
    return render_template("homepage.html", movies=movies_list)


@app.route("/about/")
def about_us():
    return render_template("about.html")


@app.route("/services/")
def get_services():
    return render_template("services.html")


@app.route("/contact/", methods=["POST", "GET"])
def contact_us():
    if request.method == "POST":

        if (
            not request.form["name"]
            or not request.form["email"]
            or not request.form["phone"]
            or not request.form["message"]
        ):
            flash("Please enter all required data", "error")
        else:
            new_message = Contacts(
                request.form["name"], request.form["email"], request.form["phone"], request.form["message"]
            )

            db.session.add(new_message)
            db.session.commit()
            flash("Message successfully send.")
            return render_template("/contact.html")
    return render_template("/contact.html")


@app.route("/<int:movie_id>/")
def get_movie():
    return "Hey!!! moving pictures"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)