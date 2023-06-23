from datetime import datetime
from pydantic import ValidationError
from pytest import fixture, raises

from energy_price_retriever.model import Price, PriceType


@fixture
def data_model() -> Price:
    """Create a price-model to test.

    This fixture creates a price model to run the unittesting on.

    Returns:
        Price: a price model to use in unittests.
    """

    return Price(
        start_datetime=datetime.now(),
        price_type=PriceType.POWER,
        price_in_eurocents=100
    )


def test_price_model(data_model: Price) -> None:
    """Unit test the Price model.

    Tests the price model by setting wrong values.
    """
    with raises(ValidationError):
        data_model.start_datetime = 'test'

    with raises(ValidationError):
        data_model.price_type = 'test'

    with raises(ValidationError):
        data_model.price_in_eurocents = 'test'
