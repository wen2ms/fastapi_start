from fastapi import APIRouter, Request

items = APIRouter()

@items.post('/items')
async def get_items(request: Request):
    return {"url": request.url, "client_ip": request.client.host, "client_host": request.headers.get('user-agent'),
            "cookie": request.cookies}