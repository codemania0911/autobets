#%%

import pandas as pd
import numpy as np
from matchbook.apiclient import APIClient

api = APIClient('DOG2018', '07C18125')

def get_client():
    if not api.session_token:
        api.login()
    return api


# %%
