import time
import asyncio
sleep = time.sleep
sleepio = asyncio.sleep

def fazer_burger(senha, n):
    print(f"Fazendo burger {n} para o cliente {senha}")
    sleep(1)
    return b"[|O]"

async def fazer_burger_io(senha, n):
    print(f"Fazendo burger {n} para o cliente {senha}")
    await sleepio(1)
    return b"[|O]"

async def app(scope, receive, send):
    await send({'type': 'http.response.start', 'status': 200})
    
    burger1 = await fazer_burger_io(1234, 1)
    burger2 = await fazer_burger_io(1234, 2)
    burger3 = await fazer_burger_io(1234, 3)
    bandeja = burger1 + burger2 + burger3

    await send({'type': 'http.response.body', 'body': bandeja})