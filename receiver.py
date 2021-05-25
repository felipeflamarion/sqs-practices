import json
import time

from utils.sqs import get_queue


def main():
    queue = get_queue("poc-practices")

    while True:
        processed_messages = []

        messages = queue.receive_messages(MaxNumberOfMessages=10)
        for message in messages:
            data = json.loads(message.body) if message.body else None
            if data is not None:
                print("Processing", data)

                processed_messages.append(
                    {"Id": message.message_id, "ReceiptHandle": message.receipt_handle}
                )

        for message in processed_messages:
            queue.delete_messages(Entries=processed_messages)

        return  # TODO: tmp
        time.sleep(1)


if __name__ == "__main__":
    main()
