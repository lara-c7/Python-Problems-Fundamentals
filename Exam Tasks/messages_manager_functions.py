def add(book, tokens_):
    if len(tokens_) < 4:
        return book
    username = tokens_[1]
    sent = int(tokens_[2])
    received = int(tokens_[3])
    if username not in book.keys():
        book[username] = {'sent': sent, 'received': received}
    return book


def message(book, tokens_, capac):
    if len(tokens_) < 3:
        return book
    sender = tokens_[1]
    receiver = tokens_[2]
    if sender in book and receiver in book:
        book[sender]['sent'] += 1
        book[receiver]['received'] += 1
        if book[sender]['sent'] + book[sender]['received'] >= capac:
            print(f"{sender} reached the capacity!")
            del book[sender]
        if book[receiver]['sent'] + book[receiver]['received'] >= capac:
            print(f"{receiver} reached the capacity!")
            del book[receiver]
    return book


def empty(book, tokens_):
    if len(tokens_) < 2:
        return book
    username = tokens_[1]
    if username == 'All':
        book.clear()
        return book
    if username in book.keys():
        book.pop(username)
    return book


def print_f(book):
    print(f"Users count: {len(book)}")
    for user, data in book.items():
        print(f'{user} - {data["sent"] + data["received"]}')


def main():
    capacity = int(input())
    phonebook = {}

    while True:
        tokens = input().split('=')
        if tokens[0] == 'Statistics':
            print_f(phonebook)
            break
        command = tokens[0]
        if command == 'Add':
            phonebook = add(phonebook, tokens)
        elif command == 'Message':
            phonebook = message(phonebook, tokens, capacity)
        else:
            phonebook = empty(phonebook, tokens)


if __name__ == '__main__':
    main()
