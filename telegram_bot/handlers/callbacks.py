import aiohttp

async def get_rate(currency: str):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status != 200:
                    raise RuntimeError(f"HTTP {resp.status}")

                data = await resp.json()

                if not data or "rate" not in data[0]:
                    raise RuntimeError(f"Invalid response: {data}")

                return data[0]["rate"]

    except Exception as e:
        raise RuntimeError(f"Error: {e}")
