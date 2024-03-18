from flask import Flask

app = Flask(__name__)

@app.route('/JiraCreate'. methods=['POST'])
def createjira():
    

if __name__ == '__main__':
    app.run(debug=True)
