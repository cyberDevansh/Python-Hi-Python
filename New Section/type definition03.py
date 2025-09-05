from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Admin"
    return None


# till now i don't used typing and optional modules so i will work upon it later