import os
from dotenv import load_dotenv
load_dotenv()

CSV_PATH= os.getenv("CSV_PATH")

def function():
    print(CSV_PATH)

function()
