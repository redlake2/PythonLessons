from flask import Flask
from fuel import MyGetFuel

app = Flask(__name__)

@app.route('/')
def index_page():
  return MyGetFuel()

#if __name__ == '__main__':
#  app.run(debug=True, host='0.0.0.0')



