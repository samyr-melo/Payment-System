import asyncio
import httpx
from fastapi import FastAPI

app = FastAPI(title="My System (Polling Client)")

STRIPE_URL = "http://127.0.0.1:8001/v1/payments/order_123"

@app.get("/start-poll")
async def start_polling():
    requests_count = 0
    total_bytes = 0
    final_status = "pending"

    async with httpx.AsyncClient() as client:
        while final_status == "pending":
            requests_count += 1
            response = await client.get(STRIPE_URL)
            
            # Estimativa de bytes de overhead de rede (payload + headers)
            payload_size = len(response.content) + sum(len(k) + len(v) for k, v in response.headers.items())
            total_bytes += payload_size
            
            data = response.json()
            final_status = data.get("status")

            print(f"[Req #{requests_count}] Status recebido: {final_status} | Bytes nesta req: {payload_size}")

            if final_status != "paid":
                await asyncio.sleep(1)  # Intervalo do polling

    return {
        "status": final_status,
        "total_requests": requests_count,
        "total_bytes_transferred": total_bytes,
        "wasted_requests": requests_count - 1
    }