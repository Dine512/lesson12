from flask import Flask
from main.main import main_blueprint
from loader.loader import loader_blueprint

app = Flask(__name__)


app.register_blueprint(loader_blueprint)
app.register_blueprint(main_blueprint)


app.run()

