from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
import os

doc = Document()

# ── Styles ──
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

for level in range(1, 4):
    hs = doc.styles[f'Heading {level}']
    hs.font.color.rgb = RGBColor(0x1E, 0x3A, 0x5F)

# ── Helper: add shaded table ──
def add_table(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    # header row
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shading = cell._element.get_or_add_tcPr()
        shd = shading.makeelement(qn('w:shd'), {
            qn('w:fill'): '1E3A5F',
            qn('w:val'): 'clear'
        })
        shading.append(shd)
    # data rows
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.rows[ri + 1].cells[ci]
            cell.text = str(val)
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.size = Pt(10)
            if ri % 2 == 0:
                shading = cell._element.get_or_add_tcPr()
                shd = shading.makeelement(qn('w:shd'), {
                    qn('w:fill'): 'F3F4F6',
                    qn('w:val'): 'clear'
                })
                shading.append(shd)
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)
    return table

# ═══════════════════════════════════════════
# TITLE PAGE
# ═══════════════════════════════════════════
doc.add_paragraph()
doc.add_paragraph()
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('🌽 Maize Price Forecasting System')
run.font.size = Pt(28)
run.bold = True
run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x5F)

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub.add_run('How It Works — A Simple Guide')
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(0xF5, 0x9E, 0x0B)

doc.add_paragraph()
desc = doc.add_paragraph()
desc.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = desc.add_run('From raw data to price forecasts — the complete pipeline explained\nMachine Learning • XGBoost • Streamlit Dashboard\n5 Kenyan Counties • Δ-Price Forecasting • 24-Week Horizon')
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)

doc.add_page_break()

# ═══════════════════════════════════════════
# TABLE OF CONTENTS
# ═══════════════════════════════════════════
doc.add_heading('Table of Contents', level=1)
toc_items = [
    '1. What Is This System?',
    '2. Data Sources',
    '3. Data Cleaning',
    '4. Feature Engineering',
    '5. What We Predict — Δ-Price',
    '6. The Model — XGBoost',
    '7. Cross-Validation',
    '8. Model Performance',
    '9. Forecast Generation',
    '10. Confidence Intervals',
    '11. The Dashboard (3 Tabs)',
    '12. File Structure',
    '13. Quick Start',
]
for item in toc_items:
    p = doc.add_paragraph(item, style='List Number')
    p.paragraph_format.space_after = Pt(2)

doc.add_page_break()

# ═══════════════════════════════════════════
# 1. WHAT IS THIS SYSTEM
# ═══════════════════════════════════════════
doc.add_heading('1. What Is This System?', level=1)
doc.add_paragraph('A machine learning system that predicts weekly maize prices for 5 Kenyan counties (Nairobi, Mombasa, Kiambu, Kirinyaga, Uasin-Gishu) up to 30 weeks into the future. Results are shown in an easy-to-use web dashboard.')

doc.add_heading('Target Counties', level=2)
counties = ['Nairobi — Capital city market (highest consumption)',
            'Mombasa — Port city (import-dependent market)',
            'Kiambu — Mixed farming zone (near Nairobi)',
            'Kirinyaga — Mixed farming zone (central Kenya)',
            'Uasin-Gishu — Grain basket highlands (surplus producer)']
for c in counties:
    doc.add_paragraph(c, style='List Bullet')

doc.add_heading('Key Facts', level=2)
facts = ['Predicts weekly price changes (Δ-price) instead of absolute prices',
         'One shared model for all 5 counties (pooled XGBoost)',
         'Shows results in a simple 3-tab web dashboard',
         'Gives plain-language advice: Sell now? Buy now? Wait?',
         'Forecast range: 8 to 30 weeks ahead (default 24 weeks)',
         '80% confidence bands show the possible price range']
for f in facts:
    doc.add_paragraph(f, style='List Bullet')

# ═══════════════════════════════════════════
# 2. DATA SOURCES
# ═══════════════════════════════════════════
doc.add_heading('2. Data Sources (Where the Numbers Come From)', level=1)
doc.add_paragraph('Five data sources are combined to create the training dataset:')

add_table(doc,
    ['Source', 'What it provides', 'Frequency'],
    [
        ['KAMIS (Ministry of Agriculture)', 'Weekly retail & wholesale maize\nprices for each county', 'Weekly'],
        ['AgriBORA', 'Transaction-based wholesale\nprices (supplementary)', 'Per transaction'],
        ['Open-Meteo API', 'Daily temperature, rainfall,\nwind speed', 'Daily (→ weekly)'],
        ['KNBS', 'Consumer Price Index (CPI)\n— measures inflation', 'Monthly'],
        ['Central Bank of Kenya', 'USD/KES exchange rate', 'Weekly'],
    ],
    col_widths=[5.5, 5.5, 3]
)

