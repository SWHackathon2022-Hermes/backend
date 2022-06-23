from pickletools import read_string1
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)
class CreateUser(Resource):
    def post(self):
        try:#보내는 코드
            parser = reqparse.RequestParser()
            parser.add_argument('tent_1', type=str)
            parser.add_argument('tent_2', type=str)
            parser.add_argument('tent_3', type=str)
            parser.add_argument('tent_4', type=str)
            args = parser.parse_args()
            #받는 코드
            _tent_1 = args['tent_1']
            _tent_2 = args['tent_2']
            _tent_3 = args['tent_3']
            _tent_4 = args['tent_4']
            
            f=open("./testing.txt",'w')
    
            content={'tent_1': args['tent_1'], 'tent_2': args['tent_2'],
                     'tent_3': args['tent_3'], 'tent_4': args['tent_4']}
            f.write(content['tent_1']+'\n')
            f.write(content['tent_2']+'\n')
            f.write(content['tent_3']+'\n')
            f.write(content['tent_4']+'\n')
            
            f.close()
            
            return {'StatusCode': '200', 'Message': '저장 성공!'}    
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/report')

if __name__ ==  '__main__':
    app.run(
    host="localhost",
    port=8080)
