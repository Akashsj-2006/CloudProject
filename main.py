from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Optional
import uvicorn

app = FastAPI(title="MConnect - Campus Marketplace")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Sample product data (in a real app, this would be in a database)
products = [
    {"id": 1, "name": "Calculus Textbook", "price": 25.99, "category": "Books", "seller": "John D.", "image": "book.jpg"},
    {"id": 2, "name": "Bicycle", "price": 150.00, "category": "Vehicles", "seller": "Alice M.", "image": "bike.jpg"},
    {"id": 3, "name": "Laptop Stand", "price": 15.50, "category": "Electronics", "seller": "Bob T.", "image": "stand.jpg"},
    {"id": 4, "name": "Coffee Maker", "price": 30.00, "category": "Appliances", "seller": "Sarah K.", "image": "coffee.jpg"},
]

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/sell", response_class=HTMLResponse)
async def sell_page(request: Request):
    return templates.TemplateResponse("sell.html", {"request": request})

@app.get("/product/{product_id}", response_class=HTMLResponse)
async def product_detail(request: Request, product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse("product.html", {"request": request, "product": product})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
