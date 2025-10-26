from contextlib import contextmanager
from typing import Optional

import pandas as pd

# We only implement the matplotlib backend for v0.1.0 to keep it lightweight.
# Plotly / Seaborn backends can be added later in a similar API.
def quickplot(df: "pd.DataFrame",
              x: Optional[str] = None,
              y: Optional[str] = None,
              kind: str = "scatter",
              theme: str = "modern",
              backend: str = "matplotlib",
              title: Optional[str] = None,
              xlabel: Optional[str] = None,
              ylabel: Optional[str] = None,
              legend: bool = True,
              grid: bool = True,
              **kwargs):
    """
    Render a quick plot with opinionated defaults.

    Parameters
    ----------
    df : pandas.DataFrame
        The data source.
    x, y : str, optional
        Column names to plot.
    kind : {"scatter", "line", "bar", "hist"}
        Plot type.
    theme : {"modern", "dark", "pastel"}
        Built-in theme.
    backend : {"matplotlib"}
        Currently only "matplotlib" is implemented.
    title, xlabel, ylabel : str, optional
        Labels and title.
    legend : bool
        Whether to show legend (if applicable).
    grid : bool
        Whether to show gridlines.
    **kwargs : dict
        Additional kwargs passed to the plotting function.
    """
    if backend != "matplotlib":
        raise NotImplementedError("Only the 'matplotlib' backend is supported in v0.1.0")

    import matplotlib.pyplot as plt

    with _apply_theme(theme):
        ax = plt.gca()

        if kind == "scatter":
            if x is None or y is None:
                raise ValueError("Scatter requires x and y.")
            ax.scatter(df[x], df[y], **kwargs)
        elif kind == "line":
            if x is None or y is None:
                raise ValueError("Line requires x and y.")
            ax.plot(df[x], df[y], **kwargs)
        elif kind == "bar":
            if x is None or y is None:
                raise ValueError("Bar requires x and y.")
            ax.bar(df[x], df[y], **kwargs)
        elif kind == "hist":
            if x is None:
                raise ValueError("Hist requires x.")
            ax.hist(df[x], **kwargs)
        else:
            raise ValueError(f"Unsupported kind: {kind}")

        if title is None:
            # simple automatic title
            base = kind.capitalize()
            if x and y:
                base += f" of {y} vs {x}"
            elif x:
                base += f" of {x}"
            title = base
        ax.set_title(title)

        if xlabel is None and x is not None:
            xlabel = x
        if ylabel is None and y is not None:
            ylabel = y

        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        if grid:
            ax.grid(True, alpha=0.3)

        # Legend: only show if labels were provided via kwargs (e.g., label="Series A")
        if legend and any(hasattr(h, "get_label") and h.get_label() != "_nolegend_" for h in ax.get_children()):
            ax.legend(loc="best", frameon=False)

        plt.tight_layout()
        plt.show()
        return ax


@contextmanager
def _apply_theme(name: str):
    """Context manager to apply simple rcParams themes for matplotlib."""
    import matplotlib as mpl
    # capture current rcParams
    old = mpl.rcParams.copy()

    if name == "modern":
        _modern_theme(mpl)
    elif name == "dark":
        _dark_theme(mpl)
    elif name == "pastel":
        _pastel_theme(mpl)
    else:
        # default to modern if unknown
        _modern_theme(mpl)

    try:
        yield
    finally:
        # restore
        mpl.rcParams.update(old)


def _modern_theme(mpl):
    mpl.rcParams["axes.facecolor"] = "white"
    mpl.rcParams["figure.facecolor"] = "white"
    mpl.rcParams["axes.edgecolor"] = "#e0e0e0"
    mpl.rcParams["axes.labelsize"] = 11
    mpl.rcParams["axes.titlesize"] = 13
    mpl.rcParams["grid.linestyle"] = "--"
    mpl.rcParams["grid.alpha"] = 0.3
    mpl.rcParams["font.size"] = 10


def _dark_theme(mpl):
    mpl.rcParams["axes.facecolor"] = "#111111"
    mpl.rcParams["figure.facecolor"] = "#111111"
    mpl.rcParams["axes.edgecolor"] = "#444444"
    mpl.rcParams["axes.labelcolor"] = "#e5e5e5"
    mpl.rcParams["xtick.color"] = "#e5e5e5"
    mpl.rcParams["ytick.color"] = "#e5e5e5"
    mpl.rcParams["axes.labelsize"] = 11
    mpl.rcParams["axes.titlesize"] = 13
    mpl.rcParams["grid.color"] = "#333333"
    mpl.rcParams["grid.alpha"] = 0.4
    mpl.rcParams["font.size"] = 10


def _pastel_theme(mpl):
    mpl.rcParams["axes.facecolor"] = "#FAFAFF"
    mpl.rcParams["figure.facecolor"] = "#FFFFFF"
    mpl.rcParams["axes.edgecolor"] = "#DADAF5"
    mpl.rcParams["axes.labelsize"] = 11
    mpl.rcParams["axes.titlesize"] = 13
    mpl.rcParams["grid.linestyle"] = ":"
    mpl.rcParams["grid.alpha"] = 0.25
    mpl.rcParams["font.size"] = 10
