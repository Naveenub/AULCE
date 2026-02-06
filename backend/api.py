from fastapi import FastAPI, UploadFile, File
from backend.analyzer.analyzer import analyze_file
from backend.selector.selector import select_pipeline
from backend.pipelines import run_pipeline
from backend.validator.validator import validate_compression

app = FastAPI()

@app.post("/compress")
async def compress_file(file: UploadFile = File(...)):
    content = await file.read()
    features = analyze_file(content)
    pipeline = select_pipeline(features)
    compressed = run_pipeline(content, pipeline)
    valid = validate_compression(content, compressed)
    return {"compressed_size": len(compressed), "valid": valid, "pipeline": pipeline}
