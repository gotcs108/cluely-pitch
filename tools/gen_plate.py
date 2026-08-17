import os, sys, json, base64, urllib.request

KEY = open(os.path.expanduser("~/.openrouter_key")).read().strip()

PROMPT = """A photorealistic first-person POV still, shot through smart glasses worn by
the viewer. Vertical 9:16 phone-video framing. Slight barrel/fisheye distortion at the edges,
mild motion judder blur, phone-camera color science, blown-out highlights.

Sunny New York City sidewalk, mid-afternoon, a crosswalk. A young woman in her twenties
stands mid-turn, looking directly into the camera with a guarded half-smile - caught
between amused and suspicious. She holds a phone in one hand; a plain canvas tote bag on
her shoulder. One wireless earbud is out. Ordinary casual clothes.

Background: out-of-focus city street, crosswalk signal, parked cars, other pedestrians,
strong afternoon sun and lens flare. Shallow depth of field, she is the only sharp subject.

Candid, unposed, documentary realism. Absolutely no text, no watermarks, no UI, no
overlays anywhere in the image. Leave clean uncluttered space in the lower-left third."""

body = {
    "model": "google/gemini-3-pro-image",
    "modalities": ["image", "text"],
    "messages": [{"role": "user", "content": PROMPT}],
}

req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps(body).encode(),
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
)
resp = json.load(urllib.request.urlopen(req, timeout=300))

msg = resp["choices"][0]["message"]
imgs = msg.get("images") or []
if not imgs:
    print("NO IMAGE RETURNED"); print(json.dumps(resp)[:2000]); sys.exit(1)

url = imgs[0]["image_url"]["url"]
raw = base64.b64decode(url.split(",", 1)[1])
open("plate.png", "wb").write(raw)
print("OK bytes:", len(raw))
print("usage:", resp.get("usage"))
