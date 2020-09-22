from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from database_connector import UserMessage


api = Flask(__name__)
CORS(api)

user_data = [
    {
        "id": 1,
        "message": "admission details",
        "response": "Full Admission Schdule can be downloaded by <a href=\"https://universalcollegeofengineering.edu.in/wp-content/uploads/2019/07/UCoE-Admission-Advt-2019.jpg\" target=\"_blank\">Clicking Here</a>",
        "sender": 0.4572782720086981
    },
    {
        "id": 2,
        "message": "/start",
        "response": "Hi! I am UniBot, I can help you with Admission Related queries, College, Location, Events, Facilities and many more..",
        "sender": 0.46712191981101414
    }
]


@api.route('/data', methods=['GET','POST'])
def get_data():
    if request.method == 'GET':
        if len(user_data) > 0:
            return jsonify(user_data)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        tempData = request.data
        data2 = json.loads(tempData)
        new_message = request.form.get('message')
        new_response = request.form.get('response')
        new_sender = request.form.get('sender')
        ID = user_data[-1]['id']+1

      
        temp = {
            "id": ID,
            "message":  data2['message'],
            "response":  data2['response'],
            "sender":  data2['sender']
        }
        user_data.append(temp)

        UserMessage(data2['message'],data2['response'],data2['sender'])
        
        return temp, 201

        print(temp)

    
if __name__ == '__main__':
    api.run(debug=True)