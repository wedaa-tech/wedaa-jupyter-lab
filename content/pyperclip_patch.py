import asyncio
import js
import pyperclip

# Define async paste
async def _paste_async():
    return await js.navigator.clipboard.readText()

# Define sync wrappers
def copy_js(text: str):
    js.navigator.clipboard.writeText(text)

def paste_js():
    return asyncio.get_event_loop().run_until_complete(_paste_async())

# Monkey-patch pyperclip
pyperclip.copy = copy_js
pyperclip.paste = paste_js

print("✅ pyperclip patched to use browser clipboard API in JupyterLite")
