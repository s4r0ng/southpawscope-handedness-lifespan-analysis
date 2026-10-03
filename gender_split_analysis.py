"""Phase 2 - Gender-split Bayesian analysis: handedness vs age at death.
Inputs : handedness_rate_by_age_gilbert_wysocki_1992.csv, us_death_distribution_by_age_sex_cdc_1999.csv
Output : gender_split_results.csv
Method : P(A|LH) = P(LH|A) * P(A) / P(LH), computed separately for each sex
         using that sex's own left-handed rate and own death counts."""

import numpy as np, pandas as pd

lh = pd.read_csv("handedness_rate_by_age_gilbert_wysocki_1992.csv")
BASE_YEAR = 1986                      # year of the handedness survey
lh["Birth_year"] = BASE_YEAR - lh["Age"]

dd = pd.read_csv("us_death_distribution_by_age_sex_cdc_1999.csv", skiprows=[1])
dd["Age"] = pd.to_numeric(dd["Age"], errors="coerce")
dd = dd.dropna(subset=["Age", "Both Sexes"]).fillna(0)   # missing female counts at extreme ages = 0
ages = dd["Age"].to_numpy(float)

def p_lh_given_age(ages, study_year, col):
    early, late = lh[col].iloc[-10:].mean(), lh[col].iloc[:10].mean()
    lo, hi = study_year - BASE_YEAR + 10, study_year - BASE_YEAR + 86
    p = np.where(ages > hi, early, late) / 100
    mid = (ages >= lo) & (ages <= hi)
    p[mid] = lh.set_index("Birth_year")[col].reindex(study_year - ages[mid]).to_numpy() / 100
    return p

rows = []
for year in (1990, 2018):
    for sex in ("Both Sexes", "Male", "Female"):
        col = "Mean" if sex == "Both Sexes" else sex
        if col == "Mean":
            lh["Mean"] = lh[["Male", "Female"]].mean(axis=1)
        n = dd[sex].to_numpy(float); prior = n / n.sum()
        p = p_lh_given_age(ages, year, col); p_lh = (p * prior).sum()
        mean_l = (ages * p * prior / p_lh).sum()
        mean_r = (ages * (1 - p) * prior / (1 - p_lh)).sum()
        rows.append(dict(study_year=year, sex=sex, p_lh_pct=round(100 * p_lh, 2),
                         mean_age_death_LH=round(mean_l, 2), mean_age_death_RH=round(mean_r, 2),
                         gap_years=round(mean_r - mean_l, 2)))
out = pd.DataFrame(rows); out.to_csv("gender_split_results.csv", index=False); print(out.to_string(index=False))
