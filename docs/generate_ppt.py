from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x1A, 0x1A, 0x1A)
DARK_BG = RGBColor(0x1E, 0x3A, 0x5F)
ACCENT_AMBER = RGBColor(0xF5, 0x9E, 0x0B)
ACCENT_GREEN = RGBColor(0x16, 0xA3, 0x4A)
ACCENT_BLUE = RGBColor(0x3B, 0x82, 0xF6)
ACCENT_ORANGE = RGBColor(0xEA, 0x58, 0x0C)
LIGHT_GRAY = RGBColor(0xF3, 0xF4, 0xF6)
MED_GRAY = RGBColor(0x6B, 0x72, 0x80)
DARK_GRAY = RGBColor(0x37, 0x47, 0x67)

def add_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_shape(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

def add_textbox(slide, left, top, width, height):
    return slide.shapes.add_textbox(left, top, width, height)

def set_text(tf, text, size=18, color=BLACK, bold=False, align=PP_ALIGN.LEFT):
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = align

def add_para(tf, text, size=18, color=BLACK, bold=False, space_before=Pt(6), align=PP_ALIGN.LEFT):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.space_before = space_before
    p.alignment = align
    return p

def bullet(tf, text, size=15, color=DARK_GRAY, bold=False):
    p = tf.add_paragraph()
    p.text = f"• {text}"
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.space_before = Pt(3)
    return p

def section_header(slide, title):
    add_shape(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.1), DARK_BG)
    add_shape(slide, Inches(0), Inches(1.1), Inches(13.333), Inches(0.06), ACCENT_AMBER)
    tb = add_textbox(slide, Inches(0.8), Inches(0.15), Inches(11.5), Inches(0.8))
    set_text(tb.text_frame, title, 28, WHITE, True)

# ═══════════ SLIDE 1 — TITLE ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_BG)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(0.12), ACCENT_AMBER)
add_shape(s, Inches(0), Inches(7.38), Inches(13.333), Inches(0.12), ACCENT_GREEN)

tb = add_textbox(s, Inches(1.5), Inches(1.5), Inches(10.3), Inches(1.2))
set_text(tb.text_frame, "🌽 Maize Price Forecasting System", 42, WHITE, True, PP_ALIGN.CENTER)

tb = add_textbox(s, Inches(1.5), Inches(3.0), Inches(10.3), Inches(0.8))
set_text(tb.text_frame, "How It Works — A Simple Guide", 26, RGBColor(0xFD, 0xE6, 0x8A), False, PP_ALIGN.CENTER)

tb = add_textbox(s, Inches(1.5), Inches(4.2), Inches(10.3), Inches(1.5))
tf = tb.text_frame
set_text(tf, "From raw data to price forecasts — the complete pipeline explained", 18, RGBColor(0x93, 0xC5, 0xFD), False, PP_ALIGN.CENTER)
add_para(tf, "Machine Learning  •  XGBoost  •  Streamlit Dashboard", 16, RGBColor(0x9C, 0xA3, 0xAF), False, Pt(16), PP_ALIGN.CENTER)
add_para(tf, "5 Kenyan Counties  •  Δ-Price Forecasting  •  24-Week Horizon", 16, RGBColor(0x9C, 0xA3, 0xAF), False, Pt(4), PP_ALIGN.CENTER)

# ═══════════ SLIDE 2 — WHAT IS THIS ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "What Is This System?")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(11.5), Inches(5.5))
tf = tb.text_frame
set_text(tf, "A machine learning system that predicts weekly maize prices for 5 Kenyan counties up to 30 weeks into the future.", 18, DARK_GRAY, False)
add_para(tf, "", 10, BLACK, False)
add_para(tf, "Target Counties", 22, DARK_BG, True, Pt(8))
add_para(tf, "  Nairobi (capital city market)   |   Mombasa (port city)   |   Kiambu (mixed farming)", 16, DARK_GRAY, False, Pt(4))
add_para(tf, "  Kirinyaga (mixed farming)      |   Uasin-Gishu (grain basket highlands)", 16, DARK_GRAY, False, Pt(4))
add_para(tf, "", 10, BLACK, False)
add_para(tf, "Key Facts", 22, DARK_BG, True, Pt(8))
bullet(tf, "Predicts weekly price changes (Δ-price) instead of absolute prices")
bullet(tf, "One shared model for all 5 counties (pooled XGBoost)")
bullet(tf, "Shows results in a simple 3-tab web dashboard")
bullet(tf, "Gives plain-language advice: Sell now? Buy now? Wait?")
bullet(tf, "Forecast range: 8 to 30 weeks ahead (default 24 weeks)")
bullet(tf, "80% confidence bands show the possible price range")

