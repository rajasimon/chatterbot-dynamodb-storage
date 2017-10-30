import unittest

from chatterbot_dynamodb_storage.storage import DynamodbStorageAdapter


class TestDynamodbStorageAdapter(unittest.TestCase):
    def setUp(self):
        self.db = DynamodbStorageAdapter()
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
