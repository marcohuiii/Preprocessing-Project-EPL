# preprocessing.py
# This script performs preprocessing on the EPL dataset.

#!/usr/bin/env python
# coding: utf-8

# # EPL Dataset Analysis

# ## Load Libraries


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ## Load Data and Drop Columns



data_folder = '../data/raw/'
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Dictionary to hold: {season: [list of column names]}
season_columns = {}

all_dfs = []

for file in csv_files:
    # Build Season string like '2000/01'
    raw = file.replace('.csv', '')
    start = 2000 + int(raw[:2])
    end   = 2000 + int(raw[2:])
    season = f"{start}/{str(end)[-2:]}"
    
    path = os.path.join(data_folder, file)
    try:

# === 2. Load Dataset ===
        df = pd.read_csv(path, on_bad_lines='skip', encoding='latin1')
        
        # Drop first column (e.g., 'Div') by position
        df = df.iloc[:, 1:]

        # Drop 'Time' and 'Referee' if present

# === 3. Drop Unnecessary Columns ===
        for col_to_drop in ['Time', 'Referee']:
            if col_to_drop in df.columns:
                df.drop(columns=col_to_drop, inplace=True)
        
        # Add Season column
        df['Season'] = season
        all_dfs.append(df)

    except Exception as e:

# Combine all into one DataFrame
        epl_combined = pd.concat(all_dfs, ignore_index=True)






# ## Data Cleaning 





# ### Drop betting stats and Keep only match stats



columns_to_keep = [
    'Date', 'HomeTeam', 'AwayTeam',
    'FTHG', 'HG', 'FTAG', 'AG', 'FTR', 'Res',
    'HTHG', 'HTAG', 'HTR', 'Attendance',
    'HS', 'AS', 'HST', 'AST', 'HHW', 'AHW',
    'HC', 'AC', 'HF', 'AF', 'HFKC', 'AFKC',
    'HO', 'AO', 'HY', 'AY', 'HR', 'AR',
]

# Ensure all columns exist before filtering
filtered_columns = [col for col in columns_to_keep if col in epl_combined.columns]

# Place 'Season' at the front
final_columns = ['Season'] + filtered_columns

# Filter and reorder
epl_final = epl_combined[final_columns]



# ### Handle Missing Value



missing_counts = epl_final.isnull().sum()
missing_percent = epl_final.isnull().mean() * 100

missing_summary = pd.DataFrame({
    'Missing Count': missing_counts,
    'Missing %': missing_percent.round(2)
}).sort_values(by='Missing Count', ascending=False)



# 'Attendance', 'HHW', 'AHW', 'AO' and 'HO' contain a high proportion of missing value. Therefore we are dropping them.



columns_to_drop = ['Attendance', 'HHW', 'AHW', 'HO', 'AO']

epl_final = epl_final.drop(columns=[col for col in columns_to_drop if col in epl_final.columns])




rows_with_missing = epl_final[epl_final.isnull().any(axis=1)]





# Drop rows with any missing values

# === 4. Handle Missing Values ===
epl_final = epl_final.dropna()


# ## Rename Columns








# === 5. Rename Columns ===
rename_map = {
    'Date': 'MatchDate',
    'FTHG': 'FullTimeHomeGoals',
    'FTAG': 'FullTimeAwayGoals',
    'FTR': 'FullTimeResult',
    'HTHG': 'HalfTimeHomeGoals',
    'HTAG': 'HalfTimeAwayGoals',
    'HTR': 'HalfTimeResult',
    'HS': 'HomeShots',
    'AS': 'AwayShots',
    'HST': 'HomeShotsOnTarget',
    'AST': 'AwayShotsOnTarget',
    'HC': 'HomeCorners',
    'AC': 'AwayCorners',
    'HF': 'HomeFouls',
    'AF': 'AwayFouls',
    'HY': 'HomeYellowCards',
    'AY': 'AwayYellowCards',
    'HR': 'HomeRedCards',
    'AR': 'AwayRedCards'
}

epl_final = epl_final.rename(columns=rename_map)


# ## Check Data Types and Reindex







# Covert to datetime
epl_final['MatchDate'] = pd.to_datetime(epl_final['MatchDate'], dayfirst=True)




# Convert goal columns to integers
goal_cols = [
    'FullTimeHomeGoals', 'FullTimeAwayGoals', 'HalfTimeHomeGoals', 'HalfTimeAwayGoals',
    'HomeShots', 'AwayShots', 'HomeShotsOnTarget', 'AwayShotsOnTarget',
    'HomeCorners', 'AwayCorners', 'HomeFouls', 'AwayFouls',
    'HomeYellowCards', 'AwayYellowCards', 'HomeRedCards', 'AwayRedCards'
]

for col in goal_cols:
    if col in epl_final.columns:
        epl_final[col] = pd.to_numeric(epl_final[col], errors='coerce').astype('Int64')




epl_final.reset_index(drop=True, inplace=True)






# ## Export csv file




# === 7. Export Cleaned Dataset ===
# epl_final.to_csv('../data/processed/epl_final.csv', index=False)

