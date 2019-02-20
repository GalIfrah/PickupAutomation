import pytest

from Infrastructure.WebDriverWrapper import Wrapper
import os
from time import sleep


@pytest.mark.usefixtures("driver_init")
class BasicTestClass:

    webDriver = Wrapper()
    env = None
