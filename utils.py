import aiohttp
from config import *


async def get_shortlink(link):

    if not (SHORTENER_API and SHORTENER_SITE):
        return link

    https = link.split(":")[0]
    if https == "http":
        https = "https"
        link = link.replace("http", https)
    url = f'https://{SHORTENER_SITE}/api'
    params = {'api': SHORTENER_API,
              'url': link,
              }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            if data["status"] == "success":
                return data['shortenedUrl']
            else:
                return f"Error: {data['message']}"
