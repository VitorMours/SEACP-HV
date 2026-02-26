from pathlib import Path


def create_media_file_structure(base_path: Path) -> None:
    """
    Create media directory structure:

    media/
        raw/
        processed/
        gray/
    """

    media_dir = base_path
    raw_dir = media_dir / "raw"
    processed_dir = media_dir / "processed"
    gray_dir = media_dir / "gray"

    directories = [media_dir, raw_dir, processed_dir, gray_dir]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)