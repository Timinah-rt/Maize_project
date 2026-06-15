from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x1A, 0x1A, 0x1A)
DARK_BG = RGBColor(0x1E, 0x3A, 0x5F)
AMBER = RGBColor(0xF5, 0x9E, 0x0B)
GREEN = RGBColor(0x16, 0xA3, 0x4A)
BLUE = RGBColor(0x3B, 0x82, 0xF6)
ORANGE = RGBColor(0xEA, 0x58, 0x0C)
RED = RGBColor(0xDC, 0x26, 0x26)
PURPLE = RGBColor(0x8B, 0x5C, 0xF6)
LGRAY = RGBColor(0xF3, 0xF4, 0xF6)
MGRAY = RGBColor(0x6B, 0x72, 0x80)
DGRAY = RGBColor(0x37, 0x47, 0x67)

def bg(slide, color):
    slide.background.fill.solid(); slide.background.fill.fore_color.rgb = color

def rect(slide, l, t, w, h, c):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    s.fill.solid(); s.fill.fore_color.rgb = c; s.line.fill.background()
    return s

def tb(slide, l, t, w, h):
    return slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))

def setp(tf, text, size=18, color=BLACK, bold=False, align=PP_ALIGN.LEFT):
    tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = text; p.font.size = Pt(size)
    p.font.color.rgb = color; p.font.bold = bold; p.alignment = align

def addp(tf, text, size=18, color=BLACK, bold=False, sp=Pt(6), align=PP_ALIGN.LEFT):
    p = tf.add_paragraph(); p.text = text; p.font.size = Pt(size)
    p.font.color.rgb = color; p.font.bold = bold; p.space_before = sp; p.alignment = align

def bul(tf, text, size=15, color=DGRAY, bold=False):
    p = tf.add_paragraph(); p.text = f"• {text}"; p.font.size = Pt(size)
    p.font.color.rgb = color; p.font.bold = bold; p.space_before = Pt(3)

def head(slide, title):
    rect(slide, 0, 0, 13.333, 1.1, DARK_BG)
    rect(slide, 0, 1.1, 13.333, 0.06, AMBER)
    tx = tb(slide, 0.8, 0.15, 11.5, 0.8)
    setp(tx.text_frame, title, 30, WHITE, True)

# ──── SLIDE 1: TITLE ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, DARK_BG)
rect(s, 0, 0, 13.333, 0.12, AMBER); rect(s, 0, 7.38, 13.333, 0.12, GREEN)
tx = tb(s, 1.5, 1.2, 10.3, 1.2); setp(tx.text_frame, "🌽 MAIZE PRICE FORECASTING SYSTEM", 44, WHITE, True, PP_ALIGN.CENTER)
tx = tb(s, 1.5, 2.6, 10.3, 0.8); setp(tx.text_frame, "Machine Learning-Based Weekly Price Prediction for Kenyan Counties", 24, RGBColor(0xFD,0xE6,0x8A), False, PP_ALIGN.CENTER)
tx = tb(s, 1.5, 3.8, 10.3, 1.5)
tf = tx.text_frame; setp(tf, "A Pooled XGBoost Approach with County-Level Fine-Tuning", 20, RGBColor(0x93,0xC5,0xFD), False, PP_ALIGN.CENTER)
addp(tf, "Interactive Streamlit Dashboard  •  Expanding Window Cross-Validation  •  MASE & Directional Accuracy", 16, RGBColor(0x9C,0xA3,0xAF), False, Pt(12), PP_ALIGN.CENTER)
addp(tf, "5 Kenyan Counties  •  Δ-Price Forecasting  •  24-Week Forecast Horizon", 16, RGBColor(0x9C,0xA3,0xAF), False, Pt(4), PP_ALIGN.CENTER)
addp(tf, "", 10, WHITE, False, Pt(20))
addp(tf, "Presented by: Timinah  |  2025", 18, WHITE, True, Pt(4), PP_ALIGN.CENTER)

# ──── SLIDE 2: TABLE OF CONTENTS ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE)
rect(s, 0, 0, 0.25, 7.5, AMBER)
tx = tb(s, 1, 0.4, 11, 0.8); setp(tx.text_frame, "TABLE OF CONTENTS", 32, DARK_BG, True)

