
import os

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}


@app.get("/")
def index():
    items = Task.query.order_by(Task.id.desc()).all()
    return render_template("index.html", tasks=items)


@app.post("/add")
def add():
    title = request.form.get("title", "")
    if title.strip():
        db.session.add(Task(title=title.strip()))
        db.session.commit()
    return redirect(url_for("index"))


@app.get("/api/tasks")
def api_list():
    items = Task.query.order_by(Task.id.desc()).all()
    return jsonify([t.to_dict() for t in items])


@app.post("/api/tasks")
def api_create():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify({"error": "title required"}), 400
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
