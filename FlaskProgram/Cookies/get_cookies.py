from flask import Flask,request

app = Flask(__name__)

# This function is getting cookie using key and value

@app.route('/get')
def getcookie():
    framework = request.cookies.get('framework')
    return 'The framework is '+ framework

if __name__ == '__main__':
    app.run(debug =True )