from flask import Flask, render_template, url_for, request
from app import app, db

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return "Pronto! Servidor OK"