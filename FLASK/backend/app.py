from flask import Flask, render_template, request, redirect

import mysql.connector
def database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="blog"
    )

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def dashboard():
    conn = database()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT id, Post_Title as title, Author_Name as author, Content as content, created_at FROM post WHERE is_deleted = 1 ORDER BY created_at DESC"
    cursor.execute(query)
    
    posts = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('dashboard.html', posts=posts)





@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        
        if request.is_json:
            data = request.get_json()
            title = data.get('title')
            author = data.get('author')
            content = data.get('content')
        else:
            title = request.form['title']
            author = request.form['author']
            content = request.form['content']

        conn = database()
        cursor = conn.cursor()
        query = "INSERT INTO post (post_Title, Author_Name, Content) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, author, content))
        conn.commit()
        cursor.close()
        conn.close()

        if request.is_json:
            return {
                "code" : 201,
                "message" : "create Successful",
                "status" : "success",
            }, 201

        return redirect('/')

    return render_template('create_post.html')



@app.route('/update-post/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    conn = database()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'GET':
        query = "SELECT id, post_Title as title, Author_Name as author, Content as content FROM post WHERE id = %s"
        cursor.execute(query, (post_id,))
        post = cursor.fetchone()
        cursor.close()
        conn.close()

        if request.is_json:
            return {
                "code" : 200,
                "message" : "Get Successful",
                "status" : "success",
            }, 200

        return render_template('update_post.html', post=post)
    
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_title = data.get('title')
            new_author = data.get('author')
            new_content = data.get('content')
        else:

            new_title = request.form['title']
            new_author = request.form['author']
            new_content = request.form['content']
        
       
        query = "UPDATE post SET post_Title=%s, Author_Name=%s, Content=%s WHERE id=%s"
        cursor.execute(query, (new_title, new_author, new_content, post_id))
        conn.commit()
        cursor.close()
        conn.close()

        if request.is_json:
            return {
                "code" : 200,
                "message" : "update Successful",
                "status" : "success",
            }, 200
        
        return redirect('/')
    





@app.route('/delete-post/<int:post_id>', )
def delete_post(post_id):
    conn = database()
    cursor = conn.cursor()
    
    query = "UPDATE post SET is_deleted = 0 WHERE id = %s"
    cursor.execute(query, (post_id,))
    
    conn.commit()
    cursor.close()
    conn.close()

    if request.is_json:
            return {
                "code" : 200,
                "message" : "Post moved to trash successfully",
                "status" : "success",
            }, 200
    
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)