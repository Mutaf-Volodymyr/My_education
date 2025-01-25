from flask import Flask
from re import sub

# import pdb; pdb.set_trace()

app = Flask(__name__)

@app.route('/<username>')
def main(username):
    with open('index.html') as f:
        content = sub('username', username, f.read())
    return content


# http://127.0.0.1:5000/reversed/123/456/789
@app.route('/reversed/<path:user_path>')
def revers_path(user_path: str):
    return '/'.join(map(lambda x: x[::-1], user_path.split('/')))


if __name__ == '__main__':
    app.run(debug=True)