sections = [
    ("1", "Introduction", "Project overview, background & importance of maize in Kenya"),
    ("2", "Problem Statement", "Key challenges across the maize value chain"),
    ("3", "Current System vs. To-Be System", "How forecasting is done now vs. how it will be done"),
    ("4", "Proposed Solution", "ML-based forecasting system architecture"),
    ("5", "Research Objectives / Questions", "Main objective & specific research questions"),
    ("6", "Source of Data", "KAMIS, AgriBORA, Weather & Economic data sources"),
    ("7", "Project Pipeline", "Complete workflow from data collection to dashboard"),
    ("8", "Model Performance", "MASE, Directional Accuracy, MAE, sMAPE results"),
    ("9", "Dashboard Demonstration", "Practical walkthrough of all 3 tabs"),
    ("10", "Limitations", "Current system constraints"),
    ("11", "Future Work", "Planned improvements & extensions"),
]
y = 1.5
for n, t, d in sections:
    tx = tb(s, 1.2, y, 11, 0.55)
    tf = tx.text_frame; setp(tf, f"  {n}.  {t}", 20, DARK_BG, True)
    addp(tf, f"         {d}", 14, MGRAY, False)
    y += 0.55

# ──── SLIDE 3: INTRODUCTION ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "1. INTRODUCTION — What Is This Project?")

tx = tb(s, 0.8, 1.5, 5.8, 5.5)
tf = tx.text_frame
setp(tf, "Project Overview", 22, DARK_BG, True)
addp(tf, "A machine learning-based system that predicts weekly maize prices for 5 major Kenyan counties up to 30 weeks ahead, presented through a farmer-friendly web dashboard.", 16, DGRAY, False, Pt(6))
addp(tf, "", 8, WHITE, False)
addp(tf, "Why Maize Matters in Kenya", 22, DARK_BG, True, Pt(8))
addp(tf, "• 4.5 million smallholder farmers grow maize", 15, DGRAY, False, Pt(4))
addp(tf, "• Average Kenyan consumes 98 kg of maize per year", 15, DGRAY, False, Pt(2))
addp(tf, "• Annual production: ~40 million bags (90 kg each)", 15, DGRAY, False, Pt(2))
addp(tf, "• Annual consumption: ~44 million bags — structural deficit", 15, DGRAY, False, Pt(2))
addp(tf, "• 10 million people employed across the value chain", 15, DGRAY, False, Pt(2))
addp(tf, "• Agriculture contributes 33% to Kenya's GDP", 15, DGRAY, False, Pt(2))

tx2 = tb(s, 7.3, 1.5, 5.3, 5.5)
tf2 = tx2.text_frame
setp(tf2, "5 Target Counties", 22, DARK_BG, True)
addp(tf2, "", 6, WHITE, False)
for nm, desc in [("Nairobi", "Capital — largest consumer market"),
                 ("Mombasa", "Port city — import-dependent"),
                 ("Kiambu", "Mixed farming — near Nairobi"),
                 ("Kirinyaga", "Mixed farming — central Kenya"),
                 ("Uasin-Gishu", "Grain basket — surplus producer")]:
    addp(tf2, f"  {nm}", 16, BLUE, True, Pt(4))
    addp(tf2, f"    {desc}", 14, MGRAY, False, Pt(1))

addp(tf2, "", 8, WHITE, False)
addp(tf2, "Price Volatility", 22, DARK_BG, True, Pt(8))
addp(tf2, "Nairobi prices range from KES 30 to KES 58/kg — a 93% swing. A 90 kg bag fluctuates from KES 2,520 to KES 4,680.", 15, DGRAY, False, Pt(4))

# ──── SLIDE 4: PROBLEM STATEMENT ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "2. PROBLEM STATEMENT")

stakeholders = [
    ("👨‍🌾 Farmers", "#fff7ed", ORANGE, "Distress sales at harvest low\nLost income: up to KES 40,000/season\nNo price information to plan when to sell"),
    ("🏪 Traders & Millers", "#f0fdf4", GREEN, "Weekly procurement: KES 2.8-5.2M\nCan't hedge against price swings\nStock-out vs. overstocking dilemma"),
    ("🏛 Policymakers", "#eff6ff", BLUE, "Reactive crisis response only\nImport permits issued after prices spike\nNo early warning system for food security"),
    ("👪 Consumers", "#fef2f2", RED, "30% of food budget on maize\nPrice spikes add KES 800/month\nVulnerable households pushed into insecurity"),
]
xs = [0.8, 6.9, 0.8, 6.9]; ys = [1.5, 1.5, 4.2, 4.2]
for (t, bgc, brd, txt), x, y in zip(stakeholders, xs, ys):
    r2,g2,b2 = int(bgc[1:3],16),int(bgc[3:5],16),int(bgc[5:7],16)
    rect(s, x, y, 5.6, 2.4, RGBColor(r2,g2,b2))
    rect(s, x, y, 5.6, 0.06, brd)
    tx = tb(s, x+0.3, y+0.2, 5, 2); tf = tx.text_frame
    setp(tf, t, 18, brd, True)
    for ln in txt.split("\n"):
        addp(tf, ln, 13, DGRAY, False, Pt(2))

