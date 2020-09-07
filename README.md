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
```bash
pip install mysql
```

```bash
pip install mysql-connector-python
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
