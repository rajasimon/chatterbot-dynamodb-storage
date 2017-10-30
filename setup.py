from setuptools import setup

from chatterbot_dynamodb_storage import VERSION

setup(
    name='chatterbot-dynamodb-storage',
    version=VERSION,
    description='Chatterbot DynamoDB Storage Adapter',
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    url='https://github.com/rajasimon/chatterbot-dynamodb-storage',
    packages=['chatterbot_dynamodb_storage']
)
