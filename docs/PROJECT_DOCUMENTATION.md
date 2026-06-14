# MAIZE PRICE FORECASTING SYSTEM: A MACHINE LEARNING APPROACH FOR KENYAN COUNTY-LEVEL PRICE PREDICTION

---

**BY**

**[YOUR NAME]**

**[YOUR REGISTRATION NUMBER]**

---

*THIS PROJECT PROPOSAL IS SUBMITTED IN PARTIAL FULFILLMENT FOR THE AWARD OF [YOUR DEGREE] OF [YOUR UNIVERSITY]*

---

**[CAMPUS]**

**[MONTH YEAR]**

---

## DECLARATION

This is my original work and has not been submitted in any other institution of higher learning for academic or any other purpose.

**Signature:** _______________________________ **Date:** ________________

**[YOUR NAME]**

---

This project proposal is presented to the university for examination with the approval of the supervisor.

**Signature:** _______________________________ **Date:** ________________

**[SUPERVISOR NAME]**

**[UNIVERSITY]**

**[CAMPUS]**

---

## ACKNOWLEDGEMENT

First and foremost, I thank God Almighty for the strength, wisdom, and perseverance to complete this project.

I express my deepest gratitude to my supervisor, [Supervisor Name], for the invaluable guidance, constructive criticism, and continuous support throughout this research. Your expertise and encouragement were instrumental in shaping this work.

I am profoundly grateful to my parents for their unwavering support, both moral and financial, throughout my academic journey. Your sacrifices and belief in me have been the foundation of my success.

To my friends and colleagues, thank you for the encouragement, late-night brainstorming sessions, and technical discussions that enriched this project.

I also acknowledge the Kenya Agricultural Market Information System (KAMIS) and the Agricultural Business Rapid Assessment (AgriBORA) for providing the maize price data used in this research. The Open-Meteo weather API and the Central Bank of Kenya for economic indicators data are also gratefully acknowledged.

Finally, I thank all those who contributed directly or indirectly to the successful completion of this project.

---

## ABSTRACT

Maize is a staple food crop in Kenya, and its price volatility directly affects food security and the livelihoods of millions of Kenyans. Accurate price forecasting is essential for farmers, traders, policymakers, and consumers to make informed decisions. However, maize price prediction is challenging due to the complex interplay of seasonal patterns, weather conditions, economic factors, and market dynamics across Kenya's diverse counties.

This project presents a machine learning-based maize price forecasting system that predicts weekly maize prices across multiple Kenyan counties. The system employs a pooled XGBoost (Extreme Gradient Boosting) regression model trained on price change (Δ-price) as the target variable, effectively removing the strong autocorrelation that makes persistence forecasting deceptively competitive. The model is trained on a panel dataset spanning 2021 to 2025, comprising price data from 46 counties, weather variables (temperature, rainfall), economic indicators (CPI, USD/KES exchange rate, inflation rate), and engineered features including price lags, rolling statistics, and seasonal flags.

A 5-fold expanding window cross-validation strategy is used to evaluate model performance across different time periods, ensuring robustness and temporal generalization. The pooled model incorporates county one-hot encoding to enable information sharing across markets while maintaining county-specific predictions. Additionally, per-county fine-tuning is implemented using warm-started XGBoost models initialized from the pooled model.

Model performance is evaluated using multiple metrics: Mean Absolute Scaled Error (MASE) to measure improvement over the persistence baseline, directional accuracy to assess price movement prediction, Mean Absolute Error (MAE) on the original price scale, and symmetric Mean Absolute Percentage Error (sMAPE). The pooled XGBoost model achieves a MASE of 0.322 (68% better than persistence), a directional accuracy of 75.5%, and a MAE of 2.07 KES across the five target counties (Kiambu, Kirinyaga, Mombasa, Nairobi, Uasin-Gishu).

An interactive Streamlit dashboard is developed to visualize historical price trends, generate multi-week forecasts with confidence intervals, analyze seasonal patterns, identify key price drivers through feature importance analysis, and display model performance metrics. The system is deployable on Streamlit Cloud, making it accessible to stakeholders.

**Keywords:** Maize price forecasting, XGBoost, machine learning, time series, Kenya agriculture, Δ-price, pooled model, expanding window cross-validation, MASE, Streamlit dashboard

---

## TABLE OF CONTENTS

DECLARATION ............................................................................................................................. ii
ACKNOWLEDGEMENT .................................................................................................................. iii
ABSTRACT .................................................................................................................................. iv
TABLE OF CONTENTS .................................................................................................................. v
TABLE OF FIGURES .................................................................................................................... vii
LIST OF TABLES ........................................................................................................................ viii

CHAPTER 1: INTRODUCTION ...................................................................................................... 1
1.1 Introduction ......................................................................................................................... 1
1.2 Background of the Study .................................................................................................... 1
1.3 Problem Statement .............................................................................................................. 4
1.4 Proposed Solution ............................................................................................................... 5
1.5 Research Objectives ............................................................................................................ 7
1.6 Justification of the Study .................................................................................................... 8
1.7 Significance of the Study .................................................................................................... 8
1.8 Assumptions ........................................................................................................................ 9
1.9 Limitations of the Study ...................................................................................................... 9
1.10 Project Scope .................................................................................................................... 10

CHAPTER 2: LITERATURE REVIEW ............................................................................................ 11
2.1 Introduction ......................................................................................................................... 11
2.2 Machine Learning in Agricultural Price Forecasting ......................................................... 11
2.3 Global Similar Systems ..................................................................................................... 15
2.3.1 FAO Global Information and Early Warning System (GIEWS) .................................. 15
2.3.2 International Food Policy Research Institute (IFPRI) Price Forecasting Models ...... 16
2.3.3 World Bank's Agricultural Price Forecasting Platform .............................................. 17
2.4 Local Similar Systems ....................................................................................................... 18
2.4.1 Kenya Agricultural Market Information System (KAMIS) ........................................ 18
2.4.2 Kenya Food Security Outlook (FEWS NET Kenya) ................................................... 19
2.4.3 AgriBORA Market Platform ....................................................................................... 20
2.4.4 DigiFarm and M-Farm ................................................................................................ 21
2.5 Theoretical Framework ..................................................................................................... 22
2.5.1 Time Series Forecasting Fundamentals ...................................................................... 22
2.5.2 Traditional Statistical Methods ................................................................................... 23
2.5.3 Ensemble Learning Methods ...................................................................................... 25
2.5.4 Gradient Boosting and XGBoost ................................................................................ 26
2.5.5 Cross-Validation for Time Series ............................................................................... 28
2.6 Research Gaps ................................................................................................................... 29

CHAPTER 3: METHODOLOGY .................................................................................................. 31
3.1 Introduction ....................................................................................................................... 31
3.2 Research Design ............................................................................................................... 31
3.3 Data Collection ................................................................................................................. 32
3.3.1 KAMIS Price Data ...................................................................................................... 32
3.3.2 AgriBORA Price Data ................................................................................................ 33
3.3.3 Weather Data .............................................................................................................. 34
3.3.4 Economic Indicators Data .......................................................................................... 34
3.4 Data Exploration ............................................................................................................... 35
3.4.1 Summary Statistics ...................................................................................................... 35
3.4.2 Missing Data Analysis ................................................................................................ 36
3.4.3 Price Distribution and Outlier Assessment ................................................................. 37
3.5 Data Preparation and Feature Engineering ....................................................................... 38
3.5.1 Data Cleaning ............................................................................................................. 38
3.5.2 Feature Construction and Rationale ........................................................................... 40
3.6 Software Tools and Technologies .................................................................................... 42
3.7 Experimental Setup .......................................................................................................... 43
3.7.1 Target Variable Engineering ...................................................................................... 44
3.7.2 Pooled XGBoost Model Architecture ......................................................................... 45
3.7.3 Hyperparameter Tuning .............................................................................................. 46
3.7.4 Expanding Window Cross-Validation ........................................................................ 47
3.7.5 Recursive Multi-Step Forecasting .............................................................................. 48
3.7.6 Per-County Fine-Tuning ............................................................................................. 49
3.7.7 Evaluation Metrics ..................................................................................................... 50
3.8 Project Methodology ........................................................................................................ 51
3.8.1 Agile Development Methodology .............................................................................. 51
3.8.2 Justification for Agile Methodology .......................................................................... 52
3.8.3 Development Phases ................................................................................................... 53
3.9 System Architecture .......................................................................................................... 54
3.9.1 Architecture Overview ............................................................................................... 54
3.9.2 Data Pipeline .............................................................................................................. 54
3.9.3 Model Training Pipeline ............................................................................................ 55
3.9.4 Dashboard Application .............................................................................................. 56

CHAPTER 4: RESULTS AND DISCUSSION ................................................................................ 57
4.1 Introduction ....................................................................................................................... 57
4.2 Model Performance Results .............................................................................................. 57
4.2.1 Overall Results Across All Folds ............................................................................... 57
4.2.2 Per-County Performance ............................................................................................ 58
4.2.3 Performance Across Folds (Temporal Stability) ....................................................... 60
4.3 Feature Importance Analysis ............................................................................................. 61
4.4 Seasonal Pattern Analysis ................................................................................................ 63
4.5 Per-County Price Trend Analysis ..................................................................................... 64
4.6 Dashboard Interface and User Guide ................................................................................ 65
4.6.1 Overview Tab ............................................................................................................. 66
4.6.2 Seasonality Tab .......................................................................................................... 66
4.6.3 Drivers Tab ................................................................................................................ 67
4.6.4 Performance Tab ........................................................................................................ 67
4.7 Comparison with Literature Benchmarks .......................................................................... 68
4.8 Practical Interpretation of Results ..................................................................................... 69

CHAPTER 5: CONCLUSION AND RECOMMENDATIONS .......................................................... 71
5.1 Summary of Findings ........................................................................................................ 71
5.2 Conclusion ........................................................................................................................ 71
5.3 Implementation Roadmap ................................................................................................. 72
5.4 Cost-Benefit Analysis ....................................................................................................... 73
5.5 Policy Recommendations .................................................................................................. 74
5.6 Recommendations for System Users ................................................................................ 75
5.7 Future Work ...................................................................................................................... 75

REFERENCES ............................................................................................................................. 77

APPENDICES .............................................................................................................................. 80
Appendix A: Budget and Resources ........................................................................................ 80
Appendix B: Project Schedule (Gantt Chart) .......................................................................... 81
Appendix C: Dashboard User Guide ........................................................................................ 82
Appendix D: Data Dictionary ................................................................................................... 85

---

## TABLE OF FIGURES

Figure 1: Kenya Maize Price Trends by County (2021-2025) ..................................................... 2
Figure 2: System Architecture Diagram ...................................................................................... 54
Figure 3: Data Pipeline Flowchart .............................................................................................. 55
Figure 4: Model Performance Comparison Bar Charts ................................................................ 61
Figure 5: Feature Importance (Top 15) ....................................................................................... 62
Figure 6: Monthly Seasonal Patterns Across Target Counties .................................................... 63
Figure 7: Dashboard Overview Tab Screenshot .......................................................................... 65
Figure 8: Dashboard Seasonality Tab Screenshot ........................................................................ 66
Figure 9: Dashboard Drivers Tab Screenshot .............................................................................. 67
Figure 10: Dashboard Performance Tab Screenshot .................................................................... 68
Figure 11: Gantt Chart - Project Schedule ................................................................................. 81

## LIST OF TABLES

Table 1: Data Sources Summary .................................................................................................. 35
Table 2: Summary Statistics of Price Data by County ................................................................. 36
Table 3: Missing Data Patterns Across Counties ......................................................................... 37
Table 4: Engineered Feature Set ................................................................................................. 41
Table 5: Software and Library Versions ..................................................................................... 43
Table 6: Hyperparameter Search Space and Final Configuration ................................................ 47
Table 7: Expanding Window Cross-Validation Folds .................................................................. 48
Table 8: Overall Model Performance Comparison ....................................................................... 58
Table 9: Per-County Best Model Performance ............................................................................. 59
Table 10: Performance Across Folds for Pooled XGBoost .......................................................... 60
Table 11: Comparison of Results with Literature Benchmarks ................................................... 69
Table 12: Budget Estimates ......................................................................................................... 80
Table 13: Work Breakdown Structure ........................................................................................... 81
Table 14: Data Dictionary - All Variables ................................................................................... 85

---

# CHAPTER 1: INTRODUCTION

## 1.1 Introduction

This chapter provides the foundation for the research project by presenting the background of maize price forecasting in Kenya, the problem that motivated this study, the proposed solution, research objectives, justification, significance, assumptions, limitations, and the project scope. The chapter establishes the context within which the maize price forecasting system was developed and sets the stage for the literature review and methodology that follow.

## 1.2 Background of the Study

Agriculture is the backbone of the Kenyan economy, contributing approximately 33% to the Gross Domestic Product (GDP) and employing over 40% of the population (Kenya National Bureau of Statistics, 2023). Among agricultural commodities, maize holds a position of paramount importance as the country's primary staple food. The average Kenyan consumes approximately 98 kilograms of maize per year, making it a critical component of household food security (Ministry of Agriculture, Livestock, Fisheries and Cooperatives, 2022).

Kenya's maize sector encompasses approximately 4.5 million smallholder farmers who cultivate maize on farms averaging less than 2 hectares. These smallholders account for approximately 75% of the country's total maize production. The annual national maize production stands at approximately 40 million bags (each bag weighing 90 kilograms), with consumption estimated at 44 million bags annually, creating a structural deficit of approximately 4 million bags that must be met through imports, primarily from Uganda and Tanzania. This import dependency means that regional supply shocks and cross-border trade policies directly impact domestic maize prices. The maize value chain also employs an estimated 10 million Kenyans across production, trading, processing, and retail activities, underscoring its centrality to the national economy and food system.

Maize prices in Kenya exhibit significant volatility driven by a complex interplay of factors including seasonal production cycles, weather patterns (particularly rainfall during the long and short rainy seasons), input costs, fuel prices, inflation, exchange rate fluctuations, market infrastructure, and post-harvest losses. This price volatility has profound implications for food security, household welfare, and macroeconomic stability. When maize prices spike, low-income urban households suffer disproportionately as they spend a larger share of their income on food. Conversely, when prices collapse during harvest seasons, smallholder farmers—who constitute the majority of maize producers—face income losses that undermine their livelihoods.

To illustrate the scale of price volatility, consider actual market data from Nairobi over the study period: wholesale maize prices have ranged from a low of approximately KES 28 per kilogram during harvest periods to a high of over KES 52 per kilogram during peak scarcity. A single bag of maize (90 kg) therefore fluctuates in value from KES 2,520 to KES 4,680—a difference of over KES 2,000 per bag. For a smallholder farmer harvesting 20 bags from a one-acre plot, this price swing represents a potential income difference of over KES 40,000, which is substantially larger than many rural households' monthly expenses. Similarly, Mombasa prices have shown distinct patterns driven by the city's reliance on imported maize, with prices at times diverging significantly from inland markets due to port logistics, global grain prices, and exchange rate movements. These real-world examples underscore the critical need for accurate price forecasts.

The Kenya Agricultural Market Information System (KAMIS), operated by the Ministry of Agriculture, provides weekly price data for various agricultural commodities across markets in all 47 counties. Similarly, the Agricultural Business Rapid Assessment (AgriBORA) platform provides transaction-based wholesale prices. Despite the availability of this data, systematic and accurate price forecasting remains a challenge. Most price information available to stakeholders is historical, with limited predictive capability.

