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
1.3 Problem Statement .............................................................................................................. 3
1.4 Proposed Solution ............................................................................................................... 4
1.5 Research Objectives ............................................................................................................ 5
1.6 Justification of the Study .................................................................................................... 6
1.7 Significance of the Study .................................................................................................... 6
1.8 Assumptions ........................................................................................................................ 7
1.9 Limitations of the Study ...................................................................................................... 7
1.10 Project Scope .................................................................................................................... 7

CHAPTER 2: LITERATURE REVIEW ............................................................................................ 9
2.1 Introduction ......................................................................................................................... 9
2.2 Machine Learning in Agricultural Price Forecasting ......................................................... 9
2.3 Global Similar Systems ..................................................................................................... 11
2.3.1 FAO Global Information and Early Warning System (GIEWS) .................................. 11
2.3.2 International Food Policy Research Institute (IFPRI) Price Forecasting Models ...... 12
2.3.3 World Bank's Agricultural Price Forecasting Platform .............................................. 13
2.4 Local Similar Systems ....................................................................................................... 14
2.4.1 Kenya Agricultural Market Information System (KAMIS) ........................................ 14
2.4.2 Kenya Food Security Outlook (FEWS NET Kenya) ................................................... 15
2.4.3 AgriBORA Market Platform ....................................................................................... 16
2.5 Theoretical Framework ..................................................................................................... 16
2.5.1 Time Series Forecasting Fundamentals ...................................................................... 17
2.5.2 Ensemble Learning Methods ...................................................................................... 18
2.5.3 Gradient Boosting and XGBoost ................................................................................ 19
2.6 Research Gaps ................................................................................................................... 20

CHAPTER 3: METHODOLOGY .................................................................................................. 22
3.1 Introduction ....................................................................................................................... 22
3.2 Research Design ............................................................................................................... 22
3.3 Data Collection ................................................................................................................. 23
3.3.1 KAMIS Price Data ...................................................................................................... 23
3.3.2 AgriBORA Price Data ................................................................................................ 24
3.3.3 Weather Data .............................................................................................................. 24
3.3.4 Economic Indicators Data .......................................................................................... 25
3.4 Data Preparation and Feature Engineering ....................................................................... 25
3.4.1 Data Cleaning ............................................................................................................. 26
3.4.2 Feature Construction .................................................................................................. 27
3.5 Experimental Setup .......................................................................................................... 29
3.5.1 Target Variable Engineering ...................................................................................... 29
3.5.2 Pooled XGBoost Model Architecture ......................................................................... 30
3.5.3 Expanding Window Cross-Validation ........................................................................ 31
3.5.4 Per-County Fine-Tuning ............................................................................................. 32
3.5.5 Evaluation Metrics ..................................................................................................... 33
3.6 Project Methodology ........................................................................................................ 35
3.6.1 Agile Development Methodology .............................................................................. 35
3.6.2 Justification for Agile Methodology .......................................................................... 36
3.6.3 Development Phases ................................................................................................... 36
3.7 System Architecture .......................................................................................................... 37
3.7.1 Architecture Overview ............................................................................................... 37
3.7.2 Data Pipeline .............................................................................................................. 37
3.7.3 Model Training Pipeline ............................................................................................ 38
3.7.4 Dashboard Application .............................................................................................. 38

CHAPTER 4: RESULTS AND DISCUSSION ................................................................................ 39
4.1 Introduction ....................................................................................................................... 39
4.2 Model Performance Results .............................................................................................. 39
4.2.1 Overall Results Across All Folds ............................................................................... 39
4.2.2 Per-County Performance ............................................................................................ 40
4.2.3 Performance Across Folds (Temporal Stability) ....................................................... 41
4.3 Feature Importance Analysis ............................................................................................. 42
4.4 Seasonal Pattern Analysis ................................................................................................ 43
4.5 Discussion ......................................................................................................................... 44

CHAPTER 5: CONCLUSION AND RECOMMENDATIONS .......................................................... 46
5.1 Conclusion ........................................................................................................................ 46
5.2 Recommendations ............................................................................................................. 46
5.3 Future Work ...................................................................................................................... 47

REFERENCES ............................................................................................................................. 48

APPENDICES .............................................................................................................................. 51
Appendix A: Budget and Resources ........................................................................................ 51
Appendix B: Project Schedule (Gantt Chart) .......................................................................... 52
Appendix C: System Code Listings ......................................................................................... 53

---

## TABLE OF FIGURES

Figure 1: Kenya Maize Price Trends by County (2021-2025) ..................................................... 2
Figure 2: System Architecture Diagram ...................................................................................... 37
Figure 3: Data Pipeline Flowchart .............................................................................................. 38
Figure 4: Model Performance Comparison Bar Charts ................................................................ 41
Figure 5: Feature Importance (Top 15) ....................................................................................... 42
Figure 6: Monthly Seasonal Patterns Across Target Counties .................................................... 43
Figure 7: Dashboard Overview Tab Screenshot .......................................................................... 44
Figure 8: Dashboard Seasonality Tab Screenshot ........................................................................ 44
Figure 9: Dashboard Drivers Tab Screenshot .............................................................................. 45
Figure 10: Dashboard Performance Tab Screenshot .................................................................... 45
Figure 11: Gantt Chart - Project Schedule ................................................................................. 52

## LIST OF TABLES

Table 1: Data Sources Summary .................................................................................................. 25
Table 2: Engineered Feature Set ................................................................................................. 28
Table 3: Expanding Window Cross-Validation Folds .................................................................. 32
Table 4: Overall Model Performance Comparison ....................................................................... 39
Table 5: Per-County Best Model Performance ............................................................................. 40
Table 6: Performance Across Folds for Pooled XGBoost ............................................................ 41
Table 7: Budget Estimates .......................................................................................................... 51
Table 8: Work Breakdown Structure ........................................................................................... 52

