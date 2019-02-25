import pytest

from Infrastructure.WebDriverWrapper import Wrapper


@pytest.mark.usefixtures("driver_init")
class BasicTestClass:

    webDriver = Wrapper()
    env = None
