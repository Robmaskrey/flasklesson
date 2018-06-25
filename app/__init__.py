#importing flask
from flask import Flask


#defining app and giving it a variable name
app = Flask(__name__)



from app import routes