---

# CHAPTER 1: INTRODUCTION

## 1.1 Introduction

This chapter provides the foundation for the research project by presenting the background of maize price forecasting in Kenya, the problem that motivated this study, the proposed solution, research objectives, justification, significance, assumptions, limitations, and the project scope. The chapter establishes the context within which the maize price forecasting system was developed and sets the stage for the literature review and methodology that follow.

## 1.2 Background of the Study

Agriculture is the backbone of the Kenyan economy, contributing approximately 33% to the Gross Domestic Product (GDP) and employing over 40% of the population (Kenya National Bureau of Statistics, 2023). Among agricultural commodities, maize holds a position of paramount importance as the country's primary staple food. The average Kenyan consumes approximately 98 kilograms of maize per year, making it a critical component of household food security (Ministry of Agriculture, Livestock, Fisheries and Cooperatives, 2022).

Maize prices in Kenya exhibit significant volatility driven by a complex interplay of factors including seasonal production cycles, weather patterns (particularly rainfall during the long and short rainy seasons), input costs, fuel prices, inflation, exchange rate fluctuations, market infrastructure, and post-harvest losses. This price volatility has profound implications for food security, household welfare, and macroeconomic stability. When maize prices spike, low-income urban households suffer disproportionately as they spend a larger share of their income on food. Conversely, when prices collapse during harvest seasons, smallholder farmers—who constitute the majority of maize producers—face income losses that undermine their livelihoods.

The Kenya Agricultural Market Information System (KAMIS), operated by the Ministry of Agriculture, provides weekly price data for various agricultural commodities across multiple markets in all 47 counties. Similarly, the Agricultural Business Rapid Assessment (AgriBORA) platform provides transaction-based wholesale prices. Despite the availability of this data, systematic and accurate price forecasting remains a challenge. Most price information available to stakeholders is historical, with limited predictive capability.

Traditional approaches to price forecasting in Kenya have relied on expert judgment, simple trend analysis, and basic statistical methods. These approaches, while providing some value, are limited in their ability to capture the complex, non-linear relationships between the numerous factors that influence maize prices. Furthermore, they often fail to provide probabilistic forecasts or confidence intervals that would enable risk-based decision-making.

In recent years, machine learning has emerged as a powerful tool for time series forecasting across various domains, including agricultural commodity prices. Techniques such as gradient boosting, random forests, and deep learning have demonstrated superior performance compared to traditional statistical methods, particularly when dealing with high-dimensional data and complex non-linear relationships. However, the application of these techniques to county-level maize price forecasting in Kenya remains relatively unexplored.

This project addresses this gap by developing a machine learning-based maize price forecasting system that leverages XGBoost—a state-of-the-art gradient boosting framework—to predict weekly maize prices across multiple Kenyan counties. The system incorporates price data from multiple sources, weather variables, economic indicators, and engineered features to capture the multi-faceted nature of maize price determination. The model is trained using a pooled approach that enables information sharing across counties, combined with per-county fine-tuning to capture local market dynamics.

Figure 1 illustrates the maize price trends for five target counties from 2021 to 2025, showing the distinct seasonal patterns and price levels across different regions.

**[Figure 1: Kenya Maize Price Trends by County (2021-2025)]**

*Caption: Weekly maize prices for Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu counties from 2021 to 2025. The chart shows county-specific price levels and common seasonal patterns.*

## 1.3 Problem Statement

Despite the critical importance of maize to Kenya's food security and economy, stakeholders across the value chain—including farmers, traders, policymakers, and consumers—lack access to accurate, timely, and reliable price forecasts. This information gap leads to several interconnected problems:

**For Farmers:** Smallholder farmers, who produce over 75% of Kenya's maize, make planting, harvesting, and marketing decisions based on limited information. Without reliable price forecasts, they often sell at suboptimal prices immediately after harvest when supply is high and prices are low, missing the opportunity to benefit from seasonal price increases. This contributes to persistent rural poverty and food insecurity.

**For Traders and Millers:** Maize traders and millers face significant inventory and procurement risks due to price uncertainty. The inability to forecast price movements leads to either excessive inventory holding costs or stock-outs, both of which have negative financial implications. These costs are ultimately passed on to consumers in the form of higher prices.

**For Policymakers:** Government agencies responsible for food security, including the Ministry of Agriculture and the National Cereals and Produce Board (NCPB), require accurate price forecasts to make timely decisions about strategic grain reserves, import licenses, and market interventions. Reactive rather than proactive policy responses often result from the absence of reliable forecasting tools.

**For Consumers:** Urban households, particularly those in low-income brackets, bear the brunt of maize price volatility. Price spikes can push vulnerable households into food insecurity, while price collapses threaten the viability of the entire maize value chain.

Existing forecasting approaches suffer from several limitations:

1. **Reliance on historical trends:** Most current approaches look backward rather than forward, providing little predictive value.

2. **Inability to capture complex relationships:** Simple statistical methods cannot adequately model the non-linear interactions between weather, economics, and market dynamics.

3. **Lack of granularity:** National-level forecasts miss important county-level variations driven by local production, market access, and demand patterns.

4. **Absence of uncertainty quantification:** Point forecasts without confidence intervals limit risk-based decision-making.

5. **Limited automation:** Manual forecasting processes are time-consuming, inconsistent, and difficult to scale.

These problems collectively create a pressing need for an automated, machine learning-based maize price forecasting system that can provide accurate, county-level predictions with quantified uncertainty to support decision-making across the maize value chain.

## 1.4 Proposed Solution

This project proposes the development of a machine learning-based maize price forecasting system that addresses the identified problems through the following key features:

**Data Integration:** The system integrates multiple data sources including KAMIS prices, AgriBORA prices, weather data (temperature, rainfall, wind), and economic indicators (CPI, USD/KES exchange rate, inflation rate) to create a comprehensive feature set for price prediction.

