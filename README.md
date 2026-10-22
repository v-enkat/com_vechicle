# Commercial Vehicle Reliability & Failure Pattern Analysis

## Project Overview

Vehicle reliability is important for fleet availability and maintenance planning. This project uses exploratory data analysis (EDA) to investigate patterns in UK MOT test results and explore how observed failure rates vary by vehicle age, mileage, vehicle characteristics, test type, and recorded defects.

The goal is to identify patterns that may help fleet operators and maintenance planners prioritise further inspection and maintenance. The analysis describes associations in the data; it does not prove that any factor directly causes a failure.

## Problem Statement

Vehicle failures can affect fleet reliability, vehicle availability, and maintenance planning. Looking at only one factor—such as age, mileage, or defect type—may not provide a complete view of observed failure patterns.

This project examines multiple vehicle and test-related factors, including the combined relationship between vehicle age and mileage, to provide a broader view of MOT failure patterns.

## Project Objectives

- Analyse MOT test-result distribution.
- Examine how vehicle age and mileage are associated with observed failure rates.
- Compare failure rates across vehicle makes, fuel types, MOT classes, test types, and engine-capacity groups.
- Explore recorded failure items and defect-related information where available.
- Examine failure rates across combinations of vehicle age and mileage.
- Present findings through tables and visualisations that can support maintenance-planning discussions.

## Dataset

**Source:** UK DVSA anonymised MOT results, provided through the UK government's open-data resource.

The data includes anonymised test outcomes and vehicle attributes such as test date, test class, test type, mileage, make, model, fuel type, engine capacity, and first-use date. A separate failure-item dataset was also used for defect-related analysis.

### Dataset size used in the project

- The initial data file documented in the project contained **6,140,803 records and 15 columns**.
- The cleaned full-year 2024 test-results dataset used for the main analysis contained **43,441,151 rows and 18 columns**.
- The separate failure-item dataset contained **10,451,564 records and 6 columns**.

These figures refer to different data files or processing stages documented during the project; they should not be interpreted as the before-and-after row count of one single file.

### Main fields

`test_id`, `vehicle_id`, `test_date`, `test_class_id`, `test_type`, `test_result`, `test_mileage`, `postcode_area`, `make`, `model`, `colour`, `fuel_type`, `cylinder_capacity`, `first_use_date`, and `completed_date`.

## Tools & Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib

## Workflow

1. Obtain the anonymised MOT data.
2. Inspect dataset shape, column names, data types, dates, and test-result values.
3. Clean and transform relevant fields.
4. Create derived vehicle-age and mileage groups.
5. Calculate and compare observed failure rates.
6. Explore relationships and patterns using tables and visualisations.
7. Summarise findings, limitations, and possible maintenance-planning applications.

## Data Cleaning & Transformation

The project cleaning workflow includes:

- Removing invalid or header-like records.
- Converting date fields to datetime format.
- Converting mileage and engine-capacity fields to numeric format.
- Applying duplicate-row removal in the cleaning script.
- Resetting the dataframe index.
- Deriving vehicle age from test date and first-use date.
- Creating vehicle-age and mileage groups.

A separate repeated-test-ID investigation examined five fields (`test_id`, `vehicle_id`, `test_date`, `test_result`, and `test_mileage`). It identified **829,687 repeated test IDs** associated with **1,672,214 records**. Among these records, **810,668 rows (48.48%)** were duplicates across those five selected fields. This is a five-column check only; it does **not** establish the number of exact duplicate rows across all 18 columns, and repeated IDs should not automatically be treated as errors.

## Exploratory Data Analysis & Findings

### 1. Test-result distribution

| Test result | Count |
|---|---:|
| P | 33,041,072 |
| F | 8,145,625 |
| PRS | 1,983,801 |
| ABR | 241,425 |
| ABA | 29,207 |
| ABRVE | 21 |
| **Total** | **43,441,151** |

The valid outcomes used for the overall observed failure-rate calculation were P, F, and PRS, totalling **43,170,498 tests**. The overall observed failure rate was **18.87%**.

### 2. Vehicle age vs failure rate

| Vehicle age group | Observed failure rate |
|---|---:|
| 0–3 years | 8.73% |
| 3–5 years | 9.89% |
| 5–8 years | 13.57% |
| 8–10 years | 18.07% |
| 10–15 years | 23.18% |
| 15+ years | 25.86% |

The observed failure rate generally increased across older vehicle-age groups.

### 3. Mileage vs failure rate

| Mileage group | Observed failure rate |
|---|---:|
| 0–20k | 6.48% |
| 20–50k | 12.17% |
| 50–100k | 20.49% |
| 100–150k | 25.93% |
| 150–200k | 26.93% |
| 200k+ | 25.88% |

The observed failure rate generally increased with mileage, reached **26.93%** in the 150–200k group, and then decreased slightly in the 200k+ group.

### 4. Combined vehicle age and mileage

The combined analysis compared failure rates across age and mileage groups. The highest observed rate in the analysed table was **29.12%** for vehicles aged **15+ years** with mileage of **150–200k**. The lowest was **4.94%** for vehicles aged **0–3 years** with mileage of **0–20k**.

These are observed group rates, not predictions for individual vehicles.

### 5. Monthly MOT failure-rate trend (2024)

| Month | Observed failure rate |
|---|---:|
| January | 20.13% |
| February | 19.18% |
| March | 18.12% |
| April | 18.99% |
| May | 18.21% |
| June | 18.18% |
| July | 18.87% |
| August | 18.57% |
| September | 18.25% |
| October | 19.55% |
| November | 19.52% |
| December | 18.62% |

January had the highest monthly observed failure rate (**20.13%**) and March had the lowest (**18.12%**). The rates fluctuated during the year; the data alone does not explain why.

