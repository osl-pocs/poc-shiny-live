# Gapminder Dashboard (Shiny for Python + Plotly)

A super-small demo to validate your deployment pipeline.

## Quick start (local)

```bash
mamba env create --file environment.yaml
conda activate poc-shiny-live
pip wheel --wheel-dir wheels lzstring==1.0.4
rm -rf site && shinylive export . ./site
python3 -m http.server --directory site 8008
```
