import json

with open(r'C:/Users/JANITHA/.gemini/antigravity/brain/9dd9f939-4015-4d50-b56a-ec0260ce6672/.system_generated/steps/515/output.txt', 'r', encoding='utf-8') as f:
    data = json.loads(f.readline())

for rt in data.get("richtexts", []):
    if rt.get("page_index") in [6, 7, 8, 11, 14]:
        p = rt.get("page_index")
        txt = "".join([r.get("text", "") for r in rt.get("regions", [])])
        pos = rt.get("containerElement", {}).get("position", {})
        dim = rt.get("containerElement", {}).get("dimension", {})
        print(f"Page {p}: '{txt[:50]}' pos=({pos.get('left'):.1f}, {pos.get('top'):.1f}) dim=({dim.get('width'):.1f}x{dim.get('height'):.1f})")
