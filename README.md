# Auto Parts Analysis 🚗🔧

Interactive web application for analyzing automotive parts data, built with Streamlit.

🌐 **Live Demo:** [https://autopartsanalysis.streamlit.app/](https://autopartsanalysis.streamlit.app/)  
🐳 **Docker Hub:** [matveivehbe/auto-parts-analysis](https://hub.docker.com/r/matveivehbe/auto-parts-analysis)

[Русская версия](README_RU.md)

## Features

- 📊 Interactive data visualization of auto parts inventory
- 🔍 Search and filter parts by category, manufacturer, and price
- 📈 Statistical analysis of pricing trends
- 💾 Export filtered results to Excel
- 🎨 Modern and responsive UI

## Quick Start

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/auto-parts-analysis.git
cd auto-parts-analysis

# Install dependencies 
pip install -r requirements.txt

# Generate sample data
python generate_data.py

# Run the application
streamlit run app.py
```

### Docker

```bash
# Pull from Docker Hub
docker pull matveivehbe/auto-parts-analysis:latest

# Run the container
docker run -p 8501:8501 matveivehbe/auto-parts-analysis:latest
```

Or build locally:

```bash
# Build the image
docker build -t auto-parts-analysis .

# Run the container
docker run -p 8501:8501 auto-parts-analysis
```

Open your browser at `http://localhost:8501`

## Project Structure

```
.
├── app.py                  # Main Streamlit application
├── generate_data.py        # Sample data generator
├── auto_parts_data.xlsx    # Generated data file
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
└── .streamlit/
    └── config.toml        # Streamlit settings
```

## Technologies

- **Python 3.11+**
- **Streamlit** - Web interface
- **Pandas** - Data manipulation
- **Plotly** - Interactive charts
- **OpenPyXL** - Excel file handling

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
