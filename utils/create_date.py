from datetime import datetime

def create_save_date() -> str:
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    return str(formatted_date)

# Example usage
date_string = create_save_date()
print(date_string)