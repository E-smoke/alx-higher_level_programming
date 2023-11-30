#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for element in name:
        if element[0] != "_" and element[1] != "_":
            print(element)
