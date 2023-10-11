from flask import Flask, render_template, request,url_for
# import sqlite3
# import resend
# import os
# postgres://raveensbsaini:U7N8FmrFrXNvL5P7brCkYJZA332hhTQp@dpg-ckiqu8b6fquc739in3fg-a.singapore-postgres.render.com/ravindrakumarsaini
app = Flask(__name__)



# success = "Your message send successfully!"
@app.route("/",methods=["GET","POST"])
def index():
    # if request.method == "GET":
    #     return render_template("index.html")
    # elif request.method == "POST":
    #     name =request.form.get("pname") 
    #     number = request.form.get("pnumber")

    #     email = request.form.get("pemail")
    #     message = request.form.get("pmessage")
    #     number = int(number)
    #     database = sqlite3.connect("database.db")
    #     cur = database.cursor()
    #     cur.execute("INSERT INTO person (name, email, phone, message) VALUES (?, ?, ?, ?)",
    #         (name, email, number, message))
    #     database.commit()
    #     cur.execute("select * from person;")
    #     row = cur.fetchall()
    #     for r in row:
    #         print(r)
    #     database.close()

    # #    re_3piwLq4L_PJaLnrFtgbs5YgTKK3eu7XT3
    #     resend.api_key = os.environ.get("databaseurl1")

    #     params = {
    #         "from": "Acme <onboarding@resend.dev>",
    #         "to": ["raveensbsaini@gmail.com"],
    #         "subject": email,
    #         "html": "<strong>{}<br>{}<br>{}</strong>".format(message,name,number),
    #     }

    #     email = resend.Emails.send(params)
    #     print(email)

    #     return render_template("index.html", success = success)
    return  render_template("index.html")
    # if __name__ == "__main__":
#     app.run()