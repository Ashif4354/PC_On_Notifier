from httpx import AsyncClient
from datetime import datetime, timezone, timedelta
from asyncio import run


async def main():
    async with AsyncClient() as client:
        discord_url: str = "" # Discord Webhook URL goes here
        
        date_time_now: datetime = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)

        data: dict = {
            "embeds": [
                {
                    "title": "PC has been switched on!",
                    "description": "Date and Time: " + date_time_now.strftime("%d-%m-%Y %H:%M:%S"),
                    "color": 0xFFFFFF
                }
            ]
        }

        headers: dict = {
            "Content-Type": "application/json"
        }

        try:
            await client.post(discord_url, json=data, headers=headers)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    run(main())