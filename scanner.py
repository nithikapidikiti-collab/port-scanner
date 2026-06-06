import asyncio, sys

async def scan(host, port):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port), timeout=2
        )
        writer.close()
        return port
    except:
        return None

async def main(host, start, end):
    tasks = [scan(host, p) for p in range(start, end+1)]
    results = await asyncio.gather(*tasks)
    open_ports = [p for p in results if p]
    print(f"\nOpen ports on {host}:")
    for p in sorted(open_ports):
        print(f"  {p}/tcp  open")

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
asyncio.run(main(host, 1, 1024))