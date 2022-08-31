import logging
from fastapi import APIRouter
from terminal.pos import PointOfSaleTerminalBuilder
from terminal.pricingmodel import create_default_pricing_model

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/checkout"
)

@router.get("/{product_string}")
async def root(
    product_string: str,
):
    terminal_builder = PointOfSaleTerminalBuilder()
    terminal_builder.set_pricing_model(create_default_pricing_model())

    terminal = terminal_builder.build()
    for product in product_string:
        terminal.scan_product(product)
    
    logger.warning("The following items have been scanned: %s", terminal.get_register())
    return terminal.calculate_total()
