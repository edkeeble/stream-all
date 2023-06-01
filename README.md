# Stream All

A utility/library for bundling all files matching a specified pattern and serving them as a single zip file from a web server. Files are streamed into an HTTP response for efficiency's sake. It uses stream-zip to construct the zip file.

Supported source backends:

[x] Local filesystem
[] S3

## Usage

### CLI

Stream All can be used as a command line utility, in cases where you just want to quickly make a large group of files available without going through trouble of setting up file sharing. In this case, simply install the package

```sh
$ pip install stream-all[server]
```

and run it

```sh
$ streamall /get-files ./my_music --pattern "*.mp3"
```

Then download the file at `http://localhost:8001/get-files`.

The CLI utilty supports a few arguments:

`pattern`: A Glob pattern that files in the source directory must match in order to be included in the archive. Defaults to "\*".

`zip_filename`: The filename of the resulting zip file. Defaults to "archive.zip".

`host`: The hostname to serve from. Defaults to "localhost"

`port`: The port to serve from. Defaults to 8001

`log_level`: The log level to pass to uvicorn. Defaults to "info".

### FastAPI and other frameworks

You can import `stream_files` from this module and use it within any framework that can return a streaming response from a file-like object. For example:

```python
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/download")
def service_route():
    return StreamingResponse(
        stream_files(Path("."), "*.mp3"),
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=music.zip"},
    )
```

## Roadmap

[ ] S3 Backend
[ ] Allow passing in other stream-zip parameters, such as chunk size, compression level and compression type (ZIP_32, ZIP_64, etc)
