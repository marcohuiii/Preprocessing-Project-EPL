# Premier League Data Preprocessing Project ⚽

This repository contains a cleaned and structured dataset of English Premier League (EPL) football data, designed for easy use in analytics and data visualization projects. The aim is to provide a reliable and well-preprocessed dataset that others can use as a foundation for machine learning, dashboards, and other data science work.

## 📌 Project Purpose

- ✅ Practice and demonstrate data preprocessing skills
- 📊 Enable others to explore, analyze, and visualize EPL team performance
- 🧹 Provide a semi-processed dataset to save time for other data analysts or students

## 📁 Folder Structure


- `data/`
  - `raw/` – Original downloaded dataset
  - `processed/` – Cleaned dataset (CSV or Parquet)
  - `README.md` – Notes about sources and changes

- `eda/`
  - `exploratory.ipynb` – Initial exploration & visual checks

- `scripts/`
  - `clean_data.py` – Python scripts for preprocessing

- `notebooks/`
  - `preprocessing.ipynb` – Main notebook documenting the process

- `.gitignore`
- `README.md`

## 🧼 Preprocessing Workflow

1. **Data Sourcing**  
   - Sourced from [Football-Data.co.uk](https://www.football-data.co.uk/englandm.php) under Creative Commons license.

2. **Cleaning Steps**
   - Renamed and standardized column names
   - Converted date fields
   - Handled missing values
   - Normalized categorical values
   - Exported as `processed/epl_data_clean.csv`

3. **Validation**
   - Summary stats & null value checks
   - Outlier detection (simple thresholds)

## 📊 Suggested Use Cases

- Team performance over time
- Home vs. away win rate analysis
- Visualizing league standings by season
- Prediction models using historical data

## 🛠️ Tools Used

- Python (Pandas, NumPy)
- Jupyter Notebook
- Matplotlib / Seaborn
- Git + GitHub

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
Please check original data source terms for use in commercial projects.

## 🤝 Contributions

Pull requests are welcome! If you want to build on this or suggest improvements, feel free to fork the repo and raise an issue.

---