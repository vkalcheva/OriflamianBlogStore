import base64

from werkzeug.exceptions import BadRequest


def decode_file(path, encoded_file):
    try:
        with open(path, "wb") as f:
            f.write(base64.b64decode(encoded_file.encode("utf-8")))
    except Exception:
        raise BadRequest("Invalid photo")

