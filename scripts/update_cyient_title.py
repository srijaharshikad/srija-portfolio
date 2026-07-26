from pathlib import Path

INDEX_PATH = Path("index.html")
OLD_TITLE = "Technical Lead — Cyient (GIS Division)"
NEW_TITLE = "Software Engineer — Cyient (Network Planning Products)"


def main() -> None:
    text = INDEX_PATH.read_text(encoding="utf-8")
    if OLD_TITLE in text:
        text = text.replace(OLD_TITLE, NEW_TITLE, 1)
    elif NEW_TITLE not in text:
        raise RuntimeError("Could not locate the Cyient designation in index.html")
    INDEX_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
