import os
import json
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_GROUP_ID = int(os.getenv("ADMIN_GROUP_ID", "0"))

pdf_files_json = os.getenv("PDF_FILES_JSON", "{}")
PDF_FILES = json.loads(pdf_files_json)
