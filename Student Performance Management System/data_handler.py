import json

FILE_PATH = "data.json"

def load_preformance():
    try: 
        with open(FILE_PATH, 'r') as file:
            preformances = json.load(file)
            return preformances
    except(FileNotFoundError, json.JSONDecodeError):
        return[]

def save_preformance(preformances):
    with open(FILE_PATH, 'w') as file:
        json.dump(preformances, file, indent=4) 
