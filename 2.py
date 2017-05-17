# Function to find type of string
def find_type_of_string(string):
    try:
        int(string)
        return "int"
    except ValueError:
        pass

    try:
        float(string)
        return "float"
    except ValueError:
        pass

    return "string"
