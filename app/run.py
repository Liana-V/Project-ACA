from __init__ import app

if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=False,port=5005)