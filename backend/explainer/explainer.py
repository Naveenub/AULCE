def explain_failure(features: dict, pipeline_name: str) -> str:
    return f"Compression failed for {pipeline_name} with features: {features}"