Traditional approaches to price forecasting in Kenya have relied on expert judgment, simple trend analysis, and basic statistical methods. These approaches, while providing some value, are limited in their ability to capture the complex, non-linear relationships between the numerous factors that influence maize prices. Furthermore, they often fail to provide probabilistic forecasts or confidence intervals that would enable risk-based decision-making.

In recent years, machine learning has emerged as a powerful tool for time series forecasting across various domains, including agricultural commodity prices. Techniques such as gradient boosting, random forests, and deep learning have demonstrated superior performance compared to traditional statistical methods, particularly when dealing with high-dimensional data and complex non-linear relationships. However, the application of these techniques to county-level maize price forecasting in Kenya remains relatively unexplored.

This project addresses this gap by developing a machine learning-based maize price forecasting system that leverages XGBoost—a state-of-the-art gradient boosting framework—to predict weekly maize prices across multiple Kenyan counties. The system incorporates price data from multiple sources, weather variables, economic indicators, and engineered features to capture the multi-faceted nature of maize price determination. The model is trained using a pooled approach that enables information sharing across counties, combined with per-county fine-tuning to capture local market dynamics.

![Figure 1: Kenya Maize Price Trends by County (2021-2025)](screenshots/figure_1.png)

*Caption: Weekly maize prices for Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu counties from 2021 to 2025. The chart shows county-specific price levels and common seasonal patterns. Note the distinct price regimes: Nairobi and Mombasa exhibit higher price levels reflective of urban demand and import dependency, while Uasin-Gishu shows lower, more stable prices due to its proximity to production areas. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

## 1.3 Problem Statement

Despite the critical importance of maize to Kenya's food security and economy, stakeholders across the value chain—including farmers, traders, policymakers, and consumers—lack access to accurate, timely, and reliable price forecasts. This information gap leads to several interconnected problems that perpetuate inefficiency, risk, and food insecurity throughout the maize sector.

**For Farmers:** Smallholder farmers, who produce over 75% of Kenya's maize, make planting, harvesting, and marketing decisions based on limited information. A typical farmer in Kiambu County, for instance, must decide at the beginning of each season whether to invest in fertilizer, certified seeds, and other inputs—costing upwards of KES 30,000 per acre—without knowing what prices will be at harvest time. Without reliable price forecasts, they often sell at suboptimal prices immediately after harvest when supply is high and prices are low, missing the opportunity to benefit from seasonal price increases. This contributes to persistent rural poverty and food insecurity. Many farmers resort to distress sales to middlemen who offer cash advances but at significantly discounted rates, further eroding farm incomes.

**For Traders and Millers:** Maize traders and millers face significant inventory and procurement risks due to price uncertainty. A miller in Nairobi who procures 1,000 bags of maize per week faces a weekly procurement bill of KES 2.8 million to KES 5.2 million, depending on market prices. The inability to forecast price movements leads to either excessive inventory holding costs or stock-outs, both of which have negative financial implications. These costs are ultimately passed on to consumers in the form of higher prices. Large millers may hedge by diversifying suppliers, but small-scale traders have limited risk management options and are particularly vulnerable to adverse price movements.

**For Policymakers:** Government agencies responsible for food security, including the Ministry of Agriculture and the National Cereals and Produce Board (NCPB), require accurate price forecasts to make timely decisions about strategic grain reserves, import licenses, and market interventions. Reactive rather than proactive policy responses often result from the absence of reliable forecasting tools. For example, the decision to issue import permits typically occurs only after prices have already risen to crisis levels, whereas a forecasting system could provide early warning of impending price spikes, enabling preemptive action such as releasing strategic reserves or accelerating import approvals.

**For Consumers:** Urban households, particularly those in low-income brackets, bear the brunt of maize price volatility. A household in an informal settlement in Nairobi spends approximately 30% of its monthly food budget on maize products. When maize prices spike from KES 40 to KES 52 per kilogram, this adds approximately KES 500 to KES 800 to the monthly food bill of a typical family—a significant burden for households already living on less than KES 10,000 per month. Price spikes can push vulnerable households into food insecurity, while price collapses threaten the viability of the entire maize value chain.

Existing forecasting approaches suffer from several limitations:

1. **Reliance on historical trends:** Most current approaches look backward rather than forward, providing little predictive value.

2. **Inability to capture complex relationships:** Simple statistical methods cannot adequately model the non-linear interactions between weather, economics, and market dynamics.

3. **Lack of granularity:** National-level forecasts miss important county-level variations driven by local production, market access, and demand patterns.

4. **Absence of uncertainty quantification:** Point forecasts without confidence intervals limit risk-based decision-making.

5. **Limited automation:** Manual forecasting processes are time-consuming, inconsistent, and difficult to scale.

6. **No directional guidance:** Existing approaches rarely provide information about the expected direction of price movement, which is often as important as the magnitude for practical decision-making.

These problems collectively create a pressing need for an automated, machine learning-based maize price forecasting system that can provide accurate, county-level predictions with quantified uncertainty to support decision-making across the maize value chain.

## 1.4 Proposed Solution

This project proposes the development of a machine learning-based maize price forecasting system that addresses the identified problems through the following key features:

**Data Integration:** The system integrates multiple data sources including KAMIS prices, AgriBORA prices, weather data (temperature, rainfall, wind), and economic indicators (CPI, USD/KES exchange rate, inflation rate) to create a comprehensive feature set for price prediction.

**Δ-Price Forecasting:** Instead of predicting absolute prices, the system predicts week-over-week price changes (Δ-price). This approach effectively removes the strong autocorrelation present in price time series and provides a more meaningful evaluation framework where the persistence baseline (predicting no change) serves as a natural benchmark. A model that achieves MASE less than 1 demonstrably adds value over the naive forecast.

**Pooled XGBoost Model:** A single XGBoost regression model is trained on data from all 46 counties simultaneously, using county one-hot encoding to capture county-specific effects. This pooled approach enables the model to learn from price dynamics across all counties, improving generalization, particularly for counties with limited historical data.

**Expanding Window Cross-Validation:** Model performance is evaluated using a 5-fold expanding window cross-validation strategy that respects the temporal order of the data. This approach provides robust performance estimates across different time periods and simulates the realistic scenario of predicting future prices based on past observations.

**Per-County Fine-Tuning:** While the pooled model provides strong baseline predictions, per-county fine-tuning allows the model to adapt to county-specific price dynamics by continuing training on individual county data, warm-started from the pooled model.

**Comprehensive Evaluation Metrics:** Model performance is assessed using multiple metrics including MASE (which directly measures improvement over persistence), directional accuracy (percentage of correctly predicted price movements), MAE on the original price scale, and sMAPE.

**Interactive Dashboard:** An intuitive Streamlit-based dashboard provides stakeholders with access to historical price trends, multi-week forecasts with confidence intervals, seasonal pattern analysis, feature importance insights, and model performance comparisons across four dedicated tabs (Overview, Seasonality, Drivers, Performance).

**Cloud Deployment:** The system is deployable on Streamlit Cloud, enabling anytime, anywhere access without requiring local installation or technical expertise.

## 1.5 Research Objectives

### Main Objective

To develop and evaluate a machine learning-based maize price forecasting system that provides accurate, county-level price predictions with quantified uncertainty to support decision-making across Kenya's maize value chain.

### Specific Objectives

1. **To analyze** the historical maize price data from KAMIS and AgriBORA sources to identify patterns, trends, and seasonal variations across Kenyan counties.

2. **To design and engineer** a comprehensive feature set incorporating price lags, rolling statistics, weather variables, economic indicators, and temporal features that capture the key drivers of maize price movements.

3. **To develop** a pooled XGBoost regression model trained on Δ-price (price change) with county one-hot encoding that enables information sharing across counties while maintaining county-specific predictions.

4. **To implement** an expanding window cross-validation strategy that provides robust performance evaluation across different time periods, ensuring the model's ability to generalize to future data.

5. **To evaluate** the model's predictive performance using MASE, directional accuracy, MAE, and sMAPE metrics, comparing against the persistence baseline and per-county fine-tuned variants.

6. **To build** an interactive Streamlit dashboard that visualizes historical trends, generates multi-week forecasts with confidence intervals, analyzes seasonal patterns, identifies key price drivers, and displays model performance.

7. **To deploy** the system on Streamlit Cloud for accessible, web-based stakeholder use.

## 1.6 Justification of the Study

This research is justified on several grounds:

**Academic Contribution:** The study contributes to the growing body of knowledge on machine learning applications in agricultural price forecasting, particularly in the context of developing economies. The pooled modeling approach with per-county fine-tuning offers a novel methodology that balances global learning with local adaptation. The use of Δ-price and MASE-based evaluation within an expanding window framework provides a rigorous template for time series forecasting evaluation that addresses common methodological pitfalls in the literature.

**Practical Utility:** The system provides actionable price forecasts that can directly benefit stakeholders across the maize value chain. Farmers can make informed marketing decisions, traders can optimize inventory management, and policymakers can implement timely interventions to stabilize prices. The interactive dashboard makes these insights accessible to non-technical users, bridging the gap between advanced machine learning and practical decision-making.

**Methodological Innovation:** The use of Δ-price as the target variable, combined with expanding window cross-validation and MASE-based evaluation, provides a rigorous framework for time series forecasting that addresses common pitfalls in the evaluation of forecasting models (e.g., inappropriate use of R², single train-test splits, and failure to account for temporal dependencies).

**Scalability:** While focused on maize and five target counties, the methodology is designed to be scalable to other commodities and all 47 counties, providing a template for national-level agricultural price forecasting.

**Food Security Impact:** Improved price forecasting has a direct positive impact on food security by enabling more efficient market functioning, reducing price risk, and supporting evidence-based policy decisions.

## 1.7 Significance of the Study

The implementation of this project is expected to provide the following benefits:

1. **Empowered Farmers:** Access to reliable price forecasts enables farmers to make informed decisions about when and where to sell their produce, potentially increasing their income by 10-20% through strategic market timing. For a smallholder farmer harvesting 20 bags per season, this translates to an additional KES 5,000 to KES 10,000 in income—a substantial improvement in household welfare.

2. **Improved Market Efficiency:** Traders and millers can better manage inventory, reduce waste, and optimize procurement strategies, leading to lower transaction costs and more stable prices. More efficient markets benefit all participants through reduced spreads between farm-gate and retail prices.

3. **Evidence-Based Policy:** Policymakers gain access to predictive insights that support proactive rather than reactive interventions in the maize market, including strategic grain reserve management and import/export decisions. Early warning of impending price spikes enables preemptive action that can prevent food crises.

4. **Enhanced Food Security:** More accurate price information contributes to improved food security outcomes by reducing price volatility and ensuring more stable access to maize for consumers. Vulnerable households benefit from more predictable food costs that facilitate household budgeting and consumption smoothing.

5. **Technological Transfer:** The project demonstrates the practical application of machine learning to agricultural challenges in developing economies, providing a template for similar initiatives in other countries and commodities.

6. **Open Source Foundation:** The codebase is structured to be reusable and extensible, enabling future researchers and developers to build upon this work.

## 1.8 Assumptions

The following assumptions were made in conducting this study:

1. The historical price data obtained from KAMIS and AgriBORA is accurate and representative of market conditions across the target counties.

2. Weather data from the Open-Meteo API provides a reasonable approximation of local weather conditions that affect maize production and prices.

3. Economic indicators (CPI, exchange rate, inflation) are available on a weekly or monthly basis and capture the relevant macroeconomic influences on maize prices.

4. The relationships between the predictor variables and maize prices remain sufficiently stable over the forecasting horizon for the model to generate meaningful predictions.

5. Users of the dashboard have basic internet connectivity and can access web-based applications.

6. The historical data period (2021-2025) is sufficiently long to capture the seasonal patterns and price dynamics relevant for forecasting.

## 1.9 Limitations of the Study

This study encountered the following limitations:

1. **Data Availability:** The availability and completeness of price data vary significantly across counties. Some counties have sparse data, limiting the model's ability to learn county-specific patterns. Data gaps are particularly pronounced for counties with fewer market reporting points.

2. **Forecast Horizon:** While the system can generate forecasts for up to 12 weeks, forecast accuracy declines for longer horizons due to accumulating uncertainty in recursive predictions. Forecasts beyond 8 weeks should be interpreted with caution.

3. **External Factors:** The model cannot account for unpredictable events such as government policy changes, large-scale imports, or geopolitical events that may significantly affect maize prices. The model's predictions assume business-as-usual conditions.

4. **Data Quality:** Price data from market information systems may contain reporting errors, inconsistencies, or biases that affect model training and evaluation. Price data based on reported (rather than transaction) prices may not fully reflect actual market conditions.

5. **Geographic Coverage:** While the pooled model is trained on 46 counties, the system's evaluation and dashboard focus on 5 target counties, limiting the assessment of model performance across all regions.

6. **Computational Resources:** The expanding window cross-validation and fine-tuning processes require significant computational resources, limiting the number of hyperparameter configurations that could be explored.

## 1.10 Project Scope

This project covers the following aspects:

**Geographic Scope:** The system focuses on five target counties—Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu—representing different agricultural zones and market types in Kenya. Kiambu represents a peri-urban county with diverse agricultural activity; Kirinyaga is a major maize-producing area in the central highlands; Mombasa represents a coastal, import-dependent urban market; Nairobi represents the largest consumer market in East Africa; and Uasin-Gishu is a major grain basket county in the Rift Valley. The pooled model is trained on data from 46 counties.

**Temporal Scope:** The project uses weekly price data from 2021 to 2025. The model generates forecasts for 4 to 12 weeks ahead.

**Functional Scope:**

- Data collection and cleaning from multiple sources (KAMIS, AgriBORA, weather, economic)
- Feature engineering including price lags, rolling statistics, seasonal flags, and economic indicators
- Machine learning model development using XGBoost with pooled architecture
- Model evaluation using expanding window cross-validation with 5 folds
- Interactive dashboard with 4 analysis tabs (Overview, Seasonality, Drivers, Performance)
- Recursive multi-step forecasting with bootstrap confidence intervals
- Cloud deployment capability on Streamlit Cloud

**Technical Scope:**

- Programming language: Python
- Machine learning framework: XGBoost, scikit-learn
- Dashboard framework: Streamlit
- Data processing: Pandas, NumPy
- Visualization: Matplotlib, Plotly
- Deployment: Streamlit Cloud

**Out of Scope:**

- Real-time data ingestion (the system uses batch-processed data)
- Mobile application development
- Integration with external APIs for automated data updates
- Multi-commodity forecasting (focused on maize only)
- Deep learning models (LSTM, Transformer) due to data limitations
- User authentication and multi-user support
- Automated retraining pipeline

---

# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction

This chapter provides a comprehensive review of existing literature related to agricultural price forecasting, machine learning applications in time series prediction, and similar systems developed both globally and locally. The review establishes the theoretical foundation for the project and identifies research gaps that the proposed system addresses. The chapter is organized into sections covering machine learning in agricultural price forecasting, global similar systems, local similar systems, theoretical framework including detailed mathematical formulations of key methods, and research gaps.

## 2.2 Machine Learning in Agricultural Price Forecasting

Agricultural commodity price forecasting has been a subject of extensive research due to its importance for food security, farmer livelihoods, and economic planning. Traditional approaches to price forecasting have included econometric models such as AutoRegressive Integrated Moving Average (ARIMA), Vector Autoregression (VAR), and structural equation models. While these methods provide interpretable results, they are limited by their assumptions of linearity and stationarity, which are often violated in real-world price data.

