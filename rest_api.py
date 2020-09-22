from flask import Flask, request, jsonify
from flask_cors import CORS
from database_connector import UserMessage

api = Flask(__name__)
CORS(api)

@api.route('/data', methods=['GET','POST'])

def get_data():
    if request.method == 'POST':
        tempData = request.data
        data2 = json.loads(tempData)
        new_message = request.form.get('message')
        new_response = request.form.get('response')
        new_sender = request.form.get('sender')

        temp = {
            "message":  data2['message'],
            "response":  data2['response'],
            "sender":  data2['sender']
        }

        UserMessage(data2['message'],data2['response'],data2['sender'])

        return temp, 201

        print(temp)


if __name__ == '__main__':
api.run(host='0.0.0.0', port='3000')
