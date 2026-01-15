from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)