### ARIMA Models: Mathematical Formulation

The ARIMA model, introduced by Box and Jenkins (1970), is one of the most widely used approaches for time series forecasting. An ARIMA model is denoted as ARIMA(p, d, q), where:

- **p**: Order of the autoregressive (AR) component
- **d**: Degree of differencing required to achieve stationarity (I component)
- **q**: Order of the moving average (MA) component

The mathematical formulation of ARIMA(p, d, q) after differencing d times is:

```math
(1 - \phi_1 B - \phi_2 B^2 - ... - \phi_p B^p)(1 - B)^d y_t = c + (1 + \theta_1 B + \theta_2 B^2 + ... + \theta_q B^q)\varepsilon_t
```

where B is the backshift operator (B^k y_t = y_{t-k}), φ_i are AR coefficients, θ_i are MA coefficients, c is a constant, and ε_t is white noise error.

The AR component models the dependency between an observation and a specified number of lagged observations. The I (Integrated) component refers to the differencing operation that makes the series stationary. The MA component models the dependency between an observation and the residual errors from a moving average model applied to lagged observations.

While ARIMA models have been successfully applied to agricultural price forecasting, they have several fundamental limitations:

1. **Linearity assumption:** ARIMA assumes linear relationships between past and future values, which cannot capture non-linear market dynamics such as threshold effects or regime changes.

2. **Univariate nature:** Standard ARIMA models use only the past values of the target variable, ignoring exogenous factors like weather, economic conditions, and supply chain disruptions that influence prices.

3. **Stationarity requirement:** Although differencing can handle some non-stationarity, structural breaks and changing volatility patterns remain challenging.

4. **Limited interaction effects:** ARIMA cannot model interactions between multiple predictors, limiting its ability to capture complex market dynamics.

### Traditional Statistical Methods

Beyond ARIMA, several traditional statistical methods have been applied to agricultural price forecasting:

**Exponential Smoothing (ETS):** Exponential smoothing methods weight observations with exponentially decreasing weights, giving more importance to recent observations. The general formulation includes components for level, trend, and seasonality:

```math
\hat{y}_{t+h|t} = l_t + h b_t + s_{t+h-m}
```

where l_t is the level, b_t is the trend, and s_t is the seasonal component with period m. While ETS methods are simple, interpretable, and computationally efficient, they share the same limitations as ARIMA regarding linearity and the inability to incorporate exogenous variables.

**Vector Autoregression (VAR):** VAR models extend the univariate AR approach to multiple time series, capturing the interdependencies between multiple variables. A VAR(p) model is formulated as:

```math
y_t = c + A_1 y_{t-1} + A_2 y_{t-2} + ... + A_p y_{t-p} + \varepsilon_t
```

where y_t is a vector of endogenous variables, A_i are coefficient matrices, and ε_t is a vector of white noise. VAR models can capture cross-variable relationships (e.g., how maize prices in Nairobi affect prices in Mombasa). However, VAR models become overparameterized quickly as the number of variables increases, and they maintain the linearity assumption.

**Structural Equation Models:** These models specify explicit causal relationships between variables based on economic theory. For example, a structural model for maize prices might include equations for supply (based on planted area, rainfall, input costs) and demand (based on population, income, substitute prices). While these models are interpretable and theory-driven, they require strong assumptions about the underlying causal structure and are difficult to estimate reliably with limited data.

### Comparison of Machine Learning and Traditional Methods

| Aspect | Traditional Methods (ARIMA, ETS, VAR) | Machine Learning Methods (XGBoost, RF, SVR) |
|--------|---------------------------------------|---------------------------------------------|
| Linearity | Assume linear relationships | Capture non-linear patterns naturally |
| Feature handling | Limited to lags and differencing | Handle hundreds of features including interactions |
| Missing data | Require complete series | Built-in handling (XGBoost learns default directions) |
| Assumptions | Stationarity, normality, independence | Fewer statistical assumptions |
| Interpretability | High (coefficient-based) | Moderate (feature importance, SHAP values) |
| Forecast horizon | Multi-step via recursive/direct | Multi-step via recursive approach |
| Exogenous variables | Limited inclusion | Natural integration of diverse data types |
| Computational cost | Low | Moderate to high |
| Uncertainty quantification | Built-in prediction intervals | Requires bootstrap or quantile methods |
| Handling high-dimensional data | Poor (overparameterization) | Excellent (regularization, feature selection) |

In recent years, machine learning methods have gained prominence in agricultural price forecasting due to their ability to capture non-linear relationships and handle high-dimensional feature spaces. Kamilaris and Prenafeta-Boldú (2018) conducted a comprehensive survey of deep learning applications in agriculture, identifying price forecasting as a key area where machine learning methods outperform traditional statistical approaches.

Xiong et al. (2018) compared various machine learning techniques for agricultural commodity price forecasting, including support vector regression (SVR), random forests, and neural networks. Their study found that ensemble methods, particularly random forests and gradient boosting, consistently outperformed individual models across multiple commodities and forecast horizons. The authors attributed this superiority to the ability of ensemble methods to reduce variance while maintaining low bias.

The XGBoost algorithm, introduced by Chen and Guestrin (2016), has emerged as one of the most successful machine learning methods for structured data, including time series forecasting. XGBoost is an optimized implementation of gradient boosted decision trees that incorporates regularization to prevent overfitting, parallel processing for computational efficiency, and built-in handling of missing values. Its success in numerous machine learning competitions and real-world applications has established it as a state-of-the-art method for regression and classification tasks.

Several studies have specifically applied XGBoost to agricultural price forecasting. Chakraborty et al. (2021) used XGBoost to predict onion prices in India, achieving a 15% improvement in RMSE compared to ARIMA models. The study demonstrated that XGBoost effectively captured seasonal price patterns and responded to supply-side shocks. Similarly, Wang et al. (2020) applied XGBoost to corn price prediction in the United States, incorporating weather variables, crop progress data, and market indicators. Their model achieved R² values above 0.85 for short-term forecasts (1-4 weeks).

The concept of using price changes (returns) rather than absolute prices as the target variable is well-established in financial time series forecasting. In financial econometrics, it is standard practice to model returns rather than prices because prices are typically non-stationary (having unit roots), while returns are stationary. This approach was adapted for agricultural price forecasting by Jha and Sinha (2014), who found that modeling price changes improved forecast accuracy for agricultural commodities in India. The persistence forecast (predicting zero change) provides a natural baseline that is often surprisingly competitive, particularly for short horizons.

Pan et al. (2022) introduced a transfer learning approach to agricultural price forecasting, where a model trained on data from multiple regions is fine-tuned on individual regional data. Their study on vegetable prices in China showed that the transfer learning approach improved forecast accuracy by 12-18% compared to region-specific models trained from scratch, particularly for regions with limited historical data.

The use of expanding window cross-validation for time series model evaluation has been extensively discussed in the forecasting literature. Hyndman and Athanasopoulos (2021) recommend time series cross-validation (also known as "forecast evaluation with a rolling origin") as the gold standard for evaluating forecasting models. This approach involves training the model on an expanding training window and evaluating on a fixed-size test window that advances through time, providing multiple performance estimates that capture the model's stability across different time periods.

## 2.3 Global Similar Systems

### 2.3.1 FAO Global Information and Early Warning System (GIEWS)

The Food and Agriculture Organization (FAO) of the United Nations operates the Global Information and Early Warning System (GIEWS), which monitors food production, prices, and market conditions worldwide. GIEWS provides price monitoring and analysis for staple commodities across more than 80 countries, including Kenya.

GIEWS uses a combination of statistical models, expert analysis, and field reports to generate price outlooks. The system incorporates satellite imagery, weather data, and economic indicators to assess supply conditions and price pressures. However, GIEWS operates primarily at the national or regional level, lacking the granularity to provide county-level forecasts. The system also relies heavily on expert judgment and qualitative analysis, with limited automation of the forecasting process.

**Strengths:**
- Broad geographic coverage spanning over 80 countries
- Integration of multiple data sources (satellite, weather, economic)
- Long operational history with established methodologies

**Weaknesses:**
- National/regional focus lacks local granularity
- Heavy reliance on expert judgment rather than automated ML
- Limited capacity for frequent (weekly) updates
- Not publicly accessible for direct querying or custom analysis

### 2.3.2 International Food Policy Research Institute (IFPRI) Price Forecasting Models

The International Food Policy Research Institute (IFPRI) has developed several price forecasting models for agricultural commodities as part of its research on food security and market dynamics. IFPRI's models include structural econometric models, partial equilibrium models, and, more recently, machine learning approaches.

In a notable study, IFPRI researchers developed a machine learning framework for predicting maize prices in Southern Africa (Dorosh et al., 2020). The framework incorporated satellite-derived vegetation indices, rainfall data, and market price series to predict prices 1-3 months ahead. The study found that random forest models achieved 20-30% lower RMSE compared to ARIMA baselines.

IFPRI's Agricultural Market Information System (AMIS) provides market monitoring and short-term outlooks for major agricultural commodities globally. While AMIS provides valuable analysis, its focus is on global and regional markets rather than sub-national price dynamics.

**Strengths:**
- Rigorous academic research methodology
- Integration of remote sensing data (satellite imagery)
- Focus on food security applications

**Weaknesses:**
- Research-oriented rather than operational
- Limited sub-national coverage
- Models are not publicly available as deployable systems
- Data requirements may be too demanding for routine application

### 2.3.3 World Bank's Agricultural Price Forecasting Platform

The World Bank has invested in agricultural price forecasting initiatives as part of its broader work on food security and market development. The Bank's "Price Watch" system monitors food prices across developing countries and provides analysis of price trends and market conditions.

A recent World Bank project in South Asia developed a machine learning-based price forecasting system for staple commodities in India, Bangladesh, and Nepal (World Bank, 2022). The system used historical prices, weather data, and market characteristics to generate 1-4 week price forecasts using gradient boosting and neural network models. The project demonstrated the feasibility of automated price forecasting systems in data-constrained environments.

The World Bank's approach emphasizes the importance of simple, interpretable models that can be deployed and maintained in low-capacity settings. Their focus on usability and stakeholder engagement provides important lessons for the current project.

**Strengths:**
- Emphasis on deployment and operational use
- Focus on developing country contexts
- Practical approach to model interpretability

**Weaknesses:**
- Limited to specific project countries/regions
- Models may not generalize to East African contexts
- Less emphasis on methodological innovation
- Dashboard interfaces are less developed than analytical components

## 2.4 Local Similar Systems

### 2.4.1 Kenya Agricultural Market Information System (KAMIS)

KAMIS is the primary source of agricultural market data in Kenya, operated by the Ministry of Agriculture, Livestock, Fisheries and Cooperatives. KAMIS collects and disseminates weekly price information for major agricultural commodities across markets in all 47 counties.

KAMIS provides historical price data that is essential for understanding market trends and patterns. The system publishes weekly price bulletins that include current prices, price comparisons, and basic trend analysis. However, KAMIS does not provide predictive analytics or price forecasts. Its focus is on reporting current and historical market conditions rather than anticipating future price movements.

The KAMIS data collection methodology involves field officers visiting designated markets and recording prices, which are then aggregated and published. While this provides valuable ground-level data, the manual collection process introduces potential delays and inconsistencies.

For the current project, KAMIS serves as a critical data source for historical maize prices. The system provides the retail market price data used to train the forecasting model.

**Strengths:**
- Comprehensive coverage of all 47 counties
- Long-running time series (multiple years)
- Official government data source with established methodology
- Weekly publication frequency

**Weaknesses:**
- No predictive/forecasting capability
- Manual data collection may introduce delays
- Data quality issues in some counties
- Limited integration with other data sources (weather, economic)

### 2.4.2 Kenya Food Security Outlook (FEWS NET Kenya)

The Famine Early Warning Systems Network (FEWS NET) Kenya provides food security analysis including price monitoring and outlooks for staple commodities. FEWS NET is funded by the United States Agency for International Development (USAID) and implemented in partnership with several technical organizations.

FEWS NET's price analysis includes monitoring of maize and other staple food prices across key reference markets in Kenya. The system produces monthly price bulletins and seasonal price outlooks that assess the likely evolution of food prices over the coming 3-6 months. These outlooks incorporate analysis of production conditions, market dynamics, and macroeconomic factors.

While FEWS NET provides valuable price outlooks, the analysis is primarily qualitative and expert-driven rather than based on automated machine learning models. The geographic coverage is limited to major reference markets rather than all counties. Additionally, the monthly publication frequency may not be sufficient for stakeholders who need weekly price forecasts.

**Strengths:**
- Established food security analysis framework
- Integration of multiple data types (production, markets, economics)
- Seasoned analysts with local knowledge
- Regular publication schedule

**Weaknesses:**
- Qualitative/expert-driven rather than automated ML
- Limited to major reference markets
- Monthly publication frequency
- Not a publicly accessible interactive system

### 2.4.3 AgriBORA Market Platform

AgriBORA is a Kenyan agritech platform that connects farmers, traders, and buyers through a digital marketplace. The platform provides transaction-based price data that reflects actual market transactions rather than reported prices.

AgriBORA's price data provides a valuable complement to KAMIS data, offering a different perspective on market prices based on actual transactions. The platform's digital nature enables more frequent and potentially more accurate price collection compared to traditional survey-based methods.

For the current project, AgriBORA's wholesale price data serves as a secondary price source and validation data. The transaction-based nature of AgriBORA prices provides insights into realized market prices rather than quoted prices.

**Strengths:**
- Transaction-based (realized) prices
- Digital data collection
- Coverage across multiple commodities
- Growing user base and data volume

**Weaknesses:**
- Limited historical data compared to KAMIS
- Geographic coverage may be uneven
- Transaction data may not represent all market segments
- Platform-focused rather than analysis-focused

### 2.4.4 DigiFarm and M-Farm

Beyond government and early warning systems, several Kenyan agritech platforms provide market information services that relate to the current project.

**DigiFarm:** Launched in 2017 by Safaricom, DigiFarm is a mobile-based platform that provides Kenyan smallholder farmers with access to quality agricultural inputs, advisory services, market linkages, and financial services. While DigiFarm does not offer price forecasting per se, it aggregates market price information that helps farmers make marketing decisions. The platform has registered over 1.5 million farmers and processes significant volumes of agricultural transactions. DigiFarm's model demonstrates the growing appetite for digital agricultural services among Kenyan smallholders and validates the importance of accessible, mobile-friendly information platforms.

**M-Farm:** M-Farm is a Kenyan agritech startup that provides farmers with real-time market prices for agricultural commodities via SMS and mobile web. Farmers can check current prices across different markets, find buyers, and access agricultural tips. While M-Farm provides current price information, it does not offer predictive analytics or price forecasting. The platform's focus on price transparency (rather than prediction) addresses one part of the information problem but does not help stakeholders anticipate future market conditions.

Both DigiFarm and M-Farm demonstrate the existing demand for agricultural market information among Kenyan farmers and the potential impact of digital information services. However, neither platform has incorporated machine learning-based price forecasting into its service offering, representing a gap that the current project can address.

## 2.5 Theoretical Framework

### 2.5.1 Time Series Forecasting Fundamentals

Time series forecasting involves predicting future values of a variable based on its historical observations. A time series is a sequence of data points indexed in time order, typically with equal spacing between observations (e.g., weekly in our case).

Key concepts in time series analysis include:

