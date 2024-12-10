import requests
from PIL import Image
import base64
from io import BytesIO

# input images should be square, and will be reduced to 6
def fvs(filepath1, filepath2):
    img1, img2 = Image.open(filepath1), Image.open(filepath2)
    img1, img2 = img1.resize((64, 64)), img2.resize((64, 64))
    file1, file2 = BytesIO(), BytesIO()

    img1.save(file1, format='JPEG')
    img2.save(file2, format='JPEG')
    img1_b64 = base64.b64encode(file1.getvalue())
    img2_b64 = base64.b64encode(file2.getvalue())

    params = {}
    params['api_key'] = 'API KEY HERE'
    params['api_secret'] = 'API SECRET HERE'
    params['image_base64_1'] = img1_b64
    params['image_base64_2'] = img2_b64

    print(len(img1_b64))

    response = requests.request('POST', 'https://api-us.faceplusplus.com/facepp/v3/compare', params=params)