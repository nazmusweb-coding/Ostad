def validate_name(name):
    return name.replace(" ", "").isalpha() and len(name) > 0

def validate_phone(phone):
    return phone.isdigit()
