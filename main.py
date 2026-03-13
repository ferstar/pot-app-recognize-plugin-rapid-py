#!/usr/bin/env .venv/bin/python
import io
import sys

from rapidocr import RapidOCR, OCRVersion, EngineType

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RESULT_START = "__POT_APP_OCR_RESULT_START__"
RESULT_END = "__POT_APP_OCR_RESULT_END__"


def build_params(engine: str, ocr_version: str, backend: str) -> dict:
    params = {
        "Det.engine_type": EngineType(engine),
        "Cls.engine_type": EngineType(engine),
        "Rec.engine_type": EngineType(engine),
        "Det.ocr_version": OCRVersion(ocr_version),
        # RapidOCR's built-in cls model is still tied to the PP-OCRv4 lineage.
        "Cls.ocr_version": OCRVersion.PPOCRV4,
        "Rec.ocr_version": OCRVersion(ocr_version),
    }

    backend_key = (backend or "auto").strip().lower()
    if backend_key in {"", "auto", "cpu"}:
        return params

    if engine == "onnxruntime":
        backend_map = {
            "cuda": "EngineConfig.onnxruntime.use_cuda",
            "directml": "EngineConfig.onnxruntime.use_dml",
            "cann": "EngineConfig.onnxruntime.use_cann",
            "coreml": "EngineConfig.onnxruntime.use_coreml",
        }
        if backend_key in backend_map:
            params[backend_map[backend_key]] = True
            return params
        raise ValueError(f"Unsupported backend for {engine}: {backend}")

    if engine == "paddle":
        backend_map = {
            "cuda": "EngineConfig.paddle.use_cuda",
            "npu": "EngineConfig.paddle.use_npu",
        }
        if backend_key in backend_map:
            params[backend_map[backend_key]] = True
            return params
        raise ValueError(f"Unsupported backend for {engine}: {backend}")

    if engine == "torch":
        backend_map = {
            "cuda": "EngineConfig.torch.use_cuda",
            "npu": "EngineConfig.torch.use_npu",
            "mps": "EngineConfig.torch.use_mps",
        }
        if backend_key in backend_map:
            params[backend_map[backend_key]] = True
            return params
        raise ValueError(f"Unsupported backend for {engine}: {backend}")

    raise ValueError(f"Unsupported backend for {engine}: {backend}")

if __name__ == "__main__":
    engine_type = sys.argv[1]
    ocr_version = sys.argv[2]
    backend = sys.argv[3]
    image_path = sys.argv[4]

    engine = RapidOCR(params=build_params(engine_type, ocr_version, backend))
    result = engine(image_path)
    print(RESULT_START)
    for txt in (result.txts or ()):
        print(txt)
    print(RESULT_END)
