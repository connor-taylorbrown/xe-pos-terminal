import pytest

from terminal.pos import PointOfSaleTerminalBuilder
from terminal.pricingmodel import create_default_pricing_model


@pytest.mark.parametrize(
    'product_string, price',
    [
        ('ABCDABA', 13.25),
        ('CCCCCCC', 6),
        ('ABCD', 7.25)
    ]
)
def test_expected_results(product_string: str, price: float):
    terminal_builder = PointOfSaleTerminalBuilder()
    terminal_builder.set_pricing_model(create_default_pricing_model())
    terminal = terminal_builder.build()

    for product in product_string:
        terminal.scan_product(product)

    result = terminal.calculate_total()

    assert result == price
