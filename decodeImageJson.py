#Decode image JSON to .jpg
import base64
import json
import cv2
import numpy as np

response = json.loads(open('./0.json', 'r').read())
string = response['img']
jpg_original = base64.b64decode(string)
jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
img = cv2.imdecode(jpg_as_np, flags=1)
cv2.imwrite('./0.jpg', img)