from mimetypes import guess_type
from os import path

from fastapi import FastAPI, Response
from utils.server_options.default_options import ServerOptions
from utils.logger import log

# pyright: reportUnusedFunction=false

async def get_file(filename: str):

    if not path.isfile(filename):
        log.warning("File '%s' is missing", filename)
        return Response(status_code=404)

    with open(filename, mode='rb') as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)


def assets_api(options:ServerOptions):
    api = FastAPI()

    @api.get("/{rest_of_path:path}")
    async def get_assets(rest_of_path: str):
        filename = path.join(options.asset_folder, options.asset_root, rest_of_path)
        return await get_file(filename)

    return api