**Δ-Price Forecasting:** Instead of predicting absolute prices, the system predicts week-over-week price changes (Δ-price). This approach effectively removes the strong autocorrelation present in price time series and provides a more meaningful evaluation framework where the persistence baseline (predicting no change) serves as a natural benchmark.

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

**Academic Contribution:** The study contributes to the growing body of knowledge on machine learning applications in agricultural price forecasting, particularly in the context of developing economies. The pooled modeling approach with per-county fine-tuning offers a novel methodology that balances global learning with local adaptation.

**Practical Utility:** The system provides actionable price forecasts that can directly benefit stakeholders across the maize value chain. Farmers can make informed marketing decisions, traders can optimize inventory management, and policymakers can implement timely interventions to stabilize prices.

**Methodological Innovation:** The use of Δ-price as the target variable, combined with expanding window cross-validation and MASE-based evaluation, provides a rigorous framework for time series forecasting that addresses common pitfalls in the evaluation of forecasting models (e.g., inappropriate use of R², single train-test splits, and failure to account for temporal dependencies).

**Scalability:** While focused on maize and five target counties, the methodology is designed to be scalable to other commodities and all 47 counties, providing a template for national-level agricultural price forecasting.

**Food Security Impact:** Improved price forecasting has a direct positive impact on food security by enabling more efficient market functioning, reducing price risk, and supporting evidence-based policy decisions.

## 1.7 Significance of the Study

The implementation of this project is expected to provide the following benefits:

1. **Empowered Farmers:** Access to reliable price forecasts enables farmers to make informed decisions about when and where to sell their produce, potentially increasing their income by 10-20% through strategic market timing.

2. **Improved Market Efficiency:** Traders and millers can better manage inventory, reduce waste, and optimize procurement strategies, leading to lower transaction costs and more stable prices.

3. **Evidence-Based Policy:** Policymakers gain access to predictive insights that support proactive rather than reactive interventions in the maize market, including strategic grain reserve management and import/export decisions.

4. **Enhanced Food Security:** More accurate price information contributes to improved food security outcomes by reducing price volatility and ensuring more stable access to maize for consumers.

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

1. **Data Availability:** The availability and completeness of price data vary significantly across counties. Some counties have sparse data, limiting the model's ability to learn county-specific patterns.

2. **Forecast Horizon:** While the system can generate forecasts for up to 12 weeks, forecast accuracy declines for longer horizons due to accumulating uncertainty in recursive predictions.

3. **External Factors:** The model cannot account for unpredictable events such as government policy changes, large-scale imports, or geopolitical events that may significantly affect maize prices.

4. **Data Quality:** Price data from market information systems may contain reporting errors, inconsistencies, or biases that affect model training and evaluation.

5. **Geographic Coverage:** While the pooled model is trained on 46 counties, the system's evaluation and dashboard focus on 5 target counties, limiting the assessment of model performance across all regions.

6. **Computational Resources:** The expanding window cross-validation and fine-tuning processes require significant computational resources, limiting the number of hyperparameter configurations that could be explored.

## 1.10 Project Scope

This project covers the following aspects:

**Geographic Scope:** The system focuses on five target counties—Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu—representing different agricultural zones and market types in Kenya. The pooled model is trained on data from 46 counties.

**Temporal Scope:** The project uses weekly price data from 2021 to 2025. The model generates forecasts for 4 to 12 weeks ahead.

**Functional Scope:**

- Data collection and cleaning from multiple sources
- Feature engineering including price lags, rolling statistics, seasonal flags, and economic indicators
- Machine learning model development using XGBoost
- Model evaluation using expanding window cross-validation
- Interactive dashboard with 4 analysis tabs
- Cloud deployment capability

**Technical Scope:**

- Programming language: Python
- Machine learning framework: XGBoost, scikit-learn
- Dashboard framework: Streamlit
- Data processing: Pandas, NumPy
- Visualization: Matplotlib
- Deployment: Streamlit Cloud

**Out of Scope:**

- Real-time data ingestion (the system uses batch-processed data)
- Mobile application development
- Integration with external APIs for automated data updates
- Multi-commodity forecasting (focused on maize only)
- Deep learning models (LSTM, Transformer) due to data limitations

---

# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction

This chapter provides a comprehensive review of existing literature related to agricultural price forecasting, machine learning applications in time series prediction, and similar systems developed both globally and locally. The review establishes the theoretical foundation for the project and identifies research gaps that the proposed system addresses. The chapter is organized into sections covering machine learning in agricultural price forecasting, global similar systems, local similar systems, theoretical framework, and research gaps.

## 2.2 Machine Learning in Agricultural Price Forecasting

Agricultural commodity price forecasting has been a subject of extensive research due to its importance for food security, farmer livelihoods, and economic planning. Traditional approaches to price forecasting have included econometric models such as AutoRegressive Integrated Moving Average (ARIMA), Vector Autoregression (VAR), and structural equation models. While these methods provide interpretable results, they are limited by their assumptions of linearity and stationarity, which are often violated in real-world price data.

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

## 2.5 Theoretical Framework

### 2.5.1 Time Series Forecasting Fundamentals

Time series forecasting involves predicting future values of a variable based on its historical observations. A time series is a sequence of data points indexed in time order, typically with equal spacing between observations (e.g., weekly in our case).

Key concepts in time series analysis include:

**Stationarity:** A time series is stationary if its statistical properties (mean, variance, autocorrelation) are constant over time. Most forecasting methods assume or require stationarity. Price series are typically non-stationary (trending), which is why first-differencing (Δ-price) is often applied to achieve stationarity.

**Autocorrelation:** The correlation between a time series and its lagged values. Price series typically exhibit strong autocorrelation at lag 1 (price today is highly correlated with price last week), which is why the persistence forecast is a strong baseline.