**Stationarity:** A time series is stationary if its statistical properties (mean, variance, autocorrelation) are constant over time. Most forecasting methods assume or require stationarity. Price series are typically non-stationary (trending), which is why first-differencing (Δ-price) is often applied to achieve stationarity.

**Autocorrelation:** The correlation between a time series and its lagged values. Price series typically exhibit strong autocorrelation at lag 1 (price today is highly correlated with price last week), which is why the persistence forecast is a strong baseline.

**Seasonality:** Regular patterns that repeat at fixed intervals (e.g., annual harvest cycles). Agricultural prices typically exhibit strong seasonality driven by planting and harvest cycles.

**Trend:** Long-term direction of the series (upward, downward, or flat). Maize prices in Kenya have shown an upward trend driven by inflation and increasing production costs.

The choice of Δ-price as the target variable in this project is grounded in time series theory. By first-differencing, we remove the non-stationary trend component and focus on predicting the short-term price change, which is more stationary and decomposable.

### 2.5.2 Traditional Statistical Methods

**Exponential Smoothing:** This family of methods assigns exponentially decreasing weights to older observations. The simplest form, Simple Exponential Smoothing, is defined as:

```math
\hat{y}_{t+1|t} = \alpha y_t + (1 - \alpha) \hat{y}_{t|t-1}
```

where α is the smoothing parameter (0 < α < 1). For data with trend, Holt's linear trend method adds a trend component. For data with both trend and seasonality, Holt-Winters seasonal method adds a seasonal component. The full Holt-Winters additive formulation is:

```math
\hat{y}_{t+h|t} = l_t + h b_t + s_{t+h-m}
```

where l_t is the level, b_t is the trend, and s_t is the seasonal component updated via:

```math
l_t = \alpha(y_t - s_{t-m}) + (1 - \alpha)(l_{t-1} + b_{t-1})
```
```math
b_t = \beta^*(l_t - l_{t-1}) + (1 - \beta^*)b_{t-1}
```
```math
s_t = \gamma(y_t - l_{t-1} - b_{t-1}) + (1 - \gamma)s_{t-m}
```

Exponential smoothing methods are widely used for their simplicity and robustness, but they share fundamental limitations with ARIMA: they are univariate, linear, and cannot incorporate exogenous variables.

**Vector Autoregression (VAR):** VAR models capture linear interdependencies among multiple time series. A VAR(p) model for a k-dimensional vector y_t:

```math
y_t = c + A_1 y_{t-1} + A_2 y_{t-2} + ... + A_p y_{t-p} + \varepsilon_t
```

VAR models are useful for capturing cross-market dynamics (e.g., how Nairobi prices influence Mombasa prices). However, the number of parameters grows as O(k²p), making them impractical for large systems. Additionally, VAR models are linear and cannot capture regime changes or non-linear relationships.

**Limitations of Traditional Approaches for This Project:**

1. **Univariate focus:** ARIMA and ETS cannot incorporate weather, economic, and temporal features simultaneously.
2. **Linearity:** Price responses to weather shocks and market events are often non-linear (e.g., drought effects amplify beyond a threshold).
3. **High-dimensional data:** With 80+ features, traditional methods either cannot handle the dimensionality or require extensive feature selection.
4. **Missing data handling:** Traditional methods require complete series or imputation, while XGBoost learns default directions for missing values.
5. **Cross-county information sharing:** Traditional methods model each county independently, missing opportunities to learn from data-rich counties.

### 2.5.3 Ensemble Learning Methods

Ensemble learning combines multiple models to produce a single, more accurate prediction. The fundamental principle is that a group of weak learners can collectively form a strong learner. Ensemble methods are among the most successful machine learning approaches for structured data.

The two main types of ensemble methods are:

**Bagging (Bootstrap Aggregating):** Multiple models are trained on different bootstrap samples of the training data, and their predictions are averaged. Random Forest is the most well-known bagging method. Bagging reduces variance without increasing bias.

**Boosting:** Models are trained sequentially, with each new model focusing on correcting the errors of the previous models. The final prediction is a weighted combination of all models. Boosting reduces both bias and variance.

Gradient boosting, the foundation of XGBoost, extends the boosting concept by optimizing a differentiable loss function using gradient descent in function space. At each iteration, a new tree is trained to predict the negative gradient (residuals) of the loss function with respect to the current ensemble prediction.

### 2.5.4 Gradient Boosting and XGBoost

**Intuition: How Gradient Boosting Works**

Gradient boosting builds an ensemble of decision trees sequentially, where each new tree corrects the errors made by the previous ensemble. The intuition is similar to how a student improves by focusing on subjects where mistakes were made:

1. **Start with a simple initial prediction** (e.g., the mean of the target variable).
2. **Compute residuals** (errors) of the current ensemble.
3. **Train a new decision tree** to predict these residuals.
4. **Add the new tree** to the ensemble with a learning rate (shrinkage) to prevent overfitting.
5. **Repeat** steps 2-4 for a specified number of iterations.

Mathematically, if we denote the ensemble after t-1 iterations as F_{t-1}(x), the t-th tree f_t(x) is trained to predict the negative gradient of the loss function:

```math
f_t(x) \approx -\frac{\partial L(y, F_{t-1}(x))}{\partial F_{t-1}(x)}
```

For squared error loss, this simplifies to predicting the residual y - F_{t-1}(x). The ensemble is updated as:

```math
F_t(x) = F_{t-1}(x) + \eta \cdot f_t(x)
```

where η is the learning rate (shrinkage parameter).

**XGBoost: Mathematical Deep-Dive**

XGBoost (Extreme Gradient Boosting) extends gradient boosting with several key innovations. The XGBoost objective function at iteration t is:

```math
\text{Obj}^{(t)} = \sum_{i=1}^{n} L(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) + \Omega(f_t)
```

where L is the differentiable loss function and Ω is the regularization term. Using a second-order Taylor expansion:

```math
\text{Obj}^{(t)} \approx \sum_{i=1}^{n} [L(y_i, \hat{y}^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i)] + \Omega(f_t)
```

where g_i = ∂L/∂ŷ (first derivative gradient) and h_i = ∂²L/∂ŷ² (second derivative Hessian).

The regularization term for a tree f_t with T leaves and leaf weights w_j is:

```math
\Omega(f_t) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^{T} w_j^2 + \alpha \sum_{j=1}^{T} |w_j|
```

where:
- γ (gamma) is the complexity parameter (minimum loss reduction for a split)
- λ (reg_lambda) is the L2 regularization on leaf weights
- α (reg_alpha) is the L1 regularization on leaf weights

The optimal leaf weight for a given tree structure is:

```math
w_j^* = -\frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}
```

And the corresponding optimal objective value (loss reduction) for a given split is:

```math
\text{Gain} = \frac{1}{2} \left[ \frac{(\sum_{i \in I_L} g_i)^2}{\sum_{i \in I_L} h_i + \lambda} + \frac{(\sum_{i \in I_R} g_i)^2}{\sum_{i \in I_R} h_i + \lambda} - \frac{(\sum_{i \in I} g_i)^2}{\sum_{i \in I} h_i + \lambda} \right] - \gamma
```

This gain formula allows XGBoost to efficiently evaluate potential split points and select the ones that maximize loss reduction while applying regularization to prevent overfitting.

Key features of XGBoost that make it effective for this project:

**Regularized Objective:** XGBoost incorporates L1 and L2 regularization directly into the objective function, reducing overfitting and improving generalization—critical when working with 80+ features and limited data.

**Handling Missing Values:** XGBoost learns optimal default directions for missing values during training, eliminating the need for imputation. This is valuable because price data may have missing weeks for certain counties.

**Column Subsampling:** Similar to Random Forest, XGBoost can randomly sample features for each tree split, reducing correlation between trees and improving generalization.

**Weighted Quantile Sketch:** XGBoost uses an approximate algorithm for finding optimal split points in continuous features, enabling efficient scaling to large datasets.

For the current project, XGBoost's ability to handle mixed data types (continuous features like price lags, categorical features like county dummies), its built-in regularization, and its resistance to overfitting make it an ideal choice for the maize price forecasting task.

The hyperparameter configuration used in this project is:

- n_estimators: 500 (maximum number of trees)
- max_depth: 3 (tree depth, limited to prevent overfitting)
- learning_rate: 0.05 (step size shrinkage)
- reg_lambda: 5 (L2 regularization strength)
- subsample: 0.7 (fraction of samples used per tree)
- colsample_bytree: 0.8 (fraction of features used per tree)
- early_stopping_rounds: 15 (stopping criterion to prevent overfitting)

### 2.5.5 Cross-Validation for Time Series

Cross-validation is essential for evaluating model performance and preventing overfitting. However, standard k-fold cross-validation, which randomly splits data into k folds, is inappropriate for time series because it violates the temporal ordering of observations. When training data contains future observations relative to test data, the model evaluates on unrealistic scenarios.

**Why Expanding Window > k-Fold for Time Series:**

1. **Temporal order preservation:** Expanding window CV respects the chronological order of data, never training on future data.
2. **Realistic simulation:** Each fold simulates the actual forecasting scenario—predicting the next N weeks based on all available past data.
3. **Performance stability assessment:** By evaluating across multiple time periods, expanding window CV reveals how model performance varies under different market conditions.
4. **Training size sensitivity:** The expanding window reveals how performance improves with more training data, informing decisions about when to retrain.

In contrast, k-fold CV for time series would train on data that may contain future observations relative to the test fold, leading to overly optimistic and unrealistic performance estimates. The expanding window approach used in this project consists of:

1. **Initial window:** Train on the first 55% of weeks (approximately 124 weeks)
2. **Test window:** Evaluate on the next 20 weeks
3. **Expand:** Add the test window to the training set (new total: 144 weeks)
4. **Repeat:** Test on the next 20 weeks, and so on for 5 folds

This design ensures robust, realistic performance estimates that stakeholders can trust.

## 2.6 Research Gaps

The literature review reveals several gaps that the proposed project aims to address:

**1. Limited County-Level Forecasting in Kenya:** Existing systems either operate at the national level (GIEWS, FEWS NET) or are limited to major reference markets. There is no operational system that provides county-level maize price forecasts for all Kenyan counties.

**2. Lack of Automated Machine Learning Approaches:** Most price analysis in Kenya relies on expert judgment and basic statistical methods. The application of modern machine learning techniques like gradient boosting to agricultural price forecasting in Kenya is largely unexplored in operational systems.

**3. Absence of Pooled Modeling Across Regions:** While individual county-level models are common, the pooled modeling approach that trains a single model on data from multiple regions has not been applied to Kenyan agricultural prices. This approach is particularly valuable for counties with limited historical data, as they can benefit from patterns learned from other counties.

**4. Limited Use of Δ-Price Target Variable:** Most agricultural price forecasting studies model absolute prices. The use of Δ-price as the target variable, combined with MASE as the evaluation metric, provides a more rigorous evaluation framework that directly compares model performance against the persistence baseline.

**5. Lack of Interactive Forecasting Dashboards:** While research papers present model results, there are few operational, interactive dashboards that allow stakeholders to access forecasts, analyze patterns, and make decisions based on machine learning predictions.

**6. Insufficient Uncertainty Quantification:** Existing approaches typically provide point forecasts without confidence intervals. The proposed system generates confidence bands around forecasts, enabling risk-based decision-making.

**7. Limited Use of Expanding Window Validation:** Many studies use a single train-test split or k-fold cross-validation that ignores temporal order. The expanding window approach used in this project provides more robust and realistic performance estimates that reflect the model's ability to forecast future data.

**8. Agritech Platform Integration Gap:** Platforms like DigiFarm and M-Farm provide current price information but lack predictive capabilities. The proposed system can complement these platforms by adding a forecasting dimension.

The proposed project directly addresses these gaps by developing an operational, machine learning-based maize price forecasting system that uses pooled XGBoost with Δ-price target, expanding window validation, and an interactive dashboard, specifically designed for Kenyan county-level price forecasting.

---

# CHAPTER 3: METHODOLOGY

## 3.1 Introduction

This chapter describes the research and project methodology employed in developing the maize price forecasting system. The chapter covers the research design, data collection methods, data exploration, data preparation and feature engineering processes, software tools and technologies, experimental setup, and the project development methodology. The chapter also presents the system architecture and describes the development tools and technologies used.

## 3.2 Research Design

This study employs a quantitative research design based on experimental methodology. The experimental approach is appropriate for this project because:

1. **Controlled Variables:** The research involves a clearly defined set of input variables (price features, weather data, economic indicators) and a measurable output variable (maize price change), allowing for controlled experimentation.

2. **Hypothesis Testing:** The research tests specific hypotheses about model performance, including whether the pooled XGBoost model outperforms the persistence baseline and whether per-county fine-tuning improves upon the pooled model.

3. **Replicability:** The experimental design is fully specified, enabling other researchers to replicate the experiments and verify the results using the same data and methodology.

4. **Comparative Evaluation:** The experimental framework allows for systematic comparison of different modeling approaches (persistence, pooled XGBoost, fine-tuned XGBoost) using standardized evaluation metrics.

The research follows the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology, which is widely used in data science and machine learning projects. CRISP-DM comprises six phases:

1. **Business Understanding:** Understanding the project objectives and requirements from a business perspective, then converting this knowledge into a data mining problem definition.

2. **Data Understanding:** Collecting initial data, describing and exploring it, and verifying data quality.

3. **Data Preparation:** Constructing the dataset from raw data through cleaning, transformation, and feature engineering.

4. **Modeling:** Selecting and applying appropriate modeling techniques, and calibrating model parameters.

5. **Evaluation:** Evaluating the model's performance against the business objectives and determining whether the model meets the project requirements.

6. **Deployment:** Organizing and presenting the knowledge gained from the model in a usable form, including the development of the interactive dashboard.

## 3.3 Data Collection

### 3.3.1 KAMIS Price Data

The Kenya Agricultural Market Information System (KAMIS) provides weekly retail and wholesale prices for maize across markets in all 47 Kenyan counties. The data was obtained from the KAMIS database and includes the following attributes:

- **County:** The administrative county where the market is located (46 counties have data)
- **Market:** Specific market location within the county
- **Commodity:** Maize (dry grains)
- **Price Type:** Retail price (primary) and wholesale price
- **Price:** Weekly average price in Kenyan Shillings (KES) per kilogram
- **Standard Deviation:** Price variation within the week
- **Date:** Week start date

The KAMIS dataset covers the period from January 2021 to October 2025, providing approximately 250 weeks of price data. The data contains 620,000+ records across all commodities; the maize-specific subset contains approximately 15,000 records across 46 counties.

### 3.3.2 AgriBORA Price Data

The Agricultural Business Rapid Assessment (AgriBORA) platform provides transaction-based wholesale maize prices. The data was obtained from the AgriBORA platform and includes:

- **County:** County where the transaction occurred
- **Commodity:** Maize (wholesale)
- **Price:** Transaction price in KES per kilogram
- **Date:** Transaction date

The AgriBORA dataset covers 2021 to 2025 and provides approximately 13,000 records. AgriBORA prices are used as a secondary price source to supplement KAMIS data.

### 3.3.3 Weather Data

Weather data was obtained from the Open-Meteo historical weather API, which provides free access to historical weather data for any location globally. Weather data was collected for each county using the county's geographic coordinates.

The weather attributes collected include:

- **Temperature:** Mean, maximum, and minimum daily temperature (Celsius)
- **Rainfall:** Total daily precipitation (millimeters)
- **Wind Speed:** Maximum daily wind speed (km/h)
- **Period:** January 2021 to October 2025 (matching price data period)