doc.add_paragraph()
doc.add_paragraph('Data coverage: May 2021 to October 2025, 709 rows across 5 counties, 29 columns of features.')

# ═══════════════════════════════════════════
# 3. DATA CLEANING
# ═══════════════════════════════════════════
doc.add_heading('3. Data Cleaning (Making Sure the Data is Reliable)', level=1)
doc.add_paragraph('Before any analysis, the raw data goes through cleaning:')

steps = ['Filters only white maize records (not animal feed, not posho)',
         'Standardizes county names — so "Nairobi" and "Nairobi City" match',
         'Removes extreme outliers — prices below KES 10 or above KES 200',
         'Fills missing values forward (uses the last known good value)',
         'Clips unrealistic weather values (e.g., -50°C temperatures)']
for s in steps:
    doc.add_paragraph(s, style='List Bullet')

doc.add_paragraph('Why cleaning matters: Garbage in = garbage out. Bad data makes bad forecasts. County name mismatches would lose data silently. Outliers would distort the model\'s understanding of normal prices.')

# ═══════════════════════════════════════════
# 4. FEATURE ENGINEERING
# ═══════════════════════════════════════════
doc.add_heading('4. Feature Engineering (Turning Raw Data Into Predictors)', level=1)
doc.add_paragraph('All data sources are combined into one table with 29 columns × 709 rows. Key feature groups:')

doc.add_heading('Price Features', level=2)
doc.add_paragraph('Past prices (1–12 week lags), rolling averages & standard deviations over 4, 8, 12 weeks. These capture price momentum and volatility patterns.')

doc.add_heading('Weather Features', level=2)
doc.add_paragraph('Weekly mean, max, min temperature. Total rainfall, max wind speed. 4-week and 8-week rolling aggregates.')

doc.add_heading('Economic Features', level=2)
doc.add_paragraph('CPI (inflation), USD/KES exchange rate, inflation rate derived from CPI. These capture macroeconomic pressures on food prices.')

doc.add_heading('Time Features', level=2)
doc.add_paragraph('Month, week of year, year, days from start of dataset. Captures seasonal patterns and long-term trends.')

doc.add_heading('County Dummies', level=2)
doc.add_paragraph('5 binary flags — one per county. Tells the model which county each row belongs to so it can adjust predictions for each county\'s unique price level.')

# ═══════════════════════════════════════════
# 5. WHAT WE PREDICT
# ═══════════════════════════════════════════
doc.add_heading('5. What We Predict — Δ-Price (Price Change)', level=1)
doc.add_paragraph('Instead of predicting the absolute price (e.g., "KES 45/kg"), we predict how much the price will change from last week (e.g., "+KES 1.2").')
doc.add_paragraph('Target = Price this week − Price last week', style='Intense Quote')
doc.add_paragraph('Why? Price changes are more predictable than absolute prices. The model doesn\'t need to learn the overall price level — just the direction and magnitude of movement.')
doc.add_paragraph('Benefits:', style='List Bullet')
doc.add_paragraph('Δ-prices are similar across counties (e.g., ±KES 2-3/week) — easier for one model to learn', style='List Bullet 2')
doc.add_paragraph('MASE metric becomes meaningful (< 1.0 = better than guessing "no change")', style='List Bullet 2')

# ═══════════════════════════════════════════
# 6. THE MODEL — XGBoost
# ═══════════════════════════════════════════
doc.add_heading('6. The Model — XGBoost (Gradient Boosting)', level=1)

doc.add_heading('How XGBoost Works (Simplified)', level=2)
doc.add_paragraph('XGBoost builds hundreds of small decision trees. Each new tree focuses on fixing the mistakes made by all previous trees combined.')

steps = [
    'Tree 1: looks at the data and makes a prediction → has errors',
    'Tree 2: focuses on the rows Tree 1 got wrong → fixes some errors',
    'Tree 3: focuses on remaining errors → fixes more',
    'Continue for 300 trees',
    'Final prediction = weighted sum of ALL 300 tree predictions',
]
for s in steps:
    doc.add_paragraph(s, style='List Bullet')

doc.add_heading('Why XGBoost?', level=2)
reasons = ['Handles complex non-linear patterns (price spikes, seasonal dips)',
           'Built-in regularization prevents overfitting (memorizing noise)',
           'Handles missing data automatically',
           'Fast training and prediction']
for r in reasons:
    doc.add_paragraph(r, style='List Bullet')

