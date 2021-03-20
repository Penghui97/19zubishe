from Back_end import app,db


@app.route('/')
def index():
    return '<h>Hello Flask !</h>'

if __name__=='__main__':
    app.run()