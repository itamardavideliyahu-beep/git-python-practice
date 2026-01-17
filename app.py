import datetime

def greet(name):
    return f"Hello from {name}!"
    return f"Hello baby, {name}!"
    return f"Hello father, {name}!"
    return f"Hello mother, {name}!"
    return f"Hello sister, {name}!"
    return f"Hello brother, {name}!"
    return f"Hello uncle, {name}!"
    return f"Hello aunt, {name}!"
    return f"Hello cousin, {name}!"
    return f"Hello friend, {name}!"
    return f"Hello enemy, {name}!"

if __name__ == "__main__":
    user = "World"
    print(greet(user), datetime.datetime.now())