The weather data was aggregated from daily to weekly frequency using appropriate statistical measures (mean for temperature, sum for rainfall).

### 3.3.4 Economic Indicators Data

Economic indicators were collected from publicly available sources to capture macroeconomic influences on maize prices:

- **CPI (Consumer Price Index):** Obtained from the Kenya National Bureau of Statistics (KNBS), monthly frequency
- **USD/KES Exchange Rate:** Obtained from the Central Bank of Kenya, weekly frequency
- **Inflation Rate:** Derived from CPI data, monthly frequency

Table 1 summarizes the data sources used in this project.

**Table 1: Data Sources Summary**

| Data Source | Type | Frequency | Period | Records | Attributes |
|-------------|------|-----------|--------|---------|------------|
| KAMIS | Retail prices | Weekly | 2021-2025 | ~15,000 | County, price, std, date |
| AgriBORA | Wholesale prices | Transaction | 2021-2025 | ~13,000 | County, price, date |
| Open-Meteo | Weather | Daily | 2021-2025 | ~800,000 | Temperature, rainfall, wind |
| KNBS | CPI | Monthly | 2021-2025 | ~57 | CPI value |
| Central Bank | Exchange rate | Weekly | 2021-2025 | ~250 | USD/KES rate |

## 3.4 Data Exploration

### 3.4.1 Summary Statistics

Before model development, a thorough data exploration was conducted to understand the characteristics of the price data across target counties.

**Table 2: Summary Statistics of Weekly Maize Prices by County (KES/kg)**

| County | Mean | Median | Std Dev | Min | Max | Count | Period |
|--------|:----:|:------:|:-------:|:---:|:---:|:-----:|:------:|
| Kiambu | 42.3 | 41.8 | 6.2 | 29.5 | 54.1 | 248 | 2021-2025 |
| Kirinyaga | 39.1 | 38.5 | 4.8 | 28.0 | 48.2 | 248 | 2021-2025 |
| Mombasa | 45.7 | 45.2 | 5.5 | 34.1 | 56.3 | 248 | 2021-2025 |
| Nairobi | 44.8 | 44.1 | 6.8 | 30.2 | 57.9 | 248 | 2021-2025 |
| Uasin-Gishu | 35.2 | 34.8 | 4.1 | 26.4 | 44.5 | 248 | 2021-2025 |

Key observations from the summary statistics:

- **Price levels vary significantly by county:** Mombasa and Nairobi have the highest average prices (45.7 and 44.8 KES/kg respectively), reflecting urban demand, higher transportation costs, and dependency on imported maize. Uasin-Gishu, located in the Rift Valley grain basket, has the lowest average price (35.2 KES/kg).
- **Volatility differs across counties:** Nairobi exhibits the highest standard deviation (6.8 KES), indicating greater price uncertainty in the largest consumer market. Kirinyaga has the lowest standard deviation (4.8 KES), suggesting more stable market conditions in this established maize-growing region.
- **Price ranges are wide:** The difference between minimum and maximum prices ranges from 18.1 KES (Kirinyaga) to 27.7 KES (Nairobi), representing 40-62% of the mean price, confirming significant price volatility over the study period.

### 3.4.2 Missing Data Analysis

Data completeness is an important consideration for model training. The KAMIS data has variable coverage across counties, with some counties having more consistent reporting than others.

**Table 3: Missing Data Patterns Across Target Counties**

| County | Total Weeks | Missing Weeks | Completeness | Pattern |
|--------|:-----------:|:-------------:|:------------:|:--------|
| Kiambu | 248 | 8 | 96.8% | Scattered |
| Kirinyaga | 248 | 12 | 95.2% | Scattered |
| Mombasa | 248 | 6 | 97.6% | Scattered |
| Nairobi | 248 | 4 | 98.4% | Scattered |
| Uasin-Gishu | 248 | 15 | 94.0% | Scattered |

Missing data was handled through forward-filling (carrying forward the last observed price) for gaps of up to 2 weeks. Longer gaps were left as missing and the corresponding rows were excluded from training for that county. The overall completeness rate across all target counties exceeds 94%, indicating that the dataset is sufficiently complete for reliable model training.

### 3.4.3 Price Distribution and Outlier Assessment

Visual inspection of price distributions revealed approximately normal distributions for most counties, with slight positive skewness (right tail). The Interquartile Range (IQR) method was used to identify potential outliers:

```math
\text{IQR} = Q_3 - Q_1
\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}
\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}
```

Observations outside the fences were flagged as potential outliers and manually reviewed. In most cases, flagged prices were genuine observations reflecting market conditions (e.g., post-harvest price drops or drought-induced price spikes) and were retained. Only clearly erroneous entries (e.g., negative prices, prices less than 5 KES/kg) were removed.

## 3.5 Data Preparation and Feature Engineering

### 3.5.1 Data Cleaning

Data cleaning was performed using a modular Python script (`src/data/clean.py`) that processes each data source:

**KAMIS Data Cleaning:**
- Filtering for maize (dry grain) records only
- Removing records with missing or zero prices
- Aggregating market-level prices to county-level weekly averages
- Handling outliers using the Interquartile Range (IQR) method—observations beyond 1.5 × IQR from the quartiles were reviewed
- Forward-filling missing weeks within each county for gaps of up to 2 weeks

**AgriBORA Data Cleaning:**
- Filtering for maize records
- Removing records with missing or zero prices
- Aggregating transaction-level prices to county-level weekly averages
- Aligning with KAMIS date format

**Weather Data Cleaning:**
- Aggregating daily data to weekly averages (temperature) and sums (rainfall)
- Spatial averaging across weather stations within each county
- Handling missing values through linear interpolation

**Economic Data Cleaning:**
- Forward-filling monthly CPI values to align with weekly price data
- Computing inflation rate as year-over-year CPI change
- Aligning exchange rate data with the weekly date format

**Data Merging:** All cleaned data sources were merged into a single panel dataset keyed by (county, week_start), ensuring temporal alignment across all features.

**Outlier Detection (IQR Method) — Detailed Explanation:**

The IQR method is a robust statistical technique for identifying potential outliers that does not assume a normal distribution. The procedure is:

1. Compute Q1 (25th percentile) and Q3 (75th percentile) of the price distribution.
2. Calculate IQR = Q3 - Q1.
3. Define lower fence = Q1 - 1.5 × IQR and upper fence = Q3 + 1.5 × IQR.
4. Flag observations below the lower fence or above the upper fence.

The multiplier of 1.5 is a standard choice that balances sensitivity (catching true outliers) with specificity (not flagging normal extreme values). For skewed distributions, an alternative multiplier (e.g., 3.0) may be used, but the standard 1.5 was appropriate given the approximately normal price distributions observed.

### 3.5.2 Feature Construction and Rationale

Feature engineering was performed using `src/data/features.py` to create a comprehensive feature set for model training. The engineered features can be categorized as follows:

**Price-Based Features:**

Price lags at 1, 2, 4, 8, and 12 weeks were created. The rationale for these specific lag periods:
- **1-week lag:** Captures the immediate autocorrelation—last week's price is the single best predictor of this week's price.
- **2-week lag:** Captures bi-weekly patterns and short-term momentum.
- **4-week lag:** Captures monthly price patterns and short-term cyclical behavior.
- **8-week lag:** Captures two-month dynamics, useful for identifying medium-term trends.
- **12-week lag:** Captures quarterly patterns that may reflect seasonal production cycles.

Rolling moving averages and standard deviations at 4, 8, and 12 weeks provide smoothed trend indicators and volatility measures:
- **Moving averages (ma_4w, ma_8w, ma_12w):** Smooth out week-to-week noise, revealing underlying price trends.
- **Standard deviations (std_4w, std_8w, std_12w):** Measure price volatility, which is an important indicator of market stability and risk.

**Δ-Price Features:**

Δ-price (current price minus previous week price) was computed, along with its 1-week and 2-week lags, and 4-week rolling mean and standard deviation. These features capture the momentum and volatility of price changes, which are more relevant for Δ-price prediction than absolute price levels.

**Weather Features:**

Weekly mean, maximum, and minimum temperature capture current growing conditions. Weekly total rainfall is critical for crop production and harvest timing. Rolling rainfall sums (4-week and 8-week) capture cumulative precipitation effects, which are more relevant for crop development than a single week's rainfall.

**Economic Features:**

CPI captures overall price level changes in the economy, affecting input costs and consumer purchasing power. USD/KES exchange rate affects the cost of imported maize and agricultural inputs (e.g., fertilizer). Inflation rate captures the erosion of purchasing power and general economic conditions.

**Temporal Features:**

Month, week of year, and year capture seasonal patterns and trends. Days from start provides a continuous trend variable. Seasonal flags (long rains: March-May, short rains: October-December, harvest periods) capture the known seasonal pattern of Kenyan agriculture.

**Geographic Features:**

County one-hot encoding (46 dummy variables) allows the pooled model to learn county-specific price levels and dynamics. This encoding creates binary variables for each county, enabling the model to have county-specific intercepts and interaction effects.

**Table 4: Engineered Feature Set**

| Category | Features | Count |
|----------|----------|-------|
| Price lags | lag_1w, lag_2w, lag_4w, lag_8w, lag_12w | 5 |
| Rolling stats | ma_4w, std_4w, ma_8w, std_8w, ma_12w, std_12w | 6 |
| Δ-price features | change_lag_1w, change_lag_2w, change_ma_4w, change_std_4w | 4 |
| Weather | temp_avg, temp_max, temp_min, rain_mm, wind_speed | 5 |
| Weather aggregates | rain_sum_4w, temp_avg_4w, rain_sum_8w, temp_avg_8w | 4 |
| Economic | cpi, usd_kes, inflation_rate | 3 |
| Temporal | month, week_of_year, year, days_from_start | 4 |
| Seasonal | is_long_rains, is_short_rains, is_harvest | 3 |
| County dummies | c_county_name (46 counties) | 46 |
| **Total** | | **80** |

## 3.6 Software Tools and Technologies

The project was implemented using the following software tools and libraries. Table 5 lists the specific versions used, which are critical for reproducibility.

**Table 5: Software and Library Versions**

| Tool/Library | Version | Purpose |
|-------------|:-------:|---------|
| Python | 3.11 | Primary programming language |
| XGBoost | 2.0.3 | Gradient boosting framework |
| scikit-learn | 1.3.2 | Data preprocessing, metrics |
| Pandas | 2.1.4 | Data manipulation and analysis |
| NumPy | 1.26.2 | Numerical computing |
| Matplotlib | 3.8.2 | Static visualizations |
| Plotly | 5.18.0 | Interactive visualizations |
| Streamlit | 1.29.0 | Dashboard web application |
| python-docx | 1.1.0 | Document generation |
| Requests | 2.31.0 | API data fetching |

Python 3.11 was chosen for its performance improvements, better error messages, and support for modern language features. XGBoost 2.0+ was selected for the model implementation due to its state-of-the-art gradient boosting performance, built-in regularization, and handling of mixed data types. scikit-learn provided the evaluation metrics framework, while Pandas and NumPy handled all data processing and numerical operations. Streamlit was chosen for the dashboard due to its Python-native development model, ease of deployment, and built-in support for interactive widgets.

## 3.7 Experimental Setup

### 3.7.1 Target Variable Engineering

A critical design decision in this project is the choice of Δ-price (first difference of price) as the target variable rather than absolute price. This decision is motivated by several considerations:

**Stationarity:** Price series are typically non-stationary (they exhibit trends and changing means), violating assumptions of many statistical methods. Δ-price is typically stationary, making it more amenable to modeling.

**Persistence Baseline:** When predicting absolute prices, the persistence forecast (predicting the current price for all future periods) is a strong baseline that is difficult to beat. By predicting Δ-price, the persistence baseline becomes zero (no change), providing a more meaningful and achievable benchmark.

**MASE Evaluation:** MASE (Mean Absolute Scaled Error) compares model errors to the errors of the persistence baseline. With Δ-price as the target, MASE < 1 directly indicates that the model predicts price changes better than assuming no change.

The Δ-price transformation is computed as:

```math
\Delta P_t = P_t - P_{t-1}
```

where P_t is the price at week t.

### 3.7.2 Pooled XGBoost Model Architecture

The core model is a pooled XGBoost regressor that learns from data across all counties simultaneously. The pooled approach enables the model to:

1. **Share information across counties:** Patterns learned from data-rich counties can benefit data-sparse counties.
2. **Learn common patterns:** Seasonal and economic effects that affect all counties can be efficiently captured.
3. **Provide consistent predictions:** A single model ensures that predictions across counties are internally consistent.

The pooled model input includes all features described in Section 3.5.2, including county one-hot encoding. The county dummies allow the model to learn county-specific intercepts and interactions with other features.

### 3.7.3 Hyperparameter Tuning

Hyperparameter tuning was performed using random search with the expanding window cross-validation framework. The objective was to minimize MASE across all folds while preventing overfitting.

**Table 6: Hyperparameter Search Space and Final Configuration**

| Parameter | Search Space | Final Value | Rationale |
|-----------|:------------:|:-----------:|-----------|
| n_estimators | [200, 300, 500, 800, 1000] | 500 | Sufficient for convergence with early stopping |
| max_depth | [2, 3, 4, 5, 6] | 3 | Shallow trees prevent overfitting; deeper trees showed diminishing returns |
| learning_rate | [0.01, 0.03, 0.05, 0.1, 0.2] | 0.05 | Conservative rate balances speed and accuracy |
| reg_lambda | [1, 3, 5, 10] | 5 | Moderate L2 regularization |
| reg_alpha | [0, 0.1, 1, 5] | 0 | L1 regularization not beneficial for this problem |
| subsample | [0.5, 0.6, 0.7, 0.8, 1.0] | 0.7 | Reduces variance through row subsampling |
| colsample_bytree | [0.6, 0.7, 0.8, 0.9, 1.0] | 0.8 | Feature diversity improves ensemble |
| early_stopping_rounds | [10, 15, 20] | 15 | Sufficient patience for convergence |

The random search explored 100 hyperparameter combinations across 5 folds. The final configuration balances model complexity (shallow trees with moderate regularization) with predictive power. The early stopping mechanism prevents overfitting by monitoring validation error during training.

### 3.7.4 Expanding Window Cross-Validation

Model evaluation was performed using a 5-fold expanding window cross-validation strategy that respects the temporal order of the data. This approach provides robust estimates of model performance across different time periods.

The cross-validation procedure:

1. **Initial Training Window:** The first 55% of weeks (approximately 124 weeks from May 2021 to October 2023)
2. **Fold Size:** 20 weeks per test window
3. **Number of Folds:** 5 (each fold adds 20 more weeks to the training window)

**Table 7: Expanding Window Cross-Validation Folds**

| Fold | Training Weeks | Test Weeks | Training Period | Test Period |
|------|:--------------:|:----------:|-----------------|-------------|
| 0 | 124 | 20 | May 2021 – Oct 2023 | Oct 2023 – Mar 2024 |
| 1 | 144 | 20 | May 2021 – Mar 2024 | Mar 2024 – Aug 2024 |
| 2 | 164 | 20 | May 2021 – Aug 2024 | Aug 2024 – Jan 2025 |
| 3 | 184 | 20 | May 2021 – Jan 2025 | Jan 2025 – May 2025 |
| 4 | 204 | 20 | May 2021 – May 2025 | May 2025 – Oct 2025 |

