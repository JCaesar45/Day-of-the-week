# 🎄 Christmas Sunday Finder
*A sophisticated multi-platform solution for discovering when December 25th falls on Sunday*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://html5.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
  - [Web Application](#web-application)
  - [Python Library](#python-library)
  - [Command Line Interface](#command-line-interface)
- [Algorithms](#algorithms)
- [Performance](#performance)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Christmas Sunday Finder is a comprehensive, multi-platform solution that accurately identifies all years within a specified range where December 25th falls on a Sunday. This project provides three distinct implementations:

1. **Interactive Web Application** - Beautiful, responsive frontend with advanced visualizations
2. **Python Library** - Enterprise-grade backend with multiple algorithms and analysis tools
3. **Command Line Interface** - Powerful CLI for automation and scripting

Perfect for HR departments planning holiday schedules, researchers studying calendar patterns, or developers building calendar-related applications.

## ✨ Features

### 🌐 Web Application
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Interactive Visualizations** - Animated charts and real-time statistics
- **Advanced UI/UX** - Snow animations, gradient backgrounds, smooth transitions
- **Accessibility** - Keyboard navigation, screen reader support
- **Performance** - Optimized for speed with caching and lazy loading

### 🐍 Python Library
- **Multiple Algorithms** - Basic, optimized, and generator-based implementations
- **Advanced Analytics** - Pattern analysis, gap detection, frequency calculations
- **Data Visualization** - Matplotlib/Seaborn integration for beautiful charts
- **Export Capabilities** - JSON, CSV, TXT formats
- **Enterprise Features** - Logging, error handling, performance monitoring

### 💻 Command Line Interface
- **Batch Processing** - Handle multiple year ranges efficiently
- **Automation Ready** - Perfect for cron jobs and scheduled tasks
- **Flexible Output** - Various formats and verbosity levels
- **Scripting Support** - Easy integration with shell scripts

## 🛠 Technologies

### Frontend
- **HTML5** - Semantic markup with accessibility features
- **CSS3** - Advanced animations, gradients, responsive design
- **JavaScript ES6+** - Modern JavaScript with classes and async/await
- **No Dependencies** - Pure vanilla JavaScript for maximum performance

### Backend
- **Python 3.7+** - Type hints, dataclasses, modern Python features
- **datetime/calendar** - Native Python date handling
- **matplotlib/seaborn** - Professional data visualization
- **pandas** - Data analysis and manipulation
- **argparse** - Command-line interface framework

## 🚀 Installation

### Web Application
```bash
# Clone the repository
git clone https://github.com/JCaesar45/christmas-sunday-finder.git
cd christmas-sunday-finder

# Open the web application
open web/index.html
# or simply double-click index.html
```

### Python Library
```bash
# Install via pip
pip install christmas-sunday-finder

# Or install from source
git clone https://github.com/JCaesar45/christmas-sunday-finder.git
cd christmas-sunday-finder/python
pip install -e .

# Install optional dependencies for visualization
pip install matplotlib seaborn pandas
```

## 📖 Usage

### 🌐 Web Application

Simply open `index.html` in your browser and:

1. Enter start and end years
2. Click "Find Sundays" 
3. View results with beautiful animations
4. Explore statistics and patterns
5. Export results (if needed)

**Features:**
- Real-time input validation
- Animated snow background
- Interactive year cards
- Statistical analysis
- Responsive design

### 🐍 Python Library

```python
from christmas_sunday_finder import ChristmasSundayFinder

# Initialize finder
finder = ChristmasSundayFinder()

# Basic usage
years = finder.find_xmas_sunday_basic(2000, 2100)
print(f"Sunday Christmases: {years}")

# Optimized algorithm
years = finder.find_xmas_sunday_optimized(1900, 2100)
print(f"Found {len(years)} occurrences")

# Generator for large datasets
for year in finder.find_xmas_sunday_generator(1900, 3000):
    process_year(year)  # Memory efficient

# Advanced analysis
analysis = finder.analyze_patterns(1900, 2100)
print(f"Average gap: {analysis['average_gap']} years")
print(f"Frequency: {analysis['frequency_percentage']}%")

# Data visualization
finder.visualize_data(1900, 2100, save_path='analysis.png')

# Export results
finder.export_results(years, 'json', 'christmas_sundays.json')
```

### 💻 Command Line Interface

```bash
# Basic usage
python -m christmas_sunday_finder --start 2000 --end 2100

# With analysis and visualization
python -m christmas_sunday_finder --start 1900 --end 2100 --analyze --visualize

# Export to different formats
python -m christmas_sunday_finder --start 2000 --end 2100 --export json
python -m christmas_sunday_finder --start 2000 --end 2100 --export csv
python -m christmas_sunday_finder --start 2000 --end 2100 --export txt

# Run tests
python -m christmas_sunday_finder --test

# Generator method for large ranges
python -m christmas_sunday_finder --start 1900 --end 3000 --method generator
```

## ⚙️ Algorithms

### Algorithm 1: Basic Datetime Approach
```python
def find_xmas_sunday_basic(start_year, end_year):
    """O(n) time complexity, O(k) space complexity"""
    sunday_years = []
    for year in range(start_year, end_year + 1):
        date = datetime.date(year, 12, 25)
        if date.weekday() == 6:  # Sunday
            sunday_years.append(year)
    return sunday_years
```

### Algorithm 2: Optimized Pattern Recognition
```python
def find_xmas_sunday_optimized(start_year, end_year):
    """Uses 28-year calendar cycle for improved performance"""
    # Leverages mathematical patterns in the Gregorian calendar
    # Caches results for repeated queries
    # Handles century year exceptions
```

### Algorithm 3: Memory-Efficient Generator
```python
def find_xmas_sunday_generator(start_year, end_year):
    """Yields results one at a time for large datasets"""
    for year in range(start_year, end_year + 1):
        if datetime.date(year, 12, 25).weekday() == 6:
            yield year
```

## 📊 Performance

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| Basic | O(n) | O(k) | Small ranges, simplicity |
| Calendar | O(n) | O(k) | Educational purposes |
| Optimized | O(n) with caching | O(k) | Production environments |
| Generator | O(n) | O(1) | Large datasets, streaming |

**Benchmarks (2000-2100):**
- Basic: ~0.002 seconds
- Optimized: ~0.001 seconds (with cache)
- Generator: ~0.0015 seconds

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m christmas_sunday_finder --test

# Test specific functionality
python -m pytest tests/ -v

# Test with coverage
python -m pytest tests/ --cov=christmas_sunday_finder --cov-report=html
```

**Test Coverage:**
- ✅ Accuracy verification against known results
- ✅ Edge case handling (leap years, century years)
- ✅ Performance benchmarking
- ✅ Input validation
- ✅ Algorithm consistency

## 📚 API Documentation

### ChristmasSundayFinder Class

#### Methods

**`find_xmas_sunday_basic(start_year: int, end_year: int) -> List[int]`**
- Basic datetime-based implementation
- Parameters: Start and end years (inclusive)
- Returns: List of years where Dec 25 is Sunday

**`find_xmas_sunday_optimized(start_year: int, end_year: int) -> List[int]`**
- Optimized implementation with caching
- Uses mathematical patterns for better performance
- Automatically handles leap years and century exceptions

**`analyze_patterns(start_year: int, end_year: int) -> Dict`**
- Comprehensive pattern analysis
- Returns statistics including gaps, frequencies, trends
- Includes decade and century distribution analysis

**`visualize_data(start_year: int, end_year: int, save_path: str = None)`**
- Creates professional visualizations
- Multiple chart types (timeline, histograms, trends)
- Optional save to file

**`export_results(years: List[int], format: str, filename: str)`**
- Export in JSON, CSV, or TXT formats
- Includes metadata and statistics
- Customizable filenames

## 💡 Examples

### HR Department Planning
```python
# Find all Sunday Christmases for next 50 years
finder = ChristmasSundayFinder()
future_sundays = finder.find_xmas_sunday_optimized(2024, 2074)

# Plan extra paid holidays
for year in future_sundays:
    print(f"Year {year}: Extra holiday week granted")
```

### Academic Research
```python
# Analyze historical patterns
analysis = finder.analyze_patterns(1900, 2100)

# Research calendar cycles
print(f"Most common gap: {analysis['most_common_gap']} years")
print(f"Average frequency: {analysis['frequency_percentage']}%")
```

### Web Integration
```javascript
// Fetch data for web application
fetch('/api/christmas-sundays?start=2000&end=2100')
    .then(response => response.json())
    .then(data => {
        displayResults(data.years);
        showStatistics(data.statistics);
    });
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md).

### Development Setup

```bash
# Clone repository
git clone https://github.com/JCaesar45/christmas-sunday-finder.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Submit pull request
git push origin feature/your-feature-name
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Python Software Foundation for the excellent datetime module
- The matplotlib team for visualization capabilities
- Contributors and testers from the open-source community

**Made with ❤️ for the open-source community. Merry Christmas and Happy Coding! 🎄**
```
