def compress_image(data: bytes) -> bytes:
    return data[:int(len(data)*0.7)]
