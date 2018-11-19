from flask import Flask
# if __name__ == '__main__':
from app.main.views import main
# else:
# 	from .app.main.views import main

app = Flask(__name__)
app.secret_key = 'test-key'
app.register_blueprint(main)
