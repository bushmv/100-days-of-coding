def encrypt(data: bytes, key: bytes) -> bytes:
    result = bytearray()
    key_len = len(key)
    for i, el in enumerate(data):
        result.append(el ^ key[i % key_len])
    return result


def main() -> None:
    with open("encrypted", "rb") as f:
        text = f.read()
    with open("key", "rb") as f:
        key = f.read()
    encrypted = encrypt(text, key)
    with open("text", "wb") as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()