# ═══════════ SLIDE 3 — DATA SOURCES ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "1. Data Sources (Where the Numbers Come From)")

tb = add_textbox(s, Inches(0.8), Inches(1.5), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, "Five data sources are combined to create the training dataset:", 18, DARK_GRAY, False)

sources = [
    ("KAMIS (Ministry of Agriculture)", "Weekly retail & wholesale maize prices for each county", ACCENT_AMBER),
    ("AgriBORA", "Transaction-based wholesale prices (supplementary check)", ACCENT_GREEN),
    ("Open-Meteo API (free weather data)", "Daily temperature, rainfall, wind speed for each county", ACCENT_BLUE),
    ("KNBS (Kenya National Bureau of Statistics)", "Monthly Consumer Price Index (CPI) — measures inflation", ACCENT_ORANGE),
    ("Central Bank of Kenya", "Weekly USD/KES exchange rate", RGBColor(0x8B, 0x5C, 0xF6)),
]
for i, (title, desc, color) in enumerate(sources):
    y = 2.3 + i * 1.0
    add_shape(s, Inches(0.8), Inches(y), Inches(0.12), Inches(0.7), color)
    tb = add_textbox(s, Inches(1.2), Inches(y), Inches(5), Inches(0.35))
    set_text(tb.text_frame, title, 16, color, True)
    tb2 = add_textbox(s, Inches(1.2), Inches(y + 0.35), Inches(5), Inches(0.3))
    set_text(tb2.text_frame, desc, 14, DARK_GRAY, False)
    if i == 0:
        tb3 = add_textbox(s, Inches(7), Inches(y), Inches(5.5), Inches(3.5))
        tf = tb3.text_frame
        set_text(tf, "Data Coverage", 18, DARK_BG, True)
        bullet(tf, "Period: May 2021 to October 2025")
        bullet(tf, "709 rows across 5 counties")
        bullet(tf, "29 columns of features")
        bullet(tf, "~142 weeks per county")

# ═══════════ SLIDE 4 — DATA CLEANING ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "Data Cleaning (Making Sure the Data is Reliable)")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "What the cleaning script does:", 20, DARK_BG, True)
bullet(tf, "Filters only white maize records (not animal feed, not posho)")
bullet(tf, "Standardizes county names — so 'Nairobi' and 'Nairobi City' match")
bullet(tf, "Removes extreme outliers: prices below KES 10 or above KES 200")
bullet(tf, "Fills missing values forward (uses the last known good value)")
bullet(tf, "Clips unrealistic weather values (e.g., -50°C temperatures)")

tb2 = add_textbox(s, Inches(7), Inches(1.6), Inches(5.5), Inches(5.3))
tf2 = tb2.text_frame
set_text(tf2, "Why cleaning matters:", 20, DARK_BG, True)
bullet(tf2, "Garbage in = garbage out. Bad data makes bad forecasts")
bullet(tf2, "County name mismatches would lose data silently")
bullet(tf2, "Outliers would distort the model's understanding of normal prices")
bullet(tf2, "Missing values would break the feature engineering pipeline")

# ═══════════ SLIDE 5 — FEATURE ENGINEERING ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "Feature Engineering (Turning Raw Data Into Predictors)")

