from bottle import static_file, route

@route('/')
def index():
    return template('cars.csv')

@route('/file/<filename:re:.*\.csv>')
def send_file(filename):
    return static_file(filename, root='/path/to/csv/files', mimetype='Cars/csv')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/path/to/static/files')

run(host='localhost', port=443, debug=True)