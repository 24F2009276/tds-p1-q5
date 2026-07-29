from dotenv import load_dotenv
import os

load_dotenv()

print("BOT:", os.getenv("BOT_TOKEN"))
print("AIPIPE:", os.getenv("AIPIPE_TOKEN"))