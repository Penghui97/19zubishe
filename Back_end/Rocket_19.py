from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h>Hello Flask !</h>'

if __name__=='__main__':
    app.run()