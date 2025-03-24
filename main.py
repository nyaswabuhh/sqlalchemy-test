from flask import Flask, render_template,request, redirect

app =Flask(__name__)


@app.route("/test", methods=["GET", "POST"])
def test():
   if request.method == "GET":
             
      return render_template("index.html")
       
   else:  
      full_name=request.form["full_name"]
      phone = request.form["phone"]
      email= request.form["email"]


      return redirect("/test")


if __name__=='__main__':
    app.run(debug=True)