tx = tb(s, 0.8, 6.8, 11.5, 0.5)
setp(tx.text_frame, "The core problem: No accurate, timely, county-level price forecasts exist for Kenya's maize sector.", 16, RED, True, PP_ALIGN.CENTER)

# ──── SLIDE 5: CURRENT VS TO-BE ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "3. CURRENT SYSTEM vs. TO-BE SYSTEM")

# Current
rect(s, 0.8, 1.5, 5.8, 5.5, RGBColor(0xFE,0xF2,0xF2))
rect(s, 0.8, 1.5, 5.8, 0.06, RED)
tx = tb(s, 1.1, 1.7, 5.2, 5); tf = tx.text_frame
setp(tf, "❌ Current System", 22, RED, True)
addp(tf, "", 6, WHITE, False)
bul(tf, "Manual price tracking — farmers ask neighbors or middlemen")
bul(tf, "Expert guesswork — no data-driven forecasts")
bul(tf, "National-level only — misses county-level variations")
bul(tf, "No uncertainty — point estimates without confidence ranges")
bul(tf, "Reactive — only know prices after they've changed")
bul(tf, "Inconsistent — no standardized methodology")
bul(tf, "Limited access — information doesn't reach rural farmers")
bul(tf, "No directional guidance — farmers don't know if prices will rise or fall")

# To-Be
rect(s, 6.7, 1.5, 5.8, 5.5, RGBColor(0xF0,0xFD,0xF4))
rect(s, 6.7, 1.5, 5.8, 0.06, GREEN)
tx = tb(s, 7, 1.7, 5.2, 5); tf = tx.text_frame
setp(tf, "✅ To-Be System (This Project)", 22, GREEN, True)
addp(tf, "", 6, WHITE, False)
bul(tf, "Automated ML-based weekly price forecasts")
bul(tf, "Data-driven — XGBoost trained on 5 data sources")
bul(tf, "County-level — forecasts for each of 5 counties")
bul(tf, "80% confidence bands for risk-based decisions")
bul(tf, "Proactive — predicts 24 weeks ahead")
bul(tf, "Standardized — consistent methodology every week")
bul(tf, "Web-based — accessible from any device, anywhere")
bul(tf, "Directional signals — Rising/Falling/Stable with advice")

# ──── SLIDE 6: SOLUTION OVERVIEW ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "4. PROPOSED SOLUTION — System Architecture")

tx = tb(s, 0.8, 1.5, 5.5, 5.5)
tf = tx.text_frame
setp(tf, "How It Works", 22, DARK_BG, True)
addp(tf, "", 6, WHITE, False)
bul(tf, "Data Integration Layer — 5 sources combined into one dataset")
bul(tf, "Feature Engineering — 30 predictive features from raw data")
bul(tf, "Δ-Price Target — predict week-over-week change (not absolute price)")
bul(tf, "Pooled XGBoost — one model shared across all 5 counties")
bul(tf, "Expanding Window CV — 5-fold temporal cross-validation")
bul(tf, "Auto-Regressive Forecast — 24-week horizon with dampening")
bul(tf, "Interactive Dashboard — 3-tab Streamlit web application")
bul(tf, "Cloud Deployment — hosted on Streamlit Cloud (free)")

tx2 = tb(s, 7, 1.5, 5.5, 5.5)
tf2 = tx2.text_frame
setp(tf2, "Why Machine Learning?", 22, DARK_BG, True)
addp(tf2, "", 6, WHITE, False)
bul(tf2, "Captures non-linear relationships traditional stats miss")
bul(tf2, "Learns from multiple data sources simultaneously")
bul(tf2, "Adapts to changing market conditions automatically")
bul(tf2, "Provides probabilistic forecasts (confidence intervals)")
addp(tf2, "", 8, WHITE, False)
addp(tf2, "Key Innovation: Pooled Training", 20, GREEN, True, Pt(8))
addp(tf2, "All 5 counties share one model. County dummies let the model adjust for each county's unique price level. Counties with less data benefit from patterns learned in larger markets.", 15, DGRAY, False, Pt(4))

# ──── SLIDE 7: RESEARCH OBJECTIVES ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "5. RESEARCH OBJECTIVES / QUESTIONS")

