import pandas as pd
from vizpack import quickplot

def test_import_only():
    # Smoke test: import and confirm function exists
    assert callable(quickplot)
