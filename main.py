import os
import sys
bot_code = os.environ.get("BOT_CODE")
if bot_code:
    exec(bot_code)
else:
    print("BOT_CODE variable not found!")
