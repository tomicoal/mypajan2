from flask import Flask, render_template, request
import smtplib


my_email = "pythontesttomasmico@gmail.com"
my_password = "oykjncmgnxdvjtig"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Making connection secure
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="tmico92@gmail.com",
                msg=f"Subject:Message from the blog.\n\nEmail from {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n")
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

