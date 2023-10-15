from flask import Flask, render_template, request,url_for
# import sqlite3
import resend
import os
import psycopg2
# postgres://raveensbsaini:U7N8FmrFrXNvL5P7brCkYJZA332hhTQp@dpg-ckiqu8b6fquc739in3fg-a.singapore-postgres.render.com/ravindrakumarsaini
app = Flask(__name__)

success = "Your message send successfully!"

# success = "Your message send successfully!"
@app.route("/",methods=["GET","POST"])
def index():
     if request.method == "GET":
         return render_template("index.html")
     elif request.method == "POST":
         name =request.form.get("pname") 
         number = request.form.get("pnumber")
         print(type(number),number)
         number = int(number)
         print(type(number),number)


         email = request.form.get("pemail")
         message = request.form.get("pmessage")
        



         conn = psycopg2.connect(
         database="ravindrakumarsaini",
         user="raveensbsaini",
         password="U7N8FmrFrXNvL5P7brCkYJZA332hhTQp",
         host="dpg-ckiqu8b6fquc739in3fg-a.singapore-postgres.render.com",
         port=5432
         )
        

         cur = conn.cursor()
         cur.execute("select count(*) from person;")
         rows = cur.fetchall()
         id = rows[0][0] +1
         query = "INSERT INTO person (id, name, email, message, number) VALUES ('{id}','{name}','{email}','{message}',{number})".format(id=id,name=name,email=email,message=message,number = number)
         print(query)
         cur.execute(query)

         cur.close()
         conn.commit() 





         resend.api_key = "re_BzNodrVF_9yDdY1Hr3bcVPKCPMnmZ94Bx"

         params = {
             "from": "Acme <onboarding@resend.dev>",
             "to": ["raveensbsaini@gmail.com"],
             "subject": email,
             "html": "<strong>{}<br>{}<br>{}</strong>".format(message,name,number),
         }

         email = resend.Emails.send(params)
    #     print(email)

         return render_template("index.html", success = success)
     return  render_template("index.html")
    # if __name__ == "__main__":
#     app.run()