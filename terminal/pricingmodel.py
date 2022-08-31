from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Pack:
    size: int
    price: float


@dataclass
class PricingRule:
    unit_price: float
    pack: Optional[Pack] = None


class PricingException(Exception):
    '''Pricing-related exception'''


class PricingModel:
    def __init__(self, rules: Dict[str, PricingRule]):
        self.rules = rules

    def price(self, product: str, amount: int) -> float:
        pricing_rule = self.rules.get(product)
        if not pricing_rule:
            raise PricingException(f'Could not find product: {product}')

        unit_price = pricing_rule.unit_price
        if pack := pricing_rule.pack:
            return pack.price * (amount // pack.size) + unit_price * (amount % pack.size)
        else:
            return unit_price * amount


def create_default_pricing_model() -> PricingModel:
    '''Static method defining the pricing model set out in the assignment'''
    return PricingModel({
        'A': PricingRule(
            unit_price=1.25,
            pack=Pack(
                size=3,
                price=3,
            ),
        ),
        'B': PricingRule(
            unit_price=4.25,
        ),
        'C': PricingRule(
            unit_price=1,
            pack=Pack(
                size=6,
                price=5,
            ),
        ),
        'D': PricingRule(
            unit_price=0.75,
        ),
    })
