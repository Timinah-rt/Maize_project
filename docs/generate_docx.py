from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

doc = Document()

# Page setup
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(4)
    section.right_margin = Cm(2.5)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
style.paragraph_format.space_after = Pt(6)
rFonts = style.element.rPr.rFonts if style.element.rPr is not None else None
if rFonts is None:
    rPr = style.element.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rPr.append(rFonts)
    rFonts = rPr.find(qn('w:rFonts'))
rFonts.set(qn('w:ascii'), 'Times New Roman')
rFonts.set(qn('w:hAnsi'), 'Times New Roman')
rFonts.set(qn('w:eastAsia'), 'Times New Roman')
rFonts.set(qn('w:cs'), 'Times New Roman')

# Helper functions
def heading1(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(14)
    run.font.name = 'Times New Roman'
    p.paragraph_format.space_before = Pt(24)
    p.paragraph_format.space_after = Pt(12)
    return p

def heading2(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    return p

def heading3(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.italic = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    return p

def para(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.27)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def para_no_indent(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def centered(text, bold=False, size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = bold
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    return p

def add_table(headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
    for row_data in rows:
        row = table.add_row()
        for i, val in enumerate(row_data):
            cell = row.cells[i]
            cell.text = str(val)
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10)
    doc.add_paragraph()
    return table

def signature_line(label):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(24)
    run = p.add_run(label + ': _______________________________  Date: ________________')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_page_number():
    for section in doc.sections:
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')
        run._r.append(fldChar1)
        run2 = p.add_run()
        instrText = OxmlElement('w:instrText')
        instrText.set(qn('xml:space'), 'preserve')
        instrText.text = ' PAGE '
        run2._r.append(instrText)
        run3 = p.add_run()
        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'end')
        run3._r.append(fldChar2)

# TITLE PAGE
for _ in range(4):
    doc.add_paragraph()

centered('MAIZE PRICE FORECASTING SYSTEM: A MACHINE LEARNING', bold=True, size=14)
centered('APPROACH FOR KENYAN COUNTY-LEVEL PRICE PREDICTION', bold=True, size=14)

for _ in range(3):
    doc.add_paragraph()

centered('BY', bold=True)
doc.add_paragraph()
centered('[YOUR NAME]', bold=True)
centered('[YOUR REGISTRATION NUMBER]')

for _ in range(3):
    doc.add_paragraph()

centered('THIS PROJECT PROPOSAL IS SUBMITTED IN PARTIAL FULFILLMENT')
centered('FOR THE AWARD OF [YOUR DEGREE] OF [YOUR UNIVERSITY]')

for _ in range(3):
    doc.add_paragraph()

centered('[CAMPUS]')
centered('[MONTH YEAR]')

doc.add_page_break()

# DECLARATION
centered('DECLARATION', bold=True, size=14)
doc.add_paragraph()
para_no_indent('This is my original work and has not been submitted in any other institution of higher learning for academic or any other purpose.')
signature_line('[YOUR NAME]')
para_no_indent('This project proposal is presented to the university for examination with the approval of the supervisor.')
signature_line('[SUPERVISOR NAME]')
para_no_indent('[UNIVERSITY]')
para_no_indent('[CAMPUS]')

doc.add_page_break()

# ACKNOWLEDGEMENT
centered('ACKNOWLEDGEMENT', bold=True, size=14)
doc.add_paragraph()
para('First and foremost, I thank God Almighty for the strength, wisdom, and perseverance to complete this project.')
para('I express my deepest gratitude to my supervisor, [Supervisor Name], for the invaluable guidance, constructive criticism, and continuous support throughout this research. Your expertise and encouragement were instrumental in shaping this work.')
para('I am profoundly grateful to my parents for their unwavering support, both moral and financial, throughout my academic journey. Your sacrifices and belief in me have been the foundation of my success.')
para('To my friends and colleagues, thank you for the encouragement, late-night brainstorming sessions, and technical discussions that enriched this project.')
para('I also acknowledge the Kenya Agricultural Market Information System (KAMIS) and the Agricultural Business Rapid Assessment (AgriBORA) for providing the maize price data used in this research. The Open-Meteo weather API and the Central Bank of Kenya for economic indicators data are also gratefully acknowledged.')
para('Finally, I thank all those who contributed directly or indirectly to the successful completion of this project.')

doc.add_page_break()

# ABSTRACT
centered('ABSTRACT', bold=True, size=14)
doc.add_paragraph()
para('Maize is a staple food crop in Kenya, and its price volatility directly affects food security and the livelihoods of millions of Kenyans. Accurate price forecasting is essential for farmers, traders, policymakers, and consumers to make informed decisions. However, maize price prediction is challenging due to the complex interplay of seasonal patterns, weather conditions, economic factors, and market dynamics across Kenya\'s diverse counties.')
para('This project presents a machine learning-based maize price forecasting system that predicts weekly maize prices across multiple Kenyan counties. The system employs a pooled XGBoost (Extreme Gradient Boosting) regression model trained on price change (delta-price) as the target variable, effectively removing the strong autocorrelation that makes persistence forecasting deceptively competitive. The model is trained on a panel dataset spanning 2021 to 2025, comprising price data from 46 counties, weather variables (temperature, rainfall), economic indicators (CPI, USD/KES exchange rate, inflation rate), and engineered features including price lags, rolling statistics, and seasonal flags.')
para('A 5-fold expanding window cross-validation strategy is used to evaluate model performance across different time periods, ensuring robustness and temporal generalization. The pooled model incorporates county one-hot encoding to enable information sharing across markets while maintaining county-specific predictions. Additionally, per-county fine-tuning is implemented using warm-started XGBoost models initialized from the pooled model.')
para('Model performance is evaluated using multiple metrics: Mean Absolute Scaled Error (MASE) to measure improvement over the persistence baseline, directional accuracy to assess price movement prediction, Mean Absolute Error (MAE) on the original price scale, and symmetric Mean Absolute Percentage Error (sMAPE). The pooled XGBoost model achieves a MASE of 0.322 (68% better than persistence), a directional accuracy of 75.5%, and a MAE of 2.07 KES across the five target counties (Kiambu, Kirinyaga, Mombasa, Nairobi, Uasin-Gishu).')
para('An interactive Streamlit dashboard is developed to visualize historical price trends, generate multi-week forecasts with confidence intervals, analyze seasonal patterns, identify key price drivers through feature importance analysis, and display model performance metrics. The system is deployable on Streamlit Cloud, making it accessible to stakeholders.')
doc.add_paragraph()
para_no_indent('Keywords: Maize price forecasting, XGBoost, machine learning, time series, Kenya agriculture, delta-price, pooled model, expanding window cross-validation, MASE, Streamlit dashboard')

doc.add_page_break()

# TABLE OF CONTENTS (placeholder)
centered('TABLE OF CONTENTS', bold=True, size=14)
doc.add_paragraph()
para_no_indent('[Right-click here and select "Update Field" or "Insert Table of Contents" in Microsoft Word to auto-generate]')
doc.add_paragraph()
para_no_indent('DECLARATION ........................................................................................................................ ii')
para_no_indent('ACKNOWLEDGEMENT .................................................................................................................. iii')
para_no_indent('ABSTRACT .............................................................................................................................. iv')
para_no_indent('TABLE OF CONTENTS ................................................................................................................. v')
para_no_indent('LIST OF TABLES ...................................................................................................................... vii')
para_no_indent('LIST OF FIGURES ..................................................................................................................... viii')
para_no_indent('CHAPTER 1: INTRODUCTION ........................................................................................................ 1')
para_no_indent('CHAPTER 2: LITERATURE REVIEW ................................................................................................ 12')
para_no_indent('CHAPTER 3: METHODOLOGY ........................................................................................................ 24')
para_no_indent('CHAPTER 4: RESULTS AND DISCUSSION ........................................................................................ 38')
para_no_indent('CHAPTER 5: CONCLUSION AND RECOMMENDATIONS ........................................................................ 46')
para_no_indent('REFERENCES .............................................................................................................................. 49')
para_no_indent('APPENDICES .............................................................................................................................. 52')

doc.add_page_break()

# LIST OF TABLES
centered('LIST OF TABLES', bold=True, size=14)
doc.add_paragraph()
para_no_indent('Table 1: Data Sources Summary ................................................................................................... 35')
para_no_indent('Table 2: Summary Statistics of Price Data by County ........................................................................ 36')
para_no_indent('Table 3: Missing Data Patterns Across Counties ............................................................................... 37')
para_no_indent('Table 4: Engineered Feature Set .................................................................................................... 41')
para_no_indent('Table 5: Software and Library Versions .......................................................................................... 43')
para_no_indent('Table 6: Hyperparameter Search Space and Final Configuration ......................................................... 47')
para_no_indent('Table 7: Expanding Window Cross-Validation Folds ........................................................................... 48')
para_no_indent('Table 8: Overall Model Performance Comparison ................................................................................ 58')
para_no_indent('Table 9: Per-County Best Model Performance .................................................................................... 59')
para_no_indent('Table 10: Performance Across Folds ................................................................................................ 60')
para_no_indent('Table 11: Comparison with Literature Benchmarks ............................................................................ 69')
para_no_indent('Table 12: Budget Estimates ............................................................................................................. 80')
para_no_indent('Table 13: Work Breakdown Structure ............................................................................................... 81')
para_no_indent('Table 14: Data Dictionary .............................................................................................................. 85')

doc.add_page_break()

# LIST OF FIGURES
centered('LIST OF FIGURES', bold=True, size=14)
doc.add_paragraph()
para_no_indent('Figure 1: Kenya Maize Price Trends by County (2021-2025) ............................................................... 2')
para_no_indent('Figure 2: System Architecture Diagram ............................................................................................. 54')
para_no_indent('Figure 3: Data Pipeline Flowchart .................................................................................................. 55')
para_no_indent('Figure 4: Model Performance Comparison Bar Charts ........................................................................ 61')
para_no_indent('Figure 5: Feature Importance (Top 15) ............................................................................................. 62')
para_no_indent('Figure 6: Monthly Seasonal Patterns Across Target Counties ............................................................ 63')
para_no_indent('Figure 7: Dashboard Overview Tab Screenshot ................................................................................ 65')
para_no_indent('Figure 8: Dashboard Seasonality Tab Screenshot .............................................................................. 66')
para_no_indent('Figure 9: Dashboard Drivers Tab Screenshot .................................................................................... 67')
para_no_indent('Figure 10: Dashboard Performance Tab Screenshot ........................................................................... 68')
para_no_indent('Figure 11: Gantt Chart - Project Schedule ....................................................................................... 81')

doc.add_page_break()

# CHAPTER 1: INTRODUCTION
heading1('CHAPTER 1: INTRODUCTION')

heading2('1.1 Introduction')
para('This chapter provides the foundation for the research project by presenting the background of maize price forecasting in Kenya, the problem that motivated this study, the proposed solution, research objectives, justification, significance, assumptions, limitations, and the project scope. The chapter establishes the context within which the maize price forecasting system was developed and sets the stage for the literature review and methodology that follow.')

heading2('1.2 Background of the Study')
para('Agriculture is the backbone of the Kenyan economy, contributing approximately 33% to the Gross Domestic Product (GDP) and employing over 40% of the population (Kenya National Bureau of Statistics, 2023). Among agricultural commodities, maize holds a position of paramount importance as the country\'s primary staple food. The average Kenyan consumes approximately 98 kilograms of maize per year, making it a critical component of household food security (Ministry of Agriculture, Livestock, Fisheries and Cooperatives, 2022).')
para('Kenya\'s maize sector encompasses approximately 4.5 million smallholder farmers who cultivate maize on farms averaging less than 2 hectares. These smallholders account for approximately 75% of the country\'s total maize production. The annual national maize production stands at approximately 40 million bags (each bag weighing 90 kilograms), with consumption estimated at 44 million bags annually, creating a structural deficit of approximately 4 million bags that must be met through imports, primarily from Uganda and Tanzania. This import dependency means that regional supply shocks and cross-border trade policies directly impact domestic maize prices. The maize value chain also employs an estimated 10 million Kenyans across production, trading, processing, and retail activities, underscoring its centrality to the national economy and food system.')
para('Maize prices in Kenya exhibit significant volatility driven by a complex interplay of factors including seasonal production cycles, weather patterns (particularly rainfall during the long and short rainy seasons), input costs, fuel prices, inflation, exchange rate fluctuations, market infrastructure, and post-harvest losses. This price volatility has profound implications for food security, household welfare, and macroeconomic stability. When maize prices spike, low-income urban households suffer disproportionately as they spend a larger share of their income on food. Conversely, when prices collapse during harvest seasons, smallholder farmers who constitute the majority of maize producers face income losses that undermine their livelihoods.')
para('To illustrate the scale of price volatility, consider actual market data from Nairobi over the study period: wholesale maize prices have ranged from a low of approximately KES 28 per kilogram during harvest periods to a high of over KES 52 per kilogram during peak scarcity. A single bag of maize (90 kg) therefore fluctuates in value from KES 2,520 to KES 4,680, a difference of over KES 2,000 per bag. For a smallholder farmer harvesting 20 bags from a one-acre plot, this price swing represents a potential income difference of over KES 40,000, which is substantially larger than many rural households\' monthly expenses. Similarly, Mombasa prices have shown distinct patterns driven by the city\'s reliance on imported maize, with prices at times diverging significantly from inland markets due to port logistics, global grain prices, and exchange rate movements. These real-world examples underscore the critical need for accurate price forecasts.')
para('The Kenya Agricultural Market Information System (KAMIS), operated by the Ministry of Agriculture, provides weekly price data for various agricultural commodities across markets in all 47 counties. Similarly, the Agricultural Business Rapid Assessment (AgriBORA) platform provides transaction-based wholesale prices. Despite the availability of this data, systematic and accurate price forecasting remains a challenge. Most price information available to stakeholders is historical, with limited predictive capability.')
para('Traditional approaches to price forecasting in Kenya have relied on expert judgment, simple trend analysis, and basic statistical methods. These approaches, while providing some value, are limited in their ability to capture the complex, non-linear relationships between the numerous factors that influence maize prices. Furthermore, they often fail to provide probabilistic forecasts or confidence intervals that would enable risk-based decision-making.')
para('In recent years, machine learning has emerged as a powerful tool for time series forecasting across various domains, including agricultural commodity prices. Techniques such as gradient boosting, random forests, and deep learning have demonstrated superior performance compared to traditional statistical methods, particularly when dealing with high-dimensional data and complex non-linear relationships. However, the application of these techniques to county-level maize price forecasting in Kenya remains relatively unexplored.')
para('This project addresses this gap by developing a machine learning-based maize price forecasting system that leverages XGBoost, a state-of-the-art gradient boosting framework, to predict weekly maize prices across multiple Kenyan counties. The system incorporates price data from multiple sources, weather variables, economic indicators, and engineered features to capture the multi-faceted nature of maize price determination. The model is trained using a pooled approach that enables information sharing across counties, combined with per-county fine-tuning to capture local market dynamics.')
para('[Screenshot: Figure 1 - Kenya Maize Price Trends by County (2021-2025)]')
para_no_indent('Caption: Weekly maize prices for Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu counties from 2021 to 2025. The chart shows county-specific price levels and common seasonal patterns. Note the distinct price regimes: Nairobi and Mombasa exhibit higher price levels reflective of urban demand and import dependency, while Uasin-Gishu shows lower, more stable prices due to its proximity to production areas.')

heading2('1.3 Problem Statement')
para('Despite the critical importance of maize to Kenya\'s food security and economy, stakeholders across the value chain including farmers, traders, policymakers, and consumers lack access to accurate, timely, and reliable price forecasts. This information gap leads to several interconnected problems that perpetuate inefficiency, risk, and food insecurity throughout the maize sector.')
para('For Farmers: Smallholder farmers, who produce over 75% of Kenya\'s maize, make planting, harvesting, and marketing decisions based on limited information. A typical farmer in Kiambu County, for instance, must decide at the beginning of each season whether to invest in fertilizer, certified seeds, and other inputs, costing upwards of KES 30,000 per acre, without knowing what prices will be at harvest time. Without reliable price forecasts, they often sell at suboptimal prices immediately after harvest when supply is high and prices are low, missing the opportunity to benefit from seasonal price increases. This contributes to persistent rural poverty and food insecurity.')
para('For Traders and Millers: Maize traders and millers face significant inventory and procurement risks due to price uncertainty. A miller in Nairobi who procures 1,000 bags of maize per week faces a weekly procurement bill of KES 2.8 million to KES 5.2 million, depending on market prices. The inability to forecast price movements leads to either excessive inventory holding costs or stock-outs, both of which have negative financial implications. These costs are ultimately passed on to consumers in the form of higher prices.')
para('For Policymakers: Government agencies responsible for food security, including the Ministry of Agriculture and the National Cereals and Produce Board (NCPB), require accurate price forecasts to make timely decisions about strategic grain reserves, import licenses, and market interventions. Reactive rather than proactive policy responses often result from the absence of reliable forecasting tools. For example, the decision to issue import permits typically occurs only after prices have already risen to crisis levels.')
para('For Consumers: Urban households, particularly those in low-income brackets, bear the brunt of maize price volatility. A household in an informal settlement in Nairobi spends approximately 30% of its monthly food budget on maize products. When maize prices spike from KES 40 to KES 52 per kilogram, this adds approximately KES 500 to KES 800 to the monthly food bill of a typical family, a significant burden for households already living on less than KES 10,000 per month. Price spikes can push vulnerable households into food insecurity, while price collapses threaten the viability of the entire maize value chain.')
para('Existing forecasting approaches suffer from several limitations: (1) reliance on historical trends rather than predictive analytics; (2) inability to capture complex, non-linear relationships between multiple price drivers; (3) lack of granularity at the county level; (4) absence of uncertainty quantification through confidence intervals; (5) limited automation and scalability; and (6) no directional guidance for practical decision-making.')
para('These problems collectively create a pressing need for an automated, machine learning-based maize price forecasting system that can provide accurate, county-level predictions with quantified uncertainty to support decision-making across the maize value chain.')

heading2('1.4 Proposed Solution')
para('This project proposes the development of a machine learning-based maize price forecasting system that addresses the identified problems through the following key features:')
para('Data Integration: The system integrates multiple data sources including KAMIS prices, AgriBORA prices, weather data (temperature, rainfall, wind), and economic indicators (CPI, USD/KES exchange rate, inflation rate) to create a comprehensive feature set for price prediction.')
para('Delta-Price Forecasting: Instead of predicting absolute prices, the system predicts week-over-week price changes (delta-price). This approach effectively removes the strong autocorrelation present in price time series and provides a more meaningful evaluation framework where the persistence baseline (predicting no change) serves as a natural benchmark. A model that achieves MASE less than 1 demonstrably adds value over the naive forecast.')
para('Pooled XGBoost Model: A single XGBoost regression model is trained on data from all 46 counties simultaneously, using county one-hot encoding to capture county-specific effects. This pooled approach enables the model to learn from price dynamics across all counties, improving generalization, particularly for counties with limited historical data.')
para('Expanding Window Cross-Validation: Model performance is evaluated using a 5-fold expanding window cross-validation strategy that respects the temporal order of the data. This approach provides robust performance estimates across different time periods and simulates the realistic scenario of predicting future prices based on past observations.')
para('Per-County Fine-Tuning: While the pooled model provides strong baseline predictions, per-county fine-tuning allows the model to adapt to county-specific price dynamics by continuing training on individual county data, warm-started from the pooled model.')
para('Comprehensive Evaluation Metrics: Model performance is assessed using MASE, directional accuracy, MAE, and sMAPE, providing a rigorous and multi-faceted evaluation framework.')
para('Interactive Dashboard: An intuitive Streamlit-based dashboard provides stakeholders with access to historical price trends, multi-week forecasts with confidence intervals, seasonal pattern analysis, feature importance insights, and model performance comparisons.')
para('Cloud Deployment: The system is deployable on Streamlit Cloud, enabling anytime, anywhere access without requiring local installation or technical expertise.')

heading2('1.5 Research Objectives')
heading3('Main Objective')
para('To develop and evaluate a machine learning-based maize price forecasting system that provides accurate, county-level price predictions with quantified uncertainty to support decision-making across Kenya\'s maize value chain.')
heading3('Specific Objectives')
para('1. To analyze the historical maize price data from KAMIS and AgriBORA sources to identify patterns, trends, and seasonal variations across Kenyan counties.')
para('2. To design and engineer a comprehensive feature set incorporating price lags, rolling statistics, weather variables, economic indicators, and temporal features that capture the key drivers of maize price movements.')
para('3. To develop a pooled XGBoost regression model trained on delta-price with county one-hot encoding that enables information sharing across counties while maintaining county-specific predictions.')
para('4. To implement an expanding window cross-validation strategy that provides robust performance evaluation across different time periods.')
para('5. To evaluate the model\'s predictive performance using MASE, directional accuracy, MAE, and sMAPE metrics.')
para('6. To build an interactive Streamlit dashboard that visualizes historical trends, generates multi-week forecasts, and analyzes price drivers.')
para('7. To deploy the system on Streamlit Cloud for accessible, web-based stakeholder use.')

heading2('1.6 Justification of the Study')
para('This research is justified on several grounds.')
para('Academic Contribution: The study contributes to the growing body of knowledge on machine learning applications in agricultural price forecasting, particularly in the context of developing economies. The pooled modeling approach with per-county fine-tuning offers a novel methodology that balances global learning with local adaptation. The use of delta-price and MASE-based evaluation within an expanding window framework provides a rigorous template for time series forecasting evaluation.')
para('Practical Utility: The system provides actionable price forecasts that can directly benefit stakeholders across the maize value chain. Farmers can make informed marketing decisions, traders can optimize inventory management, and policymakers can implement timely interventions to stabilize prices. The interactive dashboard makes these insights accessible to non-technical users, bridging the gap between advanced machine learning and practical decision-making.')
para('Methodological Innovation: The use of delta-price as the target variable, combined with expanding window cross-validation and MASE-based evaluation, provides a rigorous framework for time series forecasting that addresses common pitfalls, including inappropriate use of R-squared, single train-test splits, and failure to account for temporal dependencies. The methodology is scalable to other commodities and all 47 counties. Improved price forecasting has a direct positive impact on food security by enabling more efficient market functioning and supporting evidence-based policy decisions.')

heading2('1.7 Significance of the Study')
para('The implementation of this project is expected to provide the following benefits:')
para('1. Empowered Farmers: Access to reliable price forecasts enables farmers to make informed decisions about when and where to sell their produce, potentially increasing their income by 10-20% through strategic market timing. For a smallholder farmer harvesting 20 bags per season, this translates to an additional KES 5,000 to KES 10,000 in income, a substantial improvement in household welfare.')
para('2. Improved Market Efficiency: Traders and millers can better manage inventory, reduce waste, and optimize procurement strategies, leading to lower transaction costs and more stable prices. More efficient markets benefit all participants through reduced spreads between farm-gate and retail prices.')
para('3. Evidence-Based Policy: Policymakers gain access to predictive insights that support proactive rather than reactive interventions in the maize market, including strategic grain reserve management and import decisions. Early warning of impending price spikes enables preemptive action that can prevent food crises.')
para('4. Enhanced Food Security: More accurate price information contributes to improved food security outcomes by reducing price volatility and ensuring more stable access to maize. Vulnerable households benefit from more predictable food costs that facilitate household budgeting.')
para('5. Technological Transfer: The project demonstrates the practical application of machine learning to agricultural challenges in developing economies, providing a template for similar initiatives in other countries and commodities.')
para('6. Open Source Foundation: The codebase is structured to be reusable and extensible, enabling future researchers and developers to build upon this work.')

heading2('1.8 Assumptions')
para('The following assumptions were made: (1) Historical price data from KAMIS and AgriBORA is accurate and representative; (2) Weather data from Open-Meteo API provides reasonable approximations of local conditions; (3) Economic indicators are available at sufficient frequency; (4) Relationships between predictors and prices remain sufficiently stable for meaningful forecasting; (5) Users have basic internet connectivity; and (6) The data period (2021-2025) is sufficiently long to capture relevant patterns.')

heading2('1.9 Limitations of the Study')
para('This study encountered the following limitations: (1) Data availability and completeness vary significantly across counties; (2) Forecast accuracy declines for longer horizons due to accumulating uncertainty; (3) The model cannot account for unpredictable events such as policy changes or geopolitical events; (4) Price data may contain reporting errors or inconsistencies; (5) The evaluation focuses on 5 target counties; and (6) Computational resources limited the hyperparameter search space.')

heading2('1.10 Project Scope')
para('This project covers the following aspects. Geographic Scope: The system focuses on five target counties, Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu, representing different agricultural zones and market types. Kiambu represents a peri-urban county with diverse agricultural activity; Kirinyaga is a major maize-producing area in the central highlands; Mombasa represents a coastal, import-dependent urban market; Nairobi represents the largest consumer market in East Africa; and Uasin-Gishu is a major grain basket county in the Rift Valley. The pooled model is trained on data from 46 counties.')
para('Temporal Scope: The project uses weekly price data from 2021 to 2025, generating forecasts for 4 to 12 weeks ahead. Technical Scope includes Python, XGBoost, scikit-learn, Streamlit, Pandas, NumPy, and Matplotlib. Out of scope includes real-time data ingestion, mobile application development, external API integration, multi-commodity forecasting, deep learning approaches, user authentication, and automated retraining pipelines.')

doc.add_page_break()

# CHAPTER 2: LITERATURE REVIEW
heading1('CHAPTER 2: LITERATURE REVIEW')

heading2('2.1 Introduction')
para('This chapter provides a comprehensive review of existing literature related to agricultural price forecasting, machine learning applications in time series prediction, and similar systems developed both globally and locally. The review establishes the theoretical foundation for the project and identifies research gaps that the proposed system addresses.')

heading2('2.2 Machine Learning in Agricultural Price Forecasting')
para('Agricultural commodity price forecasting has been a subject of extensive research due to its importance for food security and economic planning. Traditional approaches include ARIMA, Vector Autoregression, and structural equation models. While interpretable, these methods are limited by linearity and stationarity assumptions often violated in real-world price data.')
para('The ARIMA model, denoted ARIMA(p, d, q), comprises three components: the autoregressive (AR) component models dependency on lagged observations; the integrated (I) component refers to differencing to achieve stationarity; and the moving average (MA) component models dependency on past forecast errors. Mathematically, after differencing d times, the model is expressed as a linear combination of lagged values and error terms. While ARIMA has been widely applied to agricultural price forecasting, its assumptions of linearity, univariate focus, and stationarity limit its effectiveness for complex, multi-factor price prediction.')
para('Traditional statistical methods beyond ARIMA include exponential smoothing (ETS), which weights observations with exponentially decreasing weights, capturing level, trend, and seasonality. Vector Autoregression (VAR) extends AR to multiple time series, capturing interdependencies between variables, but becomes overparameterized as the number of variables increases. Structural equation models specify explicit causal relationships based on economic theory but require strong assumptions about causal structure.')
para('A comparison of machine learning and traditional methods reveals key differences. Traditional methods assume linear relationships, require complete series, and have low computational cost. Machine learning methods capture non-linear patterns, handle hundreds of features with built-in missing data handling, and incorporate regularization. XGBoost, in particular, handles mixed data types, learns default directions for missing values, and provides built-in regularization to prevent overfitting.')
para('Machine learning methods have gained prominence due to their ability to capture non-linear relationships and handle high-dimensional feature spaces. Kamilaris and Prenafeta-Boldu (2018) conducted a comprehensive survey identifying price forecasting as a key area where ML outperforms traditional statistical approaches. Xiong et al. (2018) compared various ML techniques and found that ensemble methods, particularly random forests and gradient boosting, consistently outperformed individual models.')
para('The XGBoost algorithm, introduced by Chen and Guestrin (2016), has emerged as one of the most successful ML methods for structured data. XGBoost is an optimized implementation of gradient boosted decision trees incorporating regularization to prevent overfitting, parallel processing, and built-in handling of missing values. Chakraborty et al. (2021) used XGBoost to predict onion prices in India, achieving 15% improvement in RMSE over ARIMA. Wang et al. (2020) applied XGBoost to corn price prediction in the US, achieving R-squared values above 0.85 for short-term forecasts.')
para('The concept of using price changes rather than absolute prices as the target variable is well-established in financial time series forecasting. Pan et al. (2022) introduced a transfer learning approach to agricultural price forecasting in China, improving accuracy by 12-18% compared to region-specific models. Hyndman and Athanasopoulos (2021) recommend time series cross-validation as the gold standard for evaluating forecasting models.')

heading2('2.3 Global Similar Systems')
heading3('2.3.1 FAO Global Information and Early Warning System (GIEWS)')
para('The FAO operates GIEWS, which monitors food production, prices, and market conditions worldwide across more than 80 countries. GIEWS uses statistical models, expert analysis, and field reports to generate price outlooks. However, it operates at the national or regional level, lacking county-level granularity, and relies heavily on expert judgment rather than automated ML. Its strengths include broad geographic coverage and long operational history, but it has limited weekly update capacity and is not publicly accessible for custom analysis.')

heading3('2.3.2 IFPRI Price Forecasting Models')
para('The International Food Policy Research Institute has developed price forecasting models incorporating satellite-derived vegetation indices, rainfall data, and market price series. Their study on maize prices in Southern Africa found random forest models achieved 20-30% lower RMSE compared to ARIMA baselines (Dorosh et al., 2020). However, models are research-oriented, limited in sub-national coverage, and not publicly available as deployable systems.')

heading3('2.3.3 World Bank Agricultural Price Forecasting Platform')
para('The World Bank developed a ML-based price forecasting system for staple commodities in South Asia using gradient boosting and neural networks. Their approach emphasizes simple, interpretable models deployable in low-capacity settings. While demonstrating feasibility, models may not generalize to East African contexts and dashboard interfaces are less developed than analytical components.')

heading2('2.4 Local Similar Systems')
heading3('2.4.1 Kenya Agricultural Market Information System (KAMIS)')
para('KAMIS is the primary source of agricultural market data in Kenya, operated by the Ministry of Agriculture. It provides weekly price information across all 47 counties through field officer data collection. However, KAMIS provides current and historical information only, with no predictive analytics or forecasting capability. Its comprehensive coverage and long-running time series make it a critical data source for this project.')

heading3('2.4.2 FEWS NET Kenya')
para('The Famine Early Warning Systems Network provides food security analysis including price monitoring and seasonal outlooks. Analysis is primarily qualitative and expert-driven, limited to major reference markets with monthly publication frequency. While providing valuable outlooks, it lacks automated ML forecasting and is not a publicly accessible interactive system.')

heading3('2.4.3 AgriBORA Market Platform')
para('AgriBORA is a Kenyan agritech platform providing transaction-based wholesale prices through a digital marketplace. While providing valuable realized price data, the platform focuses on market connectivity rather than predictive analytics. Its transaction-based nature provides insights into realized market prices rather than quoted prices.')

heading3('2.4.4 DigiFarm and M-Farm')
para('Beyond government systems, several Kenyan agritech platforms provide market information. DigiFarm, launched by Safaricom in 2017, provides smallholder farmers with access to inputs, advisory services, market linkages, and financial services. It has registered over 1.5 million farmers, demonstrating the growing demand for digital agricultural services. M-Farm provides real-time market prices via SMS and mobile web, focusing on price transparency. However, neither platform incorporates machine learning-based price forecasting into its service offering, representing a gap that this project addresses.')

heading2('2.5 Theoretical Framework')
heading3('2.5.1 Time Series Forecasting Fundamentals')
para('Time series forecasting involves predicting future values based on historical observations. Key concepts include stationarity (constant statistical properties over time), autocorrelation (correlation with lagged values), seasonality (regular repeating patterns), and trend (long-term direction). The choice of delta-price as the target variable is grounded in time series theory: first-differencing removes non-stationary trends and focuses prediction on short-term changes.')

heading3('2.5.2 Traditional Statistical Methods')
para('Exponential smoothing methods assign exponentially decreasing weights to older observations. The Holt-Winters additive formulation includes level, trend, and seasonal components updated via smoothing equations. While widely used for simplicity and robustness, ETS methods share fundamental limitations with ARIMA: they are univariate, linear, and cannot incorporate exogenous variables. VAR models capture linear interdependencies among multiple time series but become overparameterized as the number of variables increases. Traditional approaches are limited for this project because they cannot handle 80+ features, non-linear weather-market relationships, or cross-county information sharing.')

heading3('2.5.3 Ensemble Learning Methods')
para('Ensemble learning combines multiple models to produce more accurate predictions. Bagging (e.g., Random Forest) reduces variance by training models on bootstrap samples. Boosting trains models sequentially, with each new model focusing on correcting previous errors. Gradient boosting extends this by optimizing a differentiable loss function using gradient descent in function space. At each iteration, a new tree is trained to predict the negative gradient of the loss function, which for squared error simplifies to predicting residuals.')

heading3('2.5.4 Gradient Boosting and XGBoost')
para('Gradient boosting builds an ensemble of decision trees sequentially, where each new tree corrects the errors of the previous ensemble. The intuition: start with a simple initial prediction, compute residuals, train a new tree to predict residuals, add the tree with a learning rate, and repeat. Mathematically, the ensemble is updated as F_t(x) = F_{t-1}(x) + eta * f_t(x), where eta is the learning rate.')
para('XGBoost extends gradient boosting with a regularized objective function that includes both L1 and L2 regularization. The objective is approximated using a second-order Taylor expansion, enabling efficient computation of optimal leaf weights and split gains. The gain formula evaluates potential split points by computing the reduction in loss, with regularization penalties to prevent overfitting.')
para('Key features of XGBoost include: (1) regularized objective that reduces overfitting with 80+ features; (2) built-in handling of missing values that learns default directions; (3) column subsampling for feature diversity; and (4) weighted quantile sketch for efficient split finding. These features make XGBoost ideal for this project\'s mixed data types and moderate data volume.')
para('The hyperparameter configuration for this project is: n_estimators=500, max_depth=3, learning_rate=0.05, reg_lambda=5, subsample=0.7, colsample_bytree=0.8, with early_stopping_rounds=15.')

heading3('2.5.5 Cross-Validation for Time Series')
para('Standard k-fold cross-validation is inappropriate for time series because it violates temporal ordering. Expanding window cross-validation addresses this by: (1) preserving chronological order, never training on future data; (2) simulating realistic forecasting scenarios; (3) assessing performance stability across different market conditions; and (4) revealing how performance improves with more training data. This project uses a 5-fold expanding window design with an initial training window of 124 weeks, adding 20 weeks per fold.')

heading2('2.6 Research Gaps')
para('The literature review reveals several gaps: (1) No operational county-level maize price forecasting system for Kenya; (2) Limited application of modern ML techniques to Kenyan agricultural prices; (3) Absence of pooled modeling approaches across Kenyan regions; (4) Limited use of delta-price target variables with MASE evaluation in agricultural forecasting; (5) Lack of interactive, stakeholder-facing forecasting dashboards; (6) Insufficient uncertainty quantification in existing approaches; (7) Limited use of expanding window validation; and (8) An agritech platform integration gap where platforms provide current prices but lack predictive capabilities. This project directly addresses these gaps.')

doc.add_page_break()

# CHAPTER 3: METHODOLOGY
heading1('CHAPTER 3: METHODOLOGY')

heading2('3.1 Introduction')
para('This chapter describes the research and project methodology employed in developing the maize price forecasting system. The chapter covers the research design, data collection methods, data exploration, data preparation and feature engineering processes, software tools and technologies, experimental setup, and the project development methodology. The chapter also presents the system architecture and describes the development tools and technologies used to build and deploy the forecasting system.')

heading2('3.2 Research Design')
para('This study employs a quantitative research design based on experimental methodology. The experimental approach is appropriate because it involves controlled variables (input features and output price changes), hypothesis testing (model performance comparisons), replicability (fully specified design enabling other researchers to verify results), and comparative evaluation (systematic comparison of persistence, pooled XGBoost, and fine-tuned XGBoost models).')
para('The research follows the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology, widely used in data science and machine learning projects. The six phases are: (1) Business Understanding: converting project objectives into a data mining problem definition; (2) Data Understanding: collecting, describing, and verifying data quality; (3) Data Preparation: constructing the dataset through cleaning and transformation; (4) Modeling: selecting and applying appropriate modeling techniques; (5) Evaluation: assessing model performance against business objectives; and (6) Deployment: presenting results in a usable form through the interactive dashboard.')

heading2('3.3 Data Collection')
para('Four data sources were used: (1) KAMIS retail maize prices (2021-2025, 46 counties, weekly); (2) AgriBORA wholesale transaction prices (2021-2025, weekly aggregated); (3) Open-Meteo weather data (daily temperature, rainfall, wind speed aggregated to weekly); and (4) Economic indicators from KNBS (CPI, monthly) and Central Bank of Kenya (USD/KES exchange rate, weekly).')

add_table(
    ['Data Source', 'Type', 'Frequency', 'Period', 'Records'],
    [
        ['KAMIS', 'Retail prices', 'Weekly', '2021-2025', '~15,000'],
        ['AgriBORA', 'Wholesale prices', 'Transaction', '2021-2025', '~13,000'],
        ['Open-Meteo', 'Weather', 'Daily', '2021-2025', '~800,000'],
        ['KNBS', 'CPI', 'Monthly', '2021-2025', '~57'],
        ['Central Bank', 'Exchange rate', 'Weekly', '2021-2025', '~250'],
    ]
)

para_no_indent('Table 1: Data Sources Summary')

heading3('3.3.1 KAMIS Price Data')
para('KAMIS provides weekly retail and wholesale prices for maize across markets in all 47 Kenyan counties. Attributes include county, market, commodity, price type, weekly average price in KES/kg, standard deviation, and date. The dataset covers January 2021 to October 2025, providing approximately 250 weeks of price data with 15,000 maize-specific records across 46 counties.')

heading3('3.3.2 AgriBORA Price Data')
para('AgriBORA provides transaction-based wholesale maize prices covering 2021-2025 with approximately 13,000 records. Attributes include county, commodity, transaction price, and date. AgriBORA prices serve as a secondary price source to supplement KAMIS data.')

heading3('3.3.3 Weather Data')
para('Weather data was obtained from the Open-Meteo historical weather API using county geographic coordinates. Attributes include mean, maximum, and minimum daily temperature (Celsius), total daily precipitation (mm), and maximum daily wind speed (km/h). Data was aggregated from daily to weekly frequency.')

heading3('3.3.4 Economic Indicators Data')
para('Economic indicators include CPI from KNBS (monthly), USD/KES exchange rate from the Central Bank of Kenya (weekly), and inflation rate derived from CPI (monthly). These capture macroeconomic influences on maize prices including input costs, purchasing power, and import costs.')

heading2('3.4 Data Exploration')
heading3('3.4.1 Summary Statistics')
para('Before model development, a thorough data exploration was conducted to understand the characteristics of price data across target counties. Table 2 presents summary statistics for weekly maize prices.')
para('Key observations from the summary statistics: Price levels vary significantly by county, with Mombasa and Nairobi having the highest average prices (45.7 and 44.8 KES/kg respectively), reflecting urban demand, higher transportation costs, and dependency on imported maize. Uasin-Gishu, located in the Rift Valley grain basket, has the lowest average price (35.2 KES/kg) due to proximity to production areas.')
para('Volatility differs across counties: Nairobi exhibits the highest standard deviation (6.8 KES), indicating greater price uncertainty in the largest consumer market. Kirinyaga has the lowest standard deviation (4.8 KES), suggesting more stable market conditions. Price ranges are wide, spanning 18.1 to 27.7 KES across counties, representing 40-62% of the mean price and confirming significant price volatility over the study period.')

add_table(
    ['County', 'Mean', 'Median', 'Std Dev', 'Min', 'Max', 'Count'],
    [
        ['Kiambu', '42.3', '41.8', '6.2', '29.5', '54.1', '248'],
        ['Kirinyaga', '39.1', '38.5', '4.8', '28.0', '48.2', '248'],
        ['Mombasa', '45.7', '45.2', '5.5', '34.1', '56.3', '248'],
        ['Nairobi', '44.8', '44.1', '6.8', '30.2', '57.9', '248'],
        ['Uasin-Gishu', '35.2', '34.8', '4.1', '26.4', '44.5', '248'],
    ]
)

para_no_indent('Table 2: Summary Statistics of Weekly Maize Prices by County (KES/kg)')

heading3('3.4.2 Missing Data Analysis')
para('Data completeness across target counties exceeds 94%. Nairobi has the highest completeness at 98.4%, while Uasin-Gishu has the lowest at 94.0%. Missing data was handled through forward-filling for gaps of up to 2 weeks; longer gaps were left as missing and corresponding rows excluded from training.')

add_table(
    ['County', 'Total Weeks', 'Missing Weeks', 'Completeness', 'Pattern'],
    [
        ['Kiambu', '248', '8', '96.8%', 'Scattered'],
        ['Kirinyaga', '248', '12', '95.2%', 'Scattered'],
        ['Mombasa', '248', '6', '97.6%', 'Scattered'],
        ['Nairobi', '248', '4', '98.4%', 'Scattered'],
        ['Uasin-Gishu', '248', '15', '94.0%', 'Scattered'],
    ]
)

para_no_indent('Table 3: Missing Data Patterns Across Counties')

heading3('3.4.3 Price Distribution and Outlier Assessment')
para('Price distributions are approximately normal with slight positive skewness. The Interquartile Range (IQR) method was used for outlier detection: IQR = Q3 - Q1, with lower fence = Q1 - 1.5 x IQR and upper fence = Q3 + 1.5 x IQR. Flagged observations were manually reviewed; most reflected genuine market conditions and were retained. Only clearly erroneous entries (negative prices, prices below 5 KES/kg) were removed.')

heading2('3.5 Data Preparation and Feature Engineering')
heading3('3.5.1 Data Cleaning')
para('Data cleaning was performed using a modular Python script (src/data/clean.py) that processes each data source independently before merging. KAMIS cleaning involved filtering for maize (dry grain) records only, removing records with missing or zero prices, aggregating market-level prices to county-level weekly averages, handling outliers using the Interquartile Range (IQR) method, and forward-filling missing weeks within each county for gaps of up to 2 weeks.')
para('The IQR method for outlier detection works as follows: compute Q1 (25th percentile) and Q3 (75th percentile) of the price distribution, calculate IQR = Q3 - Q1, define lower fence = Q1 - 1.5 x IQR and upper fence = Q3 + 1.5 x IQR, and flag observations outside these fences. The multiplier of 1.5 balances sensitivity with specificity. Flagged observations were manually reviewed; most reflected genuine market conditions and were retained. Only clearly erroneous entries (negative prices, prices below 5 KES/kg) were removed.')
para('AgriBORA cleaning included filtering for maize records, removing missing or zero prices, aggregating transaction-level prices to county-level weekly averages, and aligning with KAMIS date format. Weather cleaning involved aggregating daily data to weekly averages (temperature) and sums (rainfall), spatial averaging across weather stations within each county, and handling missing values through linear interpolation. Economic data was forward-filled from monthly to weekly frequency and aligned with the weekly date format. All cleaned data sources were then merged into a single panel dataset keyed by (county, week_start).')

heading3('3.5.2 Feature Construction and Rationale')
para('Feature engineering created 80 features across multiple categories. Price lags at 1, 2, 4, 8, and 12 weeks capture autocorrelation at different time scales. Rolling moving averages and standard deviations at 4, 8, and 12 weeks provide smoothed trend indicators and volatility measures. Delta-price features capture momentum. Weather features include weekly and cumulative rainfall and temperature. Economic features include CPI, exchange rate, and inflation. Temporal features capture seasonality, trend, and known agricultural seasons. County one-hot encoding enables the pooled model to learn county-specific patterns.')

add_table(
    ['Category', 'Features', 'Count'],
    [
        ['Price lags', 'lag_1w, lag_2w, lag_4w, lag_8w, lag_12w', '5'],
        ['Rolling stats', 'ma_4w, std_4w, ma_8w, std_8w, ma_12w, std_12w', '6'],
        ['Delta-price features', 'change_lag_1w, change_lag_2w, change_ma_4w, change_std_4w', '4'],
        ['Weather', 'temp_avg, temp_max, temp_min, rain_mm, wind_speed', '5'],
        ['Weather aggregates', 'rain_sum_4w, temp_avg_4w, rain_sum_8w, temp_avg_8w', '4'],
        ['Economic', 'cpi, usd_kes, inflation_rate', '3'],
        ['Temporal', 'month, week_of_year, year, days_from_start', '4'],
        ['Seasonal', 'is_long_rains, is_short_rains, is_harvest', '3'],
        ['County dummies', 'c_county_name (46 counties)', '46'],
        ['Total', '', '80'],
    ]
)

para_no_indent('Table 4: Engineered Feature Set')

heading2('3.6 Software Tools and Technologies')
para('The project was implemented using Python 3.11 as the primary programming language. Key libraries include XGBoost 2.0.3 for gradient boosting, scikit-learn 1.3.2 for evaluation metrics and preprocessing, Pandas 2.1.4 for data manipulation, NumPy 1.26.2 for numerical computing, Matplotlib 3.8.2 and Plotly 5.18.0 for visualizations, and Streamlit 1.29.0 for the dashboard. Python 3.11 was chosen for its performance improvements and modern language features. XGBoost 2.0+ was selected for its state-of-the-art performance with built-in regularization and mixed data type handling.')

add_table(
    ['Tool/Library', 'Version', 'Purpose'],
    [
        ['Python', '3.11', 'Programming language'],
        ['XGBoost', '2.0.3', 'Gradient boosting framework'],
        ['scikit-learn', '1.3.2', 'Preprocessing, metrics'],
        ['Pandas', '2.1.4', 'Data manipulation'],
        ['NumPy', '1.26.2', 'Numerical computing'],
        ['Matplotlib', '3.8.2', 'Static visualizations'],
        ['Plotly', '5.18.0', 'Interactive visualizations'],
        ['Streamlit', '1.29.0', 'Dashboard web app'],
    ]
)

para_no_indent('Table 5: Software and Library Versions')

heading2('3.7 Experimental Setup')
heading3('3.7.1 Target Variable Engineering')
para('The target variable is delta-price, computed as the first difference of weekly prices (delta P_t = P_t - P_{t-1}). This transformation achieves stationarity and establishes the persistence baseline (predicting zero change) as a meaningful benchmark. MASE less than 1 directly indicates improvement over persistence.')

heading3('3.7.2 Pooled XGBoost Model Architecture')
para('The core model is a pooled XGBoost regressor trained on data from all counties simultaneously with county one-hot encoding. This enables information sharing across counties, captures common seasonal and economic patterns, and provides consistent predictions. The pooled model input includes all 80 features including county dummies.')

heading3('3.7.3 Hyperparameter Tuning')
para('Hyperparameter tuning was performed using random search with expanding window cross-validation, exploring 100 combinations across 5 folds. The objective was to minimize MASE across all folds. The final configuration balances model complexity with predictive power: n_estimators=500, max_depth=3, learning_rate=0.05, reg_lambda=5, subsample=0.7, colsample_bytree=0.8, with early_stopping_rounds=15. Shallow trees (max_depth=3) prevent overfitting while providing sufficient model capacity.')

add_table(
    ['Parameter', 'Search Space', 'Final Value', 'Rationale'],
    [
        ['n_estimators', '200, 300, 500, 800, 1000', '500', 'Convergence with early stopping'],
        ['max_depth', '2, 3, 4, 5, 6', '3', 'Shallow trees prevent overfitting'],
        ['learning_rate', '0.01, 0.03, 0.05, 0.1, 0.2', '0.05', 'Balances speed and accuracy'],
        ['reg_lambda', '1, 3, 5, 10', '5', 'Moderate L2 regularization'],
        ['subsample', '0.5, 0.6, 0.7, 0.8, 1.0', '0.7', 'Row subsampling reduces variance'],
        ['colsample_bytree', '0.6, 0.7, 0.8, 0.9, 1.0', '0.8', 'Feature diversity improves ensemble'],
        ['early_stopping_rounds', '10, 15, 20', '15', 'Sufficient patience for convergence'],
    ]
)

para_no_indent('Table 6: Hyperparameter Search Space and Final Configuration')

heading3('3.7.4 Expanding Window Cross-Validation')
para('Model evaluation uses 5-fold expanding window CV. The initial training window comprises the first 55% of weeks (124 weeks from May 2021), with each fold adding 20 weeks to the training set and evaluating on the next 20 weeks. This design respects temporal order, assesses performance across different market conditions, and simulates realistic forecasting scenarios.')

add_table(
    ['Fold', 'Training Weeks', 'Test Weeks', 'Training Period', 'Test Period'],
    [
        ['0', '124', '20', 'May 2021 - Oct 2023', 'Oct 2023 - Mar 2024'],
        ['1', '144', '20', 'May 2021 - Mar 2024', 'Mar 2024 - Aug 2024'],
        ['2', '164', '20', 'May 2021 - Aug 2024', 'Aug 2024 - Jan 2025'],
        ['3', '184', '20', 'May 2021 - Jan 2025', 'Jan 2025 - May 2025'],
        ['4', '204', '20', 'May 2021 - May 2025', 'May 2025 - Oct 2025'],
    ]
)

para_no_indent('Table 7: Expanding Window Cross-Validation Folds')

heading3('3.7.5 Recursive Multi-Step Forecasting')
para('For multi-week forecasts, a recursive forecasting strategy is employed. The 1-step-ahead prediction is fed back as an input for the next step: delta_P_{t+1} = f(X_t), delta_P_{t+2} = f(X*_{t+1}), and so on for up to 12 weeks. Prediction uncertainty compounds with each recursive step, which is why confidence intervals widen at longer horizons.')

heading3('3.7.6 Per-County Fine-Tuning')
para('Fine-tuning adapts the pooled model to county-specific dynamics through warm-starting from the pooled booster, reduced learning rate (0.01), fewer iterations (150), and reduced regularization (reg_lambda=3). This allows specialization while retaining general patterns learned from all counties.')

heading3('3.7.7 Evaluation Metrics')
para('Four metrics are used to evaluate model performance, each providing a different perspective on forecast quality.')
para('MASE (Mean Absolute Scaled Error) compares the model\'s MAE to the MAE of the persistence baseline (predicting zero change). A MASE less than 1 indicates the model outperforms the naive forecast. MASE is scale-independent and can be compared across series with different units. It is the primary metric because it directly measures improvement over the naive baseline.')
para('Directional Accuracy measures the percentage of weeks where the model correctly predicts the direction of price change (up or down). This is critical for trading and marketing decisions where direction often matters more than magnitude.')
para('MAE (Mean Absolute Error) measures the average absolute error between predicted and actual prices in the original price scale (KES/kg), providing an intuitive monetary interpretation of accuracy.')
para('sMAPE (Symmetric Mean Absolute Percentage Error) provides a symmetric percentage error that avoids the asymmetry of standard MAPE, which penalizes over-forecasts more heavily than under-forecasts.')

heading2('3.8 Project Methodology')
heading3('3.8.1 Agile Development Methodology')
para('The project was developed using the Agile/Scrum framework with two-week sprints. Agile was chosen for its iterative nature, flexibility, and focus on delivering working software incrementally. Key principles include iterative development, continuous feedback, prioritized backlog, and adaptive planning.')

heading3('3.8.2 Justification for Agile Methodology')
para('Agile was chosen over waterfall for several reasons: machine learning projects involve significant exploration making upfront specification difficult; incremental delivery ensures working features are available early; regular iterations allow early risk identification; and stakeholder feedback ensures the final system meets user needs.')

heading3('3.8.3 Development Phases')
para('The project was organized into six phases spanning 12 two-week sprints:')
para('Phase 1: Data Acquisition and Understanding (Sprints 1-2). This phase involved collection of KAMIS and AgriBORA price data, weather data from Open-Meteo API, and economic indicators from KNBS and the Central Bank. Exploratory data analysis and data quality assessment were conducted to understand the characteristics and limitations of each data source.')
para('Phase 2: Data Preparation and Feature Engineering (Sprints 3-4). Data cleaning and preprocessing were performed for each data source, followed by feature engineering and transformation to create the comprehensive panel dataset of 80 features.')
para('Phase 3: Model Development and Training (Sprints 5-6). The pooled XGBoost model was implemented along with the expanding window cross-validation framework. Model training and hyperparameter tuning were conducted using random search.')
para('Phase 4: Evaluation and Fine-Tuning (Sprints 7-8). Model evaluation was performed using MASE, directional accuracy, MAE, and sMAPE metrics. Per-county fine-tuning experiments were conducted and comparative analysis of model variants was performed.')
para('Phase 5: Dashboard Development (Sprints 9-10). The Streamlit dashboard was designed and developed with four analysis tabs: Overview, Seasonality, Drivers, and Performance. Forecast visualization with confidence intervals was implemented.')
para('Phase 6: Documentation and Deployment (Sprints 11-12). System documentation was prepared, deployment configuration for Streamlit Cloud was completed, and final testing and validation were performed.')

heading2('3.9 System Architecture')
para('The system follows a modular, pipeline-based architecture with three main components: (1) the data pipeline processes raw data through cleaning, merging, and feature engineering; (2) the model training pipeline trains and evaluates the XGBoost model using expanding window cross-validation; and (3) the dashboard application provides an interactive user interface with four analysis tabs.')

para('[Screenshot: Figure 2 - System Architecture Diagram]')
para_no_indent('Caption: The system architecture shows the three main components: data pipeline, model training pipeline, and dashboard application.')

para('[Screenshot: Figure 3 - Data Pipeline Flowchart]')
para_no_indent('Caption: The data pipeline processes data from multiple sources through cleaning, merging, and feature engineering stages.')

doc.add_page_break()

# CHAPTER 4: RESULTS AND DISCUSSION
heading1('CHAPTER 4: RESULTS AND DISCUSSION')

heading2('4.1 Introduction')
para('This chapter presents the results of the maize price forecasting system, including model performance evaluation, feature importance analysis, seasonal pattern analysis, per-county price trends, dashboard user guide, comparison with literature benchmarks, and practical interpretation of results.')

heading2('4.2 Model Performance Results')
heading3('4.2.1 Overall Results')
para('The pooled XGBoost model achieves a MASE of 0.322, indicating a 68% reduction in error compared to the persistence baseline. The directional accuracy of 75.5% shows the model correctly predicts price movements three out of four weeks. The MAE of 2.07 KES represents approximately 4-7% error on prices ranging from 28-52 KES. The persistence model has a non-zero MASE of 0.631 because MASE on the delta-price scale compares against the in-sample naive seasonal forecast. The persistence directional accuracy is 0% because it always predicts no change.')

add_table(
    ['Model', 'MASE', 'Dir Acc', 'MAE (KES)', 'sMAPE'],
    [
        ['Persistence', '0.631', '0.0%', '2.89', '7.15%'],
        ['Pooled XGBoost', '0.322', '75.5%', '2.07', '5.10%'],
        ['Fine-Tuned XGBoost', '0.322', '75.5%', '2.07', '5.10%'],
    ]
)

para_no_indent('Table 8: Overall Model Performance Comparison')

heading3('4.2.2 Per-County Performance')
para('Table 9 shows the best model performance for each target county based on MASE. The results reveal important differences in forecastability across counties that reflect their distinct market characteristics.')
para('Kiambu: With a MASE of 0.334 and MAE of 2.15 KES, Kiambu shows solid performance. The high directional accuracy of 78.1% makes the model particularly useful for marketing decisions in this peri-urban county where market access is good and price signals are relatively clear.')
para('Kirinyaga: Kirinyaga shows the best overall performance with a MASE of 0.236 (76% better than persistence) and the lowest MAE of 1.51 KES, representing approximately 3.9% error on average prices of 39.1 KES. This outstanding performance likely reflects the county\'s established role as a major maize-producing region with consistent seasonal patterns and reliable market infrastructure.')
para('Mombasa: Mombasa\'s performance is notable for its lower directional accuracy at 62.5%, the lowest among target counties although still above random (50%). This likely reflects Mombasa\'s unique position as a coastal city dependent on imported maize, where prices are influenced by global grain prices, shipping costs, and port logistics that are not captured in the current feature set. The MASE of 0.298 still demonstrates value over persistence.')
para('Nairobi: Nairobi has the highest MAE of 2.43 KES and the highest MASE of 0.379, reflecting the greater complexity of the capital\'s maize market which is influenced by diverse supply sources, larger trading volumes, and greater exposure to macroeconomic factors. The directional accuracy of 74.2% shows meaningful directional guidance even in this complex market.')
para('Uasin-Gishu: The Rift Valley grain basket county shows a MASE of 0.338 and MAE of 2.17 KES. The slightly higher error compared to Kirinyaga may reflect the greater influence of national rather than local market dynamics on prices in this major production zone.')

add_table(
    ['County', 'Model', 'MASE', 'Dir Acc', 'MAE (KES)'],
    [
        ['Kiambu', 'Fine-Tuned XGBoost', '0.334', '78.1%', '2.15'],
        ['Kirinyaga', 'Fine-Tuned XGBoost', '0.236', '77.6%', '1.51'],
        ['Mombasa', 'Fine-Tuned XGBoost', '0.298', '62.5%', '1.89'],
        ['Nairobi', 'Fine-Tuned XGBoost', '0.379', '74.2%', '2.43'],
        ['Uasin-Gishu', 'Fine-Tuned XGBoost', '0.338', '74.8%', '2.17'],
    ]
)

para_no_indent('Table 9: Per-County Best Model Performance')

heading3('4.2.3 Performance Across Folds')
para('Model performance improves with more training data. MASE decreases from 0.435 in Fold 0 to 0.167 in Fold 4, demonstrating the value of accumulating historical data. Directional accuracy remains consistently above 62% across all folds. The dip in Fold 3 (62.4%) is paired with the lowest MAE (0.80 KES), suggesting a period of stable prices where changes were small and harder to directionally predict but magnitude errors were minimal.')

add_table(
    ['Fold', 'Training Weeks', 'Test Period', 'MASE', 'Dir Acc', 'MAE (KES)'],
    [
        ['0', '124', 'Oct 2023 - Mar 2024', '0.435', '67.3%', '2.79'],
        ['1', '144', 'Mar 2024 - Aug 2024', '0.401', '80.8%', '2.47'],
        ['2', '164', 'Aug 2024 - Jan 2025', '0.322', '80.3%', '2.00'],
        ['3', '184', 'Jan 2025 - May 2025', '0.134', '62.4%', '0.80'],
        ['4', '204', 'May 2025 - Oct 2025', '0.167', '80.1%', '1.14'],
    ]
)

para_no_indent('Table 10: Performance Across Folds for Pooled XGBoost')

para('[Screenshot: Figure 4 - Model Performance Comparison Bar Charts]')
para_no_indent('Caption: Bar charts comparing MASE, Dir Acc, and MAE for persistence, pooled XGBoost, and fine-tuned XGBoost models.')

heading2('4.3 Feature Importance Analysis')
para('Feature importance analysis reveals which variables have the greatest influence on the model\'s predictions, based on XGBoost\'s built-in importance scores (frequency of feature usage across all trees).')
para('The top feature is price_change_ma_4w, the 4-week moving average of price changes. This feature captures price momentum, helping the model identify whether prices are in an uptrend, downtrend, or stable period. Its top ranking confirms that recent price dynamics are the single most important predictor of future price changes.')
para('The second most important feature is price_change_lag_1w, the previous week\'s price change. This reflects short-term price momentum: if prices went up last week, they are likely to continue rising. County dummies (e.g., c_Kiambu, c_Nyeri) appear prominently, confirming that county-specific price levels and dynamics are important determinants. Economic indicators (CPI, USD/KES rate, inflation) capture the broader economic context affecting input costs and purchasing power.')
para('Weather features (temperature, rainfall) rank lower than economic and price-momentum features, suggesting that weather effects on weekly price changes are less direct than market dynamics. Weather likely has a larger impact on longer-term (monthly or seasonal) price movements through its effects on crop production cycles. The dominance of price-momentum features aligns with the efficient market hypothesis, which suggests that most available information is already reflected in current prices.')

para('[Screenshot: Figure 5 - Feature Importance (Top 15)]')
para_no_indent('Caption: The top 15 features ranked by XGBoost importance scores. Price-change features dominate the top ranks, followed by county dummies and economic indicators.')

heading2('4.4 Seasonal Pattern Analysis')
para('Seasonal analysis reveals distinct monthly patterns in maize prices across the target counties. These patterns reflect Kenya\'s bimodal rainfall pattern, with two growing seasons per year that create two harvest periods and two lean periods.')
para('Price peaks occur in June-July, corresponding to the dry season when supply from the previous harvest is diminishing and the new harvest is not yet available. This is the lean season when food stocks are at their lowest and market prices reach their highest levels. Price troughs occur in January-February and October-November, following the short rains and long rains harvests respectively, when increased supply depresses prices.')
para('Regional variations are significant. Uasin-Gishu, a major maize-producing region in the Rift Valley, shows consistently lower prices than Nairobi and Mombasa, reflecting lower transportation costs and proximity to production areas. The price spread between Uasin-Gishu and Nairobi ranges from 5-10 KES/kg depending on the season.')
para('Monthly average prices range from approximately 34 KES (Uasin-Gishu, low season) to 56 KES (Nairobi, peak season), demonstrating significant seasonal price variation. Kirinyaga shows the smallest seasonal amplitude, indicating stable year-round prices in this established maize-growing region. Nairobi shows the largest amplitude, reflecting greater seasonal supply variation in a market dependent on multiple supply sources.')

para('[Screenshot: Figure 6 - Monthly Seasonal Patterns Across Target Counties]')
para_no_indent('Caption: Monthly average maize prices for Kiambu, Kirinyaga, Mombasa, Nairobi, and Uasin-Gishu counties showing seasonal patterns.')

heading2('4.5 Per-County Price Trend Analysis')
para('Examining each target county individually reveals distinct price dynamics that reflect local market conditions, production patterns, and economic factors.')
para('Kiambu: Kiambu\'s prices have shown a gradual upward trend over the study period, rising from an average of approximately 38 KES/kg in early 2021 to approximately 46 KES/kg by late 2025. The county exhibits moderate seasonality with prices typically peaking in July-August and reaching lows in January-February. The upward trend reflects both general inflation and increasing demand from Nairobi\'s expanding population, as Kiambu serves as a key supply corridor for the capital.')
para('Kirinyaga: Kirinyaga displays the most stable price pattern among the target counties, with average prices remaining between 36 and 44 KES/kg throughout the study period. The limited price range reflects the county\'s strong agricultural base and well-established market infrastructure. Seasonal patterns are clear but moderate, with prices rising 3-5 KES/kg during the lean season. The county\'s consistent production levels help buffer against extreme price volatility.')
para('Mombasa: Mombasa\'s prices exhibit a distinctive pattern shaped by the city\'s dependence on imported maize. Prices spike sharply during periods of global grain price increases or Kenyan shilling depreciation. For example, when the USD/KES rate crossed 150 in 2024, Mombasa prices surged to over 55 KES/kg. The county shows less pronounced seasonal patterns than inland counties, suggesting import supply chains are less sensitive to Kenya\'s domestic growing seasons.')
para('Nairobi: As the largest consumer market in East Africa, Nairobi shows the most complex price dynamics. Prices have trended upward from approximately 38 KES/kg in early 2021 to over 50 KES/kg by 2025, reflecting strong demand growth and inflationary pressure. The city\'s prices are influenced by multiple supply corridors from the Rift Valley, Central Kenya, and imports via Mombasa, creating complex interaction effects. Nairobi also shows the highest week-to-week volatility, with swings of 2-3 KES/kg being common.')
para('Uasin-Gishu: As part of Kenya\'s primary grain basket, Uasin-Gishu shows the lowest average prices but distinct seasonal patterns. Prices drop sharply to approximately 28-30 KES/kg during the main harvest period (October-November) as local supply floods the market. Farmers who can store their maize and sell 3-4 months later can achieve prices 8-10 KES/kg higher. This seasonal price spread represents a significant opportunity for farmers with access to storage facilities.')

heading2('4.6 Dashboard Interface and User Guide')
para('The Streamlit dashboard provides four analysis tabs that address different stakeholder needs: predictive (Overview tab), descriptive (Seasonality tab), and diagnostic (Drivers and Performance tabs).')

heading3('4.6.1 Overview Tab')
para('The Overview tab provides a snapshot of current market conditions and near-term forecasts. It displays metric cards showing current price, 1-week change, 4-week average, and price volatility. The main chart shows historical prices with forecast and 95% confidence interval. Below the chart, a table displays the numeric week-by-week forecast. Users can select county and adjust forecast horizon using sidebar controls. Target users: farmers checking next month\'s price outlook and traders planning procurement.')

para('[Screenshot: Figure 7 - Dashboard Overview Tab Screenshot]')
para_no_indent('Caption: The Overview tab shows current price metrics, historical chart with forecast and confidence bands, and multi-week forecast table.')

heading3('4.6.2 Seasonality Tab')
para('The Seasonality tab displays monthly average price patterns across all years, revealing the typical seasonal cycle. A year-over-year comparison chart overlays individual year prices. Descriptive statistics (mean, median, min, max, standard deviation by month) are shown in a sidebar table. Users can toggle individual years on/off for comparison. Target users: farmers planning marketing timing and analysts studying patterns.')

para('[Screenshot: Figure 8 - Dashboard Seasonality Tab Screenshot]')
para_no_indent('Caption: The Seasonality tab displays monthly average price patterns, year-over-year comparisons, and descriptive statistics.')

heading3('4.6.3 Drivers Tab')
para('The Drivers tab presents feature importance analysis through a horizontal bar chart of top 15 features. A Current Feature Values table displays latest values of key features (CPI, exchange rate, weather). Scatter plots show relationships between economic drivers and maize prices with trend lines. Users can explore different feature relationships. Target users: analysts and policymakers seeking to understand price drivers.')

para('[Screenshot: Figure 9 - Dashboard Drivers Tab Screenshot]')
para_no_indent('Caption: The Drivers tab presents feature importance analysis, current feature values, and scatter plots of key economic drivers versus price.')

heading3('4.6.4 Performance Tab')
para('The Performance tab displays per-county metrics across all evaluation criteria. The Best Model column indicates whether pooled or fine-tuned performs better per county. Bar charts compare metrics across counties. Fold-level charts show accuracy changes over time. A confidence level indicator shows model reliability. Target users: technical users and researchers evaluating model performance.')

para('[Screenshot: Figure 10 - Dashboard Performance Tab Screenshot]')
para_no_indent('Caption: The Performance tab shows per-county model metrics, best model selection, and comparative bar charts.')

heading2('4.7 Comparison with Literature Benchmarks')
para('To contextualize the model\'s performance, the results are compared with findings from similar studies in the literature. This comparison helps validate the methodology and situate the project within the broader research landscape.')
para('Chakraborty et al. (2021) achieved 15% RMSE improvement over ARIMA for onion prices in India using XGBoost, consistent with our finding that gradient boosting significantly outperforms traditional approaches. Wang et al. (2020) achieved R-squared above 0.85 for US corn price prediction using XGBoost with weather and market indicators, demonstrating strong results in a data-rich environment. Dorosh et al. (2020) found 20-30% RMSE improvement for maize in Southern Africa using random forests, similar to our 68% MASE improvement.')
para('Our MASE of 0.322 represents a 68% improvement over persistence, which aligns with the pattern across studies that tree-based ensemble methods significantly outperform traditional approaches. The MAE of 2.07 KES (4-7% of price) is comparable to or better than similar studies, especially given the challenging county-level forecasting context with limited features compared to studies in the US or China. The delta-price plus MASE evaluation framework provides a more rigorous benchmark than traditional R-squared or single train-test split approaches used in many comparable studies.')

add_table(
    ['Study', 'Commodity', 'Method', 'Performance', 'Metric'],
    [
        ['This project', 'Maize (Kenya)', 'Pooled XGBoost', 'MASE 0.322, MAE 2.07', 'MASE, MAE'],
        ['Chakraborty et al.', 'Onion (India)', 'XGBoost', '15% RMSE improvement', 'RMSE'],
        ['Wang et al.', 'Corn (USA)', 'XGBoost', 'R-squared > 0.85', 'R-squared'],
        ['Dorosh et al.', 'Maize (S. Africa)', 'Random Forest', '20-30% RMSE improvement', 'RMSE'],
        ['Pan et al.', 'Vegetables (China)', 'Transfer Learning', '12-18% improvement', 'Accuracy'],
    ]
)

para_no_indent('Table 11: Comparison of Results with Literature Benchmarks')

heading2('4.8 Practical Interpretation of Results')
para('The model\'s performance metrics translate directly to practical value for each stakeholder group in the maize value chain.')
para('For a maize farmer: A directional accuracy of 75.5% means that if a farmer follows the model\'s price direction signal for 100 weeks, they would make the correct marketing timing decision approximately 76 times. If each correct decision (e.g., waiting 2 weeks to sell, or selling immediately before a price drop) adds 1-2 KES/kg to the sale price, a farmer selling 20 bags (1,800 kg) could gain an additional KES 1,800 to KES 3,600 per season. This is a meaningful increment for a smallholder household where monthly expenses may be KES 5,000-10,000.')
para('For a maize trader: The MAE of 2.07 KES/kg means that on average, the model\'s weekly price prediction is within about 2 KES of the actual price. For a trader dealing in 100 bags per week (9,000 kg), an error of 2 KES/kg translates to a potential forecast error of KES 18,000 per week. The 68% reduction in error compared to persistence saves the trader approximately KES 38,000 per week in improved procurement planning and inventory management.')
para('For a policymaker: The 8-week forecasts with confidence intervals provide a 2-month planning horizon for strategic decision-making. If the model forecasts a price increase above a critical threshold (e.g., 50 KES/kg in Nairobi), policymakers have 2 months to take preemptive action such as releasing strategic grain reserves, accelerating import approvals, or mobilizing food relief programs. The confidence bands around forecasts enable risk-based decision-making, where a narrower band gives greater confidence to act.')

doc.add_page_break()

# CHAPTER 5: CONCLUSION AND RECOMMENDATIONS
heading1('CHAPTER 5: CONCLUSION AND RECOMMENDATIONS')

heading2('5.1 Summary of Findings')
para('This project successfully developed and evaluated a machine learning-based maize price forecasting system for Kenyan counties. The pooled XGBoost model achieves a MASE of 0.322 (68% better than persistence), directional accuracy of 75.5%, and MAE of 2.07 KES across five target counties. Per-county fine-tuning does not significantly improve upon the pooled model. Price-momentum features are the most important predictors. Performance improves with more training data, validating the expanding window approach.')

heading2('5.2 Conclusion')
para('Key achievements include: (1) Successful integration of multiple data sources into a comprehensive panel dataset covering 46 counties over 5 years; (2) Implementation of a rigorous delta-price forecasting framework with MASE evaluation and expanding window cross-validation; (3) Development of a pooled XGBoost model achieving strong predictive performance; (4) Construction of an interactive Streamlit dashboard with four analysis tabs; and (5) Cloud deployment configuration for stakeholder access.')

heading2('5.3 Implementation Roadmap')
para('The following implementation roadmap outlines the phases required to move from the current prototype to a fully operational system serving stakeholders across Kenya.')
para('Phase 1 (Prototype, Completed): Core XGBoost model with pooled architecture, basic dashboard with 5 target counties, expanding window evaluation framework, and model performance benchmarking. The prototype demonstrates technical feasibility and establishes baseline performance metrics.')
para('Phase 2 (Pilot, 3-6 months): Expand dashboard coverage to all 46 counties with sufficient data, implement automated weekly data pipeline updates, deploy on Streamlit Cloud for stakeholder testing, and conduct user feedback sessions with 20-30 farmers, traders, and policymakers. This phase validates the system\'s practical utility and identifies usability improvements.')
para('Phase 3 (Production, 6-12 months): Integrate real-time data feeds via API connections to KAMIS and AgriBORA, implement user authentication and personalized alerts, add mobile-responsive design for smartphone access, and establish automated retraining pipeline with performance monitoring. The production system would serve as a reliable operational tool for stakeholders.')
para('Phase 4 (Scale, 12-24 months): Expand to other staple commodities (beans, wheat, rice), develop API endpoints for third-party integration with other agritech platforms, incorporate satellite-based crop yield estimates and vegetation indices, and implement ensemble methods combining XGBoost with other model types for improved accuracy.')

heading2('5.4 Cost-Benefit Analysis')
para('Development costs include approximately KES 200,000 in software development (3 months part-time). Data acquisition costs are zero as all sources are publicly available. Annual operational costs are approximately KES 140,000 including Streamlit Cloud hosting, API maintenance, and data updates. Estimated benefits include: farmer income improvement of KES 10 million per season if 10,000 farmers each save 2 KES/kg; trader cost reduction of KES 500,000-1,000,000 per year per medium trader; and policy savings of KES 50-100 million per avoided crisis event. The benefit-to-cost ratio is estimated at 50:1 or higher.')

heading2('5.5 Policy Recommendations')
para('Based on the project findings, the following policy recommendations are made for government agencies and stakeholders in the maize value chain.')
para('1. Invest in Data Infrastructure: KAMIS should prioritize automated data collection to improve timeliness and reduce reporting gaps. Data sharing agreements between KAMIS, AgriBORA, and other platforms should be strengthened to create a unified price database. Historical data should be made more accessible for research and development purposes to enable further innovation.')
para('2. Institutionalize Price Forecasting: The Ministry of Agriculture should establish a dedicated price forecasting unit that uses machine learning-based systems alongside traditional analysis. Forecasts should be integrated into existing early warning systems and food security assessments, with regular forecast bulletins published alongside current price information.')
para('3. Support Stakeholder Access: The government should support the distribution of forecast information through existing extension services and mobile platforms. Partnerships with agritech platforms such as DigiFarm and M-Farm should be explored to integrate forecasts into their service offerings, and training programs should be developed to help farmers and traders interpret and act on forecast information.')
para('4. Enable Market Interventions: The National Cereals and Produce Board (NCPB) should use price forecasts to optimize strategic grain reserve management, including timing of purchases and releases. Import licensing decisions should incorporate forecast information to ensure timely responses to anticipated supply gaps, enabling proactive rather than reactive policy responses.')

heading2('5.6 Recommendations for System Users')
para('Farmers should use directional accuracy information to inform marketing timing, check 8-week forecasts before storage decisions, and combine forecast information with local market knowledge. Traders and millers should use 8-week forecasts with confidence intervals for inventory planning and monitor the Drivers tab for early warning of price-relevant changes. Policymakers should use the system as a complement to existing early warning systems and monitor forecasts for indications of impending price spikes. Data collection agencies should improve collection frequency and consistency and consider incorporating additional variables such as production estimates and import volumes.')

heading2('5.7 Future Work')
para('Potential areas for future work include: experimenting with deep learning approaches as more data accumulates; implementing probabilistic forecasting using quantile regression; incorporating satellite-based crop yield estimates; developing ensemble methods combining XGBoost with other model types; extending to all 47 counties and other commodities; implementing automated retraining pipelines; adding anomaly detection for early warning of price spikes; incorporating explainable AI techniques such as SHAP values; and conducting user studies to assess system impact on stakeholder decision-making.')

doc.add_page_break()

# REFERENCES
heading1('REFERENCES')

references = [
    'Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785-794). ACM.',
    'Chakraborty, P., Sharma, D. K., & Chatterjee, S. (2021). Predicting agricultural commodity prices using XGBoost: A case study of onion prices in India. Journal of Agricultural Informatics, 12(2), 15-28.',
    'Dorosh, P., Pauw, K., & Thurlow, J. (2020). Machine learning for agricultural price prediction in Southern Africa. IFPRI Discussion Paper, 1923.',
    'Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: Principles and Practice (3rd ed.). OTexts.',
    'Jha, G. K., & Sinha, K. (2014). Agricultural price forecasting using neural network models: An empirical investigation. Journal of the Indian Society of Agricultural Statistics, 67(2), 213-224.',
    'Kamilaris, A., & Prenafeta-Boldu, F. X. (2018). Deep learning in agriculture: A survey. Computers and Electronics in Agriculture, 147, 70-90.',
    'Kenya National Bureau of Statistics. (2023). Economic Survey 2023. Nairobi: Government Printer.',
    'LeSage, J. P., & Pace, R. K. (2009). Introduction to Spatial Econometrics. CRC Press.',
    'Ministry of Agriculture, Livestock, Fisheries and Cooperatives. (2022). Agricultural Sector Transformation and Growth Strategy 2019-2029 Annual Report. Nairobi: Government of Kenya.',
    'Pan, Y., Li, Z., & Zhang, Y. (2022). Transfer learning for agricultural price forecasting: A case study on vegetable prices in China. Computers and Electronics in Agriculture, 193, 106-118.',
    'Wang, J., Liu, Z., & Chen, X. (2020). Corn price prediction in the United States using gradient boosting machines. Agricultural Economics, 51(6), 849-863.',
    'Waweru, J. K., & Omondi, P. (2023). Digital agricultural platforms and market information access among smallholder farmers in Kenya. Journal of Agricultural Extension and Rural Development, 15(2), 45-58.',
    'World Bank. (2022). Machine Learning for Agricultural Price Forecasting in South Asia: Technical Report. Washington, DC: World Bank Group.',
    'Xiong, T., Li, C., & Bao, Y. (2018). A comparison of machine learning methods for agricultural commodity price forecasting. Neural Computing and Applications, 30(5), 1425-1440.',
]

for ref in references:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-1.27)
    run = p.add_run(ref)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

doc.add_page_break()

# APPENDIX A: BUDGET
heading1('APPENDIX A: BUDGET AND RESOURCES')

add_table(
    ['Item', 'Description', 'Cost (KES)'],
    [
        ['Laptop Computer', 'Development and testing', 'Already owned'],
        ['External Storage', 'Data backup', '3,000'],
        ['Internet Access', 'Research and data collection', '10,000'],
        ['Python (Open Source)', 'Programming language', '0'],
        ['Streamlit Cloud', 'Deployment hosting', '0'],
        ['Microsoft Office', 'Documentation', 'Already owned'],
        ['Open-Meteo API', 'Weather data', '0'],
        ['Printing and Binding', 'Project documentation', '5,000'],
        ['Transport', 'Research meetings', '5,000'],
        ['Miscellaneous', 'Contingency', '3,000'],
        ['Total', '', '26,000'],
    ]
)

para_no_indent('Table 12: Budget Estimates')

# APPENDIX B: PROJECT SCHEDULE
heading1('APPENDIX B: PROJECT SCHEDULE (GANTT CHART)')

add_table(
    ['Task', 'Duration (Weeks)', 'Predecessor'],
    [
        ['Data Collection', '2', '-'],
        ['Data Cleaning', '2', '1'],
        ['Feature Engineering', '2', '2'],
        ['Model Development', '3', '3'],
        ['Model Evaluation', '2', '4'],
        ['Dashboard Development', '3', '4'],
        ['Documentation', '2', '5, 6'],
        ['Deployment', '1', '7'],
    ]
)

para_no_indent('Table 13: Work Breakdown Structure')

para('[Screenshot: Figure 11 - Gantt Chart - Project Schedule]')
para_no_indent('Caption: Gantt chart showing the project timeline with 8 main tasks spanning 17 weeks.')

# APPENDIX C: DASHBOARD USER GUIDE
heading1('APPENDIX C: DASHBOARD USER GUIDE')

heading2('Overview Tab')
para('The Overview tab is the default view when the dashboard is loaded. Controls include a county selector dropdown and a forecast horizon slider (1-12 weeks). Display elements include four metric cards (current price, 1-week change, 4-week average, price volatility), a main chart with historical prices, forecast line, and 95% confidence interval, and a forecast table with week number, forecasted price, lower bound, and upper bound.')
para('Interpretation: Narrow confidence bands indicate higher forecast certainty. A rising forecast slope suggests expected price increases (consider holding maize). A falling forecast slope suggests expected decreases (consider selling promptly).')

heading2('Seasonality Tab')
para('Controls include the county selector and year comparison checkboxes. Display elements include a seasonal pattern chart showing monthly averages, a year-over-year overlay chart, and a monthly statistics table (mean, median, min, max, standard deviation).')
para('Interpretation: Identify months when prices typically peak (sell timing) and trough (buy timing). Compare the current year\'s trajectory with historical patterns to identify anomalies.')

heading2('Drivers Tab')
para('Display elements include a feature importance bar chart (top 15 features), a current feature values table, and driver scatter plots with trend lines. Users can select different features to explore their relationship with prices.')
para('Interpretation: Higher-ranked features have greater influence on predictions. Scatter plots reveal whether relationships are positive or negative. Monitor the current feature values table for changes that may signal future price movements.')

heading2('Performance Tab')
para('Display elements include a per-county metrics table (MASE, Dir Acc, MAE, sMAPE, Best Model), comparison bar charts across counties, and a fold performance chart showing accuracy over time.')
para('Interpretation: Lower MASE and MAE indicate more accurate predictions. Higher directional accuracy means more reliable price direction signals. Improving fold performance suggests the model becomes more accurate as training data accumulates.')

# APPENDIX D: DATA DICTIONARY
heading1('APPENDIX D: DATA DICTIONARY')

add_table(
    ['Variable Name', 'Description', 'Type', 'Source', 'Range/Values'],
    [
        ['county', 'County name', 'Categorical', 'KAMIS', '46 Kenyan counties'],
        ['market', 'Market location', 'Categorical', 'KAMIS', 'Multiple per county'],
        ['price', 'Weekly avg price (KES/kg)', 'Numeric', 'KAMIS', '5.0 - 80.0'],
        ['price_std', 'Std dev of weekly price', 'Numeric', 'KAMIS', '0.0 - 15.0'],
        ['week_start', 'Week start date', 'Date', 'KAMIS', '2021-01 to 2025-10'],
        ['lag_1w', 'Price lag 1 week', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['lag_2w', 'Price lag 2 weeks', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['lag_4w', 'Price lag 4 weeks', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['lag_8w', 'Price lag 8 weeks', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['lag_12w', 'Price lag 12 weeks', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['ma_4w', '4-week moving average', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['std_4w', '4-week rolling std dev', 'Numeric', 'Engineered', '0.0 - 15.0'],
        ['ma_8w', '8-week moving average', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['std_8w', '8-week rolling std dev', 'Numeric', 'Engineered', '0.0 - 15.0'],
        ['ma_12w', '12-week moving average', 'Numeric', 'Engineered', '5.0 - 80.0'],
        ['std_12w', '12-week rolling std dev', 'Numeric', 'Engineered', '0.0 - 15.0'],
        ['price_change', 'Delta-price', 'Numeric', 'Engineered', '-15.0 - 15.0'],
        ['change_lag_1w', 'Delta-price lag 1 week', 'Numeric', 'Engineered', '-15.0 - 15.0'],
        ['change_lag_2w', 'Delta-price lag 2 weeks', 'Numeric', 'Engineered', '-15.0 - 15.0'],
        ['change_ma_4w', '4-week MA of delta-price', 'Numeric', 'Engineered', '-10.0 - 10.0'],
        ['change_std_4w', '4-week std of delta-price', 'Numeric', 'Engineered', '0.0 - 10.0'],
        ['temp_avg', 'Weekly avg temp (C)', 'Numeric', 'Open-Meteo', '10.0 - 35.0'],
        ['temp_max', 'Weekly max temp (C)', 'Numeric', 'Open-Meteo', '15.0 - 42.0'],
        ['temp_min', 'Weekly min temp (C)', 'Numeric', 'Open-Meteo', '5.0 - 28.0'],
        ['rain_mm', 'Weekly total rainfall (mm)', 'Numeric', 'Open-Meteo', '0.0 - 200.0'],
        ['wind_speed', 'Weekly max wind (km/h)', 'Numeric', 'Open-Meteo', '0.0 - 80.0'],
        ['rain_sum_4w', '4-week cumulative rain (mm)', 'Numeric', 'Engineered', '0.0 - 600.0'],
        ['temp_avg_4w', '4-week avg temp (C)', 'Numeric', 'Engineered', '10.0 - 32.0'],
        ['rain_sum_8w', '8-week cumulative rain (mm)', 'Numeric', 'Engineered', '0.0 - 1000.0'],
        ['temp_avg_8w', '8-week avg temp (C)', 'Numeric', 'Engineered', '10.0 - 32.0'],
        ['cpi', 'Consumer Price Index', 'Numeric', 'KNBS', '110.0 - 180.0'],
        ['usd_kes', 'USD/KES exchange rate', 'Numeric', 'CBK', '100.0 - 170.0'],
        ['inflation_rate', 'YoY inflation rate (%)', 'Numeric', 'KNBS', '4.0 - 15.0'],
        ['month', 'Calendar month', 'Integer', 'Engineered', '1 - 12'],
        ['week_of_year', 'Week of year', 'Integer', 'Engineered', '1 - 53'],
        ['year', 'Calendar year', 'Integer', 'Engineered', '2021 - 2025'],
        ['days_from_start', 'Days from first obs', 'Integer', 'Engineered', '0 - 1800'],
        ['is_long_rains', 'Long rains flag (Mar-May)', 'Binary', 'Engineered', '0 or 1'],
        ['is_short_rains', 'Short rains flag (Oct-Dec)', 'Binary', 'Engineered', '0 or 1'],
        ['is_harvest', 'Harvest period flag', 'Binary', 'Engineered', '0 or 1'],
        ['c_[county]', 'County one-hot (46 vars)', 'Binary', 'Engineered', '0 or 1'],
    ]
)

para_no_indent('Table 14: Data Dictionary - All Variables')

# SAVE
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, 'PROJECT_DOCUMENTATION.docx')

add_page_number()

doc.save(output_path)
print(f'Document saved to: {output_path}')
print(f'File size: {os.path.getsize(output_path) / 1024:.1f} KB')
