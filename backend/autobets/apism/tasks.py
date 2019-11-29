import logging
logging.basicConfig(level=logging.DEBUG)

from smarkets.streaming_api.api import SessionSettings, Session, StreamingAPIClient

username = 'tomirl2008@gmail.com'
password = '07C18125!!'

settings = SessionSettings(username, password)
settings.host = 'stream.smarkets.com'
session = Session(settings)

client = StreamingAPIClient(session)
client.login()
