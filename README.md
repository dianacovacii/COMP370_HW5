# COMP 370 -- Homework 5 NYC 311 Data Analysis and Dashboard

This repository contains solutions for a technical exercise from homework 5 for the COMP370 Fall 2025 course at McGill University. The data science assignment involved New York City 311 serive request data. The goal of the project is to explore discrepancies in service response across zipcodes and provide interactive tools for analysis. 

## Features
- CLI Investigation Tool: `borough_complaints.py` outputs the number of each complaint type per borough for a given date range. 
- Jupyter Analysis: Visualize trends in the most frequent complaint type over different months. 
- Bokeh Dashboard: Compare average create-to-close response time between zip codes, with interactive dropdowns for selection. 
- Preprocessing Scripts: Designed to work with a trimmed dataset containing only the relevant year (2024)

## Installation & Setup
1. Clone this repository: 

    ```bash
    git clone https://github.com/dianacovacii/COMP370_HW5.git
    cd COMP370_HW5
    ```

2. Create and active a virtual environment (optional): 

    ```bash 
    python -m venv venv
    # Windows 
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. Install dependencies: 

    ```bash 
    pip install -r requirements.txt
    ```

## Data Instructions

**Important:** The fully NYC 331 dataset is not included in this repository due to its large size. 

1. Download the dataset yourself from [NYC Open Data 311](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/about_data)
2. Trim the dataset to only include incidents from 2024. 
    - You can use pandas, Excel, or command-line tools like grep for filtering. 
    - Ensure the CSV file is saved locally as "2024_short.csv"
    - Date columns have the following format: **MM/DD/YYYY HH:MM:SS AM/PM**

## Usage

CLI Tool: 
    ```
    python borough_complaints.py -i <input_csv> -s <start_date> -e <end_date> [-o <output_file>]
    ``` 

Jupyter Notebook: 
1. Open `charts.ipynb`
2. Observe the charts already generated

Bokeh Dashboard: 
1. Ensure the 2024 CSV ("2024_short.csv") is in the expected folder
2. Run the dashboard with `python app.py`
3. Use the dropdown menus to select zip codes and explore average response times interactively

## License 
This project is licensed under the [MIT License](LICENSE)


