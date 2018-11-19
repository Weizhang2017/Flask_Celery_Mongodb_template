from flask import render_template, Flask, render_template,\
				Blueprint, jsonify, request, url_for, redirect

from flask import current_app as app
try:
	from ...app_config import config
except:
	from app_config import config
from .. import tasks
from ..models import *

main = Blueprint('main', __name__, template_folder='../templates', static_folder='../static')

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/add/', methods=['POST'])
def add():
	values = request.get_json()
	res = tasks._add.delay(values['1'], values['2'])
	addition_ = Addition(
						value1 = values['1'],
						value2 = values['2'],
						result = res.get(timeout=1),
						method = 'addition'
		)
	addition_.save()
	return redirect(url_for('main.result'))

@main.route('/multiply/', methods=['POST'])
def multiply():
	values = request.get_json()
	res = tasks._multiply.delay(values['1'], values['2'])
	multiplication_ = Multiplication(
						value1 = values['1'],
						value2 = values['2'],
						result = res.get(timeout=1),
						method = 'multiplication'
		)
	multiplication_.save()
	return redirect(url_for('main.result'))

@main.route('/sum/', methods=['POST'])
def xsum():
	values = request.get_json()
	res = tasks._xsum.delay(values['1'], values['2'])
	summation_ = Summation(
						value1 = values['1'],
						value2 = values['2'],
						result = res.get(timeout=1),
						method = 'summation'
		)
	summation_.save()
	return redirect(url_for('main.result'))

@main.route('/result/')
def result():
	return jsonify(status='success')
