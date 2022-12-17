def basic_text_import(txt:str) -> str:
    with open(txt) as file:
        return file.read()

def list_text_import(txt:str) -> list:
    with open(txt) as file:
        return file.readlines()
