import fastapi

app = fastapi.FastAPI()


@app.get('/')
def root():
    return {"message": "Hello, Crypto World!"}


@app.get("/crypto/{coin}")
def get_crypto_price(coin: str):
    return {"coin": coin, "price": "...Fetching from API soon..."}
