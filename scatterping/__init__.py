import boto3


class Lambda:
    def __init__(self) -> None:
        self.client = boto3.client("lambda")
