from httpx import AsyncClient
from datetime import datetime
from asyncio import run


async def main() -> None:
    async with AsyncClient() as client:
        discord_url: str = "" # Discord Webhook URL goes here
        
        date_time_now: datetime = datetime.now()

        data: dict = {
            "embeds": [
                {
                    "title": "PC has been switched on",
                    "description": "Date and Time: " + date_time_now.strftime("%d-%m-%Y %H:%M:%S"),
                    "color": 0xFFFFFF # Only hexadecimals are allowed
                }
            ]
        }

        headers: dict = {
            "Content-Type": "application/json"
        }

        try:
            await client.post(discord_url, json=data, headers=headers)
        except Exception as _:
            pass


if __name__ == "__main__":
    run(main())