features = [
    ("📊 Price Features", "Past prices (1–12 week lags), rolling averages & standard deviations over 4, 8, 12 weeks. These capture price momentum and volatility patterns.", ACCENT_ORANGE),
    ("🌦 Weather Features", "Weekly mean, max, min temperature. Total rainfall, max wind speed. 4-week and 8-week rolling aggregates.", ACCENT_BLUE),
    ("💰 Economic Features", "CPI (inflation), USD/KES exchange rate, inflation rate derived from CPI. These capture macroeconomic pressures on food prices.", ACCENT_GREEN),
    ("📅 Time Features", "Month, week of year, year, days from start of dataset. Captures seasonal patterns and long-term trends.", RGBColor(0x8B, 0x5C, 0xF6)),
    ("🏷 County Dummies", "5 binary flags — one per county. Tells the model which county each row belongs to so it can adjust predictions accordingly.", ACCENT_AMBER),
]
for i, (title, desc, color) in enumerate(features):
    col = i % 3
    row = i // 3
    x = 0.8 + col * 4.1
    y = 1.5 + row * 2.9
    add_shape(s, Inches(x), Inches(y), Inches(3.8), Inches(2.5), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(y), Inches(3.8), Inches(0.06), color)
    tb = add_textbox(s, Inches(x + 0.3), Inches(y + 0.2), Inches(3.2), Inches(0.4))
    set_text(tb.text_frame, title, 16, color, True)
    tb2 = add_textbox(s, Inches(x + 0.3), Inches(y + 0.7), Inches(3.2), Inches(1.6))
    set_text(tb2.text_frame, desc, 13, DARK_GRAY, False)

# ═══════════ SLIDE 6 — WHAT WE PREDICT ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "2. What We Predict — Δ-Price (Price Change)")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "Instead of predicting absolute price...", 20, DARK_BG, True)
add_para(tf, 'Absolute price: "What will maize cost next month?"', 16, DARK_GRAY, False, Pt(6))
add_para(tf, "Problem: Absolute prices vary wildly by county (KES 35 to KES 58).", 16, DARK_GRAY, False, Pt(4))
add_para(tf, "The model would need to learn each county's unique price level.", 16, DARK_GRAY, False, Pt(4))
add_para(tf, "", 10, BLACK, False)
set_text(tf, "We predict price CHANGE instead", 20, ACCENT_GREEN, True)
add_para(tf, 'Price change: "Will prices go up or down next week, and by how much?"', 16, DARK_GRAY, False, Pt(6))
add_para(tf, "Target = Price this week − Price last week", 16, ACCENT_GREEN, True, Pt(8))
add_para(tf, "", 8, BLACK, False)
add_para(tf, "Benefits:", 18, DARK_BG, True, Pt(6))
bullet(tf, "Δ-prices are similar across counties (e.g., ±KES 2-3/week)")
bullet(tf, "Easier for one model to learn patterns across all counties")
bullet(tf, "MASE metric becomes meaningful (< 1.0 = better than guessing 'no change')")

tb2 = add_textbox(s, Inches(7), Inches(1.6), Inches(5.5), Inches(5.3))
tf2 = tb2.text_frame
set_text(tf2, "Analogy: Weather Forecast", 20, DARK_BG, True)
add_para(tf2, 'If we said "tomorrow will be 25°C" — that tells you nothing useful.', 16, DARK_GRAY, False, Pt(6))
add_para(tf2, 'But if we say "tomorrow will be 5°C warmer than today" — that\'s actionable.', 16, DARK_GRAY, False, Pt(4))
add_para(tf2, "", 10, BLACK, False)
add_para(tf2, 'Same with prices: "KES 45 next week" is less useful than', 16, DARK_GRAY, False, Pt(4))
add_para(tf2, '"Prices will rise by KES 2 next week."', 16, DARK_GRAY, False, Pt(4))

# ═══════════ SLIDE 7 — XGBoost ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "The Model — XGBoost (Gradient Boosting)")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "How XGBoost works (simplified):", 20, DARK_BG, True)
add_para(tf, "XGBoost builds hundreds of small decision trees. Each new tree focuses on fixing the mistakes made by all previous trees combined.", 16, DARK_GRAY, False, Pt(6))
add_para(tf, "", 8, BLACK, False)
add_para(tf, "Step-by-step:", 18, DARK_BG, True, Pt(4))
bullet(tf, "Tree 1 looks at the data and makes a prediction → has errors")
bullet(tf, "Tree 2 focuses on the rows Tree 1 got wrong → fixes some errors")
bullet(tf, "Tree 3 focuses on remaining errors → fixes more")
bullet(tf, "Continue for 300 trees")
bullet(tf, "Final prediction = weighted sum of ALL 300 tree predictions")
add_para(tf, "", 8, BLACK, False)
add_para(tf, "Why XGBoost?", 18, DARK_BG, True, Pt(4))
bullet(tf, "Handles complex non-linear patterns (price spikes, seasonal dips)")
bullet(tf, "Built-in regularization prevents overfitting (memorizing noise)")
bullet(tf, "Handles missing data automatically")
bullet(tf, "Fast training and prediction")

