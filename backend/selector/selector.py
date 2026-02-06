from backend.pipelines import available_pipelines

def select_pipeline(features: dict):
    mime_type = features.get("mime_type", "application/octet-stream")
    if "pdf" in mime_type:
        return "pdf_pipeline"
    elif "image" in mime_type:
        return "image_pipeline"
    elif "audio" in mime_type:
        return "audio_pipeline"
    else:
        return "generic_pipeline"
