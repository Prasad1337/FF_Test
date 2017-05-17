def findTypeOfString(string):
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
