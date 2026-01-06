from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

HTML = '''
<h2>Admin Panel</h2>
<form method="POST">
Username:<input name="user"><br>
Password:<input name="pass" type="password"><br>
<button>Login</button>
</form>
<p>{{msg}}</p>
'''

@app.route("/", methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST":
        u=request.form["user"]
        p=request.form["pass"]
        con=sqlite3.connect("users.db")
        cur=con.cursor()

        # ❌ LOGIC FLAW – improper auth validation
        q=f"SELECT * FROM users WHERE username='{u}'"
        res=cur.execute(q).fetchone()
        if res and res[2]==p:
            msg="Welcome Admin!"
        else:
            msg="Invalid Login"
    return render_template_string(HTML,msg=msg)

app.run(host="0.0.0.0",port=5000)
