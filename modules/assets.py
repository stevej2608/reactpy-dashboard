from mimetypes import guess_type
from os.path import isfile

from fastapi import FastAPI, Response
from utils.logger import log


assets_api = FastAPI()

async def get_file(filename):
    filename = './static/' + filename

    if not isfile(filename):
        log.warning("File '%s' is missing", filename)
        return Response(status_code=404)

    with open(filename, mode='rb') as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)


@assets_api.get("/{rest_of_path:path}")
async def get_assets(rest_of_path: str):
    return await get_file(rest_of_path)