**Seasonality:** Regular patterns that repeat at fixed intervals (e.g., annual harvest cycles). Agricultural prices typically exhibit strong seasonality driven by planting and harvest cycles.

**Trend:** Long-term direction of the series (upward, downward, or flat). Maize prices in Kenya have shown an upward trend driven by inflation and increasing production costs.

The choice of Δ-price as the target variable in this project is grounded in time series theory. By first-differencing, we remove the non-stationary trend component and focus on predicting the short-term price change, which is more stationary and decomposable.

### 2.5.2 Ensemble Learning Methods

Ensemble learning combines multiple models to produce a single, more accurate prediction. The fundamental principle is that a group of weak learners can collectively form a strong learner. Ensemble methods are among the most successful machine learning approaches for structured data.

The two main types of ensemble methods are:

**Bagging (Bootstrap Aggregating):** Multiple models are trained on different bootstrap samples of the training data, and their predictions are averaged. Random Forest is the most well-known bagging method. Bagging reduces variance without increasing bias.

**Boosting:** Models are trained sequentially, with each new model focusing on correcting the errors of the previous models. The final prediction is a weighted combination of all models. Boosting reduces both bias and variance.

Gradient boosting, the foundation of XGBoost, extends the boosting concept by optimizing a differentiable loss function using gradient descent in function space. At each iteration, a new tree is trained to predict the negative gradient (residuals) of the loss function with respect to the current ensemble prediction.

### 2.5.3 Gradient Boosting and XGBoost

XGBoost (Extreme Gradient Boosting) is an optimized implementation of gradient boosted decision trees that has become one of the most popular and effective machine learning algorithms. Key features of XGBoost include:

**Regularized Objective:** XGBoost incorporates L1 (Lasso) and L2 (Ridge) regularization in the objective function, reducing overfitting and improving generalization.

```math
\text{Obj} = \sum_{i=1}^{n} L(y_i, \hat{y}_i) + \sum_{k=1}^{K} \Omega(f_k)
```

where L is the loss function, and Ω is the regularization term penalizing model complexity.

**Gradient Tree Boosting:** The algorithm builds trees sequentially, where each tree predicts the residuals of the previous ensemble. The update rule is:

```math
\hat{y}_i^{(t)} = \hat{y}_i^{(t-1)} + \eta \cdot f_t(x_i)
```

where η is the learning rate and f_t is the t-th tree.

**Handling Missing Values:** XGBoost learns optimal default directions for missing values, eliminating the need for imputation.

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

## 2.6 Research Gaps

The literature review reveals several gaps that the proposed project aims to address:

**1. Limited County-Level Forecasting in Kenya:** Existing systems either operate at the national level (GIEWS, FEWS NET) or are limited to major reference markets. There is no operational system that provides county-level maize price forecasts for all Kenyan counties.

**2. Lack of Automated Machine Learning Approaches:** Most price analysis in Kenya relies on expert judgment and basic statistical methods. The application of modern machine learning techniques like gradient boosting to agricultural price forecasting in Kenya is largely unexplored in operational systems.

**3. Absence of Pooled Modeling Across Regions:** While individual county-level models are common, the pooled modeling approach that trains a single model on data from multiple regions has not been applied to Kenyan agricultural prices. This approach is particularly valuable for counties with limited historical data, as they can benefit from patterns learned from other counties.

**4. Limited Use of Δ-Price Target Variable:** Most agricultural price forecasting studies model absolute prices. The use of Δ-price as the target variable, combined with MASE as the evaluation metric, provides a more rigorous evaluation framework that directly compares model performance against the persistence baseline.

**5. Lack of Interactive Forecasting Dashboards:** While research papers present model results, there are few operational, interactive dashboards that allow stakeholders to access forecasts, analyze patterns, and make decisions based on machine learning predictions.

**6. Insufficient Uncertainty Quantification:** Existing approaches typically provide point forecasts without confidence intervals. The proposed system generates confidence bands around forecasts, enabling risk-based decision-making.

**7. Limited Use of Expanding Window Validation:** Many studies use a single train-test split or k-fold cross-validation that ignores temporal order. The expanding window approach used in this project provides more robust and realistic performance estimates that reflect the model's ability to forecast future data.

The proposed project directly addresses these gaps by developing an operational, machine learning-based maize price forecasting system that uses pooled XGBoost with Δ-price target, expanding window validation, and an interactive dashboard, specifically designed for Kenyan county-level price forecasting.

---

# CHAPTER 3: METHODOLOGY

## 3.1 Introduction

This chapter describes the research and project methodology employed in developing the maize price forecasting system. The chapter covers the research design, data collection methods, data preparation and feature engineering processes, experimental setup, and the project development methodology. The chapter also presents the system architecture and describes the development tools and technologies used.

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

## 3.4 Data Preparation and Feature Engineering

### 3.4.1 Data Cleaning

Data cleaning was performed using a modular Python script (`src/data/clean.py`) that processes each data source:

**KAMIS Data Cleaning:**
- Filtering for maize (dry grain) records only
- Removing records with missing or zero prices
- Aggregating market-level prices to county-level weekly averages
- Handling outliers using Interquartile Range (IQR) method
- Forward-filling missing weeks within each county

**AgriBORA Data Cleaning:**
- Filtering for maize records
- Removing records with missing or zero prices
- Aggregating transaction-level prices to county-level weekly averages
- Aligning with KAMIS date format

**Weather Data Cleaning:**
- Aggregating daily data to weekly averages (temperature) and sums (rainfall)
- Spatial averaging across weather stations within each county
- Handling missing values through interpolation

### 3.4.2 Feature Construction

Feature engineering was performed using `src/data/features.py` to create a comprehensive feature set for model training. The engineered features can be categorized as follows:

