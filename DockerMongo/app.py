import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    bDist = request.args.get('bDist', type = float)
    bTime = request.args.get('bTime', type = float)
    bDate = request.args.get('bDate', type = float)
    
    
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    #Now takes correct distance/time
   
    open_time = acp_times.open_time(km, bDist, bTime)
    close_time = acp_times.close_time(km, bDist, bTime)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)



@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))


@app.route('/display', methods=['POST'])
def display():
    _items = db.acpTimes.find()
    items = [item for item in _items]
    return render_template('elements.html, items = items) 
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