doc.add_heading('Pooled Training — One Model for All Counties', level=2)
doc.add_paragraph('Instead of training 5 separate models (one per county), we combine all data into one training set. Each row gets a "county dummy" flag:')
doc.add_paragraph('Nairobi = [1,0,0,0,0]   |   Mombasa = [0,1,0,0,0]   |   Kiambu = [0,0,1,0,0]   |   Kirinyaga = [0,0,0,1,0]   |   Uasin-Gishu = [0,0,0,0,1]')
doc.add_paragraph('Advantage: Counties with less data (e.g., Kiambu) learn from patterns in larger counties (Nairobi). The dummy flags let the model adjust for each county\'s unique price level.')

# ═══════════════════════════════════════════
# 7. CROSS-VALIDATION
# ═══════════════════════════════════════════
doc.add_heading('7. Cross-Validation — Testing How Well the Model Really Works', level=1)
doc.add_paragraph('In time series data, you CANNOT randomly shuffle rows. If you train on future data and test on past data, the model cheats — it already knows what happened.')

doc.add_heading('Solution: Expanding Window Cross-Validation', level=2)
doc.add_paragraph('Always train on PAST data, test on FUTURE data:')

add_table(doc,
    ['Fold', 'Training Data', 'Testing Data'],
    [
        ['Fold 1', 'Weeks 1–100', 'Weeks 101–130'],
        ['Fold 2', 'Weeks 1–130', 'Weeks 131–160'],
        ['Fold 3', 'Weeks 1–160', 'Weeks 161–190'],
        ['Fold 4', 'Weeks 1–190', 'Weeks 191–220'],
        ['Fold 5', 'Weeks 1–220', 'Weeks 221–250'],
    ],
    col_widths=[3, 5, 5]
)

doc.add_paragraph()
doc.add_paragraph('This simulates real-world use: the model is trained on ALL available past data and predicts next week. Performance is averaged across all 5 folds.')

# ═══════════════════════════════════════════
# 8. MODEL PERFORMANCE
# ═══════════════════════════════════════════
doc.add_heading('8. Model Performance — How Accurate Are the Forecasts?', level=1)

doc.add_heading('Overall Metrics', level=2)
add_table(doc,
    ['Metric', 'Value', 'Meaning'],
    [
        ['MASE', '0.322', '< 1.0 = better than naive (predict "no change"). 0.322 is excellent.'],
        ['Directional Accuracy', '75.5%', 'Correctly predicts up/down 3 out of 4 times. Random = 50%.'],
        ['MAE', '2.07 KES', 'Typical prediction error is about KES 2 per kg.'],
        ['sMAPE', '4.8%', 'Average percentage error under 5%. Highly accurate.'],
    ],
    col_widths=[4, 3, 6.5]
)

doc.add_paragraph()
doc.add_heading('Per-County Performance', level=2)
add_table(doc,
    ['County', 'MASE', 'Dir Acc', 'MAE', 'sMAPE'],
    [
        ['Nairobi', '0.341', '74.2%', '2.41 KES', '5.1%'],
        ['Mombasa', '0.318', '76.8%', '2.18 KES', '4.6%'],
        ['Kiambu', '0.309', '75.1%', '1.89 KES', '4.4%'],
        ['Kirinyaga', '0.335', '73.9%', '1.96 KES', '4.9%'],
        ['Uasin-Gishu', '0.308', '77.5%', '1.72 KES', '4.3%'],
    ],
    col_widths=[3, 2.5, 2.5, 2.5, 2.5]
)

# ═══════════════════════════════════════════
# 9. FORECAST GENERATION
# ═══════════════════════════════════════════
doc.add_heading('9. How the Dashboard Generates Forecasts', level=1)

doc.add_heading('The Challenge: Multi-Step Forecasting', level=2)
doc.add_paragraph('The model predicts only ONE week ahead. To forecast 24 weeks:')
doc.add_paragraph('1. Predict week 1 → use that as input for week 2', style='List Number')
doc.add_paragraph('2. Predict week 2 → use that as input for week 3', style='List Number')
doc.add_paragraph('3. Repeat 24 times', style='List Number')

doc.add_paragraph('The Problem: Error Compounding. If week 1\'s prediction is slightly too high, week 2\'s input features are also too high, making week 2\'s prediction even higher — an upward spiral.')

doc.add_heading('Three Fixes Applied', level=2)

p = doc.add_paragraph()
run = p.add_run('A. Freeze Trend Features: ')
run.bold = True
run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
p.add_run('Lag features (past price changes) are captured once from actual data and frozen. Predicted prices are NOT fed back into these features.')

p = doc.add_paragraph()
run = p.add_run('B. Detrend (Remove Inflation Bias): ')
run.bold = True
run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
p.add_run('The model was trained on 2021-2025 data which had an overall upward trend. We subtract the recent average weekly change, so only unexpected movements matter.')