This design ensures that:
- The model is always evaluated on data it has not seen during training
- Performance is assessed across multiple time periods with different market conditions
- The evaluation simulates the realistic scenario of predicting the future from the past

### 3.7.5 Recursive Multi-Step Forecasting

For multi-week forecasts (beyond 1 week ahead), a recursive forecasting strategy is employed. In this approach, the model's 1-step-ahead prediction is fed back as an input feature for the next step:

1. Train model to predict Δ-price for week t+1 using features available up to week t.
2. For week t+2: use the predicted Δ-price (and any derived features) as if it were the actual value.
3. Continue recursively for up to 12 weeks ahead.

The recursive approach can be visualized as:

```math
\hat{\Delta P}_{t+1} = f(X_t)
\hat{\Delta P}_{t+2} = f(X_{t+1}^*)
\hat{\Delta P}_{t+3} = f(X_{t+2}^*)
```

where X_{t+k}^* includes features computed from previously predicted values. This approach allows the model to forecast any horizon from a single model, but prediction uncertainty compounds with each recursive step, which is why forecast confidence intervals widen with longer horizons.

### 3.7.6 Per-County Fine-Tuning

After training the pooled model, per-county fine-tuning is performed to adapt the model to county-specific price dynamics. The fine-tuning approach:

1. **Warm Start:** Each county's model is initialized from the pooled model's booster
2. **County-Specific Training:** The model is further trained on only that county's training data
3. **Reduced Learning Rate:** learning_rate is reduced to 0.01 for fine-tuning
4. **Fewer Iterations:** 150 additional trees are trained per county
5. **Reduced Regularization:** reg_lambda is reduced to 3 to allow more adaptation

The fine-tuning step allows the model to specialize while retaining the general patterns learned from all counties. This is particularly valuable for counties with price dynamics that differ from the national average.

### 3.7.7 Evaluation Metrics

Four metrics are used to evaluate model performance:

**1. MASE (Mean Absolute Scaled Error)**

```math
\text{MASE} = \frac{\text{MAE}_{\text{model}}}{\text{MAE}_{\text{persistence}}}
```

MASE compares the model's MAE to the MAE of the persistence baseline (predicting zero change). A MASE less than 1 indicates that the model outperforms the naive persistence forecast. MASE is scale-independent and can be compared across series with different units.

**2. Directional Accuracy (Dir Acc)**

```math
\text{Dir Acc} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}(\text{sign}(\hat{\Delta}_i) = \text{sign}(\Delta_i))
```

Directional accuracy measures the percentage of weeks where the model correctly predicts the direction of price change (up or down). This metric is particularly important for trading and marketing decisions, where direction is often more important than magnitude.

**3. MAE (Mean Absolute Error)**

```math
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |P_i - \hat{P}_i|
```

MAE measures the average absolute error between predicted and actual prices in the original price scale (KES). This metric provides an intuitive understanding of the model's accuracy in monetary terms.

**4. sMAPE (Symmetric Mean Absolute Percentage Error)**

```math
\text{sMAPE} = \frac{100\%}{n} \sum_{i=1}^{n} \frac{|P_i - \hat{P}_i|}{(|P_i| + |\hat{P}_i|)/2}
```

sMAPE provides a symmetric percentage error metric that avoids the asymmetry of standard MAPE (where MAPE penalizes over-forecasts more heavily than under-forecasts).

## 3.8 Project Methodology

### 3.8.1 Agile Development Methodology

This project was developed using the Agile development methodology, specifically the Scrum framework. Agile methodology was chosen due to its iterative nature, flexibility, and focus on delivering working software incrementally.

The key Agile principles applied in this project include:

**Iterative Development:** The project was developed in two-week sprints, with each sprint producing a potentially shippable increment of the system.

**Continuous Feedback:** Regular sprint reviews with the supervisor provided feedback that guided subsequent development iterations.

**Prioritized Backlog:** Features were prioritized based on their value to the project objectives, ensuring that the most critical functionality was developed first.

**Adaptive Planning:** The project plan evolved based on emerging insights and changing requirements, rather than following a rigid, predetermined plan.

### 3.8.2 Justification for Agile Methodology

Agile methodology was chosen over traditional waterfall methodology for the following reasons:

1. **Exploratory Nature:** Machine learning projects involve significant exploration and experimentation, making it difficult to specify all requirements upfront.

2. **Incremental Value:** Agile delivery ensures that working features are available early, even if the complete system is not yet finished.

3. **Risk Management:** Regular iterations allow for early identification and mitigation of technical risks.

4. **Stakeholder Involvement:** Agile's emphasis on stakeholder feedback ensures that the final system meets user needs.

### 3.8.3 Development Phases

The project was organized into the following phases:

**Phase 1: Data Acquisition and Understanding (Sprint 1-2)**
- Collection of KAMIS and AgriBORA price data
- Collection of weather data from Open-Meteo API
- Collection of economic indicators from KNBS and Central Bank
- Exploratory data analysis and data quality assessment

**Phase 2: Data Preparation and Feature Engineering (Sprint 3-4)**
- Data cleaning and preprocessing
- Feature engineering and transformation
- Creation of panel dataset

**Phase 3: Model Development and Training (Sprint 5-6)**
- Implementation of pooled XGBoost model
- Implementation of expanding window cross-validation
- Model training and hyperparameter tuning

**Phase 4: Evaluation and Fine-Tuning (Sprint 7-8)**
- Model evaluation using MASE, Dir Acc, MAE, sMAPE
- Per-county fine-tuning experiments
- Comparative analysis of model variants

**Phase 5: Dashboard Development (Sprint 9-10)**
- Design and development of Streamlit dashboard
- Implementation of 4 analysis tabs
- Forecast visualization with confidence intervals

**Phase 6: Documentation and Deployment (Sprint 11-12)**
- System documentation
- Deployment configuration for Streamlit Cloud
- Final testing and validation

## 3.9 System Architecture

### 3.9.1 Architecture Overview

The maize price forecasting system follows a modular, pipeline-based architecture with three main components: the data pipeline, the model training pipeline, and the dashboard application.

![Figure 2: System Architecture Diagram](screenshots/figure_2.png)

*Caption: The system architecture shows the three main components: data pipeline (raw data → cleaned data → features), model training pipeline (features → cross-validation → trained model), and dashboard application (model + features → Streamlit web app). Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

### 3.9.2 Data Pipeline

The data pipeline (`src/data/clean.py` and `src/data/features.py`) processes raw data into a feature-rich panel dataset:

1. **Raw Data Ingestion:** Load raw CSV files (KAMIS, AgriBORA, weather, economic)
2. **Data Cleaning:** Filter, aggregate, and clean each data source
3. **Data Merging:** Combine all data sources into a panel dataset keyed by (county, week_start)
4. **Feature Engineering:** Compute price lags, rolling statistics, seasonal flags, and temporal features
5. **Output:** Panel features CSV file (`data/features/panel_features.csv`)

![Figure 3: Data Pipeline Flowchart](screenshots/figure_3.png)

*Caption: The data pipeline processes data from multiple sources through cleaning, merging, and feature engineering stages to produce the final panel feature dataset. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

### 3.9.3 Model Training Pipeline

The model training pipeline (`src/models/train.py`) trains and evaluates the forecasting model:

1. **Data Loading:** Load panel features dataset
2. **Target Engineering:** Compute Δ-price and Δ-price features
3. **Expanding Window CV:** For each of 5 folds:
   a. Split data into training and test periods
   b. Prepare features (including county dummies)
   c. Train pooled XGBoost model
   d. Evaluate on test set
   e. Fine-tune per county
   f. Evaluate fine-tuned model
4. **Save Artifacts:** Save trained model, feature config, and evaluation results

### 3.9.4 Dashboard Application

The dashboard application (`src/dashboard/app.py`) provides an interactive user interface:

1. **Data Loading:** Load panel data, trained model, config, and evaluation results
2. **Forecast Generation:** Recursive multi-step forecasting using the trained model
3. **Confidence Intervals:** Bootstrap-based uncertainty estimation
4. **Visualization:** Four-tab interface (Overview, Seasonality, Drivers, Performance)
5. **User Interaction:** County selection, forecast horizon adjustment

---

# CHAPTER 4: RESULTS AND DISCUSSION

## 4.1 Introduction

This chapter presents the results of the maize price forecasting system, including model performance evaluation, feature importance analysis, seasonal pattern analysis, per-county price trends, dashboard user guide, comparison with literature benchmarks, and practical interpretation of results. The results are discussed in the context of the research objectives and compared with findings from the literature.

## 4.2 Model Performance Results

### 4.2.1 Overall Results Across All Folds

Table 8 presents the aggregate performance of the three models evaluated across all 5 folds of the expanding window cross-validation.

**Table 8: Overall Model Performance Comparison**

| Model | MASE | Dir Acc | MAE (KES) | sMAPE |
|-------|:---:|:-------:|:---------:|:-----:|
| Persistence | 0.631 | 0.0% | 2.89 | 7.15% |
| Pooled XGBoost | 0.322 | 75.5% | 2.07 | 5.10% |
| Fine-Tuned XGBoost | 0.322 | 75.5% | 2.07 | 5.10% |

Note: The persistence baseline has a non-zero MASE of 0.631 because MASE is computed on the Δ-price (change) scale using the in-sample training data as the scaling factor. The persistence model predicts zero change, and its MAE on the Δ-price scale is compared against the MAE of the in-sample naive seasonal forecast. The directional accuracy of persistence is 0% because it always predicts no change (direction = 0), and the comparison is against actual positive or negative changes.

Key observations from the results:

1. **All models beat persistence:** Both XGBoost models achieve MASE values well below 1 (0.322), indicating that they reduce forecast error by approximately 68% compared to the naive "no change" forecast. This is a practically significant improvement that translates to real cost savings for market participants.

2. **Directional accuracy is strong:** The XGBoost models correctly predict the direction of price change 75.5% of the time, compared to 0% for persistence (since persistence always predicts no change). This is a practically significant result, as directional accuracy is critical for trading and marketing decisions.

3. **Fine-tuning matches pooled performance:** The fine-tuned XGBoost achieves identical aggregate performance to the pooled model. This suggests that the county dummies in the pooled model already capture county-specific patterns effectively, leaving little room for improvement through per-county specialization.

4. **MAE is modest:** The average error of 2.07 KES on prices ranging from 28-52 KES represents approximately 4-7% error, which is reasonable for agricultural price forecasting.

### 4.2.2 Per-County Performance

Table 9 shows the best model performance for each target county based on MASE.

**Table 9: Per-County Best Model Performance**

| County | Model | MASE | Dir Acc | MAE (KES) |
|--------|-------|:---:|:-------:|:---------:|
| Kiambu | Fine-Tuned XGBoost | 0.334 | 78.1% | 2.15 |
| Kirinyaga | Fine-Tuned XGBoost | 0.236 | 77.6% | 1.51 |
| Mombasa | Fine-Tuned XGBoost | 0.298 | 62.5% | 1.89 |
| Nairobi | Fine-Tuned XGBoost | 0.379 | 74.2% | 2.43 |
| Uasin-Gishu | Fine-Tuned XGBoost | 0.338 | 74.8% | 2.17 |

Key observations by county:

**Kiambu:** With a MASE of 0.334 and MAE of 2.15 KES, Kiambu shows solid performance. The high directional accuracy (78.1%) makes the model particularly useful for marketing decisions in this peri-urban county where market access is good and price signals are relatively clear.

**Kirinyaga:** Kirinyaga shows the best overall performance with a MASE of 0.236 (76% better than persistence) and the lowest MAE of 1.51 KES. This outstanding performance likely reflects the county's established role as a major maize-producing region with consistent seasonal patterns and reliable market infrastructure. The model's MAE of only 1.51 KES on prices averaging 39.1 KES represents approximately 3.9% error.

**Mombasa:** Mombasa's performance is notable for its lower directional accuracy (62.5%), the lowest among the target counties, although still well above random (50%). This likely reflects Mombasa's unique position as a coastal city that depends heavily on imported maize. Prices in Mombasa are influenced by global grain prices, shipping costs, and port logistics—factors that are not captured in the current feature set. The model's MASE of 0.298 (better than persistence) still demonstrates value, but the lower directional accuracy suggests that additional import-related features could improve performance for this market.

**Nairobi:** Nairobi has the highest MAE (2.43 KES) and the highest MASE (0.379) among the target counties. This reflects the greater complexity of the capital's maize market, which is influenced by more diverse supply sources, larger trading volumes, and greater exposure to macroeconomic factors. The directional accuracy of 74.2% shows that even in this complex market, the model provides meaningful directional guidance.

**Uasin-Gishu:** The Rift Valley grain basket county shows a MASE of 0.338 and MAE of 2.17 KES. While the error is higher than Kirinyaga (also a producing region), the model still demonstrates strong improvement over persistence. The slightly higher error may reflect the greater influence of national rather than local market dynamics on prices in this major production zone.

### 4.2.3 Performance Across Folds (Temporal Stability)

Table 10 shows the pooled XGBoost performance across the 5 expanding window folds.

**Table 10: Performance Across Folds for Pooled XGBoost**

| Fold | Training Weeks | Test Period | MASE | Dir Acc | MAE (KES) |
|------|:-------------:|-------------|:---:|:-------:|:---------:|
| 0 | 124 | Oct 2023 – Mar 2024 | 0.435 | 67.3% | 2.79 |
| 1 | 144 | Mar 2024 – Aug 2024 | 0.401 | 80.8% | 2.47 |
| 2 | 164 | Aug 2024 – Jan 2025 | 0.322 | 80.3% | 2.00 |
| 3 | 184 | Jan 2025 – May 2025 | 0.134 | 62.4% | 0.80 |
| 4 | 204 | May 2025 – Oct 2025 | 0.167 | 80.1% | 1.14 |

Key observations:

1. **Improving performance over time:** MASE shows a general decreasing trend from Fold 0 (0.435) to Fold 4 (0.167), indicating that the model performs better when trained on more data. This confirms the value of accumulating historical price data.

2. **Best performance in later folds:** Folds 3 and 4 show substantially lower MAE and MASE values, likely due to both the larger training dataset and possibly more stable market conditions in the 2025 period.

3. **Directional accuracy remains strong:** Dir Acc stays above 62% across all folds, confirming that the model consistently provides value for directional predictions. The dip in Fold 3 (62.4%) is paired with the lowest MAE (0.80 KES), suggesting a period where prices were more stable (smaller changes) and thus direction was harder to predict but magnitude errors were small.

![Figure 4: Model Performance Comparison Bar Charts](screenshots/figure_4.png)

*Caption: Bar charts comparing MASE, Dir Acc, and MAE for persistence, pooled XGBoost, and fine-tuned XGBoost models. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

## 4.3 Feature Importance Analysis

Feature importance analysis reveals which variables have the greatest influence on the model's predictions. Figure 5 shows the top 15 features based on the XGBoost model's built-in importance scores (based on the frequency of feature usage across all trees, known as "weight" importance).

![Figure 5: Feature Importance (Top 15)](screenshots/figure_5.png)

*Caption: The top 15 features ranked by XGBoost importance scores. Price-change features dominate the top ranks, followed by county dummies and economic indicators. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

The top features are:

1. **price_change_ma_4w** (4-week moving average of price changes) — This feature captures the momentum of price movements, helping the model identify whether prices are in an uptrend, downtrend, or stable period. Its top ranking confirms that price momentum is the single most important predictor of future price changes.

