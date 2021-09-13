from flask import Flask, jsonify
from DBcm import UseDataBase, ConnectionErrors, SQLError

app = Flask(__name__)
app.secret_key = '43twyfu3647h4'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'postgres',
                          'password': 'qwerty',
                          'dbname': 'demo', }


@app.route('/parser/api/article', methods=['GET'])
def info() -> 'json':
    try:
        with UseDataBase(app.config['dbconfig']) as cursor:
            _SQL = """select * from aircrafts"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        return jsonify(contents)
    except ConnectionErrors as err:
        print('Is your data base switched on?', str(err))
    return jsonify('Hello')


if __name__ == '__main__':
    app.run(debug=True)
