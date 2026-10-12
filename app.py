# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Quiz
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# ---------------------------
# Rotas principais
# ---------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        novo_user = User(nome=nome, email=email, senha=senha)
        db.session.add(novo_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        user = User.query.filter_by(email=email, senha=senha).first()
        if user:
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    users = User.query.order_by(User.pontos.desc()).all()
    return render_template("dashboard.html", users=users)

@app.route("/quiz/<int:id>", methods=["GET", "POST"])
def quiz(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    quiz = Quiz.query.get(id)
    user = User.query.get(session["user_id"])

    if request.method == "POST":
        resposta = request.form.get("resposta")
        if resposta == quiz.resposta_correta:
            user.pontos += 10
            db.session.commit()
            return redirect(url_for("dashboard"))
    return render_template("quiz.html", quiz=quiz)

# ---------------------------
# Inicialização
# ---------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
