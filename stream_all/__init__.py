import logging
from datetime import datetime
from pathlib import Path
from stream_zip import stream_zip
from typing import Any, Generator, Iterator

__all__ = ["stream_files", "get_file_list", "generate_zip_data"]


def generate_zip_data(files: Iterator[Path], compression_type):
    logger = logging.getLogger(__name__)
    modified_at = datetime.now()
    for file in files:
        logger.debug(f"Streaming {file}")
        with open(file, "rb") as data:
            yield str(file), modified_at, 0o600, compression_type, data


def get_file_list(path: Path, pattern: str = "*") -> Generator[Path, None, None]:
    return path.glob(pattern)


def stream_files(path: Path, pattern: str = "*") -> Generator[bytes, Any, None]:
    from stream_zip import ZIP_32

    file_generator = generate_zip_data(
        files=get_file_list(path, pattern),
        compression_type=ZIP_32,
    )

    zipped_file_stream = stream_zip(
        file_generator,
    )
    return zipped_file_stream
