import sqlite3 , datetime, phrases
from flask import Flask, render_template, request, redirect, url_for, jsonify
app=Flask(__name__)
db = sqlite3.connect("enrollees.db",check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

@app.route('/')
def endix():
    return render_template("endix.html")

@app.route("/Form")
def Form():
    return render_template("Form.html", strands=phrases.STRANDS(), sections=phrases.SECTIONS())

@app.route("/History")
def history():
    return render_template('History.html')

@app.route("/Campus_Map")
def Map():
    return render_template('Campus_Map.html')

@app.route("/leaderboards", methods = ["POST"])
def Enroll():   
    username = request.form.get("name")
    score = request.form.get("score")
    time = request.form.get("total_time_spent")

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%m-%d-%y %H:%M:%S')

    print(username,score,time,formatted_datetime)
    if not username:
       return render_template('fail.html')
    
    db.execute("INSERT INTO userscores (name, score, time, date) VALUES (?, ?, ?, ?)", (username, score,time,formatted_datetime))
    db.commit()         
    return redirect('/Enrollees')   
                
@app.route("/Enrollees")
def Enrollees():
    userscores=db.execute("SELECT * FROM userscores")
    return render_template('Enrollees.html', userscores=userscores)  

@app.route("/EnrolleesJSON")
def EnrolleesJSON():
    sort_column = request.args.get('sort', default='score')  # Default to sorting by score
    # Adjust the SQL query based on the selected column
    if sort_column == 'time':
        userscores = db.execute("SELECT * FROM userscores ORDER BY time ASC, score DESC").fetchall()
    elif sort_column == 'date':
        userscores = db.execute("SELECT * FROM userscores ORDER BY date DESC, score DESC").fetchall()
    elif sort_column == 'name':
        userscores = db.execute("SELECT * FROM userscores ORDER BY name ASC, score DESC, time DESC").fetchall()    
    else:
        # Default sorting by score
        userscores = db.execute("SELECT * FROM userscores ORDER BY score DESC, time ASC").fetchall()
    
    userscores_list = [{"id": row["id"], "name": row["name"], "score": row["score"], "time": row["time"], "date": row["date"]} for row in userscores]
    return jsonify(userscores_list)

@app.route("/Deregister", methods =["post"])
def deregister():
    id=request.form.get("id")
    if id:
        db.execute("DELETE FROM enrollees WHERE id=?", [id] )
        db.commit()
    return redirect("/Enrollees")   

@app.route("/Chemistry")
def Chemistry():
    return render_template('Chemistry.html')
                           
@app.route("/chemistryData")
def Chemistry_data():
    conn = sqlite3.connect('flashcards.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Retrieve flashcards from the database
    cursor.execute('SELECT * FROM flashcards')
    elements = cursor.fetchall()
    cursor.execute('SELECT * FROM compounds')
    compounds = cursor.fetchall()
    
    compounds_list = [dict(row) for row in compounds]
    elements_list = [dict(row) for row in elements]
    conn.close()
    
    return {'elements':elements_list,
             'compounds': compounds_list,
            'phrases':phrases.PHRASES()
            }
#if __name__ == "__main__":
#Specify the host and port here
#    app.run(host="192.168.1.2", port=5100)
