from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import checkout
from terminal.pricingmodel import PricingException

app = FastAPI()
app.include_router(checkout.router)

@app.exception_handler(PricingException)
async def handle_pricing_exception(
    _: Request,
    exc: PricingException,
):
    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc)
        }
    )
