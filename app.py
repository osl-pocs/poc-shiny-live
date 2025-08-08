"""
Gapminder Shiny dashboard.

A tiny Shiny-for-Python app that visualises the Gapminder dataset
with a Plotly scatter plot.

Run locally:
    $ pip install -r requirements.txt
    $ shiny run --reload app:app   # or: python -m shiny run app:app
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #
GAPMINDER: pd.DataFrame = px.data.gapminder()  # built-in helper


def available_years() -> list[int]:
    """Return the sorted list of years available in the dataset."""
    years: list[int] = sorted(GAPMINDER["year"].unique().tolist())
    return years


# --------------------------------------------------------------------------- #
# UI
# --------------------------------------------------------------------------- #
page: ui.Page = ui.page_fluid(
    ui.markdown("## 🌍 Gapminder live dashboard"),
    ui.input_slider(
        "year",
        "Select year",
        min(available_years()),
        max(available_years()),
        2007,
        step=5,
        animate=True,
    ),
    ui.output_plot("scatter"),
    ui.hr(),
    ui.markdown(
        "Source: [Gapminder](https://www.gapminder.org/data/) | Built with "
        "[Shiny for Python](https://shiny.rstudio.com/py/) & "
        "[Plotly](https://plotly.com/python/)"
    ),
)

# --------------------------------------------------------------------------- #
# Server
# --------------------------------------------------------------------------- #
def server(input: Inputs, output: Outputs, session: Session) -> None:
    """Shiny server logic."""

    @reactive.Calc
    def _filtered() -> pd.DataFrame:
        """Return a subset of GAPMINDER for the selected year."""
        return GAPMINDER[GAPMINDER["year"] == input.year()]

    @output
    @render.plot
    def scatter():
        """Render an interactive scatter plot."""
        df: pd.DataFrame = _filtered()
        fig = px.scatter(
            df,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
            title=f"Gapminder — {input.year()}",
        )
        fig.update_layout(margin=dict(l=20, r=20, t=60, b=20))
        return fig


# --------------------------------------------------------------------------- #
# Shiny application object
# --------------------------------------------------------------------------- #
app = App(page, server)

if __name__ == "__main__":
    # Makes `python app.py` work as well
    from shiny import run_app

    run_app(app, reload=True)
