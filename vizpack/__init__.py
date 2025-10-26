"""
vizpack — Beautiful Charts Without Boilerplate

Public API:
    quickplot(df, x=None, y=None, kind="scatter", theme="modern", backend="matplotlib", **kwargs)
"""
from .quickplot import quickplot

__all__ = ["quickplot"]
__version__ = "0.1.0"
