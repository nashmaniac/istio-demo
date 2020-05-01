from flask import Flask, jsonify, request

app = Flask(__name__)
import os, socket

APP_NAME = os.getenv('APP_NAME')


@app.route('/')
def hello_world():
    title = '%s Home Page'%APP_NAME
    return jsonify(
        dict(
            app=APP_NAME,
            served_from=socket.gethostname(),
            title=title,
            path=request.path,
        )
    )


@app.route('/about')
def about():
    title = '%s About Page'%APP_NAME
    return jsonify(
        dict(
            served_from=socket.gethostname(),
            title=title,
            path=request.path,
            app=APP_NAME
        )
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