tb2 = add_textbox(s, Inches(7), Inches(1.6), Inches(5.5), Inches(5.3))
tf2 = tb2.text_frame
set_text(tf2, "Pooled Training — One Model for All Counties", 20, ACCENT_GREEN, True)
add_para(tf2, "", 6, BLACK, False)
add_para(tf2, "Instead of training 5 separate models (one per county), we combine all data into one training set.", 16, DARK_GRAY, False, Pt(4))
add_para(tf2, "", 6, BLACK, False)
add_para(tf2, 'Each row gets a "county dummy" flag:', 16, DARK_GRAY, False, Pt(4))
add_para(tf2, "  Nairobi = [1,0,0,0,0]    Mombasa = [0,1,0,0,0]", 14, MED_GRAY, False, Pt(2))
add_para(tf2, "  Kiambu = [0,0,1,0,0]    Kirinyaga = [0,0,0,1,0]", 14, MED_GRAY, False, Pt(2))
add_para(tf2, "  Uasin-Gishu = [0,0,0,0,1]", 14, MED_GRAY, False, Pt(2))
add_para(tf2, "", 6, BLACK, False)
add_para(tf2, "Advantage:", 16, ACCENT_GREEN, True, Pt(4))
add_para(tf2, "Counties with less data (e.g., Kiambu) learn from patterns in larger counties (Nairobi). The dummy flags let the model adjust for each county's unique price level.", 14, DARK_GRAY, False, Pt(4))

# ═══════════ SLIDE 8 — CROSS-VALIDATION ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "Cross-Validation — Testing How Well the Model Really Works")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "The Problem with Random Train/Test Split:", 20, DARK_BG, True)
add_para(tf, "In time series data, you CANNOT randomly shuffle rows. If you train on future data and test on past data, the model cheats — it already knows what happened.", 16, DARK_GRAY, False, Pt(6))
add_para(tf, "", 8, BLACK, False)
set_text(tf, "Solution: Expanding Window Cross-Validation", 20, ACCENT_GREEN, True)
add_para(tf, "Always train on PAST data, test on FUTURE data:", 16, DARK_GRAY, False, Pt(6))

folds_info = [
    ("Fold 1", "Train: weeks 1-100   →   Test: weeks 101-130"),
    ("Fold 2", "Train: weeks 1-130   →   Test: weeks 131-160"),
    ("Fold 3", "Train: weeks 1-160   →   Test: weeks 161-190"),
    ("Fold 4", "Train: weeks 1-190   →   Test: weeks 191-220"),
    ("Fold 5", "Train: weeks 1-220   →   Test: weeks 221-250"),
]
for label, desc in folds_info:
    p = tf.add_paragraph()
    p.space_before = Pt(3)
    run1 = p.add_run()
    run1.text = f"  {label}:  "
    run1.font.size = Pt(14)
    run1.font.bold = True
    run1.font.color.rgb = ACCENT_GREEN
    run2 = p.add_run()
    run2.text = desc
    run2.font.size = Pt(14)
    run2.font.color.rgb = DARK_GRAY

tb2 = add_textbox(s, Inches(7), Inches(1.6), Inches(5.5), Inches(5.3))
tf2 = tb2.text_frame
set_text(tf2, "This simulates real-world use:", 20, DARK_BG, True)
add_para(tf2, "In real life, the model is trained on ALL available past data and predicts next week. Each fold in cross-validation mimics this exact scenario.", 16, DARK_GRAY, False, Pt(6))
add_para(tf2, "", 8, BLACK, False)
add_para(tf2, "Performance is averaged across all 5 folds.", 16, DARK_GRAY, True, Pt(4))
add_para(tf2, "", 8, BLACK, False)
add_para(tf2, "Result:", 18, ACCENT_AMBER, True, Pt(4))
add_para(tf2, "MASE = 0.322 (well below 1.0 = excellent)", 16, DARK_GRAY, False, Pt(4))
add_para(tf2, "Directional Accuracy = 75.5% (correctly predicts up/down 3 out of 4 times)", 16, DARK_GRAY, False, Pt(2))

