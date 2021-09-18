from flask import Flask, jsonify, make_response, request
from DBcm import UseDataBase, ConnectionErrors, SQLError
from enites import Filtr

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = '43twyfu3647h4'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'postgres',
                          'password': 'qwerty',
                          'dbname': 'demo', }


@app.route('/article', methods=['GET'])
def get_article() -> 'json':
    article = Filtr(link = request.args.get('url'))
    # try:
    #     with UseDataBase(app.config['dbconfig']) as cursor:
    #         _SQL = """select * from aircrafts"""
    #         cursor.execute(_SQL)
    #         contents = cursor.fetchall()

    #     return jsonify(contents)
    # except ConnectionErrors as err:
    #     print('Is your data base switched on?', str(err))
    return jsonify(article.finder())


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