tx = tb(s, 0.8, 1.5, 11.5, 1)
tf = tx.text_frame
setp(tf, "Main Objective", 22, DARK_BG, True)
addp(tf, "To develop and evaluate a machine learning-based maize price forecasting system that provides accurate, county-level weekly price predictions with quantified uncertainty to support decision-making across Kenya's maize value chain.", 16, DGRAY, False, Pt(6))

tx = tb(s, 0.8, 3.2, 11.5, 4)
tf = tx.text_frame
setp(tf, "Research Questions", 22, DARK_BG, True)

qs = [
    "RQ1: How accurately can a pooled XGBoost model predict weekly maize price changes across 5 Kenyan counties?",
    "RQ2: What is the optimal set of features (price lags, weather, economic indicators, temporal features) for maize price prediction?",
    "RQ3: How does the pooled model compare to per-county individual models in terms of MASE and directional accuracy?",
    "RQ4: Can the model provide reliable directional signals (up/down) that are actionable for farmers and buyers?",
    "RQ5: How far into the future (4, 8, 12, 24 weeks) can the model maintain useful predictive accuracy?",
    "RQ6: Can an interactive dashboard present forecasts in a way that is useful to non-technical stakeholders?",
]
for i, q in enumerate(qs, 1):
    rect(s, 1.2, 3.9 + (i-1)*0.55, 0.35, 0.35, [AMBER,GREEN,BLUE,ORANGE,PURPLE,RED][i-1])
    tx2 = tb(s, 1.2, 3.9 + (i-1)*0.55, 0.35, 0.35)
    setp(tx2.text_frame, str(i), 14, WHITE, True, PP_ALIGN.CENTER)
    tx3 = tb(s, 1.7, 3.9 + (i-1)*0.55, 10.5, 0.5)
    setp(tx3.text_frame, q, 14, DGRAY, False)

# ──── SLIDE 8: SOURCE OF DATA ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "6. SOURCE OF DATA")

tx = tb(s, 0.8, 1.5, 11.5, 0.5)
setp(tx.text_frame, "Five data sources are integrated to create the training dataset:", 18, DGRAY, False)

sources = [
    ("KAMIS (Ministry of Agriculture)", "Weekly retail & wholesale maize prices\nfor each county", "Weekly\n2021-2025\n~15,000 records", AMBER),
    ("AgriBORA", "Transaction-based wholesale\nprices (supplementary)", "Per transaction\n2021-2025\n~13,000 records", GREEN),
    ("Open-Meteo API", "Daily weather data: temperature,\nrainfall, wind speed", "Daily → Weekly\n2021-2025\n~800,000 records", BLUE),
    ("KNBS", "Consumer Price Index (CPI)\n— measures inflation", "Monthly\n2021-2025\n~57 records", ORANGE),
    ("Central Bank of Kenya", "USD/KES exchange rate", "Weekly\n2021-2025\n~250 records", PURPLE),
]
for i, (src, desc, meta, clr) in enumerate(sources):
    y = 2.3 + i * 1.0
    rect(s, 0.8, y, 0.1, 0.7, clr)
    tx = tb(s, 1.2, y, 4, 0.35); setp(tx.text_frame, src, 15, clr, True)
    tx2 = tb(s, 1.2, y+0.35, 4, 0.35); setp(tx2.text_frame, desc, 13, DGRAY, False)
    tx3 = tb(s, 5.5, y, 3, 0.7); setp(tx3.text_frame, meta, 12, MGRAY, False)

tx = tb(s, 0.8, 7, 11.5, 0.4)
setp(tx.text_frame, "Final dataset: 709 rows × 29 columns  |  5 counties  |  May 2021 — October 2025", 15, DARK_BG, True, PP_ALIGN.CENTER)

# ──── SLIDE 9: PROJECT PIPELINE ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "7. PROJECT PIPELINE — Complete Workflow")

