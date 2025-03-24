from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


app =Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    __tablename__="users"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[int]

with app.app_context():
    db.create_all()

@app.route("/test", methods=["GET", "POST"])
def test():
   if request.method == "GET":
      users = db.session.execute(db.select(User)).scalars()

      print(users)
             
      return render_template("index.html", users=users)
       
   else:  
      full_name=request.form["full_name"]      
      email= request.form["email"]
      phone = request.form["phone"]

      user=User(
         full_name=full_name,
         email=email,
         phone=phone
      )
      db.session.add(user)
      db.session.commit()
      
      return redirect("/test")
   

   


if __name__=='__main__':
    app.run(debug=True)