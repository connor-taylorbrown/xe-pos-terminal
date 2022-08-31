## Point of Sale Terminal Instructions

This project contains a PointOfSaleTerminal class and associated API for testing purposes. A method has been added in excess of the specification to enable logging of current register state, and the builder pattern has been used to ensure that every PointOfSaleTerminal has a properly defined pricing model. A default pricing model has been added in accordance with the specifications. The following code provides an example setup:
```
from terminal.pos import PointOfSaleTerminalBuilder
from terminal.pricingmodel import create_default_pricing_model

terminal_builder = PointOfSaleTerminalBuilder()
terminal_builder.set_pricing_model(create_default_pricing_model())

terminal = terminal_builder.build()
```

To build the application and run the tests, execute the following commands:
```
pip install -r requirements.txt
pytest
```

To try out the API, run the following command:
```
uvicorn main:app --reload
```
Requests to the `/checkout/:items` endpoint will return a calculated price, where `:items` is a string of product labels. 404 is returned if the product label does not appear in the pricing model.
