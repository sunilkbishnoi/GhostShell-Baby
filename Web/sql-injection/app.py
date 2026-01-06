from flask import Flask, request, render_template_string
import sqlite3

app=Flask(__name__)

HTML='''
<h2>Employee Portal</h2>
<form method="POST">
Username:<input name="u"><br>
Password:<input name="p" type="password"><br>
<button>Login</button>
</form>
<p>{{msg}}</p>
'''

@app.route("/",methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST":
        u=request.form["u"]
        p=request.form["p"]
        db=sqlite3.connect("users.db")
        cur=db.cursor()

        # ❌ RAW QUERY
        q=f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
        if cur.execute(q).fetchone():
            msg="Dashboard Access Granted"
        else:
            msg="Access Denied"
    return render_template_string(HTML,msg=msg)

app.run(host="0.0.0.0",port=5001)