2. **price_change_lag_1w** (last week's price change) — The most recent week's price change is highly predictive of the next week's change, reflecting short-term price momentum. If prices went up last week, they are likely to continue rising.

3. **County dummies** (e.g., c_Kiambu, c_Nyeri, c_Kilifi) — County indicators appear prominently, confirming that county-specific price levels and dynamics are important determinants of price changes. Different counties have different baseline price behaviors.

4. **Economic indicators** (CPI, USD/KES rate, inflation) — These macroeconomic variables capture the broader economic context affecting input costs and purchasing power. CPI's importance reflects how general inflation feeds into maize prices.

5. **Temporal features** (year, days_from_start) — Time-trend features capture long-term price trends driven by inflation and structural changes in the maize market.

6. **Weather features** (temperature, rainfall) — While present, weather features rank lower than economic and price-momentum features, suggesting that weather effects on weekly price changes are less direct than market dynamics. Weather may have a larger impact on longer-term (monthly or seasonal) price movements.

The dominance of price-momentum features provides important practical insight: for short-term (weekly) price forecasting, the most valuable information comes from recent price dynamics rather than external factors. This aligns with the efficient market hypothesis, which suggests that most available information is already reflected in prices.

## 4.4 Seasonal Pattern Analysis

The seasonal analysis reveals distinct monthly patterns in maize prices across the target counties.

![Figure 6: Monthly Seasonal Patterns Across Target Counties](screenshots/figure_6.png)

*Caption: Monthly average maize prices for Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu counties showing seasonal patterns. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

Key observations:

1. **Price peaks:** Most counties show price peaks around June-July, corresponding to the dry season when supply from the previous harvest is diminishing and the new harvest is not yet available. This is the "lean season" when food stocks are at their lowest.

2. **Price troughs:** Prices typically bottom out around January-February and October-November, following the short rains and long rains harvests respectively. These post-harvest periods see increased supply that depresses prices.

3. **Regional variations:** Uasin-Gishu, a major maize-producing region in the Rift Valley, shows consistently lower prices than Nairobi and Mombasa, reflecting lower transportation costs and proximity to production areas. The price spread between Uasin-Gishu and Nairobi ranges from 5-10 KES/kg depending on the season.

4. **Price range:** Monthly average prices range from approximately 34 KES (Uasin-Gishu, low season) to 56 KES (Nairobi, peak season), demonstrating the significant seasonal price variation that farmers and traders can exploit through strategic timing.

5. **Amplitude variation:** Kirinyaga shows the smallest seasonal amplitude, suggesting more stable year-round prices in this established maize-growing region. Nairobi shows the largest amplitude, reflecting greater seasonal supply variation in a market that depends on multiple supply sources.

## 4.5 Per-County Price Trend Analysis

**Kiambu:** Kiambu's maize prices have shown a gradual upward trend over the study period, rising from an average of approximately 38 KES/kg in early 2021 to approximately 46 KES/kg by late 2025. The county exhibits moderate seasonality with prices typically peaking in July-August and reaching lows in January-February. The upward trend reflects both general inflation and increasing demand from Nairobi's expanding population, as Kiambu serves as a key supply corridor for the capital.

**Kirinyaga:** Kirinyaga displays the most stable price pattern among the target counties, with average prices remaining between 36 and 44 KES/kg throughout the study period. The limited price range reflects the county's strong agricultural base and well-established market infrastructure. Seasonal patterns are clear but moderate, with prices rising 3-5 KES/kg during the lean season. The county's consistent production levels help buffer against extreme price volatility.

**Mombasa:** Mombasa's prices exhibit a distinctive pattern shaped by the city's dependence on imported maize. Prices tend to spike sharply during periods of global grain price increases or when the Kenyan shilling depreciates against the US dollar. For example, when the USD/KES rate crossed 150 in 2024, Mombasa prices surged to over 55 KES/kg. The county also shows less pronounced seasonal patterns than inland counties, suggesting that import supply chains are less sensitive to Kenya's domestic growing seasons.

**Nairobi:** As the largest consumer market in East Africa, Nairobi shows the most complex price dynamics. Prices have trended upward from approximately 38 KES/kg in early 2021 to over 50 KES/kg by 2025, reflecting strong demand growth and inflationary pressure. The city's prices are influenced by multiple supply corridors (from the Rift Valley, Central Kenya, and imports via Mombasa), creating more complex interaction effects. Nairobi also shows the highest week-to-week volatility, with swings of 2-3 KES/kg being common.

**Uasin-Gishu:** As part of Kenya's primary grain basket, Uasin-Gishu shows the lowest average prices but distinct seasonal patterns. Prices drop sharply (to approximately 28-30 KES/kg) during the main harvest period (October-November) as local supply floods the market. Farmers who can store their maize and sell 3-4 months later can achieve prices 8-10 KES/kg higher. This seasonal price spread represents a significant opportunity for farmers with access to storage.

## 4.6 Dashboard Interface and User Guide

The Streamlit dashboard provides four analysis tabs that address different stakeholder needs. Each tab is designed to answer specific questions that stakeholders have about maize prices.

![Figure 7: Dashboard Overview Tab Screenshot](screenshots/figure_7.png)

*Caption: The Overview tab shows the current price metrics, historical price chart with forecast and confidence bands, and the multi-week forecast table. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

### 4.6.1 Overview Tab

**Purpose:** Provides a quick snapshot of current market conditions and near-term price forecasts.

**User Guide:**
1. Select a county from the dropdown menu in the sidebar.
2. View current price metrics: current price, 1-week change, 4-week average, and price volatility.
3. The main chart shows historical prices (solid blue line) with the forecast (dashed orange line) and 95% confidence interval (shaded band). The confidence band widens with forecast horizon, reflecting increasing uncertainty.
4. Below the chart, a table displays the numeric week-by-week forecast for the selected horizon (default: 8 weeks).
5. Use the "Forecast Horizon" slider in the sidebar to adjust the forecast length (1-12 weeks).

**Target Users:** Farmers checking next month's price outlook, traders planning procurement timing.

### 4.6.2 Seasonality Tab

**Purpose:** Analyzes historical seasonal patterns and year-over-year price comparisons.

![Figure 8: Dashboard Seasonality Tab Screenshot](screenshots/figure_8.png)

*Caption: The Seasonality tab displays monthly average price patterns, year-over-year comparisons, and descriptive statistics. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

**User Guide:**
1. The main chart shows monthly average prices across all years, clearly revealing the seasonal pattern (peaks and troughs).
2. Below the seasonal chart, a year-over-year comparison chart overlays prices from individual years, enabling stakeholders to compare the current year's pattern with historical years.
3. Descriptive statistics are shown as a sidebar table (mean, median, min, max, and standard deviation by month).
4. An "Add Year" checkbox allows users to toggle individual years on/off for comparison.

**Target Users:** Farmers planning planting and marketing timing, analysts studying seasonal patterns.

### 4.6.3 Drivers Tab

**Purpose:** Identifies and visualizes the key factors influencing maize prices.

![Figure 9: Dashboard Drivers Tab Screenshot](screenshots/figure_9.png)

*Caption: The Drivers tab presents feature importance analysis, current feature values, and scatter plots of key economic drivers versus price. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

**User Guide:**
1. The feature importance bar chart (horizontal) shows the top 15 features ranked by importance score, helping users understand what drives prices.
2. A "Current Feature Values" table displays the latest values of key features (e.g., current CPI, exchange rate, weather).
3. Scatter plots show relationships between key economic drivers (CPI, exchange rate, inflation) and maize prices, with trend lines.
4. Users can select different features from a dropdown to explore their relationship with prices.

**Target Users:** Analysts and policymakers seeking to understand price drivers.

### 4.6.4 Performance Tab

**Purpose:** Displays model performance metrics and enables comparison across counties and models.

![Figure 10: Dashboard Performance Tab Screenshot](screenshots/figure_10.png)

*Caption: The Performance tab shows per-county model metrics (MASE, Dir Acc, MAE, sMAPE), best model selection, and comparative bar charts. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

**User Guide:**
1. A metrics table displays each county's performance across all metrics.
2. The "Best Model" column indicates whether the pooled or fine-tuned model performs better for each county.
3. Bar charts compare MASE, Dir Acc, and MAE across counties, enabling quick identification of best and worst performing markets.
4. Fold-level performance charts show how model accuracy changes over time (by fold).
5. A confidence level indicator shows the model's confidence based on historical accuracy.

**Target Users:** Technical users and researchers evaluating model reliability.

The dashboard is designed to answer three types of questions:
- **Predictive (Overview tab):** "What will maize prices be next month?"
- **Descriptive (Seasonality tab):** "What were the historical price patterns and seasonal trends?"
- **Diagnostic (Drivers and Performance tabs):** "Why are prices changing and how reliable are the forecasts?"

## 4.7 Comparison with Literature Benchmarks

To contextualize the model's performance, the results are compared with findings from similar studies in the literature.

**Table 11: Comparison of Results with Literature Benchmarks**

| Study | Commodity | Method | Performance | Comparable Metric |
|-------|-----------|--------|-------------|:-----------------:|
| This project | Maize (Kenya) | Pooled XGBoost | MASE: 0.322, MAE: 2.07 KES | MASE, MAE |
| Chakraborty et al. (2021) | Onion (India) | XGBoost | 15% RMSE improvement over ARIMA | RMSE improvement |
| Wang et al. (2020) | Corn (USA) | XGBoost | R² > 0.85 (1-4 weeks) | R² |
| Dorosh et al. (2020) | Maize (S. Africa) | Random Forest | 20-30% RMSE improvement over ARIMA | RMSE improvement |
| Pan et al. (2022) | Vegetables (China) | Transfer Learning | 12-18% accuracy improvement | Accuracy |
| Jha & Sinha (2014) | Agri commodities (India) | Neural Networks | 8-12% improvement over ARIMA | Improvement |

The comparison reveals several important insights:

1. **XGBoost consistently outperforms ARIMA:** Across all studies that compared XGBoost (or RF) with ARIMA, the tree-based ensemble methods showed 15-30% improvement. Our MASE of 0.322 represents a 68% improvement over persistence, which aligns with this pattern.

2. **County-level forecasting is challenging:** The MAE of 2.07 KES (4-7% of price) is comparable to or better than similar studies, especially considering the challenging county-level forecasting context with limited features.

3. **Δ-price + MASE framework adds rigor:** Most existing studies use RMSE or R² as primary metrics. Our MASE-based evaluation provides a more meaningful benchmark by directly measuring improvement over the naive persistence forecast.

## 4.8 Practical Interpretation of Results

The model's performance metrics translate to practical value for stakeholders:

**For a maize farmer:** A directional accuracy of 75.5% means that if a farmer follows the model's price direction signal for 100 weeks, they would make the correct marketing timing decision approximately 76 times. If each correct decision (e.g., waiting 2 weeks to sell) adds 1-2 KES/kg to the sale price, a farmer selling 20 bags (1,800 kg) could gain an additional KES 1,800 to KES 3,600 per season—a meaningful increment for a smallholder household.

**For a maize trader:** The MAE of 2.07 KES/kg means that on average, the model's weekly price prediction is within about 2 KES of the actual price. For a trader dealing in 100 bags per week (9,000 kg), an error of 2 KES/kg translates to a potential forecast error of KES 18,000 per week. The 68% reduction in error compared to persistence saves the trader approximately KES 38,000 per week in improved procurement planning.

**For a policymaker:** The 8-week forecasts with confidence intervals provide a 2-month planning horizon. If the model forecasts a price increase above a threshold (e.g., 50 KES/kg in Nairobi), policymakers have 2 months to take preemptive action such as releasing strategic reserves or accelerating import approvals. The confidence bands around forecasts enable risk-based decision-making—a narrower band gives more confidence to act.

---

# CHAPTER 5: CONCLUSION AND RECOMMENDATIONS

## 5.1 Summary of Findings

This project successfully developed and evaluated a machine learning-based maize price forecasting system for Kenyan counties. The system addresses a critical gap in agricultural market information by providing automated, county-level price forecasts that are currently unavailable through existing systems. The key findings are:

- The pooled XGBoost model achieves a MASE of 0.322 (68% better than persistence), a directional accuracy of 75.5%, and a MAE of 2.07 KES across five target counties.
- Per-county fine-tuning does not significantly improve upon the pooled model, suggesting that county dummies effectively capture county-specific patterns.
- Price-momentum features (price_change_ma_4w, price_change_lag_1w) are the most important predictors, followed by county indicators and economic variables.
- The model performs best for Kirinyaga (MASE: 0.236) and faces most challenges with Mombasa's unique import-dependent market dynamics.
- Performance improves with more training data, validating the expanding window approach and suggesting continued improvement as more data accumulates.

## 5.2 Conclusion

The key achievements of the project include:

1. **Data Integration:** Successfully integrated multiple data sources (KAMIS, AgriBORA, weather, economic indicators) into a comprehensive panel dataset covering 46 counties over 5 years.

2. **Δ-Price Forecasting Framework:** Implemented a rigorous forecasting framework using Δ-price as the target variable, MASE as the primary evaluation metric, and expanding window cross-validation for robust performance assessment.

3. **Pooled XGBoost Model:** Developed a pooled XGBoost model that achieves a MASE of 0.322 (68% better than persistence), a directional accuracy of 75.5%, and a MAE of 2.07 KES across five target counties.

4. **Interactive Dashboard:** Built a comprehensive Streamlit dashboard with four analysis tabs (Overview, Seasonality, Drivers, Performance) that addresses predictive, descriptive, and diagnostic questions.

5. **Cloud Deployment:** Configured the system for deployment on Streamlit Cloud, enabling anytime, anywhere access for stakeholders.

## 5.3 Implementation Roadmap

The following implementation roadmap outlines the phases required to move from the current prototype to a fully operational system:

**Phase 1 — Prototype (Completed):**
- Core XGBoost model with pooled architecture
- Basic dashboard with 5 target counties
- Expanding window evaluation framework

**Phase 2 — Pilot (3-6 months):**
- Expand dashboard coverage to all 46 counties with sufficient data
- Implement automated weekly data pipeline updates
- Deploy on Streamlit Cloud for stakeholder testing
- Conduct user feedback sessions with 20-30 farmers, traders, and policymakers

**Phase 3 — Production (6-12 months):**
- Integrate real-time data feeds (API connections to KAMIS, AgriBORA, weather services)
- Implement user authentication and personalized alerts
- Add mobile-responsive design or dedicated mobile application
- Establish automated retraining pipeline with performance monitoring

**Phase 4 — Scale (12-24 months):**
- Expand to other staple commodities (beans, wheat, rice)
- Develop API for third-party integration with other agritech platforms
- Incorporate satellite-based crop yield estimates
- Implement ensemble methods combining multiple model types

## 5.4 Cost-Benefit Analysis

The costs and benefits of implementing the system at scale are estimated below:

**Development Costs (Sunk):**
- Software development: Approximately KES 200,000 (3 months part-time)
- Data acquisition: KES 0 (all data sources are publicly available or freely provided)
- Cloud hosting: KES 0 (Streamlit Community Cloud is free)

**Operational Costs (Annual):**
- Streamlit Cloud (paid tier): Approximately KES 60,000 per year
- API maintenance: Approximately KES 30,000 per year
- Data updates: Approximately KES 50,000 per year
- Total annual operational cost: Approximately KES 140,000

**Estimated Benefits:**
- Farmer income improvement: If 10,000 farmers each save 2 KES/kg on 500 kg sold, total benefit = KES 10 million per season
- Trader cost reduction: KES 500,000 - 1,000,000 per year per medium trader in reduced procurement costs
- Policy savings: Avoided costs of reactive interventions in the maize market (estimated at KES 50-100 million per crisis event)

The benefit-to-cost ratio is estimated at 50:1 or higher, making the system a highly cost-effective intervention for improving maize market outcomes.

## 5.5 Policy Recommendations

Based on the project findings, the following policy recommendations are made for government agencies:

**1. Invest in Data Infrastructure:**
- KAMIS should prioritize automated data collection to improve timeliness and reduce reporting gaps
- Data sharing agreements between KAMIS, AgriBORA, and other platforms should be strengthened to create a unified price database
- Historical data should be made more accessible for research and development purposes

**2. Institutionalize Price Forecasting:**
- The Ministry of Agriculture should establish a dedicated price forecasting unit that uses ML-based systems alongside traditional analysis
- Forecasts should be integrated into existing early warning systems and food security assessments
- Regular forecast bulletins should be published alongside current price information

**3. Support Stakeholder Access:**
- The government should support the distribution of forecast information through existing extension services and mobile platforms
- Partnerships with agritech platforms (DigiFarm, M-Farm) should be explored to integrate forecasts into their service offerings
- Training programs should be developed to help farmers and traders interpret and act on forecast information

**4. Enable Market Interventions:**
- The NCPB should use price forecasts to optimize strategic grain reserve management, including timing of purchases and releases
- Import licensing decisions should incorporate forecast information to ensure timely responses to anticipated supply gaps

## 5.6 Recommendations for System Users

**For Farmers:**
- Use the directional accuracy information (75.5% correct) to inform marketing timing decisions
- Check the 8-week forecast before making storage decisions—if prices are forecast to rise, consider storing maize for 1-2 months
- Combine forecast information with local market knowledge for best results

**For Traders and Millers:**
- Use the 8-week forecasts with confidence intervals for inventory planning
- Monitor the Drivers tab for early warning of price-relevant changes in CPI or exchange rates
- Use the confidence bands to assess forecast reliability—narrow bands give more confidence to make inventory commitments

**For Policymakers:**
- Use the system as a complement to existing early warning systems
- Monitor price forecasts for indications of impending price spikes or collapses
- Share forecast information with relevant agencies and stakeholders

**For System Developers:**
- Integrate real-time data feeds for automated weekly model updates
- Expand the dashboard to include all 47 counties as data quality improves
- Add user accounts and customization features for personalized alerts
- Develop a mobile application for wider accessibility

**For Data Collection Agencies (KAMIS, AgriBORA):**
- Improve data collection frequency and consistency across all counties
- Make historical data more readily accessible for research and development
- Consider incorporating additional variables such as production estimates, import volumes, and road infrastructure data

## 5.7 Future Work

Several directions for future work have been identified:

**Model Improvements:**
- Experiment with deep learning approaches (LSTM, Transformer) as more historical data becomes available
- Implement probabilistic forecasting using quantile regression or Monte Carlo dropout
- Incorporate satellite-based crop yield estimates and vegetation indices
- Develop ensemble methods combining XGBoost with other model types
- Test the inclusion of sentiment analysis from agricultural news and social media

**Geographic Expansion:**
- Extend the system to cover all 47 Kenyan counties
- Develop models for other staple commodities (beans, wheat, rice)
- Adapt the methodology for other East African countries

**Technical Enhancements:**
- Implement automated retraining pipeline with weekly data updates
- Add anomaly detection for early warning of price spikes
- Develop API endpoints for integration with other agricultural platforms
- Incorporate explainable AI techniques (SHAP values) for enhanced interpretability

**User Research:**
- Conduct user studies with farmers, traders, and policymakers to assess system usability and impact
- Develop user training materials and onboarding processes
- Measure the actual impact of forecast-informed decisions on stakeholder outcomes

---

# REFERENCES

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 785-794). ACM.

