import json

with open(r'C:/Users/JANITHA/.gemini/antigravity/brain/9dd9f939-4015-4d50-b56a-ec0260ce6672/.system_generated/steps/473/output.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    data = json.loads(line)

print("Keys in data:", data.keys())
print("Fills count:", len(data.get("fills", [])))
for fill in data.get("fills", [])[:10]:
    print(fill)

print("\nSample shapes and text elements:")
for rt in data.get("richtexts", []):
    if rt.get("page_index") in [6, 7, 10, 11]:
        print(f"Page {rt.get('page_index')}: {rt.get('containerElement')} | texts={[r.get('text') for r in rt.get('regions', [])]}")
