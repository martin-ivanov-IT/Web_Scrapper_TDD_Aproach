"""
Configuration for pytest.

NOTE: This file is automatically included when running pytest.
      There is no need to import it explicitly in the test files.
"""

import os
import sys
import pytest


# allow the contents to be found automatically as if we were in that directory
sys.path.append(
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)