# ═══════════ SLIDE 9 — PERFORMANCE ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "Model Performance — How Accurate Are the Forecasts?")

metrics = [
    ("MASE", "0.322", "Mean Absolute Scaled Error\n< 1.0 = better than naive\n(better than guessing 'no change')"),
    ("Directional\nAccuracy", "75.5%", "Correctly predicts whether\nprices go up or down\n3 out of 4 times correct"),
    ("MAE", "2.07 KES", "Mean Absolute Error\nTypical prediction error\n≈ KES 2 per kilogram"),
    ("sMAPE", "4.8%", "Symmetric Mean Absolute\nPercentage Error\nUnder 5% = highly accurate"),
]
for i, (label, value, desc) in enumerate(metrics):
    x = 0.8 + i * 3.15
    add_shape(s, Inches(x), Inches(1.5), Inches(2.9), Inches(2.5), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(1.5), Inches(2.9), Inches(0.06), ACCENT_GREEN)
    tb = add_textbox(s, Inches(x), Inches(1.7), Inches(2.9), Inches(0.5))
    set_text(tb.text_frame, label, 16, MED_GRAY, False, PP_ALIGN.CENTER)
    tb2 = add_textbox(s, Inches(x), Inches(2.2), Inches(2.9), Inches(0.6))
    set_text(tb2.text_frame, value, 34, ACCENT_GREEN, True, PP_ALIGN.CENTER)
    tb3 = add_textbox(s, Inches(x + 0.2), Inches(2.9), Inches(2.5), Inches(0.9))
    set_text(tb3.text_frame, desc, 12, DARK_GRAY, False, PP_ALIGN.CENTER)

# Per-county table
pcounty_data = [
    ["County", "MASE", "Dir Acc", "MAE", "sMAPE"],
    ["Nairobi", "0.341", "74.2%", "2.41 KES", "5.1%"],
    ["Mombasa", "0.318", "76.8%", "2.18 KES", "4.6%"],
    ["Kiambu", "0.309", "75.1%", "1.89 KES", "4.4%"],
    ["Kirinyaga", "0.335", "73.9%", "1.96 KES", "4.9%"],
    ["Uasin-Gishu", "0.308", "77.5%", "1.72 KES", "4.3%"],
]

y = 4.5
cols_p = [1.5, 2.5, 2.5, 2.5, 2.5]
add_shape(s, Inches(1.5), Inches(y), Inches(10), Inches(0.4), DARK_BG)
xp = 1.5
for ci, h in enumerate(["County", "MASE", "Dir Acc", "MAE", "sMAPE"]):
    tb = add_textbox(s, Inches(xp), Inches(y + 0.02), Inches(cols_p[ci]), Inches(0.35))
    set_text(tb.text_frame, h, 13, WHITE, True, PP_ALIGN.CENTER)
    xp += cols_p[ci]
y += 0.4
for row_idx, row in enumerate(pcounty_data[1:]):
    bg = LIGHT_GRAY if row_idx % 2 == 0 else WHITE
    add_shape(s, Inches(1.5), Inches(y), Inches(10), Inches(0.35), bg)
    xp = 1.5
    for ci, val in enumerate(row):
        tb = add_textbox(s, Inches(xp), Inches(y + 0.02), Inches(cols_p[ci]), Inches(0.3))
        set_text(tb.text_frame, val, 12, DARK_GRAY, row_idx == 0, PP_ALIGN.CENTER)
        xp += cols_p[ci]
    y += 0.35

tb = add_textbox(s, Inches(0.8), Inches(y + 0.2), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, "All counties perform well. Pooled model shares strength across counties — Uasin-Gishu (highland grain basket) has the best accuracy with MASE=0.308.", 14, MED_GRAY, False)

# ═══════════ SLIDE 10 — FORECAST GENERATION ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "3. How the Dashboard Generates Forecasts")

