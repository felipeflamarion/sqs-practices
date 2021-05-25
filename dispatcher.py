import json

from utils.sqs import get_queue


def make_message_body(
    first_name,
    last_name,
    email,
    username,
):
    return json.dumps(
        {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "username": username,
        }
    )


def main():
    print("Sign in")

    first_name = input("First name: ") or "Felipe"
    last_name = input("Last name: ") or "Conceicao"
    email = input("Email: ") or "felipe.conceicao@contaazul.com"
    username = input("Username: ") or "felipe.conceicao"

    queue = get_queue("poc-practices")
    queue.send_message(
        MessageBody=make_message_body(first_name, last_name, email, username)
    )


if __name__ == "__main__":
    main()
