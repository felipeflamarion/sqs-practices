import boto3

sqs = boto3.resource("sqs")


def get_queue(queue_name):
    try:
        queue = sqs.get_queue_by_name(QueueName=queue_name)
    except Exception:
        queue = sqs.create_queue(QueueName=queue_name, Attributes={"DelaySeconds": "5"})

    return queue