tb = add_textbox(s, Inches(0.8), Inches(1.5), Inches(5.5), Inches(5.5))
tf = tb.text_frame
set_text(tf, "The Challenge: Multi-Step Forecasting", 20, DARK_BG, True)
add_para(tf, "The model predicts only ONE week ahead. To forecast 24 weeks:", 16, DARK_GRAY, False, Pt(6))
add_para(tf, "1. Predict week 1 → use that as input for week 2", 15, DARK_GRAY, False, Pt(4))
add_para(tf, "2. Predict week 2 → use that as input for week 3", 15, DARK_GRAY, False, Pt(4))
add_para(tf, "3. Repeat 24 times", 15, DARK_GRAY, False, Pt(4))
add_para(tf, "", 8, BLACK, False)
add_para(tf, "The Problem: Error Compounding", 18, RGBColor(0xDC, 0x26, 0x26), True, Pt(4))
add_para(tf, "If week 1's prediction is slightly too high, week 2's input features are also too high, making week 2's prediction even higher — an upward spiral.", 15, DARK_GRAY, False, Pt(4))

tb2 = add_textbox(s, Inches(7), Inches(1.5), Inches(5.5), Inches(5.5))
tf2 = tb2.text_frame
set_text(tf2, "Three Fixes Applied:", 20, ACCENT_GREEN, True)

add_para(tf2, "", 6, BLACK, False)
add_para(tf2, "A. Freeze Trend Features", 17, ACCENT_BLUE, True, Pt(4))
add_para(tf2, "Lag features (past price changes) are captured once from actual data and frozen. Predicted prices are NOT fed back into these features.", 14, DARK_GRAY, False, Pt(2))
add_para(tf2, "", 6, BLACK, False)
add_para(tf2, "B. Detrend (Remove Inflation Bias)", 17, ACCENT_BLUE, True, Pt(4))
add_para(tf2, "The model was trained on 2021-2025 data that had an overall upward trend. We subtract the recent average weekly change, so only unexpected movements matter.", 14, DARK_GRAY, False, Pt(2))
add_para(tf2, "", 6, BLACK, False)
add_para(tf2, "C. Dampen Long-Term Forecasts", 17, ACCENT_BLUE, True, Pt(4))
add_para(tf2, "Far-out predictions are pulled toward the current price:", 14, DARK_GRAY, False, Pt(2))
add_para(tf2, "  Week 1: 100% of model signal", 13, MED_GRAY, False, Pt(1))
add_para(tf2, "  Week 12: 70% of model signal", 13, MED_GRAY, False, Pt(1))
add_para(tf2, "  Week 24: 40% of model signal", 13, MED_GRAY, False, Pt(1))

# ═══════════ SLIDE 11 — CONFIDENCE INTERVALS ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "Confidence Intervals — Showing Uncertainty")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "Forecasts are never 100% certain.", 22, DARK_BG, True)
add_para(tf, "The dashboard shows an 80% confidence band — the range where the actual price is likely to fall 80% of the time.", 16, DARK_GRAY, False, Pt(8))
add_para(tf, "", 8, BLACK, False)
add_para(tf, "How it works:", 18, DARK_BG, True, Pt(4))
add_para(tf, "The band widens for farther-out predictions because uncertainty grows with time:", 15, DARK_GRAY, False, Pt(4))
add_para(tf, "  Lower bound = forecast − 0.8 × 1.28 × √(week)", 15, MED_GRAY, False, Pt(4))
add_para(tf, "  Upper bound = forecast + 0.8 × 1.28 × √(week)", 15, MED_GRAY, False, Pt(2))

