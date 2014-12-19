def user():
    character = input("Enter character: ")
    number = int(input("INput number: "))
    return character, number

def loop(character, number):
    print(character)
    print(number)
    for count in range(number):
        print(character)

def main():
    de = user()
    loop(de)
