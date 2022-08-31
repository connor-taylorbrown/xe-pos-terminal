from argparse import ArgumentError
from typing import Dict, Optional

from terminal.pricingmodel import PricingModel


class PointOfSaleTerminal:
    def __init__(self, pricing_model: PricingModel):
        self.pricing_model = pricing_model
        self._register: Dict[str, int] = {}

    def get_register(self) -> Dict[str, int]:
        '''Provide copy of current register state for logging purposes'''
        return {
            **self._register
        }
    
    def scan_product(self, product: str) -> None:
        '''Add new item to register'''
        if not self._register.get(product):
            self._register[product] = 1
        else:
            self._register[product] += 1

    def calculate_total(self) -> float:
        '''Apply pricing model to items in register'''
        return sum(
            self.pricing_model.price(product, amount)
            for product, amount in self._register.items()
        )


class PointOfSaleTerminalBuilder:
    '''Builder to ensure every PointOfSaleTerminal instance has a pricing model'''
    def __init__(self):
        self.pricing_model: Optional[PricingModel] = None

    def set_pricing_model(
        self,
        pricing_model: PricingModel,
    ) -> 'PointOfSaleTerminalBuilder':
        self.pricing_model = pricing_model
        return self

    def build(self) -> PointOfSaleTerminal:
        if not self.pricing_model:
            raise ArgumentError('Expected pricing model')
        
        return PointOfSaleTerminal(self.pricing_model)
