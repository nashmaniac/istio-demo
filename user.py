from flask import Flask, jsonify, request

app = Flask(__name__)
import os, socket

APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')


@app.route('/')
def hello_world():
    title = '%s Home Page' % APP_NAME
    print(request.headers)
    # V1 code start #
    data = dict(
        app=APP_NAME,
        served_from=socket.gethostname(),
        title=title,
        path=request.path,
        version=VERSION
    )
    # V1 code end #
    # V2 code start #
    # data = dict(
    #     app=APP_NAME,
    #     title=title,
    #     path=request.path,
    #     version=dict(
    #         tag=VERSION
    #     )
    # )
    # V2 code end #
    return jsonify(data)


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
