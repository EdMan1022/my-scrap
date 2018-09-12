import os

from eloqua_api_interactions.eloqua_session import BaseEloquaHandler


session = BaseEloquaHandler(
    company=os.environ['COMPANY'],
    username=os.environ['USERNAME'],
    password=os.environ['PASSWORD']
)

