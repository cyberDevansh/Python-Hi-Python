from typing import Literal

def get_status(code: Literal[200, 404, 500]) -> str:
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    else:
        return "Server Error"

print(get_status(404))  
