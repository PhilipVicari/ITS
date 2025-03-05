import json

def Serialize(data_dict, file_path= 'file.json'):
    try:
        with open(file_path, 'w') as f:
            json.dump(data_dict, f)
        return True
    except Exception:
        return False
def deSerialize(file_path= 'file.json'):
    try:
        with open(file_path, 'r') as f:
            data_dict = json.load(f)
        return data_dict
    except Exception:
        return None