steps = [
    ("1", "Data Collection", "5 sources:\nKAMIS, AgriBORA,\nWeather, CPI, FX", AMBER),
    ("2", "Data Cleaning", "Filter, standardize,\nremove outliers,\nfill missing values", GREEN),
    ("3", "Feature Engineering", "30 features: lags,\nrolling stats,\nweather, economic", BLUE),
    ("4", "Model Training", "Pooled XGBoost\nΔ-price target\nExpanding window CV", ORANGE),
    ("5", "Forecast Gen.", "Auto-regressive\n24-week horizon\nDampened, detrended", PURPLE),
    ("6", "Dashboard", "3-tab Streamlit app\nFarmer-friendly\nCloud deployment", RED),
]
for i, (num, title, desc, clr) in enumerate(steps):
    x = 0.8 + i * 2.05
    rect(s, x, 1.5, 1.85, 3.5, LGRAY)
    rect(s, x, 1.5, 1.85, 0.06, clr)
    rect(s, x+0.6, 1.8, 0.55, 0.55, clr)
    tx = tb(s, x+0.6, 1.8, 0.55, 0.55)
    setp(tx.text_frame, num, 22, WHITE, True, PP_ALIGN.CENTER)
    tx2 = tb(s, x+0.15, 2.5, 1.55, 0.4); setp(tx2.text_frame, title, 15, clr, True, PP_ALIGN.CENTER)
    tx3 = tb(s, x+0.15, 3.0, 1.55, 1.5); setp(tx3.text_frame, desc, 11, DGRAY, False, PP_ALIGN.CENTER)

# Arrow connectors between steps
for i in range(5):
    x = 2.65 + i * 2.05
    tx = tb(s, x, 3.1, 0.4, 0.4); setp(tx.text_frame, "→", 24, MGRAY, True, PP_ALIGN.CENTER)

# Bottom details
tx = tb(s, 0.8, 5.3, 11.5, 1.8)
tf = tx.text_frame
setp(tf, "Key Technical Details", 20, DARK_BG, True)
bul(tf, "Target variable: Δ-Price = Price(week) − Price(week-1) — predicts CHANGE, not absolute price")
bul(tf, "Model: XGBoost Regressor — 300 trees, max_depth=6, learning_rate=0.05, early stopping=10 rounds")
bul(tf, "Pooled training: County dummies (one-hot encoding) let one model serve all 5 counties")
bul(tf, "Forecast: Autoregressive with frozen lag features + detrending + dampening to prevent drift")
bul(tf, "Metrics: MASE (0.322), Directional Accuracy (75.5%), MAE (2.07 KES), sMAPE (4.8%)")

# ──── SLIDE 10: MODEL PERFORMANCE ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "8. MODEL PERFORMANCE")

metrics = [
    ("MASE", "0.322", "Mean Absolute Scaled Error\n< 1.0 = better than naive\n(better than guessing 'no change')", GREEN),
    ("Directional\nAccuracy", "75.5%", "Correctly predicts whether\nprices go up or down\n3 out of 4 times correct", BLUE),
    ("MAE", "2.07 KES", "Mean Absolute Error\nTypical prediction error\n≈ KES 2 per kilogram", AMBER),
    ("sMAPE", "4.8%", "Symmetric Mean Absolute\nPercentage Error\nUnder 5% = highly accurate", PURPLE),
]
for i, (label, value, desc, clr) in enumerate(metrics):
    x = 0.8 + i * 3.15
    rect(s, x, 1.4, 2.9, 2.5, LGRAY); rect(s, x, 1.4, 2.9, 0.06, clr)
    tx = tb(s, x, 1.6, 2.9, 0.4); setp(tx.text_frame, label, 16, MGRAY, False, PP_ALIGN.CENTER)
    tx2 = tb(s, x, 2.0, 2.9, 0.6); setp(tx2.text_frame, value, 34, clr, True, PP_ALIGN.CENTER)
    tx3 = tb(s, x+0.2, 2.7, 2.5, 1); setp(tx3.text_frame, desc, 12, DGRAY, False, PP_ALIGN.CENTER)

# Per-county table
pdata = [
    ["County", "MASE", "Dir Acc", "MAE", "sMAPE"],
    ["Nairobi", "0.341", "74.2%", "2.41 KES", "5.1%"],
    ["Mombasa", "0.318", "76.8%", "2.18 KES", "4.6%"],
    ["Kiambu", "0.309", "75.1%", "1.89 KES", "4.4%"],
    ["Kirinyaga", "0.335", "73.9%", "1.96 KES", "4.9%"],
    ["Uasin-Gishu", "0.308", "77.5%", "1.72 KES", "4.3%"],
]
y = 4.3; cols = [1.5, 2.5, 2.5, 2.5, 2.5]
rect(s, 1.5, y, 10, 0.4, DARK_BG)
xp = 1.5
for ci, h in enumerate(["County", "MASE", "Dir Acc", "MAE", "sMAPE"]):
    tx = tb(s, xp, y+0.02, cols[ci], 0.35)
    setp(tx.text_frame, h, 13, WHITE, True, PP_ALIGN.CENTER)
    xp += cols[ci]
