import sys
import time
from datetime import datetime


def assistant_greeting():
    now = datetime.now()
    hour = now.hour
    if hour < 12:
        return 'Good morning!'
    elif 12 <= hour < 18:
        return 'Good afternoon!'
    else:
        return 'Good evening!'