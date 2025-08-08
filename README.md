# Gapminder Dashboard (Shiny for Python + Plotly)

A super-small demo to validate your deployment pipeline.

## Quick start (local)

```bash
mamba env create --file environment.yaml
conda activate poc-shiny-live
rm -rf site && shinylive export . ./site
python3 -m http.server --directory site 8008
```