y += 0.4
for ri, row in enumerate(pdata[1:]):
    bgc = LGRAY if ri % 2 == 0 else WHITE
    rect(s, 1.5, y, 10, 0.35, bgc); xp = 1.5
    for ci, val in enumerate(row):
        tx = tb(s, xp, y+0.02, cols[ci], 0.3)
        setp(tx.text_frame, val, 12, DGRAY, False, PP_ALIGN.CENTER)
        xp += cols[ci]
    y += 0.35

tx = tb(s, 0.8, y+0.2, 11.5, 0.5)
setp(tx.text_frame, "Key Insight: The pooled model outperforms individual per-county models — sharing data across counties improves all metrics.", 14, GREEN, False)

# ──── SLIDE 11: FORECAST GENERATION ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "HOW FORECASTS ARE GENERATED (Multi-Step)")

tx = tb(s, 0.8, 1.5, 5.8, 5.3)
tf = tx.text_frame
setp(tf, "The Challenge", 22, RED, True)
addp(tf, "The model predicts only ONE week ahead. To get 24 weeks:", 16, DGRAY, False, Pt(6))
addp(tf, "1. Predict week 1 → feed into week 2's features", 15, DGRAY, False, Pt(4))
addp(tf, "2. Predict week 2 → feed into week 3's features", 15, DGRAY, False, Pt(4))
addp(tf, "3. Repeat 24 times", 15, DGRAY, False, Pt(4))
addp(tf, "", 6, WHITE, False)
addp(tf, "Problem: Error Compounding", 18, RED, True, Pt(4))
addp(tf, "A slightly-high prediction in week 1 makes week 2's features too high, making week 2's prediction even higher — creating an upward spiral. This is called autoregressive forecast drift.", 15, DGRAY, False, Pt(4))

tx2 = tb(s, 7, 1.5, 5.8, 5.3)
tf2 = tx2.text_frame
setp(tf2, "Our 3 Fixes", 22, GREEN, True)
addp(tf2, "", 6, WHITE, False)
addp(tf2, "A. Freeze Trend Features", 17, BLUE, True, Pt(4))
addp(tf2, "Lag features captured once from actual data and frozen. Predicted prices are NOT fed back into these features.", 14, DGRAY, False, Pt(2))
addp(tf2, "", 4, WHITE, False)
addp(tf2, "B. Detrend (Remove Inflation Bias)", 17, BLUE, True, Pt(4))
addp(tf2, "Subtract recent average weekly change from predictions — only unexpected movements matter.", 14, DGRAY, False, Pt(2))
addp(tf2, "", 4, WHITE, False)
addp(tf2, "C. Dampen Long-Term", 17, BLUE, True, Pt(4))
addp(tf2, "Week 1: 100% signal → Week 12: 70% → Week 24: 40%. Far-out predictions pull toward current price.", 14, DGRAY, False, Pt(2))
addp(tf2, "", 8, WHITE, False)
addp(tf2, "Confidence Bands", 18, PURPLE, True, Pt(6))
addp(tf2, "80% CI: Forecast ± 0.8 × 1.28 × √(week). Wider for longer horizons — reflects growing uncertainty.", 14, DGRAY, False, Pt(2))

# ──── SLIDE 12: DASHBOARD DEMO ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "9. DASHBOARD DEMONSTRATION — Practical Walkthrough")

tabs = [
    ("📈 Tab 1:\nPrice Forecast", GREEN,
     "How to use:\n• Select county from sidebar dropdown\n• Adjust forecast horizon slider (8-30 weeks)\n\nWhat you see:\n• Signal banner: 🚀 Rising / 🔻 Falling / ➡️ Stable\n• Plain-language advice: \"Sell now\" / \"Buy now\" / \"Wait\"\n• Forecast chart: past (blue) + forecast (red dashed) + confidence band\n• Table: week-by-week predicted prices with change arrows\n\nFarmer takeaway: \"Prices rising in Nairobi. SELL.\""),
    ("🏪 Tab 2:\nCompare Markets", BLUE,
     "How to use:\n• Automatically shows all 5 counties\n\nWhat you see:\n• 🏪 Best market to SELL (highest price, green card)\n• 🛒 Best market to BUY (lowest price, blue card)\n• Multi-county forecast comparison chart\n• Ranked table by current and forecasted price\n\nFarmer takeaway: \"Sell in Mombasa at KES 48, buy in Uasin-Gishu at KES 35.\""),
    ("🗓 Tab 3:\nBest Time & Tips", AMBER,
     "How to use:\n• Automatically computed from historical data\n\nWhat you see:\n• Best month to sell (peak price month)\n• Best month to buy (trough price month)\n• Monthly price bar chart (green/red)\n• Year-over-year comparison chart\n• Tips cards: advice for farmers vs families\n• Simple price drivers explanation\n\nFarmer takeaway: \"Best to sell in January, buy in August.\""),
]
for i, (title, clr, items) in enumerate(tabs):
    x = 0.5 + i * 4.2
    rect(s, x, 1.4, 3.9, 5.8, LGRAY); rect(s, x, 1.4, 3.9, 0.06, clr)
    tx = tb(s, x+0.2, 1.6, 3.5, 0.7); setp(tx.text_frame, title, 16, clr, True, PP_ALIGN.CENTER)
    tx2 = tb(s, x+0.2, 2.4, 3.5, 4.5); tf2 = tx2.text_frame
    setp(tf2, items, 11, DGRAY, False)

