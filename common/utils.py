import json

def parse_int(string:str):
    """
    字符串转int，异常时返回None
    """
    try:
        number = int(string)
    except:
        return None
    return number

def parse_float(string:str):
    """
    字符串转float,异常时返回None
    """
    try:
        number = float(string)
    except:
        return None
    return number

def json_load(string:str):
    """
    字符串转字典，异常时返回None
    """
    try:
        json_dict = json.load(string)
    except:
        return None
    return json_dict

def json_dump(json_dict:dict):
    """
    json字典转字符串，异常时返回None
    """
    try:
        string = json.dump(json_dict)
    except:
        return None
    return string

if __name__ == "__main__":
    print(parse_float('s'))