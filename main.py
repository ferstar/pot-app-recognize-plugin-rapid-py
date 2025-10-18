#!/usr/bin/env .venv/bin/python
import io
import os
import sys

from rapidocr import RapidOCR, OCRVersion, EngineType

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    engine = RapidOCR(
        params={
            "Rec.engine_type": EngineType(sys.argv[1]),
            "Rec.ocr_version": OCRVersion(sys.argv[2]),
        }
    )
    for txt in engine(sys.argv[3]).txts:
        print(txt)
