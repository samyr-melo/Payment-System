import asyncio
import httpx
from fastapi import FastAPI, BackgroundTasks

app = FastAPI(title="Mock Stripe (Webhook Dispatcher)")

MY_SYSTEM_WEBHOOK_URL = "http://127.0.0.1:8000/webhook/pagamento"

async def dispatch_webhook(payload: dict):
    # Simula o processamento bancário assíncrono (ex: 3 segundos)
    await asyncio.sleep(3)
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(MY_SYSTEM_WEBHOOK_URL, json=payload, timeout=5.0)
            print(f"[STRIPE] Webhook enviado com sucesso! Status code do cliente: {response.status_code}")
        except Exception as e:
            print(f"[STRIPE] Erro ao entregar webhook: {e}")

@app.post("/simulate-customer-payment/{order_id}")
async def simulate_payment(order_id: str, background_tasks: BackgroundTasks):
    event_payload = {
        "event": "payment_intent.succeeded",
        "data": {
            "order_id": order_id,
            "status": "paid",
            "amount": 150.00,
            "currency": "BRL"
        }
    }
    
    # Dispara a notificação via webhook em background
    background_tasks.add_task(dispatch_webhook, event_payload)
    
    return {
        "message": f"Pagamento da ordem {order_id} iniciado. O webhook será disparado em 3 segundos."
    }