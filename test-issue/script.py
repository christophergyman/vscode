# encoding: utf-8

from pathlib import Path

if __name__ == "__main__":
    Path("\ufeffc.txt").write_text("this is test file", encoding="utf-8")
