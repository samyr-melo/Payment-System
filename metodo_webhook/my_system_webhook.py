from fastapi import FastAPI, Request

app = FastAPI(title="My System (Webhook Receiver)")

# Armazena eventos recebidos para consulta
EVENTS_LOG = []

@app.post("/webhook/pagamento")
async def receive_webhook(request: Request):
    payload = await request.json()
    raw_body = await request.body()
    
    # Tamanho real transferido nessa única requisição
    headers_size = sum(len(k) + len(v) for k, v in request.headers.items())
    total_bytes = len(raw_body) + headers_size

    event_info = {
        "event": payload.get("event"),
        "order_id": payload.get("data", {}).get("order_id"),
        "status": payload.get("data", {}).get("status"),
        "bytes_received": total_bytes
    }
    EVENTS_LOG.append(event_info)

    print(f"\n[WEBHOOK RECEBIDO] Evento: {event_info['event']} | Status: {event_info['status']} | Bytes: {total_bytes}")
    
    # Responde 200 OK imediatamente para o Stripe não tentar reenviar
    return {"received": True}

@app.get("/orders")
async def list_orders():
    return {"processed_events": EVENTS_LOG}