from matchbook.apiclient import APIClient
import logging
import requests
import json
from .models import SessionToken

logger = logging.getLogger(__name__)
api = APIClient('DOG2018', '07C18125')


def get_client():
    if not api.session_token:
        api.login()
        logger.warning(f'login has been called{api}')
    return api

def get_reports_token():
    if not api.session_token:
        api.login()
        se, created = SessionToken.objects.create(session_token=session_token)
        se.save()
        logger.warning(f'Login has been called for reports')
    
    

