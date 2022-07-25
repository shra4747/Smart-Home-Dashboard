import asyncio
from kasa import SmartPlug


async def turn_on(ip, name):
    device = SmartPlug(ip)
    await device.update()
    await device.turn_on()
    print(f"{name} turned on.")


async def turn_off(ip, name):
    device = SmartPlug(ip)
    await device.update()
    await device.turn_off()
    print(f"{name} turned off.")


asyncio.run(turn_off("10.0.0.27", "SR Night Lamp"))
