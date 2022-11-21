from bottle import static_file, route

@route('/')
def index():
    return template('cars.xml')

@route('/file/<filename:re:.*\.xml>')
def send_file(filename):
    return static_file(filename, root='/path/to/xml/files', mimetype='Cars/xml')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/path/to/static/files')

run(host='localhost', port=443, debug=True)