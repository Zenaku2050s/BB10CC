import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
token = int(getenv("token"))
subscriber = getenv("subscriber")
