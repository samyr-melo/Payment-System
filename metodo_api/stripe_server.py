import time
from fastapi import FastAPI

app = FastAPI(title="Mock Stripe API")

# Estado em memória simulando a transação
PAYMENT_DB = {
    "order_123": {
        "status": "pending",
        "amount": 150.00,
        "currency": "BRL",
        "created_at": None
    }
}

@app.get("/v1/payments/{order_id}")
async def get_payment_status(order_id: str):
    order = PAYMENT_DB.get(order_id)
    if not order:
        return {"error": "Order not found"}, 404

    # Dispara a mudança de status após 5 segundos da 1ª chamada
    if order["created_at"] is None:
        order["created_at"] = time.time()
    elif time.time() - order["created_at"] > 5:
        order["status"] = "paid"

    return order