### 6. Vehicle make

The highest observed rates among the makes reported in the analysis included:

- DAEWOO — 31.68%
- TALBOT — 31.49%
- IVECO FORD — 30.43%
- WHITE KNUCKLE — 30.28%
- PROTON — 29.65%

Rates should be interpreted alongside the number of tests for each make, especially where categories have small sample sizes.

### 7. Fuel type

Among the analysed fuel types, the observed rates included LP at **23.74%**, DI at **20.75%**, and PE at **18.17%**. Comparisons should account for the number of tests in each category.

### 8. MOT vehicle class

The observed failure rates included:

- Class 7 — 23.10%
- Class 4 — 19.02%
- Class 5 — 19.22%
- Class 1 — 14.39%
- Class 3 — 11.54%
- Class 2 — 6.53%

These are comparisons across MOT classes. A class should not be assumed to represent only commercial vehicles without checking the relevant classification definition.

### 9. Test type

The NT test type had an observed failure rate of **22.64%**, while RT had **0.42%**. EI (**90.85%**) and ES (**52.31%**) had very small sample sizes of 317 and 65 tests respectively, so their rates should be treated cautiously and not compared without considering sample size and test purpose.

### 10. Engine capacity

The 2000–2500 cc group recorded the highest observed failure rate (**21.57%**) among the reported engine-capacity groups, while the 4000+ cc group recorded the lowest (**13.10%**).

### 11. Failure-item analysis

A separate failure-item dataset was used to explore recorded failure types, dangerous marks, defect locations, and defect categories. The analysis identified tyre-, wear-, corrosion-, and structural/component-related defects among frequently recorded items. These findings describe recorded defects in the available data; they do not establish the cause of a vehicle's failure.

## Key Insights

- The observed failure rate generally increased across older vehicle-age groups.
- The observed failure rate generally increased with mileage, with a small decrease in the 200k+ group compared with the 150–200k group.
- The combined age-and-mileage analysis showed variation across groups.
- Observed failure rates varied across makes, fuel types, MOT classes, test types, and engine-capacity groups.
- Monthly failure rates fluctuated during 2024.
- Defect records can help identify frequently reported issues for further review.
- These are descriptive associations; they do not demonstrate causation or predict the outcome of an individual MOT test.

## Recommendations

- Consider giving additional maintenance attention to older and higher-mileage vehicles.
- Monitor recurring defect categories as part of routine maintenance reviews.
- Compare category-level rates alongside test counts to avoid over-interpreting small groups.
- Use MOT history as one supporting input for maintenance planning, alongside fleet-specific inspection records and operational context.
- Investigate repeated test IDs and potential duplicate records before making data-removal decisions.

## Visualisations

The project includes Matplotlib visualisations for the following analyses, where the corresponding image files are available:

- Test-result distribution — `Visualizations/distribution_analysis.png`
- Failure rate by mileage — `Visualizations/trend_analysis.png`
- Monthly failure trend — `Visualizations/monthly_failure_trend.png`
- Make-wise failure rate — `Visualizations/make_failure_rate.png`
- Vehicle age and mileage combined failure rate — `Visualizations/correlation_analysis.png`
- Additional category charts, including fuel type, vehicle class, test type, engine capacity, colour, model, and postcode area.

Ensure the `Visualizations` folder and referenced image files are included in the submitted project so that the images render in the README.

## Project Structure

```text
Commercial Vehicle Reliability & Failure Pattern Analysis/
├── README.md
├── datasets/
│   └── cleaned_2024_final.csv
├── Notebook/
│   └── EDA_2024.ipynb
├── python/
│   ├── data_cleaning.py
│   └── exploratory_analysis.py
├── Visualizations/
│   ├── distribution_analysis.png
│   ├── trend_analysis.png
│   ├── age_failure_rate.png
│   ├── make_failure_rate.png
│   ├── fuel_failure_rate.png
│   ├── test_class_failure_rate.png
│   ├── model_failure_rate.png
│   ├── postcode_failure_rate.png
│   ├── monthly_failure_trend.png
│   ├── colour_failure_rate.png
│   ├── cylinder_capacity_failure_rate.png
│   ├── test_type_failure_rate.png
│   ├── correlation_analysis.png
│   └── category_analysis.png
└── Documentation/
    └── Project_Report.pdf
```

This structure reflects the files documented for the project; adjust names only if the actual folder contents differ.

## Limitations

- The analysis is descriptive and identifies associations rather than causal relationships.
- Missing values are present in some fields, including mileage and engine capacity, so some analyses may use fewer records than the full dataset.
- Category-level rates can be affected by differences in test counts and sample sizes.
- The repeated-test-ID verification compared five selected columns; exact duplicate rows across all 18 columns were not verified by that check.
- The README's project structure and image links depend on the corresponding files being present in the submitted folder.
- The analysis does not provide a validated predictive model or individual-vehicle failure-risk score.

## Future Scope

- Develop and validate a vehicle failure-risk prediction model using suitable historical data.
- Explore predictive-maintenance methods using additional vehicle and fleet records.
- Build a fleet-level maintenance-prioritisation approach.
- Extend the analysis across additional years to examine longer-term patterns.
- Improve defect-category analysis and document sample sizes and data-quality checks for each comparison.

## Conclusion

This project used Python-based EDA to explore anonymised UK MOT test results and examine how observed failure rates vary with vehicle age, mileage, and other vehicle and test characteristics. The results showed meaningful differences across groups and highlighted the value of analysing age and mileage together. These findings can support further investigation and maintenance planning, but should be interpreted as descriptive patterns rather than proof of causation or individual-vehicle predictions.
