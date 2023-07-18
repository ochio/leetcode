import hashlib


class Codec:
    def __init__(self) -> None:
        self.u = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        e = "http://tinyurl.com/" + hashlib.md5(longUrl.encode()).hexdigest()
        self.u[e] = longUrl
        return e

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.u[shortUrl]
