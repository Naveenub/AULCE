from backend.compressors.pdf_pipeline import compress_pdf
from backend.compressors.image_pipeline import compress_image
from backend.compressors.audio_pipeline import compress_audio
from backend.compressors.generic_pipeline import compress_generic

available_pipelines = {
"pdf_pipeline": compress_pdf,
"image_pipeline": compress_image,
"audio_pipeline": compress_audio,
"generic_pipeline": compress_generic
}

def run_pipeline(data: bytes, pipeline_name: str):
func = available_pipelines.get(pipeline_name, compress_generic)
return func(data)
