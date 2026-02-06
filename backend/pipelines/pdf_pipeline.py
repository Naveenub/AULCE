def compress_pdf(data: bytes) -> bytes:
    return data[:int(len(data)*0.8)]
