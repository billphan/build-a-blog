# Assignment: Build-a-Blog
# In this assignment, we will build a web app that displays blog posts on a main page and allows users to add new blog posts on a form page. After submitting a new blog entry on the form page, the user is redirected to a page that displays only that blog (rather than returning to the form page or to the main page). Each blog post has a title and a body.

# TODO - Display the posts in order of most recent to the oldest (the opposite of the current order).
# TODO - Add flash messages indicating successful post?

# importing necessary modules + session + flask?
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
# importing datetime for bonus in reverse ordering blog posts
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['DEBUG'] = True

# SQL database configuration: username:password@server:portnumber/databasename
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
# generated random secret_key
app.secret_key = 'xfd{H\xe5<\xf9\x6a2\xa0\x9fR"\xa1\xa8'

# creating blog persistent class
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1200))
    pub_date = db.Column(db.DateTime)
    # initializer or constructor for blog class
    def __init__(self, title, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

# route to main blog page
@app.route('/blog')
def index():
    blog_id = request.args.get('id')
    blogs = Blog.query.all()

    if blog_id:
        post = Blog.query.get(blog_id)
        blog_title = post.title
        blog_body = post.body
        # user case #1 send user to individual entry page.
        return render_template('entry.html', title="Blog Entry #" + blog_id, blog_title = blog_title, blog_body = blog_body)
    else:
        return render_template('blog.html', title="Build A Blog", blogs = blogs)

# handler route to new post page.
@app.route('/post')
def new_post():
    return render_template('post.html', title="Add New Blog Entry")

# handler route to validate post title & body fields
@app.route('/post', methods=['POST'])
def verify_post():
    blog_title = request.form['title']
    blog_body = request.form['body']
    title_error = ''
    body_error = ''

    # error validation messages
    if blog_title == "":
        title_error = "Title required."
    if blog_body == "":
        body_error = "Content required."

    # add new blog post and commit it to table with new id.
    if not title_error and not body_error:
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()
        blog = new_blog.id
        # user case #2 send user to individual entry page after posting.
        return redirect('/blog?id={0}'.format(blog))
    else:
        # return user to post page with errors.
        return render_template('post.html', title="Add New Blog Entry", blog_title = blog_title, blog_body = blog_body, title_error = title_error, body_error = body_error)

if __name__ == '__main__':
    app.run()
