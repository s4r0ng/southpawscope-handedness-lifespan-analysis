# SouthpawScope: Handedness & Lifespan Risk Analysis

## 📌 Project Overview

This project explores real-world statistical datasets to identify patterns, relationships, and demographic differences using Python, Bayesian probability, and data visualization.

It tests a widely held belief: **do left-handers die younger than right-handers?** The question is framed as a business problem: should an insurer treat left-handedness as a mortality-risk factor?

The project focuses on applying statistical concepts to real datasets rather than simply performing basic exploratory data analysis.

## 🎯 Objectives

- Explore and understand real-world datasets
- Clean and prepare data for analysis
- Analyze demographic patterns and distributions
- Compare groups using Bayesian probability (left-handed vs right-handed, male vs female)
- Identify meaningful relationships and differences
- Present findings through visualizations and an interactive dashboard
- Translate statistical results into clear, data-driven insights

## 🔑 Key Findings

| Study year | Group | Mean age at death (LH) | Mean age at death (RH) | Gap (years) |
|-----------|-------|-----------------------|-----------------------|-------------|
| 1990 | All | 67.3 | 72.8 | 5.5 |
| 1990 | Male | 63.2 | 69.1 | 5.9 |
| 1990 | Female | 71.8 | 76.3 | 4.5 |
| 2018 | All | 70.3 | 72.6 | **2.3** |
| 2018 | Male | 67.1 | 68.8 | 1.7 |
| 2018 | Female | 73.6 | 76.3 | 2.7 |

- The gap shrinks sharply from 1990 to 2018 in every group, which points to a **birth-cohort effect** rather than biology. Older generations were pushed to use their right hand, so fewer old left-handers exist.
- A small residual gap remains in 2018, so the data shows the popular claim is greatly overstated, not that there is zero effect.
- **Recommendation:** do not use handedness as a pricing variable; use age, smoking, BMI and birth cohort instead.

## 📊 Datasets

The project uses publicly available datasets covering areas such as:

- **Handedness by age** — Gilbert & Wysocki (1992)
- **US death distribution by age and sex** — CDC (1999), about 2.39 million deaths
- Gender-based analysis derived from the available datasets

The original source datasets are included in the repository for reproducibility.

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Bayesian Probability & Statistical Analysis
- Jupyter Notebook
- HTML / CSS / JavaScript
- Git & GitHub

## 🔍 Analysis Performed

The project includes:

- Data cleaning and preprocessing (removed the "ALL" summary row and empty ages, converted Age to numeric, set missing female counts above age 100 to 0)
- Birth-year reconstruction (1986 survey year − age)
- Distribution analysis of deaths by age
- Age-group analysis
- Gender-based comparison
- Bayesian estimation of P(Age at death | Handedness) = P(Handedness | Age) × P(Age) / P(Handedness)
- Comparison of the 1990 and 2018 study years
- Data visualization
- Result generation and interpretation

## 📈 Dashboard

An interactive dashboard has been created to present the analyzed results in an easy-to-understand format.

The dashboard provides visual insights into the underlying datasets. Users can switch between study years (1990 / 2018) and populations (All / Male / Female), view the posterior age-at-death curves, compare gaps across groups, and test a premium-sensitivity slider.

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `Re-testing.ipynb` | Main analysis notebook |
| `gender_split_analysis.py` | Python analysis script |
| `gender_split_results.csv` | Generated analysis results |
| `db_index.html` | Interactive dashboard |
| `Screenshot db layout.png` | Dashboard preview |
| `Screenshot db layout2.png` | Dashboard preview |
| `handedness_rate_by_age_gilbert_wysocki_1992.csv` | Handedness dataset |
| `us_death_distribution_by_age_sex_cdc_1999.csv` | US mortality dataset |

## ⚠️ Limitations

- Handedness rates were digitised from a figure in the 1992 paper.
- 1999 mortality data is reused for the 1990 and 2018 study years.
- Results show association, not causation.

## 💡 Key Focus

The main focus of this project is not only to visualize data, but to demonstrate how statistical analysis can be used to move from:

**Raw Data → Data Cleaning → Statistical Analysis → Visualization → Insights**

## 🚀 Future Improvements

- Add confidence intervals and further statistical tests
- Improve dashboard interactivity
- Add additional demographic variables
- Automate the analysis pipeline
- Expand the project with additional datasets

## 👤 Author

**Sarang Mahajan**

Data Analyst | Data & Statistical Analysis | Business Intelligence

---

⭐ If you found this project useful, feel free to explore the analysis and dashboard.
