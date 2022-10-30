from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgres://aoevcjxijbvzui:7a977da6e94473b7b66497dd56b7a31792280eda65b0d5710e235c5ed2e3fbb9@ec2-44-209-57-4.compute-1.amazonaws.com:5432/d8t0kmpfhbcmur'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' # this is a default command to start with SQLALCHEMY and 
#here 'SQLALCHEMY_DATABASE_URI' is the path to where the DB is stored
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author = db.Column(db.String(100),nullable=False,default='Anonymous')
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow) #try using func.now() or func.current_timestrap() however this is an "important function"
    
    def __repr__(self):   #executes everytime the BlogPost class is executed
        return 'Blog post ' + str(self.id)

#after setting up this db. Open python3 in terminal and run "from app import db" (app.py won't work) and "db.create_all()" to create 'posts.db' file configured above
#dummy data for posts.html
"""
all_post=[{
    "title":"Post 1",
    "content":"This is the content of post 1",
    "author":"Patrick"
},{
    "title":"Post 2",
    "content":"This is the content of post 2",
    "author":"Stephen"}
    ]
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts',methods=['GET','POST'])
def posts():             #if the html form submits(posts) any data using this function the data is inputed to db
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post_delete=BlogPost.query.get_or_404(id)         #gets the id if exists else displays a 404 error 
    db.session.delete(post_delete)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post_edit=BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post_edit.title = request.form['title']     #we use post.title(post as object) to access the title content in the
        post_edit.content = request.form['content']
        post_edit.author = request.form['author']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html',post=post_edit)

if __name__=="__main__":
    app.run(debug=True)


