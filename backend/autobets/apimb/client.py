from matchbook.apiclient import APIClient
import logging
logger = logging.getLogger(__name__)
import json
api = APIClient('DOG2018', '07C18125')

def get_client():
    if not api.session_token:
        api.login()
        logger.warning(f'login has been called{api}')
    return api
