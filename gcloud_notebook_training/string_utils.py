import random
import string
from datetime import datetime

def build_random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(n)])

def str_time_stamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H:%M:%S.%f")