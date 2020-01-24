import base64
import hashlib


def decode(file):

    with open(file, 'rb') as f:
        image = f.read()
    base64code = base64.encodestring(image)
    md5 = hashlib.md5(image).hexdigest()
    with open('image_in_base64code.txt', 'wb') as b64f:
        b64f.write(base64code)
    with open('md5_in_image.txt', 'w') as md5f:
        md5f.write(md5)

    return md5, base64code


def encode(file):
    with open(file, "rb") as b64f:
        bfile = b64f.read()
    with open('out.png','wb') as out:
        out.write(base64.decodestring(bfile))


if __name__ == "__main__":
    encode('image_in_base64code.txt')