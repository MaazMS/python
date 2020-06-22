"""
This program show the specific data type variable value.
 syntax <converter:variable_name>
example http://127.0.0.1:5000/blog/80
        http://127.0.0.1:5000/rev/1.1
"""
from flask import Flask

app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return  'blog  id%d ' %postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revesion Number %f' %revNo

if __name__ == '__main__':
    app.run()