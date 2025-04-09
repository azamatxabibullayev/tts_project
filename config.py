import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_GROUP_ID = int(os.getenv("ADMIN_GROUP_ID", "0"))


PDF_FILES_DIR = os.path.join(os.path.dirname(__file__), "pdfs")

PDF_FILES = {
    # "1": "document1.pdf",
    # "2": "document2.pdf",
    # "3": "document3.pdf",

}
