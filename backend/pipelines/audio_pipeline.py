def compress_audio(data: bytes) -> bytes:
    return data[:int(len(data)*0.75)]
