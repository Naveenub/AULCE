import magic
import numpy as np

def analyze_file(data: bytes):
    mime_type = magic.from_buffer(data, mime=True)
    size = len(data)
    entropy = -sum([p/size * np.log2(p/size) for p in np.bincount(np.frombuffer(data, dtype=np.uint8)) if p > 0])
    return {"mime_type": mime_type, "size": size, "entropy": entropy}
