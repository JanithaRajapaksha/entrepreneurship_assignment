import json
import urllib.request

with open(r'C:/Users/JANITHA/.gemini/antigravity/brain/9dd9f939-4015-4d50-b56a-ec0260ce6672/.system_generated/steps/505/output.txt', 'r', encoding='utf-8') as f:
    data = json.loads(f.readline())

items = data.get('items', [])
print(f"Total pages: {len(items)}")
for it in items:
    pg = it.get('page_number')
    thumb = it.get('thumbnail', {}).get('url')
    print(f"Page {pg}: {thumb[:80]}...")