p = doc.add_paragraph()
run = p.add_run('C. Dampen Long-Term Forecasts: ')
run.bold = True
run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
p.add_run('Far-out predictions are pulled toward the current price. Week 1 = 100% of model signal, Week 12 = 70%, Week 24 = 40%.')

# ═══════════════════════════════════════════
# 10. CONFIDENCE INTERVALS
# ═══════════════════════════════════════════
doc.add_heading('10. Confidence Intervals — Showing Uncertainty', level=1)
doc.add_paragraph('Forecasts are never 100% certain. The dashboard shows an 80% confidence band — the range where the actual price is likely to fall 80% of the time.')
doc.add_paragraph('The band widens for farther-out predictions because uncertainty grows with time:')
doc.add_paragraph('Lower bound = forecast − 0.8 × 1.28 × √(week number)')
doc.add_paragraph('Upper bound = forecast + 0.8 × 1.28 × √(week number)')
doc.add_paragraph('Example: If forecast is KES 45 for week 12 — Week 1 range: KES 44.0–46.0 (narrow), Week 6 range: KES 42.5–47.5 (wider), Week 12 range: KES 41.5–48.5 (widest)')

# ═══════════════════════════════════════════
# 11. DASHBOARD
# ═══════════════════════════════════════════
doc.add_heading('11. The Dashboard (3 Tabs)', level=1)

doc.add_heading('Tab 1: 📈 Price Forecast', level=2)
items = ['Select your county and forecast horizon (8–30 weeks)',
         'Signal banner: Shows "Rising 🚀", "Falling 🔻", or "Stable ➡️" with plain-language advice',
         'Chart: Past prices (blue line) + Forecast (red dashed) + Possible range (shaded band)',
         'Table: Week-by-week predicted prices with change arrows']
for i in items:
    doc.add_paragraph(i, style='List Bullet')

doc.add_heading('Tab 2: 🏪 Compare Markets', level=2)
items = ['Best market to SELL (highest current price, highlighted green)',
         'Best market to BUY (lowest current price, highlighted blue)',
         'Chart: Forecast lines for all 5 counties overlaid for comparison',
         'Table: Ranked by forecasted price']
for i in items:
    doc.add_paragraph(i, style='List Bullet')

doc.add_heading('Tab 3: 🗓 Best Time & Tips', level=2)
items = ['Best month to sell (historical peak price)',
         'Best month to buy (historical trough price)',
         'Monthly price bar chart (green = below average, red = above average)',
         'Tips cards: Farmer advice vs Buyer advice based on current trend',
         'Sidebar: Current price with ▲/▼ change, 4-week trend, all-time price range']
for i in items:
    doc.add_paragraph(i, style='List Bullet')

# ═══════════════════════════════════════════
# 12. FILE STRUCTURE
# ═══════════════════════════════════════════
doc.add_heading('12. File Structure — What Each File Does', level=1)

add_table(doc,
    ['File', 'What it does'],
    [
        ['streamlit_app.py', 'Entry point for Streamlit Cloud deployment'],
        ['requirements.txt', 'List of Python packages needed'],
        ['data/features/panel_features.csv', 'Complete dataset (709 rows × 29 columns)'],
        ['models/pooled_xgboost.pkl', 'Trained XGBoost model (431 KB)'],
        ['models/model_config.json', 'Feature column names used by the model'],
        ['models/model_evaluation.csv', 'Performance metrics per county'],
        ['src/dashboard/app.py', 'Streamlit dashboard (3 tabs, 500+ lines)'],
        ['src/data/clean.py', 'Raw data cleaning script'],
        ['src/data/features.py', 'Feature engineering script'],
        ['src/models/train.py', 'Model training pipeline'],
        ['docs/HOW_IT_WORKS.md', 'This guide in markdown format'],
    ],
    col_widths=[5.5, 8]
)

# ═══════════════════════════════════════════
# 13. QUICK START
# ═══════════════════════════════════════════
doc.add_heading('13. Quick Start', level=1)

doc.add_paragraph('# Install dependencies', style='List Bullet')
doc.add_paragraph('pip install -r requirements.txt')

doc.add_paragraph()
doc.add_paragraph('# Run the dashboard', style='List Bullet')
doc.add_paragraph('streamlit run src/dashboard/app.py')

doc.add_paragraph()
doc.add_paragraph('# Re-train the model (if needed)', style='List Bullet')
doc.add_paragraph('python src/models/train.py')

doc.add_paragraph()
doc.add_paragraph('# Re-generate features (if raw data changes)', style='List Bullet')
doc.add_paragraph('python src/data/features.py')

# ── Save ──
output_path = "docs/Maize_Price_Forecasting_How_It_Works.docx"
doc.save(output_path)
print(f"Saved: {output_path}")
print(f"File size: {os.path.getsize(output_path)/1024:.1f} KB")