**Price-Based Features:**
- Price lags at 1, 2, 4, 8, and 12 weeks
- Rolling moving averages at 4, 8, and 12 weeks
- Rolling standard deviations at 4, 8, and 12 weeks

**Δ-Price Features (computed in training):**
- Δ-price (current price minus previous week price)
- Δ-price lags at 1 and 2 weeks
- Δ-price 4-week rolling mean and standard deviation

**Weather Features:**
- Weekly mean, maximum, and minimum temperature
- Weekly total rainfall
- Weekly maximum wind speed
- 4-week and 8-week rolling rainfall sums
- 4-week and 8-week rolling mean temperature

**Economic Features:**
- CPI value (monthly, forward-filled to weekly)
- USD/KES exchange rate
- Inflation rate (monthly, forward-filled to weekly)

**Temporal Features:**
- Month (1-12)
- Week of year (1-53)
- Year (2021-2025)
- Days from start (numerical for trend)
- Season (off_season, long_rains, short_rains)
- Long rains flag (March-May)
- Short rains flag (October-December)
- Harvest flag (post-rains periods)

**Geographic Features (for pooled model):**
- County one-hot encoding (46 dummy variables)

**Table 2: Engineered Feature Set**

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

## 3.5 Experimental Setup

### 3.5.1 Target Variable Engineering

A critical design decision in this project is the choice of Δ-price (first difference of price) as the target variable rather than absolute price. This decision is motivated by several considerations:

**Stationarity:** Price series are typically non-stationary (they exhibit trends and changing means), violating assumptions of many statistical methods. Δ-price is typically stationary, making it more amenable to modeling.

**Persistence Baseline:** When predicting absolute prices, the persistence forecast (predicting the current price for all future periods) is a strong baseline that is difficult to beat. By predicting Δ-price, the persistence baseline becomes zero (no change), providing a more meaningful and achievable benchmark.

**MASE Evaluation:** MASE (Mean Absolute Scaled Error) compares model errors to the errors of the persistence baseline. With Δ-price as the target, MASE < 1 directly indicates that the model predicts price changes better than assuming no change.

The Δ-price transformation is computed as:

```math
\Delta P_t = P_t - P_{t-1}
```

where P_t is the price at week t.

### 3.5.2 Pooled XGBoost Model Architecture

The core model is a pooled XGBoost regressor that learns from data across all counties simultaneously. The pooled approach enables the model to:

1. **Share information across counties:** Patterns learned from data-rich counties can benefit data-sparse counties.
2. **Learn common patterns:** Seasonal and economic effects that affect all counties can be efficiently captured.
3. **Provide consistent predictions:** A single model ensures that predictions across counties are internally consistent.

The pooled model input includes all features described in Section 3.4.2, including county one-hot encoding. The county dummies allow the model to learn county-specific intercepts and interactions with other features.

The XGBoost hyperparameters were selected based on experimentation and best practices:

- **n_estimators:** 500 — sufficient trees for convergence with early stopping
- **max_depth:** 3 — shallow trees to prevent overfitting
- **learning_rate:** 0.05 — conservative learning rate
- **reg_lambda:** 5 — L2 regularization to reduce overfitting
- **subsample:** 0.7 — 70% sample per tree for diversity
- **colsample_bytree:** 0.8 — 80% feature subsampling
- **early_stopping_rounds:** 15 — stops if validation error doesn't improve for 15 rounds
- **random_state:** 42 — reproducible results

The model was trained with an internal validation split (80% training, 20% validation) for early stopping.

### 3.5.3 Expanding Window Cross-Validation

Model evaluation was performed using a 5-fold expanding window cross-validation strategy that respects the temporal order of the data. This approach provides robust estimates of model performance across different time periods.

The cross-validation procedure:

1. **Initial Training Window:** The first 55% of weeks (approximately 124 weeks from May 2021 to October 2023)
2. **Fold Size:** 20 weeks per test window
3. **Number of Folds:** 5 (each fold adds 20 more weeks to the training window)

**Table 3: Expanding Window Cross-Validation Folds**

| Fold | Training Weeks | Test Weeks | Training Period | Test Period |
|------|----------------|------------|-----------------|-------------|
| 0 | 124 | 20 | May 2021 – Oct 2023 | Oct 2023 – Mar 2024 |
| 1 | 144 | 20 | May 2021 – Mar 2024 | Mar 2024 – Aug 2024 |
| 2 | 164 | 20 | May 2021 – Aug 2024 | Aug 2024 – Jan 2025 |
| 3 | 184 | 20 | May 2021 – Jan 2025 | Jan 2025 – May 2025 |
| 4 | 204 | 20 | May 2021 – May 2025 | May 2025 – Oct 2025 |

This design ensures that:
- The model is always evaluated on data it has not seen during training
- Performance is assessed across multiple time periods with different market conditions
- The evaluation simulates the realistic scenario of predicting the future from the past

### 3.5.4 Per-County Fine-Tuning

After training the pooled model, per-county fine-tuning is performed to adapt the model to county-specific price dynamics. The fine-tuning approach:

1. **Warm Start:** Each county's model is initialized from the pooled model's booster
2. **County-Specific Training:** The model is further trained on only that county's training data
3. **Reduced Learning Rate:** learning_rate is reduced to 0.01 for fine-tuning
4. **Fewer Iterations:** 150 additional trees are trained per county
5. **Reduced Regularization:** reg_lambda is reduced to 3 to allow more adaptation

The fine-tuning step allows the model to specialize while retaining the general patterns learned from all counties. This is particularly valuable for counties with price dynamics that differ from the national average.

### 3.5.5 Evaluation Metrics

Four metrics are used to evaluate model performance:

**1. MASE (Mean Absolute Scaled Error)**

```math
\text{MASE} = \frac{\text{MAE}_{\text{model}}}{\text{MAE}_{\text{persistence}}}
```

