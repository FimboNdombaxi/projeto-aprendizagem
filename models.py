from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100))
    pontos = db.Column(db.Integer, default=0)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(200))
    resposta_correta = db.Column(db.String(100))
    alternativas = db.Column(db.String(300))  # Guardar opções separadas por vírgula
