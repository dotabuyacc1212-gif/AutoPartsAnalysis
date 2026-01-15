# Deployment Guide

## Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `app.py` as the main file
5. Deploy!

The app will automatically run `generate_data.py` during Docker build.

## Docker Hub

```bash
# Build
docker build -t yourusername/auto-parts-analysis:latest .

# Push
docker push yourusername/auto-parts-analysis:latest

# Run
docker run -p 8501:8501 yourusername/auto-parts-analysis:latest
```

## GitHub Container Registry

The included GitHub Action automatically builds and pushes to `ghcr.io` on every push to main.

```bash
# Pull and run
docker pull ghcr.io/yourusername/auto-parts-analysis:main
docker run -p 8501:8501 ghcr.io/yourusername/auto-parts-analysis:main
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Generate data
python generate_data.py

# Run app
streamlit run app.py
```