# ──── SLIDE 13: HOW TO DEMONSTRATE LIVE ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE)
rect(s, 0, 0, 13.333, 1.1, DARK_BG); rect(s, 0, 1.1, 13.333, 0.06, GREEN)
tx = tb(s, 0.8, 0.15, 11.5, 0.8); setp(tx.text_frame, "LIVE DEMONSTRATION — How to Walk Through the System", 28, WHITE, True)

steps_demo = [
    ("Step 1\nOpen Dashboard", "Launch the Streamlit app in browser.\nURL: *.streamlit.app\n(or run locally: streamlit run src/dashboard/app.py)", GREEN),
    ("Step 2\nSelect County", "Sidebar dropdown → pick Nairobi.\nObserve: Current price KPI, 4-week trend,\nall-time price range update automatically.", BLUE),
    ("Step 3\nAdjust Forecast", "Sidebar slider → set to 24 weeks.\nObserve: Forecast chart extends to 2026,\nconfidence bands widen over time.", AMBER),
    ("Step 4\nRead the Signal", "Tab 1: Check signal banner color & text.\nRead advice: Is it telling farmers to sell?\nCheck the forecast table for weekly prices.", ORANGE),
    ("Step 5\nCompare Markets", "Tab 2: See which county has the\nhighest/lowest price. Best sell vs best\nbuy markets highlighted.", PURPLE),
    ("Step 6\nSeasonal Advice", "Tab 3: Best month to sell/buy.\nMonthly price guide. Tips cards\nfor farmers and families.", RED),
]
for i, (step, desc, clr) in enumerate(steps_demo):
    col = i % 3; row = i // 3
    x = 0.8 + col * 4.1; y = 1.4 + row * 3.0
    rect(s, x, y, 3.8, 2.7, LGRAY); rect(s, x, y, 3.8, 0.06, clr)
    tx = tb(s, x+0.2, y+0.15, 3.4, 0.7); setp(tx.text_frame, step, 16, clr, True, PP_ALIGN.CENTER)
    tx2 = tb(s, x+0.2, y+0.9, 3.4, 1.6); setp(tx2.text_frame, desc, 12, DGRAY, False)

tx = tb(s, 0.8, 6.9, 11.5, 0.4)
setp(tx.text_frame, "Total time: ~5 minutes  |  No technical knowledge needed to use the dashboard  |  Designed for farmers, traders, and policymakers", 14, DARK_BG, True, PP_ALIGN.CENTER)

# ──── SLIDE 14: LIMITATIONS ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "10. LIMITATIONS")

lims = [
    ("Data Coverage", "Only 5 counties out of 47. Limited to 2021-2025 (5 years). Missing real-time data updates — forecasts use cached data.", ORANGE),
    ("Forecast Horizon", "Accuracy decreases for longer horizons. Beyond 12 weeks, confidence bands widen significantly. Model predicts Δ-price, so occasional drift remains possible.", RED),
    ("External Factors", "Does not account for: government policy changes (import permits, tariffs), geopolitical events, major weather disasters, disease outbreaks (e.g., Fall Armyworm), fertilizer subsidy programs.", PURPLE),
    ("Model Limitations", "No causal inference — correlation ≠ causation. County dummies capture level differences but not structural market changes. Assumes historical patterns continue.", BLUE),
    ("Data Quality", "KAMIS data is self-reported by markets — may contain errors. AgriBORA data is transaction-based but limited coverage. Weather data from API, not ground stations.", AMBER),
    ("Technical", "Dashboard requires internet (Streamlit Cloud). Free tier has limited compute. No mobile app — web-only. No SMS/USSD for offline farmers.", GREEN),
]
for i, (title, desc, clr) in enumerate(lims):
    col = i % 3; row = i // 3
    x = 0.8 + col * 4.1; y = 1.5 + row * 2.9
    rect(s, x, y, 3.8, 2.6, LGRAY); rect(s, x, y, 3.8, 0.06, clr)
    tx = tb(s, x+0.3, y+0.2, 3.2, 0.4); setp(tx.text_frame, f"⚠ {title}", 16, clr, True)
    tx2 = tb(s, x+0.3, y+0.7, 3.2, 1.7); setp(tx2.text_frame, desc, 12, DGRAY, False)

