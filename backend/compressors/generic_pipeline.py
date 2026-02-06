def compress_generic(data: bytes) -> bytes:
  return data[:int(len(data)*0.85)]
