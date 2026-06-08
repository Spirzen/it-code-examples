from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-in-production"

tasks: list[dict] = []
_next_id = 1


def add_task(title: str) -> dict:
    global _next_id
    item = {"id": _next_id, "title": title.strip(), "done": False}
    _next_id += 1
    tasks.append(item)
    return item


@app.get("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.post("/add")
def add():
    title = request.form.get("title", "")
    if title.strip():
        add_task(title)
    return redirect(url_for("index"))


@app.get("/api/tasks")
def api_list():
    return jsonify(tasks)


@app.post("/api/tasks")
def api_create():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify({"error": "title required"}), 400
    return jsonify(add_task(title)), 201


if __name__ == "__main__":
    app.run(debug=True)