MASE compares the model's MAE to the MAE of the persistence baseline (predicting zero change). A MASE less than 1 indicates that the model outperforms the naive persistence forecast. MASE is scale-independent and can be compared across series with different units.

**2. Directional Accuracy (Dir Acc)**

```math
\text{Dir Acc} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}(\text{sign}(\hat{\Delta}_i) = \text{sign}(\Delta_i))
\]

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

## 3.6 Project Methodology

### 3.6.1 Agile Development Methodology

This project was developed using the Agile development methodology, specifically the Scrum framework. Agile methodology was chosen due to its iterative nature, flexibility, and focus on delivering working software incrementally.

The key Agile principles applied in this project include:

**Iterative Development:** The project was developed in two-week sprints, with each sprint producing a potentially shippable increment of the system.

**Continuous Feedback:** Regular sprint reviews with the supervisor provided feedback that guided subsequent development iterations.

**Prioritized Backlog:** Features were prioritized based on their value to the project objectives, ensuring that the most critical functionality was developed first.

**Adaptive Planning:** The project plan evolved based on emerging insights and changing requirements, rather than following a rigid, predetermined plan.

### 3.6.2 Justification for Agile Methodology

Agile methodology was chosen over traditional waterfall methodology for the following reasons:

1. **Exploratory Nature:** Machine learning projects involve significant exploration and experimentation, making it difficult to specify all requirements upfront.

2. **Incremental Value:** Agile delivery ensures that working features are available early, even if the complete system is not yet finished.

3. **Risk Management:** Regular iterations allow for early identification and mitigation of technical risks.

4. **Stakeholder Involvement:** Agile's emphasis on stakeholder feedback ensures that the final system meets user needs.

### 3.6.3 Development Phases

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

## 3.7 System Architecture

### 3.7.1 Architecture Overview

The maize price forecasting system follows a modular, pipeline-based architecture with three main components: the data pipeline, the model training pipeline, and the dashboard application.

**[Figure 2: System Architecture Diagram]**

*Caption: The system architecture shows the three main components: data pipeline (raw data → cleaned data → features), model training pipeline (features → cross-validation → trained model), and dashboard application (model + features → Streamlit web app).*

### 3.7.2 Data Pipeline

The data pipeline (`src/data/clean.py` and `src/data/features.py`) processes raw data into a feature-rich panel dataset:

1. **Raw Data Ingestion:** Load raw CSV files (KAMIS, AgriBORA, weather, economic)
2. **Data Cleaning:** Filter, aggregate, and clean each data source
3. **Data Merging:** Combine all data sources into a panel dataset keyed by (county, week_start)
4. **Feature Engineering:** Compute price lags, rolling statistics, seasonal flags, and temporal features
5. **Output:** Panel features CSV file (`data/features/panel_features.csv`)

**[Figure 3: Data Pipeline Flowchart]**

*Caption: The data pipeline processes data from multiple sources through cleaning, merging, and feature engineering stages to produce the final panel feature dataset.*

### 3.7.3 Model Training Pipeline

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

### 3.7.4 Dashboard Application

The dashboard application (`src/dashboard/app.py`) provides an interactive user interface:

1. **Data Loading:** Load panel data, trained model, config, and evaluation results
2. **Forecast Generation:** Recursive multi-step forecasting using the trained model
3. **Confidence Intervals:** Bootstrap-based uncertainty estimation
4. **Visualization:** Four-tab interface (Overview, Seasonality, Drivers, Performance)
5. **User Interaction:** County selection, forecast horizon adjustment

---

# CHAPTER 4: RESULTS AND DISCUSSION

## 4.1 Introduction

This chapter presents the results of the maize price forecasting system, including model performance evaluation, feature importance analysis, seasonal pattern analysis, and the dashboard interface. The results are discussed in the context of the research objectives and compared with findings from the literature.

## 4.2 Model Performance Results

### 4.2.1 Overall Results Across All Folds

Table 4 presents the aggregate performance of the three models evaluated across all 5 folds of the expanding window cross-validation.

**Table 4: Overall Model Performance Comparison**

| Model | MASE | Dir Acc | MAE (KES) | sMAPE |
|-------|:---:|:-------:|:---------:|:-----:|
| Persistence | 0.631 | 0.0% | 2.89 | 7.15% |
| Pooled XGBoost | 0.322 | 75.5% | 2.07 | 5.10% |
| Fine-Tuned XGBoost | 0.322 | 75.5% | 2.07 | 5.10% |

Key observations:

1. **All models beat persistence:** Both XGBoost models achieve MASE values well below 1 (0.322), indicating that they reduce forecast error by approximately 68% compared to the naive "no change" forecast.

2. **Directional accuracy is strong:** The XGBoost models correctly predict the direction of price change 75.5% of the time, compared to 0% for persistence (since persistence always predicts no change). This is a practically significant result, as directional accuracy is critical for trading and marketing decisions.

3. **Fine-tuning matches pooled performance:** The fine-tuned XGBoost achieves identical aggregate performance to the pooled model. This suggests that the county dummies in the pooled model already capture county-specific patterns effectively, leaving little room for improvement through per-county specialization.

4. **MAE is modest:** The average error of 2.07 KES on prices ranging from 28-52 KES represents approximately 4-7% error, which is reasonable for agricultural price forecasting.

### 4.2.2 Per-County Performance

Table 5 shows the best model performance for each target county based on MASE.

**Table 5: Per-County Best Model Performance**

| County | Model | MASE | Dir Acc | MAE (KES) |
|--------|-------|:---:|:-------:|:---------:|
| Kiambu | Fine-Tuned XGBoost | 0.334 | 78.1% | 2.15 |
| Kirinyaga | Fine-Tuned XGBoost | 0.236 | 77.6% | 1.51 |
| Mombasa | Fine-Tuned XGBoost | 0.298 | 62.5% | 1.89 |
| Nairobi | Fine-Tuned XGBoost | 0.379 | 74.2% | 2.43 |
| Uasin-Gishu | Fine-Tuned XGBoost | 0.338 | 74.8% | 2.17 |

Key observations:

1. **Kirinyaga shows the best performance:** With a MASE of 0.236 and MAE of 1.51 KES, Kirinyaga has the most predictable price patterns, likely due to its established role as a major maize-producing region with consistent market dynamics.

2. **Mombasa has lower directional accuracy:** Mombasa's 62.5% directional accuracy, while still better than random (50%), is notably lower than other counties. This may reflect Mombasa's unique position as a coastal import-dependent market with different price drivers.

3. **Nairobi has the highest MAE:** At 2.43 KES, Nairobi's MAE is the highest among the target counties, reflecting the greater price volatility and complexity of the capital city's market.

### 4.2.3 Performance Across Folds (Temporal Stability)

Table 6 shows the pooled XGBoost performance across the 5 expanding window folds.

**Table 6: Performance Across Folds for Pooled XGBoost**

| Fold | Training Weeks | Test Period | MASE | Dir Acc | MAE (KES) |
|------|:-------------:|-------------|:---:|:-------:|:---------:|
| 0 | 124 | Oct 2023 – Mar 2024 | 0.435 | 67.3% | 2.79 |
| 1 | 144 | Mar 2024 – Aug 2024 | 0.401 | 80.8% | 2.47 |
| 2 | 164 | Aug 2024 – Jan 2025 | 0.322 | 80.3% | 2.00 |
| 3 | 184 | Jan 2025 – May 2025 | 0.134 | 62.4% | 0.80 |
| 4 | 204 | May 2025 – Oct 2025 | 0.167 | 80.1% | 1.14 |

Key observations:

1. **Improving performance over time:** MASE shows a general decreasing trend from Fold 0 (0.435) to Fold 4 (0.167), indicating that the model performs better when trained on more data.

2. **Best performance in later folds:** Folds 3 and 4 show substantially lower MAE and MASE values, likely due to both the larger training dataset and possibly more stable market conditions in the 2025 period.

3. **Directional accuracy remains strong:** Dir Acc stays above 62% across all folds, confirming that the model consistently provides value for directional predictions.

**[Figure 4: Model Performance Comparison Bar Charts]**

*Caption: Bar charts comparing MASE, Dir Acc, and MAE for persistence, pooled XGBoost, and fine-tuned XGBoost models.*

## 4.3 Feature Importance Analysis

Feature importance analysis reveals which variables have the greatest influence on the model's predictions. Figure 5 shows the top 15 features based on the XGBoost model's built-in importance scores (based on the frequency of feature usage across all trees).

**[Figure 5: Feature Importance (Top 15)]**

*Caption: The top 15 features ranked by XGBoost importance scores. Price-change features dominate the top ranks, followed by county dummies and economic indicators.*

The top features are:

1. **price_change_ma_4w** (4-week moving average of price changes) — This feature captures the momentum of price movements, helping the model identify whether prices are in an uptrend, downtrend, or stable period.

2. **price_change_lag_1w** (last week's price change) — The most recent week's price change is highly predictive of the next week's change, reflecting short-term price momentum.

3. **County dummies** (e.g., c_Kiambu, c_Nyeri, c_Kilifi) — County indicators appear prominently, confirming that county-specific price levels and dynamics are important determinants of price changes.

4. **Economic indicators** (CPI, USD/KES rate, inflation) — These macroeconomic variables capture the broader economic context affecting input costs and purchasing power.

5. **Temporal features** (year, days_from_start) — Time-trend features capture long-term price trends driven by inflation and structural changes in the maize market.

6. **Weather features** (temperature, rainfall) — While present, weather features rank lower than economic and price-momentum features, suggesting that weather effects on weekly price changes are less direct than market dynamics.

## 4.4 Seasonal Pattern Analysis

The seasonal analysis reveals distinct monthly patterns in maize prices across the target counties.

**[Figure 6: Monthly Seasonal Patterns Across Target Counties]**

*Caption: Monthly average maize prices for Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu counties showing seasonal patterns.*

Key observations:

1. **Price peaks:** Most counties show price peaks around June-July, corresponding to the dry season when supply from the previous harvest is diminishing and the new harvest is not yet available.

2. **Price troughs:** Prices typically bottom out around January-February and October-November, following the short rains and long rains harvests respectively.

3. **Regional variations:** Uasin-Gishu, a major maize-producing region in the Rift Valley, shows consistently lower prices than Nairobi and Mombasa, reflecting lower transportation costs and proximity to production areas.

4. **Price range:** Monthly average prices range from approximately 38 KES (Uasin-Gishu, low season) to 54 KES (Kirinyaga, peak season), demonstrating the significant seasonal price variation that farmers and traders can exploit.

## 4.5 Dashboard Interface

The Streamlit dashboard provides four analysis tabs that address different stakeholder needs.

**[Figure 7: Dashboard Overview Tab Screenshot]**

*Caption: The Overview tab shows the current price metrics, historical price chart with forecast and confidence bands, and the multi-week forecast table.*

**[Figure 8: Dashboard Seasonality Tab Screenshot]**

*Caption: The Seasonality tab displays monthly average price patterns, year-over-year comparisons, and descriptive statistics.*

**[Figure 9: Dashboard Drivers Tab Screenshot]**

*Caption: The Drivers tab presents feature importance analysis, current feature values, and scatter plots of key economic drivers versus price.*

**[Figure 10: Dashboard Performance Tab Screenshot]**

*Caption: The Performance tab shows per-county model metrics (MASE, Dir Acc, MAE, sMAPE), best model selection, and comparative bar charts.*

The dashboard is designed to answer three types of questions:

- **Predictive (Overview tab):** "What will maize prices be next month?"
- **Descriptive (Seasonality tab):** "What were the historical price patterns and seasonal trends?"
- **Diagnostic (Drivers and Performance tabs):** "Why are prices changing and how reliable are the forecasts?"

## 4.6 Discussion

The results demonstrate that the machine learning-based maize price forecasting system achieves its primary objective of providing accurate, county-level price predictions. Several findings merit discussion:

**Pooled Modeling Advantage:** The pooled XGBoost model's strong performance across all counties, including those with limited historical data, validates the approach of training a single model on multi-county data. This is consistent with the findings of Pan et al. (2022) on transfer learning for agricultural price forecasting.

**Δ-Price Target Effectiveness:** The MASE metric clearly demonstrates that the model improves upon the persistence baseline by approximately 68%. This is a more meaningful and rigorous evaluation than traditional R²-based metrics, which are inappropriate for time series data (Hyndman & Athanasopoulos, 2021).

**Fine-Tuning Results:** The observation that per-county fine-tuning does not improve upon the pooled model suggests that the county dummies in the pooled model effectively capture county-specific patterns. This is a useful finding for future implementations, as it suggests that the pooled model alone may be sufficient.

**Feature Importance Insights:** The dominance of price-momentum features (price_change_ma_4w, price_change_lag_1w) indicates that short-term price dynamics are the most important predictors of future price changes. This aligns with the efficient market hypothesis, which suggests that most available information is already reflected in current prices.

**Practical Utility:** With a directional accuracy of 75.5%, the model provides significant value for stakeholders making decisions based on expected price movements. Even when the magnitude prediction is imperfect, correct directional predictions enable better timing of sales and purchases.

---

# CHAPTER 5: CONCLUSION AND RECOMMENDATIONS

## 5.1 Conclusion

This project successfully developed and evaluated a machine learning-based maize price forecasting system for Kenyan counties. The system addresses a critical gap in agricultural market information by providing automated, county-level price forecasts that are currently unavailable through existing systems.

The key achievements of the project include:

1. **Data Integration:** Successfully integrated multiple data sources (KAMIS, AgriBORA, weather, economic indicators) into a comprehensive panel dataset covering 46 counties over 5 years.

2. **Δ-Price Forecasting Framework:** Implemented a rigorous forecasting framework using Δ-price as the target variable, MASE as the primary evaluation metric, and expanding window cross-validation for robust performance assessment.

3. **Pooled XGBoost Model:** Developed a pooled XGBoost model that achieves a MASE of 0.322 (68% better than persistence), a directional accuracy of 75.5%, and a MAE of 2.07 KES across five target counties.

4. **Interactive Dashboard:** Built a comprehensive Streamlit dashboard with four analysis tabs (Overview, Seasonality, Drivers, Performance) that addresses predictive, descriptive, and diagnostic questions.

5. **Cloud Deployment:** Configured the system for deployment on Streamlit Cloud, enabling anytime, anywhere access for stakeholders.

## 5.2 Recommendations

Based on the project findings, the following recommendations are made:

**For System Users:**
- Farmers should use the directional accuracy information (75.5% correct) to inform marketing timing decisions
- Traders should use the 8-week forecasts with confidence intervals for inventory planning
- Policymakers should use the system as a complement to existing early warning systems

**For Future Development:**
- Integrate real-time data feeds for automated weekly model updates
- Expand the dashboard to include all 47 counties as data quality improves
- Add user accounts and customization features for personalized alerts
- Develop a mobile application for wider accessibility

**For Data Collection Agencies (KAMIS, AgriBORA):**
- Improve data collection frequency and consistency across all counties
- Make historical data more readily accessible for research and development
- Consider incorporating additional variables such as production estimates, import volumes, and road infrastructure data

## 5.3 Future Work

Several directions for future work have been identified:

**Model Improvements:**
- Experiment with deep learning approaches (LSTM, Transformer) as more historical data becomes available
- Implement probabilistic forecasting using quantile regression or Monte Carlo dropout
- Incorporate satellite-based crop yield estimates and vegetation indices
- Develop ensemble methods combining XGBoost with other model types

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

Ministry of Agriculture, Livestock, Fisheries and Cooperatives. (2022). *Agricultural Sector Transformation and Growth Strategy 2019-2029 Annual Report*. Nairobi: Government of Kenya.

Pan, Y., Li, Z., & Zhang, Y. (2022). Transfer learning for agricultural price forecasting: A case study on vegetable prices in China. *Computers and Electronics in Agriculture*, 193, 106-118.

Wang, J., Liu, Z., & Chen, X. (2020). Corn price prediction in the United States using gradient boosting machines. *Agricultural Economics*, 51(6), 849-863.

World Bank. (2022). *Machine Learning for Agricultural Price Forecasting in South Asia: Technical Report*. Washington, DC: World Bank Group.

Xiong, T., Li, C., & Bao, Y. (2018). A comparison of machine learning methods for agricultural commodity price forecasting. *Neural Computing and Applications*, 30(5), 1425-1440.

---

# APPENDICES

## Appendix A: Budget and Resources

**Table 7: Budget Estimates**

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

**Table 8: Work Breakdown Structure**

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

**[Figure 11: Gantt Chart - Project Schedule]**

*Caption: Gantt chart showing the project timeline with 8 main tasks spanning 17 weeks.*

## Appendix C: System Code Listings

The complete source code for the maize price forecasting system is available in the GitHub repository. Key files include:

1. `src/data/clean.py` — Data cleaning and preprocessing
2. `src/data/features.py` — Feature engineering
3. `src/models/train.py` — Model training and evaluation
4. `src/dashboard/app.py` — Streamlit dashboard
5. `streamlit_app.py` — Streamlit Cloud entry point
6. `run.py` — Pipeline runner
7. `requirements.txt` — Python dependencies

The codebase follows Python best practices with modular design, comprehensive documentation, and consistent coding standards.
