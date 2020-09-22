# UniBot

UniBot is Artificial Intelligence Powered ChatBot for College Related Enquiries and FAQs.

## Requirements

1. Python 3.6/3.7

2. Rasa Version 1.10.10

3. Node.js

## Installation

### For RASA Server

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Rasa.

```bash
pip install rasa==1.10.10
```

```bash
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

### Packages used for custom Actions

#### Packages for Database Connection

```bash
pip install mysql
```

```bash
pip install mysql-connector-python
```

#### Database Connection, Create Table, Insert Data

1. Database Connection

	```bash
	def function():
		mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "database_name"
	)
	```
2. Creating table
	
	```bash
	table = "CREATE TABLE table_name (message VARCHAR(255), response VARCHAR(255), sender FLOAT(30));"
	```

3. Insert data

	```bash
	sql = 'INSERT INTO table_name (message, response, sender) VALUES ("{0}","{1}","{2}");'.format(message, response, sender)
	```

### For Node JS, Json Server
1. Download and Install node.js setup and run following command in target folder  

```bash
npm install json-server
```


## Usage

### To Train Chatbot

```bash
rasa train
```

### To Start RASA Server

```bash
rasa run -m models --enable-api --cors "*" --debug --verbose
```

```bash
rasa run actions
```

### To Start JSON server

1. create a json file in target folder, add following content

```json
{
      "message": "",
      "response": "",
      "sender": ,
      "id": 1
},
```

2. To run json server
```bash
json-server --watch data/filename.json
```
###To train the model in VM
```docker exec -it unibot_rasa_1 rasa train```

###To update the deployment
```bash 
cd /root/Unibot
docker-compose build
docker-compose down && docker-compose up
```
