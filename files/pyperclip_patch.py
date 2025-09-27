import asyncio
import js

# ensure pyperclip is available
import micropip
await micropip.install("pyperclip")

import pyperclip

# async paste helper
async def _paste_async():
    return await js.navigator.clipboard.readText()

# wrappers
def copy_js(text: str):
    js.navigator.clipboard.writeText(text)

def paste_js():
    return asyncio.get_event_loop().run_until_complete(_paste_async())

# patch pyperclip
pyperclip.copy = copy_js
pyperclip.paste = paste_js

print("✅ pyperclip installed & patched for JupyterLite")
