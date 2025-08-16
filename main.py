#!/usr/bin/env .venv/bin/python
import sys

from rapidocr import RapidOCR, OCRVersion, EngineType

if __name__ == "__main__":
    engine = RapidOCR(
        params={
            "Rec.engine_type": EngineType(sys.argv[1]),
            "Rec.ocr_version": OCRVersion(sys.argv[2]),
        }
    )
    for txt in engine(sys.argv[3]).txts:
        print(txt)