tb2 = add_textbox(s, Inches(7), Inches(1.6), Inches(5.5), Inches(5.3))
tf2 = tb2.text_frame
set_text(tf2, "Example:", 20, DARK_BG, True)
add_para(tf2, 'If forecast is KES 45 for week 12:', 16, DARK_GRAY, False, Pt(6))
add_para(tf2, "  Week 1 range: KES 44.0 – KES 46.0 (narrow)", 14, MED_GRAY, False, Pt(4))
add_para(tf2, "  Week 6 range: KES 42.5 – KES 47.5 (wider)", 14, MED_GRAY, False, Pt(2))
add_para(tf2, "  Week 12 range: KES 41.5 – KES 48.5 (widest)", 14, MED_GRAY, False, Pt(2))
add_para(tf2, "", 8, BLACK, False)
add_para(tf2, "In the dashboard chart:", 18, DARK_BG, True, Pt(4))
add_para(tf2, "• Blue line = actual historical prices", 14, ACCENT_BLUE, False, Pt(4))
add_para(tf2, "• Red dashed line = forecast (best guess)", 14, RGBColor(0xDC, 0x26, 0x26), False, Pt(2))
add_para(tf2, "• Pink shaded band = possible range", 14, RGBColor(0xF9, 0xA8, 0xA8), False, Pt(2))

# ═══════════ SLIDE 12 — DASHBOARD ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "4. The Dashboard (3 Tabs)")

tabs_info = [
    ("📈 Price Forecast", ACCENT_GREEN,
     "Select your county → see the outlook\n\n"
     "• Signal banner: Rising 🚀 / Falling 🔻 / Stable ➡️\n"
     "• Plain-language advice: Sell now? Buy now? Wait?\n"
     "• 12-week forecast chart with confidence bands\n"
     "• Week-by-week predicted prices table"),
    ("🏪 Compare Markets", ACCENT_BLUE,
     "See all 5 counties side-by-side\n\n"
     "• Best market to SELL (highest price) — green\n"
     "• Best market to BUY (lowest price) — blue\n"
     "• Multi-county forecast comparison chart\n"
     "• Ranked table by forecasted price"),
    ("🗓 Best Time & Tips", ACCENT_ORANGE,
     "Seasonal timing advice\n\n"
     "• Best month to sell (peak price)\n"
     "• Best month to buy (trough price)\n"
     "• Monthly price bar chart (green/red)\n"
     "• Tips: Farmer vs Buyer advice cards\n"
     "• Simple explanations of price drivers"),
]
for i, (title, color, items) in enumerate(tabs_info):
    x = 0.8 + i * 4.1
    add_shape(s, Inches(x), Inches(1.5), Inches(3.8), Inches(5.5), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(1.5), Inches(3.8), Inches(0.06), color)
    tb = add_textbox(s, Inches(x + 0.3), Inches(1.7), Inches(3.2), Inches(5))
    tf = tb.text_frame
    set_text(tf, title, 20, color, True)
    for line in items.split("\n"):
        add_para(tf, line, 13, DARK_GRAY if line.strip().startswith("•") else MED_GRAY, False, Pt(2))

# ═══════════ SLIDE 13 — SIDEBAR + DEPLOY ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "Sidebar KPIs & Deployment")

tb = add_textbox(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "Sidebar (Key Numbers at a Glance)", 20, DARK_BG, True)
add_para(tf, "On every page, the sidebar shows:", 16, DARK_GRAY, False, Pt(6))
bullet(tf, "Current Price — with ▲/▼ weekly change arrow")
bullet(tf, "4-Week Trend — how much prices moved over the last month")
bullet(tf, "All-Time Range — lowest and highest price ever recorded")
bullet(tf, "County selector — switch counties anytime")
bullet(tf, "Look-ahead slider — choose 8 to 30 weeks")

tb2 = add_textbox(s, Inches(7), Inches(1.6), Inches(5.5), Inches(5.3))
tf2 = tb2.text_frame
set_text(tf2, "Deployment (How to Access)", 20, DARK_BG, True)
add_para(tf2, "The dashboard is deployed on Streamlit Cloud:", 16, DARK_GRAY, False, Pt(6))
bullet(tf2, "Free cloud hosting — no server to manage")
bullet(tf2, "Auto-deploys on every git push to main branch")
bullet(tf2, "Public URL — share with anyone")
bullet(tf2, "GitHub repo: github.com/Timinah-rt/Maize_project")
add_para(tf2, "", 8, BLACK, False)
add_para(tf2, "To run locally:", 16, ACCENT_GREEN, True, Pt(4))
add_para(tf2, "  pip install -r requirements.txt", 14, MED_GRAY, False, Pt(2))
add_para(tf2, "  streamlit run src/dashboard/app.py", 14, MED_GRAY, False, Pt(2))

