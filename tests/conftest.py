import os

import boto3
import pytest
from moto import mock_sqs
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session")
def main(sqs):
    pg = None
    try:
        print("Starting postgres db...")
        pg = PostgresContainer("postgres:11.6-alpine")
        pg.start()
        os.environ['DB_URL'] = pg.get_connection_url()
        sqs.create_queue(QueueName="test-queue.fifo", Attributes={"FifoQueue": "true"})
        from app import main
        yield main
    finally:
        if pg is not None:
            pg.stop()


@pytest.fixture(scope="session")
def sqs():
    with mock_sqs():
        conn = boto3.resource("sqs", region_name="us-east-1")
        yield conn