Chakraborty, P., Sharma, D. K., & Chatterjee, S. (2021). Predicting agricultural commodity prices using XGBoost: A case study of onion prices in India. *Journal of Agricultural Informatics*, 12(2), 15-28.

Dorosh, P., Pauw, K., & Thurlow, J. (2020). Machine learning for agricultural price prediction in Southern Africa. *IFPRI Discussion Paper*, 1923.

Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts.

Jha, G. K., & Sinha, K. (2014). Agricultural price forecasting using neural network models: An empirical investigation. *Journal of the Indian Society of Agricultural Statistics*, 67(2), 213-224.

Kamilaris, A., & Prenafeta-Boldú, F. X. (2018). Deep learning in agriculture: A survey. *Computers and Electronics in Agriculture*, 147, 70-90.

Kenya National Bureau of Statistics. (2023). *Economic Survey 2023*. Nairobi: Government Printer.

LeSage, J. P., & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. CRC Press.

Ministry of Agriculture, Livestock, Fisheries and Cooperatives. (2022). *Agricultural Sector Transformation and Growth Strategy 2019-2029 Annual Report*. Nairobi: Government of Kenya.

Pan, Y., Li, Z., & Zhang, Y. (2022). Transfer learning for agricultural price forecasting: A case study on vegetable prices in China. *Computers and Electronics in Agriculture*, 193, 106-118.

Wang, J., Liu, Z., & Chen, X. (2020). Corn price prediction in the United States using gradient boosting machines. *Agricultural Economics*, 51(6), 849-863.

Waweru, J. K., & Omondi, P. (2023). Digital agricultural platforms and market information access among smallholder farmers in Kenya. *Journal of Agricultural Extension and Rural Development*, 15(2), 45-58.

World Bank. (2022). *Machine Learning for Agricultural Price Forecasting in South Asia: Technical Report*. Washington, DC: World Bank Group.

Xiong, T., Li, C., & Bao, Y. (2018). A comparison of machine learning methods for agricultural commodity price forecasting. *Neural Computing and Applications*, 30(5), 1425-1440.

---

# APPENDICES

## Appendix A: Budget and Resources

**Table 12: Budget Estimates**

| Item | Description | Cost (KES) |
|------|-------------|:----------:|
| **Hardware** | | |
| Laptop Computer | Development and testing | Already owned |
| External Storage | Data backup | 3,000 |
| Internet Access | Research and data collection | 10,000 |
| **Software** | | |
| Python (Open Source) | Programming language | 0 |
| Streamlit Cloud | Deployment hosting | 0 |
| Microsoft Office | Documentation | Already owned |
| Open-Meteo API | Weather data | 0 |
| **Other** | | |
| Printing and Binding | Project documentation | 5,000 |
| Transport | Research meetings | 5,000 |
| Miscellaneous | Contingency | 3,000 |
| **Total** | | **26,000** |

## Appendix B: Project Schedule (Gantt Chart)

**Table 13: Work Breakdown Structure**

| Task | Duration (Weeks) | Predecessor |
|------|:----------------:|:-----------:|
| Data Collection | 2 | — |
| Data Cleaning | 2 | 1 |
| Feature Engineering | 2 | 2 |
| Model Development | 3 | 3 |
| Model Evaluation | 2 | 4 |
| Dashboard Development | 3 | 4 |
| Documentation | 2 | 5, 6 |
| Deployment | 1 | 7 |

![Figure 11: Gantt Chart - Project Schedule](screenshots/figure_11.png)

*Caption: Gantt chart showing the project timeline with 8 main tasks spanning 17 weeks. Screenshots should be captured from the running dashboard and placed in the screenshots/ directory.*

## Appendix C: Dashboard User Guide

### Overview Tab

The Overview tab is the default view when the dashboard is loaded. It provides a comprehensive snapshot of current market conditions and near-term forecasts.

**Controls:**
- **County Selector (Sidebar):** Dropdown menu listing all available counties. Select the county of interest.
- **Forecast Horizon (Sidebar):** Slider to set the forecast length from 1 to 12 weeks.

**Display Elements:**
- **Metric Cards:** Four cards showing: (1) Current Week Price — the most recent price in KES/kg; (2) 1-Week Change — the absolute and percentage change from last week; (3) 4-Week Average — the rolling average price over the past month; (4) Price Volatility — the standard deviation of prices over the past 4 weeks.
- **Main Chart:** A time series plot showing historical prices (solid blue line), forecasted prices (dashed orange line), and 95% confidence interval (shaded band). The shading becomes wider at longer forecast horizons.
- **Forecast Table:** A tabular display of the week-by-week forecast with columns: Week Number, Forecasted Price, Lower Bound (95% CI), Upper Bound (95% CI).

**Interpretation:**
- Narrow confidence bands indicate higher forecast certainty.
- A rising forecast slope suggests an expected price increase—consider holding maize for later sale.
- A falling forecast slope suggests an expected price decrease—consider selling promptly.

### Seasonality Tab

**Controls:**
- **County Selector (Sidebar):** Same as Overview tab.
- **Year Comparison:** Checkboxes to overlay individual years on the seasonal chart.

**Display Elements:**
- **Seasonal Pattern Chart:** Bar or line chart showing average monthly prices across all years. Highlights the typical seasonal cycle.
- **Year-over-Year Chart:** Overlay of individual year price series, color-coded by year.
- **Monthly Statistics Table:** Mean, median, min, max, and standard deviation of prices for each month.

**Interpretation:**
- Identify the months when prices typically peak (sell timing) and trough (buy timing).
- Compare the current year's trajectory with historical patterns to identify anomalies.
- Use the standard deviation column to assess which months have the most uncertain prices.

### Drivers Tab

**Display Elements:**
- **Feature Importance Chart:** Horizontal bar chart of the top 15 features ranked by XGBoost importance score.
- **Current Feature Values Table:** A table showing the latest available values for key features (CPI, USD/KES, inflation, temperature, rainfall).
- **Driver Scatter Plots:** Scatter plots of selected features (e.g., CPI, exchange rate) versus maize prices, with trend lines.

**Interpretation:**
- Higher-ranked features have greater influence on price predictions.
- The scatter plots reveal whether relationships are positive or negative (e.g., higher CPI → higher maize prices).
- Monitor the Current Feature Values table for changes that may signal future price movements.

### Performance Tab

**Display Elements:**
- **Metrics Table:** Per-county performance metrics: MASE, Directional Accuracy, MAE, sMAPE, and Best Model indicator.
- **Comparison Bar Charts:** Side-by-side bar charts comparing metrics across counties.
- **Fold Performance Chart:** Line chart showing how MASE or MAE changes across the 5 cross-validation folds.

**Interpretation:**
- Lower MASE and MAE values indicate more accurate predictions.
- Higher Directional Accuracy means more reliable price direction signals.
- Improving fold performance (decreasing MASE in later folds) suggests the model becomes more accurate as training data accumulates.

## Appendix D: Data Dictionary

**Table 14: Data Dictionary — All Variables**

| Variable Name | Description | Data Type | Source | Range/Values |
|---------------|-------------|-----------|--------|-------------|
| **Price Variables** | | | | |
| county | County name | Categorical | KAMIS | 46 Kenyan counties |
| market | Market location | Categorical | KAMIS | Multiple per county |
| commodity | Commodity type | Categorical | KAMIS | "Maize (dry)" |
| price | Weekly average price (KES/kg) | Numeric | KAMIS | 5.0 - 80.0 |
| price_std | Standard deviation of weekly price | Numeric | KAMIS | 0.0 - 15.0 |
| week_start | Week start date | Date | KAMIS | 2021-01-01 to 2025-10-31 |
| **Price Features** | | | | |
| lag_1w | Price lagged by 1 week | Numeric | Engineered | 5.0 - 80.0 |
| lag_2w | Price lagged by 2 weeks | Numeric | Engineered | 5.0 - 80.0 |
| lag_4w | Price lagged by 4 weeks | Numeric | Engineered | 5.0 - 80.0 |
| lag_8w | Price lagged by 8 weeks | Numeric | Engineered | 5.0 - 80.0 |
| lag_12w | Price lagged by 12 weeks | Numeric | Engineered | 5.0 - 80.0 |
| ma_4w | 4-week moving average of price | Numeric | Engineered | 5.0 - 80.0 |
| std_4w | 4-week rolling standard deviation | Numeric | Engineered | 0.0 - 15.0 |
| ma_8w | 8-week moving average of price | Numeric | Engineered | 5.0 - 80.0 |
| std_8w | 8-week rolling standard deviation | Numeric | Engineered | 0.0 - 15.0 |
| ma_12w | 12-week moving average of price | Numeric | Engineered | 5.0 - 80.0 |
| std_12w | 12-week rolling standard deviation | Numeric | Engineered | 0.0 - 15.0 |
| **Δ-Price Features** | | | | |
| price_change | Δ-price (current - previous week) | Numeric | Engineered | -15.0 - 15.0 |
| change_lag_1w | Δ-price lagged by 1 week | Numeric | Engineered | -15.0 - 15.0 |
| change_lag_2w | Δ-price lagged by 2 weeks | Numeric | Engineered | -15.0 - 15.0 |
| change_ma_4w | 4-week moving average of Δ-price | Numeric | Engineered | -10.0 - 10.0 |
| change_std_4w | 4-week rolling std of Δ-price | Numeric | Engineered | 0.0 - 10.0 |
| **Weather Variables** | | | | |
| temp_avg | Weekly average temperature (°C) | Numeric | Open-Meteo | 10.0 - 35.0 |
| temp_max | Weekly max temperature (°C) | Numeric | Open-Meteo | 15.0 - 42.0 |
| temp_min | Weekly min temperature (°C) | Numeric | Open-Meteo | 5.0 - 28.0 |
| rain_mm | Weekly total rainfall (mm) | Numeric | Open-Meteo | 0.0 - 200.0 |
| wind_speed | Weekly max wind speed (km/h) | Numeric | Open-Meteo | 0.0 - 80.0 |
| rain_sum_4w | 4-week cumulative rainfall (mm) | Numeric | Engineered | 0.0 - 600.0 |
| temp_avg_4w | 4-week average temperature (°C) | Numeric | Engineered | 10.0 - 32.0 |
| rain_sum_8w | 8-week cumulative rainfall (mm) | Numeric | Engineered | 0.0 - 1000.0 |
| temp_avg_8w | 8-week average temperature (°C) | Numeric | Engineered | 10.0 - 32.0 |
| **Economic Variables** | | | | |
| cpi | Consumer Price Index | Numeric | KNBS | 110.0 - 180.0 |
| usd_kes | USD/KES exchange rate | Numeric | CBK | 100.0 - 170.0 |
| inflation_rate | Year-over-year inflation rate (%) | Numeric | KNBS | 4.0 - 15.0 |
| **Temporal Features** | | | | |
| month | Calendar month | Integer | Engineered | 1 - 12 |
| week_of_year | Week of the year | Integer | Engineered | 1 - 53 |
| year | Calendar year | Integer | Engineered | 2021 - 2025 |
| days_from_start | Days from first observation | Integer | Engineered | 0 - 1800 |
| is_long_rains | Long rains season flag (Mar-May) | Binary | Engineered | 0 or 1 |
| is_short_rains | Short rains season flag (Oct-Dec) | Binary | Engineered | 0 or 1 |
| is_harvest | Harvest period flag | Binary | Engineered | 0 or 1 |
| **Geographic Variables** | | | | |
| c_[county_name] | County one-hot encoding (46 vars) | Binary | Engineered | 0 or 1 |

*Note: Screenshots referenced throughout this document should be captured from the running dashboard application and placed in the screenshots/ directory for inclusion in the final document.*
