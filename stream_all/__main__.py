"""Stream All

Usage:
    streamall <src_path> --pattern=[src_pattern]
"""


from pathlib import Path
import fire
from stream_all import stream_files


def serve(
    serve_path: str,
    zip_filename="archive.zip",
    src_path: str = ".",
    pattern: str = "*",
    host: str = "127.0.0.1",
    port: int = 8001,
    log_level: str = "info",
):
    from fastapi import FastAPI
    from fastapi.responses import StreamingResponse

    app = FastAPI()

    @app.get(serve_path)
    def service_route():
        return StreamingResponse(
            stream_files(Path(src_path), pattern),
            media_type="application/zip",
            headers={"Content-Disposition": f"attachment; filename={zip_filename}"},
        )

    try:
        import uvicorn

        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level=log_level,
            reload=False,
        )
    except ImportError:
        raise RuntimeError("Uvicorn must be installed in order to use command")


if __name__ == "__main__":
    fire.Fire(serve, name="streamall")
