#!/usr/bin/env .venv/bin/python
import sys

from rapidocr import RapidOCR

if __name__ == "__main__":
    for txt in RapidOCR(params={f"Global.{sys.argv[1]}": True})(sys.argv[2]).txts:
        print(txt)
