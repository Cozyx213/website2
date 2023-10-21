import sqlite3 , datetime, phrases, os
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
app=Flask(__name__)
app.debug = True
db = sqlite3.connect("enrollees.db",check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

@app.route('/show_ppt', methods=['GET','POST'])     
def show_ppt():
    # Get the subject value from the form
    subject = request.form.get('subject')
    # Get the list of files for that subject
    ppt_files = get_ppt_files(subject)
    file_info = []
    # Render the template with the list of files
    base_file_path = f"modules/{subject}"
    for filename in ppt_files:
        file_path = os.path.join(base_file_path, filename)
        size = get_file_size(file_path)
        file_info.append({'filename': filename, 'size': size, 'subject': subject})

    return render_template('Resources.html', file_info=file_info)
@app.route('/Resources')
def resource_download():
    return render_template('Resources.html')
 
def get_ppt_files(subject):
    file_path = f"modules/{subject}"
    files = []
    for filename in os.listdir(file_path):
        #if filename.endswith(".pdf"):  # You can adjust the file extension if needed
        files.append(filename)
    files.sort()
    return files
    

@app.context_processor
def inject_get_file_size():
    return dict(get_file_size=get_file_size)
def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path) # size in bytes
        if size >= (1024 * 1024 * 1024): # size is greater than or equal to 1 GB
            size = size / (1024 * 1024 * 1024) # size in GB
            unit = "GB"
        elif size >= (1024 * 1024): # size is greater than or equal to 1 MB
            size = size / (1024 * 1024) # size in MB
            unit = "MB"
        elif size >= 1024: # size is greater than or equal to 1 KB
            size = size / 1024 # size in KB
            unit = "KB"
        else: # size is less than 1 KB
            unit = "bytes"
        size = round(size, 1) # round the size to one decimal place
        return f"{size} {unit}"
    except OSError:
        return "0 bytes"
    

@app.route('/download_ppt/<subject>/<ppt_filename>')
def download_ppt(subject,ppt_filename):
    file_path =f"modules/{subject}"
    return send_from_directory(file_path, ppt_filename, as_attachment=True)

@app.route('/')
def endix():
    return render_template("endix.html")
@app.route("/Create")
def Create():
    return render_template('Create.html')
@app.route("/Chemistry")
def Chemistry():
    return render_template('Chemistry.html')

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


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        uploaded_subject= request.form['subject']
        if uploaded_file and uploaded_subject:
            # Save the uploaded file to a directory
            file_path = f"modules/{uploaded_subject}/{uploaded_file.filename}"
            uploaded_file.save(file_path)

            # You can process or further handle the file here

            return "File uploaded successfully."

    return render_template('upload.html')      
@app.route("/chemistryData")
def Chemistry_data():
    conn = sqlite3.connect('flashcards.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Retrieve flashcards from the database
    cursor.execute('SELECT * FROM flashcards')
    elements = cursor.fetchall()
    #cursor.execute('SELECT * FROM compounds')
    #compounds = cursor.fetchall()

    cursor.execute('SELECT * FROM polyions')
    compounds = cursor.fetchall()

    cursor.execute('SELECT * FROM acids')
    acids = cursor.fetchall()

    cursor.execute('SELECT * FROM ions')
    ions = cursor.fetchall()

    compounds_list = [dict(row) for row in compounds]
    elements_list = [dict(row) for row in elements]
    acids_list = [dict(row) for row in acids]
    ions_list = [dict(row) for row in ions]
    conn.close()
    
    return {'elements':elements_list,
             'compounds': compounds_list,
             'acids':acids_list,
             'ions':ions_list,
             'phrases':phrases.PHRASES()
            }

#if __name__ == "__main__":
#Specify the host and port here
#    app.run(host="192.168.1.2", port=5100)
