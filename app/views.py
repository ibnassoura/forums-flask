from flask import render_template, request, redirect, url_for
from app import models
from app import app, member_store, post_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")

@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    post_store.delete(id)
    return redirect(url_for("home"))

@app.route("/topic/show/<int:id>")
def topic_show(id):
    return render_template("topic_show.html", post = post_store.get_by_id(id))
