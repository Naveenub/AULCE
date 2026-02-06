def validate_compression(original: bytes, compressed: bytes) -> bool:
    return len(compressed) < len(original)