# ──── SLIDE 15: FUTURE WORK ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, WHITE); head(s, "11. FUTURE WORK")

tx = tb(s, 0.8, 1.5, 11.5, 0.5)
setp(tx.text_frame, "Planned improvements and extensions to the system:", 18, DGRAY, False)

futures = [
    ("🌍 Expand to All 47 Counties", "Scale the model from 5 to all 47 Kenyan counties using the full KAMIS dataset. This would provide nationwide coverage.", BLUE),
    ("📱 Mobile & SMS Access", "Build a mobile-friendly version and SMS notification system so farmers without smartphones can receive price alerts and forecasts.", GREEN),
    ("🔮 Multi-Model Ensemble", "Add additional model types (LightGBM, Random Forest, LSTM) and ensemble them for improved accuracy and robustness.", ORANGE),
    ("📡 Real-Time Data Pipeline", "Automate weekly data ingestion from KAMIS/AgriBORA APIs so forecasts update automatically every week without manual intervention.", PURPLE),
    ("🌾 Crop-Specific Expansion", "Extend forecasting to other staple crops: beans, rice, potatoes, and wheat. The same pipeline can be adapted with minimal changes.", AMBER),
    ("📊 Advanced Analytics", "Add feature importance analysis, partial dependence plots, what-if scenario modeling, and automated insight generation.", RED),
]
for i, (title, desc, clr) in enumerate(futures):
    col = i % 3; row = i // 3
    x = 0.8 + col * 4.1; y = 2.2 + row * 1.7
    rect(s, x, y, 0.08, 1.2, clr)
    tx = tb(s, x+0.3, y, 3.3, 0.4); setp(tx.text_frame, title, 15, clr, True)
    tx2 = tb(s, x+0.3, y+0.4, 3.3, 0.8); setp(tx2.text_frame, desc, 12, DGRAY, False)

# ──── SLIDE 16: THANK YOU ────
s = prs.slides.add_slide(prs.slide_layouts[6]); bg(s, DARK_BG)
rect(s, 0, 0, 13.333, 0.12, AMBER); rect(s, 0, 7.38, 13.333, 0.12, GREEN)

tx = tb(s, 1.5, 1.0, 10.3, 1)
setp(tx.text_frame, "THANK YOU", 44, WHITE, True, PP_ALIGN.CENTER)

tx2 = tb(s, 1.5, 2.3, 10.3, 4.5)
tf2 = tx2.text_frame
setp(tf2, "Summary of Achievements", 24, RGBColor(0xFD,0xE6,0x8A), False, PP_ALIGN.CENTER)
addp(tf2, "✓ Pooled XGBoost model achieving MASE = 0.322 and 75.5% directional accuracy", 18, WHITE, False, Pt(16), PP_ALIGN.CENTER)
addp(tf2, "✓ County-level forecasts with 80% confidence intervals for 5 Kenyan counties", 18, WHITE, False, Pt(6), PP_ALIGN.CENTER)
addp(tf2, "✓ Farmer-centric interactive dashboard with plain-language advice", 18, WHITE, False, Pt(6), PP_ALIGN.CENTER)
addp(tf2, "✓ Deployed on Streamlit Cloud for public access", 18, WHITE, False, Pt(6), PP_ALIGN.CENTER)
addp(tf2, "✓ Comprehensive system with 30 features, 5 data sources, 24-week forecast horizon", 18, WHITE, False, Pt(6), PP_ALIGN.CENTER)

addp(tf2, "", 12, WHITE, False, Pt(24))
addp(tf2, "📧 Contact information  |  📍 Nairobi, Kenya", 16, RGBColor(0x93,0xC5,0xFD), False, Pt(4), PP_ALIGN.CENTER)
addp(tf2, "🌽 Maize Price Forecasting System  •  2025", 16, RGBColor(0x93,0xC5,0xFD), False, Pt(4), PP_ALIGN.CENTER)

# Save
out = "docs/Maize_Price_Forecasting_Full_Presentation.pptx"
prs.save(out)
print(f"Saved: {out}")
print(f"Slides: {len(prs.slides)}")
print(f"Size: {os.path.getsize(out)/1024:.1f} KB")