# ═══════════ SLIDE 14 — FILE STRUCTURE ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
section_header(s, "File Structure — What Each File Does")

files = [
    ("streamlit_app.py", "Entry point for Streamlit Cloud deployment", ACCENT_GREEN),
    ("requirements.txt", "List of Python packages needed (dependencies)", ACCENT_BLUE),
    ("data/features/panel_features.csv", "The complete dataset (709 rows, 29 columns)", ACCENT_AMBER),
    ("models/pooled_xgboost.pkl", "The trained XGBoost model (431 KB)", ACCENT_ORANGE),
    ("models/model_config.json", "List of feature column names used by the model", RGBColor(0x8B, 0x5C, 0xF6)),
    ("models/model_evaluation.csv", "Performance metrics per county", ACCENT_GREEN),
    ("src/dashboard/app.py", "Streamlit dashboard (3 tabs, 500+ lines)", ACCENT_BLUE),
    ("src/data/clean.py", "Raw data cleaning script", ACCENT_AMBER),
    ("src/data/features.py", "Feature engineering script", ACCENT_ORANGE),
    ("src/models/train.py", "Model training pipeline (XGBoost + CV)", RGBColor(0xEC, 0x48, 0x99)),
    ("docs/HOW_IT_WORKS.md", "This guide in markdown format", ACCENT_GREEN),
]
for i, (name, desc, color) in enumerate(files):
    col = i % 2
    row = i // 2
    x = 0.8 + col * 6.2
    y = 1.5 + row * 0.95
    add_shape(s, Inches(x), Inches(y), Inches(0.08), Inches(0.7), color)
    tb = add_textbox(s, Inches(x + 0.3), Inches(y), Inches(5.5), Inches(0.35))
    set_text(tb.text_frame, name, 15, color, True)
    tb2 = add_textbox(s, Inches(x + 0.3), Inches(y + 0.35), Inches(5.5), Inches(0.3))
    set_text(tb2.text_frame, desc, 13, DARK_GRAY, False)

# ═══════════ SLIDE 15 — THANK YOU ═══════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_BG)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(0.12), ACCENT_AMBER)
add_shape(s, Inches(0), Inches(7.38), Inches(13.333), Inches(0.12), ACCENT_GREEN)

tb = add_textbox(s, Inches(1.5), Inches(1.2), Inches(10.3), Inches(1))
set_text(tb.text_frame, "Summary", 40, WHITE, True, PP_ALIGN.CENTER)

tb = add_textbox(s, Inches(1.5), Inches(2.5), Inches(10.3), Inches(4))
tf = tb.text_frame
set_text(tf, "The system takes raw price data from 5 sources,", 20, RGBColor(0xFD, 0xE6, 0x8A), False, PP_ALIGN.CENTER)
add_para(tf, "engineers 29 predictive features, trains a pooled XGBoost model,", 20, RGBColor(0xFD, 0xE6, 0x8A), False, Pt(4), PP_ALIGN.CENTER)
add_para(tf, "and shows the results in a farmer-friendly dashboard.", 20, RGBColor(0xFD, 0xE6, 0x8A), False, Pt(4), PP_ALIGN.CENTER)
add_para(tf, "", 12, WHITE, False, Pt(20))
add_para(tf, "Key Results:", 22, WHITE, True, Pt(4), PP_ALIGN.CENTER)
add_para(tf, "MASE = 0.322  |  Directional Accuracy = 75.5%", 18, ACCENT_GREEN, False, Pt(8), PP_ALIGN.CENTER)
add_para(tf, "MAE = 2.07 KES  |  sMAPE = 4.8%", 18, ACCENT_GREEN, False, Pt(4), PP_ALIGN.CENTER)
add_para(tf, "", 12, WHITE, False, Pt(20))
add_para(tf, "🌽  Maize Price Forecasting System  •  2025", 18, RGBColor(0x93, 0xC5, 0xFD), False, Pt(4), PP_ALIGN.CENTER)

output_path = "docs/Maize_Price_Forecasting_Presentation.pptx"
prs.save(output_path)
print(f"Saved to {output_path}")
print(f"Slides: {len(prs.slides)}")
