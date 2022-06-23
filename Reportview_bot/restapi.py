from pickletools import read_string1
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import Flask
import pymysql

app = Flask(__name__)
api = Api(app)

#mysql 연결
db = pymysql.connect(host='192.168.219.142', port = 3306, user='계정명',
db='hermes', password='password', charset='utf8')
            
class CreateUser(Resource):
    def post(self):
        try:
            #입력 파라미터를 설정
            parser = reqparse.RequestParser()
            #필수 매개변수
            parser.add_argument('db_Category', type=str)
            parser.add_argument('Address', type=str)
            parser.add_argument('AddressDetail', type=str)
            parser.add_argument('Description', type=str)

            #입력 파싱
            args = parser.parse_args() 
            _db_Category = args['db_Category']
            _Address = args['Address']
            _AddressDetail = args['AddressDetail']
            _Description = args['Description']

            curs = db.cursor()

            #sql문 실행
            sql = "insert into report_table (db_Category, Address, AddressDetail, Description) values(%s,%s,%s,%s)"
            val = (_db_Category,_Address,_AddressDetail, _Description)
            curs.execute(sql,val)

            #db 커밋
            db.commit()
            #db 닫기
            db.close()

            #성공값 출력
            return {'StatusCode': '200', 'Message': '저장 성공!'}

        #에러메세지 출력
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/report')

#flask ip, port 설정
if __name__ ==  '__main__':
    app.run(
    host='0.0.0.0',
    port=50)
