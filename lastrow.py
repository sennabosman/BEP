import os
import pandas as pd

os.getcwd()

filepath = f"Data/Gevoeligheidsanalyse/GVA_UV4_D7.csv"
results = pd.read_csv(filepath)


def find_last_step(results):
    results_filtered = pd.DataFrame(columns=list(results.columns))

    for run in list(results["RunId"].unique()):
        results_run = results.loc[results["RunId"] == run]
        last_row_df = pd.DataFrame([results_run.iloc[-1]])
        results_filtered = pd.concat([results_filtered, last_row_df])

    return results_filtered

results_filtered = find_last_step(results)

results_filtered.to_csv(f"Data/Gevoeligheidsanalyse/GVA_UV4_D7_lastrow.csv")