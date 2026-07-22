import re

with open('JIVOL.py', encoding='utf-8-sig') as f:
    content = f.read()

content = content.lstrip('\ufeff')

# 1. Add ALLOWED_USERS if missing
if 'ALLOWED_USERS' not in content:
    old = 'OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")\n'
    new = old + '\nALLOWED_USERS = {8977482308}  # Only Sir can talk to Jivol\n'
    content = content.replace(old, new, 1)

# 2. Insert sender authorization into telegram_poll
if 'chat_id not in ALLOWED_USERS' not in content:
    pattern = r'(msg = update\[\"message\"\]\n.*?chat_id = msg\[\"chat\"\]\[\"id\"\]\n.*?text = msg\.get\(\"text\", \"\"\)\n\s+print\()'
    replacement = (
        'msg = update["message"]\n'
        '                    chat_id = msg["chat"]["id"]\n'
        '                    # --- SIR-ONLY LOCK ---\n'
        '                    if chat_id not in ALLOWED_USERS:\n'
        '                        print(f"[Telegram] Unauthorized access from {chat_id} - denied")\n'
        '                        telegram_send(chat_id, "Access denied. This bot answers only to Sir.")\n'
        '                        continue\n'
        '                    # --- END LOCK ---\n'
        '                    text = msg.get("text", "")\n'
        '                    print('
    )
    content = re.sub(pattern, replacement, content, count=1)

# 3. Auto-restart loop for Flask
old_run = "app.run(host=\"0.0.0.0\", port=8080, debug=False, use_reloader=False)"
new_run = (
    "while True:\n"
    "        try:\n"
    "            app.run(host=\"0.0.0.0\", port=8080, debug=False, use_reloader=False)\n"
    "        except Exception as e:\n"
    "            print(f\"[JIVOL] Crash: {e}. Restarting in 5s...\")\n"
    "            time.sleep(5)\n"
    "            continue\n"
    "        else:\n"
    "            break"
)
content = content.replace(old_run, new_run, 1)

# 4. Startup status additions
content = content.replace(
    'print(f"[JIVOL] Persona backup: READY TO ROLL")',
    'print(f"[JIVOL] Access lock: ONLY user ID {ALLOWED_USERS}")'
)

with open('JIVOL.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('JIVOL patched successfully.')
