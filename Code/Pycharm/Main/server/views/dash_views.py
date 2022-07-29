from flask import Flask, Blueprint, request, render_template, url_for, session, g, flash, jsonify
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from server.forms import UserCreateForm
from server.models import Members, Food_recipe, Wholesale_quantity
from server import db
import json
import re
from server.yolo5_def import YoloRun
import urllib.request
from glob import glob
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

bp = Blueprint('dash', __name__, url_prefix='/')


# bcrypt = Bcrypt(Flask(__name__))


# app = Flask(__name__)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id


# Dashboard
@bp.route('/dash')
def board():
    dt = Food_recipe.query.filter(and_(Food_recipe.dish == '김치찌개', Food_recipe.registrant == '김패쓰'))
    return render_template('dash.html', dt=dt)


# Dashboard_가격예측
@bp.route('/forecast')
def forecast():
    user_id = session.get('user_id')
    if user_id is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
        return render_template('dash/forecast.html', dt=dt)


# Dashboard_가격비교
@bp.route('/compare')
def compare():
    user_id = session.get('user_id')
    if user_id is None:
        flash("로그인이 필요합니다.")
        return redirect(url_for('main.login'))
    else:
        dt = Food_recipe.query.filter(Food_recipe.dish == '김치찌개').all()
        return render_template('dash/compare.html', dt=dt)
