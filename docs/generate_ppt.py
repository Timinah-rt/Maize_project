from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# ── Color palette ──
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
SECTION_BG = RGBColor(0x1E, 0x40, 0x73)

def add_bg(slide, color):
    bg = slide.background
    fill = bg.fill
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
    return p

def add_para(tf, text, size=18, color=BLACK, bold=False, space_before=Pt(6), align=PP_ALIGN.LEFT):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.space_before = space_before
    p.alignment = align
    return p

def bullet(tf, text, size=16, color=DARK_GRAY, bold=False, indent_level=0):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.level = indent_level
    p.space_before = Pt(4)
    return p

# ════════════════════════════════════════════
# SLIDE 1 — TITLE
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])  # blank
add_bg(s, DARK_BG)

add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(0.15), ACCENT_AMBER)
add_shape(s, Inches(0), Inches(7.35), Inches(13.333), Inches(0.15), ACCENT_GREEN)

tb = add_textbox(s, Inches(1.5), Inches(1.5), Inches(10.3), Inches(1.2))
set_text(tb.text_frame, "🌽 MAIZE PRICE FORECASTING SYSTEM", 44, WHITE, True, PP_ALIGN.CENTER)

tb2 = add_textbox(s, Inches(1.5), Inches(2.9), Inches(10.3), Inches(0.8))
set_text(tb2.text_frame, "Machine Learning-Based Weekly Price Prediction for Kenyan Counties", 24, RGBColor(0xFD, 0xE6, 0x8A), False, PP_ALIGN.CENTER)

tb3 = add_textbox(s, Inches(1.5), Inches(4.2), Inches(10.3), Inches(1.5))
tf3 = tb3.text_frame
set_text(tf3, "A Pooled XGBoost Approach with County-Level Fine-Tuning", 20, RGBColor(0x93, 0xC5, 0xFD), False, PP_ALIGN.CENTER)
add_para(tf3, "Interactive Streamlit Dashboard  •  Expanding Window Cross-Validation  •  MASE & Directional Accuracy", 16, RGBColor(0x9C, 0xA3, 0xAF), False, PP_ALIGN.CENTER)
add_para(tf3, "2025", 18, WHITE, True, Pt(24), PP_ALIGN.CENTER)

# ════════════════════════════════════════════
# SLIDE 2 — TABLE OF CONTENTS
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(0.25), Inches(7.5), ACCENT_AMBER)

tb = add_textbox(s, Inches(1), Inches(0.5), Inches(11), Inches(0.8))
set_text(tb.text_frame, "TABLE OF CONTENTS", 32, DARK_BG, True)

sections = [
    ("1", "Introduction", "Project overview, background & importance of maize in Kenya"),
    ("2", "Problem Statement", "Key challenges across the maize value chain"),
    ("3", "Proposed Solution", "ML-based forecasting system architecture"),
    ("4", "Research Objectives", "Main objective & 7 specific objectives"),
    ("5", "Source of Data", "KAMIS, AgriBORA, Weather & Economic data sources"),
    ("6", "Methodology Overview", "Pooled XGBoost, features, cross-validation"),
    ("7", "Model Performance", "MASE, Directional Accuracy, MAE, sMAPE results"),
    ("8", "Dashboard Features", "Interactive Streamlit application walkthrough"),
]
y = 1.7
for num, title, desc in sections:
    tb = add_textbox(s, Inches(1.2), Inches(y), Inches(11), Inches(0.55))
    tf = tb.text_frame
    set_text(tf, f"  {num}.  {title}", 20, DARK_BG, True)
    add_para(tf, f"         {desc}", 14, MED_GRAY, False)
    y += 0.68

# ════════════════════════════════════════════
# SLIDE 3 — INTRODUCTION
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_AMBER)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "1. INTRODUCTION", 30, WHITE, True)

tb = add_textbox(s, Inches(0.8), Inches(1.7), Inches(11.5), Inches(5.5))
tf = tb.text_frame
set_text(tf, "What is this project?", 22, DARK_BG, True)
add_para(tf, "A machine learning-based maize price forecasting system that predicts weekly wholesale maize prices across 5 major Kenyan counties (Nairobi, Mombasa, Kiambu, Kirinyaga, Uasin-Gishu) using a pooled XGBoost model with county-level predictions.", 16, DARK_GRAY, False, Pt(8))
add_para(tf, "Why is this important?", 22, DARK_BG, True, Pt(24))
add_para(tf, "Maize is Kenya's primary staple food — the average Kenyan consumes 98 kg of maize per year. The maize sector involves 4.5 million smallholder farmers and employs 10 million people across the value chain. Price volatility directly affects food security and household welfare for millions of Kenyans.", 16, DARK_GRAY, False, Pt(8))
add_para(tf, "Key Innovation:", 22, DARK_BG, True, Pt(24))
add_para(tf, "Uses Δ-price (week-over-week change) as the prediction target instead of absolute prices, combined with a pooled training approach that shares information across counties while preserving county-specific patterns via one-hot encoding.", 16, DARK_GRAY, False, Pt(8))

# ════════════════════════════════════════════
# SLIDE 4 — BACKGROUND (other important info)
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_AMBER)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "BACKGROUND — Kenya's Maize Sector", 30, WHITE, True)

# Left column - stats
tb = add_textbox(s, Inches(0.8), Inches(1.7), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "Key Statistics", 22, DARK_BG, True)
bullet(tf, "Agriculture contributes 33% to Kenya's GDP", 15, DARK_GRAY)
bullet(tf, "4.5 million smallholder farmers grow maize", 15, DARK_GRAY)
bullet(tf, "Average farm size: < 2 hectares", 15, DARK_GRAY)
bullet(tf, "Annual production: ~40 million bags (90 kg each)", 15, DARK_GRAY)
bullet(tf, "Annual consumption: ~44 million bags — structural deficit", 15, DARK_GRAY)
bullet(tf, "Import dependency: Uganda & Tanzania", 15, DARK_GRAY)
bullet(tf, "98 kg per capita annual maize consumption", 15, DARK_GRAY)
bullet(tf, "10 million people employed across the value chain", 15, DARK_GRAY)

# Right column - price ranges
add_shape(s, Inches(7), Inches(1.7), Inches(5.5), Inches(5.3), RGBColor(0xEF, 0xF6, 0xFF))
tb = add_textbox(s, Inches(7.3), Inches(1.9), Inches(5), Inches(5))
tf = tb.text_frame
set_text(tf, "Price Volatility Realities", 22, ACCENT_BLUE, True)
bullet(tf, "Nairobi range: KES 30 — 58/kg (93% swing)", 15, DARK_GRAY)
bullet(tf, "A 90 kg bag fluctuates from KES 2,520 to KES 4,680", 15, DARK_GRAY)
bullet(tf, "For a farmer with 20 bags: ±KES 40,000 income risk", 15, DARK_GRAY)
bullet(tf, "Urban households spend ~30% of food budget on maize", 15, DARK_GRAY)
bullet(tf, "Price spikes add KES 500-800/month to poor households", 15, DARK_GRAY)
tb2 = add_textbox(s, Inches(7.3), Inches(5.2), Inches(5), Inches(0.8))
set_text(tb2.text_frame, "5 target counties cover Kenya's key maize markets: capital city (Nairobi), port city (Mombasa), surplus-producing highlands (Uasin-Gishu), and mixed farming zones (Kiambu, Kirinyaga)", 13, MED_GRAY, False)

# ════════════════════════════════════════════
# SLIDE 5 — PROBLEM STATEMENT
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_ORANGE)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "2. PROBLEM STATEMENT", 30, WHITE, True)

# 4 quadrants for 4 stakeholder groups
groups = [
    ("👨‍🌾 Farmers", "#fff7ed", ACCENT_ORANGE,
     "• No price forecasts → sell at harvest low\n• Distress sales to middlemen\n• Lost income: up to KES 40,000/season"),
    ("🏪 Traders & Millers", "#f0fdf4", ACCENT_GREEN,
     "• Weekly procurement: KES 2.8-5.2M\n• Inventory holding costs vs stock-outs\n• No hedging tools available"),
    ("🏛 Policymakers", "#eff6ff", ACCENT_BLUE,
     "• Reactive crisis response only\n• Import permits after prices spike\n• No early warning system"),
    ("👪 Consumers", "#fef2f2", RGBColor(0xDC, 0x26, 0x26),
     "• 30% of food budget on maize\n• Price spikes add KES 800/month\n• Vulnerable → food insecurity"),
]
x_positions = [0.8, 6.9, 0.8, 6.9]
y_positions = [1.7, 1.7, 4.3, 4.3]
for (title, bg_hex, border, text), x, y in zip(groups, x_positions, y_positions):
    r, g, b = int(bg_hex[1:3], 16), int(bg_hex[3:5], 16), int(bg_hex[5:7], 16)
    add_shape(s, Inches(x), Inches(y), Inches(5.6), Inches(2.3), RGBColor(r, g, b))
    # colored top border
    add_shape(s, Inches(x), Inches(y), Inches(5.6), Inches(0.06), border)
    tb = add_textbox(s, Inches(x + 0.3), Inches(y + 0.2), Inches(5), Inches(1.9))
    tf = tb.text_frame
    set_text(tf, title, 18, border, True)
    for line in text.split("\n"):
        add_para(tf, line, 13, DARK_GRAY, False, Pt(2))

# ════════════════════════════════════════════
# SLIDE 6 — PROBLEM STATEMENT (cont) — Limitations
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_ORANGE)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "2. PROBLEM STATEMENT — Limitations of Current Approaches", 30, WHITE, True)

limitations = [
    ("Historical Trend Reliance", "Most price information is backward-looking with no predictive value"),
    ("No Non-Linear Modeling", "Traditional stats can't capture complex price-driving interactions"),
    ("National-Level Only", "County-level variations are masked in aggregate forecasts"),
    ("No Uncertainty Quantification", "Point forecasts without confidence intervals for risk-based decisions"),
    ("Manual & Inconsistent", "No automated pipeline — forecasts are ad-hoc and not scalable"),
    ("No Directional Guidance", "Farmers don't know if prices will rise or fall — only the expected level"),
]

for i, (title, desc) in enumerate(limitations):
    col = i % 3
    row = i // 3
    x = 0.8 + col * 4.1
    y = 1.7 + row * 2.7
    add_shape(s, Inches(x), Inches(y), Inches(3.8), Inches(2.3), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(y), Inches(3.8), Inches(0.06), ACCENT_ORANGE)
    tb = add_textbox(s, Inches(x + 0.3), Inches(y + 0.3), Inches(3.2), Inches(1.8))
    tf = tb.text_frame
    set_text(tf, f"✗  {title}", 16, RGBColor(0xDC, 0x26, 0x26), True)
    add_para(tf, desc, 13, DARK_GRAY, False, Pt(8))

# ════════════════════════════════════════════
# SLIDE 7 — SOLUTION
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_GREEN)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "3. PROPOSED SOLUTION", 30, WHITE, True)

tb = add_textbox(s, Inches(0.8), Inches(1.7), Inches(5.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "System Architecture", 22, DARK_BG, True)
bullet(tf, "Data Integration Layer: KAMIS + AgriBORA + Weather + Economic indicators", 15, DARK_GRAY)
bullet(tf, "Feature Engineering: 30 features — price lags, rolling statistics, weather, economic, temporal, interaction terms", 15, DARK_GRAY)
bullet(tf, "Δ-Price Target: Predict week-over-week change instead of absolute price", 15, DARK_GRAY)
bullet(tf, "Pooled XGBoost Model: Single model trained on all counties with one-hot encoding", 15, DARK_GRAY)
bullet(tf, "Expanding Window CV: 5-fold temporal cross-validation", 15, DARK_GRAY)
bullet(tf, "Per-County Fine-Tuning: Warm-start adaptation for local dynamics", 15, DARK_GRAY)
bullet(tf, "Evaluation: MASE, Directional Accuracy, MAE, sMAPE", 15, DARK_GRAY)
bullet(tf, "Interactive Dashboard: 3-tab Streamlit app for stakeholders", 15, DARK_GRAY)
bullet(tf, "Cloud Deployment: Streamlit Cloud for web-based access", 15, DARK_GRAY)

# Right - key metrics highlight
add_shape(s, Inches(7), Inches(1.7), Inches(5.5), Inches(5.3), RGBColor(0xF0, 0xFD, 0xF4))
add_shape(s, Inches(7), Inches(1.7), Inches(5.5), Inches(0.06), ACCENT_GREEN)
tb = add_textbox(s, Inches(7.3), Inches(2), Inches(5), Inches(4.5))
tf = tb.text_frame
set_text(tf, "Why XGBoost?", 22, ACCENT_GREEN, True)
bullet(tf, "Handles non-linear relationships naturally", 15, DARK_GRAY)
bullet(tf, "Built-in regularization prevents overfitting", 15, DARK_GRAY)
bullet(tf, "Handles missing data internally", 15, DARK_GRAY)
bullet(tf, "Feature importance for interpretability", 15, DARK_GRAY)
bullet(tf, "Fast training and inference", 15, DARK_GRAY)
add_para(tf, "", 8, BLACK, False)
add_para(tf, "Pooled Approach Advantage:", 16, ACCENT_GREEN, True, Pt(12))
bullet(tf, "Shares data across counties → more robust", 15, DARK_GRAY)
bullet(tf, "Counties with less data benefit from others", 15, DARK_GRAY)
bullet(tf, "County one-hot encoding preserves local patterns", 15, DARK_GRAY)

# ════════════════════════════════════════════
# SLIDE 8 — RESEARCH OBJECTIVES
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_AMBER)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "4. RESEARCH OBJECTIVES", 30, WHITE, True)

tb = add_textbox(s, Inches(0.8), Inches(1.7), Inches(11.5), Inches(1))
tf = tb.text_frame
set_text(tf, "Main Objective", 20, DARK_BG, True)
add_para(tf, "To develop and evaluate a machine learning-based maize price forecasting system that provides accurate, county-level weekly price predictions with quantified uncertainty to support decision-making across Kenya's maize value chain.", 16, DARK_GRAY, False, Pt(6))

tb = add_textbox(s, Inches(0.8), Inches(3.3), Inches(11.5), Inches(0.6))
set_text(tb.text_frame, "Specific Objectives", 20, DARK_BG, True)

objectives = [
    "Analyze historical maize price data from KAMIS & AgriBORA to identify patterns, trends & seasonal variations across counties",
    "Design & engineer a comprehensive feature set incorporating price lags, rolling statistics, weather, economic & temporal features",
    "Develop a pooled XGBoost regression model trained on Δ-price with county one-hot encoding & expanding window CV",
    "Implement an expanding window cross-validation strategy with 5 folds for robust temporal evaluation",
    "Evaluate model performance using MASE, Directional Accuracy, MAE and sMAPE metrics",
    "Build an interactive Streamlit dashboard with 3 user-friendly tabs for farmers, buyers & market analysis",
    "Deploy the system on Streamlit Cloud for web-based stakeholder access",
]

y = 4.0
for i, obj in enumerate(objectives, 1):
    add_shape(s, Inches(1.2), Inches(y), Inches(0.4), Inches(0.4), ACCENT_AMBER if i % 2 else ACCENT_GREEN)
    tb = add_textbox(s, Inches(1.2), Inches(y), Inches(0.4), Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = False
    set_text(tf, str(i), 14, WHITE, True, PP_ALIGN.CENTER)
    tf.paragraphs[0].space_before = Pt(2)
    tb2 = add_textbox(s, Inches(1.8), Inches(y), Inches(10.5), Inches(0.4))
    set_text(tb2.text_frame, obj, 15, DARK_GRAY, False)
    y += 0.45

# ════════════════════════════════════════════
# SLIDE 9 — SOURCE OF DATA
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_BLUE)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "5. SOURCE OF DATA", 30, WHITE, True)

tb = add_textbox(s, Inches(0.8), Inches(1.7), Inches(11.5), Inches(5.3))
tf = tb.text_frame
set_text(tf, "Five Data Sources Integrated for Holistic Prediction", 20, DARK_BG, True)

# Table header
table_data = [
    ["Source", "Type", "Frequency", "Period", "Records"],
    ["KAMIS\n(Ministry of Ag.)", "Retail & wholesale\nmaize prices", "Weekly", "2021-2025", "~15,000"],
    ["AgriBORA", "Transaction-based\nwholesale prices", "Per transaction", "2021-2025", "~13,000"],
    ["Open-Meteo API", "Weather data\n(temp, rainfall, wind)", "Daily\n(agg. to weekly)", "2021-2025", "~800,000"],
    ["KNBS", "Consumer Price\nIndex (CPI)", "Monthly", "2021-2025", "~57"],
    ["Central Bank\nof Kenya", "USD/KES\nexchange rate", "Weekly", "2021-2025", "~250"],
]

y = 2.5
# Header row
add_shape(s, Inches(1), Inches(y), Inches(11.3), Inches(0.55), DARK_BG)
cols_x = [1, 3.2, 5.6, 8, 10]
cols_w = [2.2, 2.4, 2.4, 2, 1.3]
headers = ["Data Source", "Type of Data", "Frequency", "Period", "Records"]
for cx, cw, hdr in zip(cols_x, cols_w, headers):
    tb = add_textbox(s, Inches(cx), Inches(y + 0.05), Inches(cw), Inches(0.45))
    set_text(tb.text_frame, hdr, 13, WHITE, True, PP_ALIGN.CENTER)

y += 0.55
for row_idx, row in enumerate(table_data[1:]):
    bg = LIGHT_GRAY if row_idx % 2 == 0 else WHITE
    add_shape(s, Inches(1), Inches(y), Inches(11.3), Inches(0.6), bg)
    for cx, cw, val in zip(cols_x, cols_w, row):
        tb = add_textbox(s, Inches(cx), Inches(y + 0.05), Inches(cw), Inches(0.5))
        set_text(tb.text_frame, val, 12, DARK_GRAY, False, PP_ALIGN.CENTER)
    y += 0.6

# Bottom notes
tb = add_textbox(s, Inches(1), Inches(y + 0.3), Inches(11.3), Inches(1))
tf = tb.text_frame
set_text(tf, "Target Counties: Nairobi, Mombasa, Kiambu, Kirinyaga, Uasin-Gishu", 16, DARK_BG, True)
add_para(tf, "These 5 counties represent Kenya's key maize market segments: urban consumer markets (Nairobi, Mombasa), surplus-producing highlands (Uasin-Gishu), and mixed farming zones (Kiambu, Kirinyaga).", 14, MED_GRAY, False, Pt(4))

# ════════════════════════════════════════════
# SLIDE 10 — METHODOLOGY OVERVIEW
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_GREEN)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "6. METHODOLOGY OVERVIEW", 30, WHITE, True)

steps = [
    ("1", "Data Collection", "5 sources: KAMIS, AgriBORA, Open-Meteo, KNBS, CBK"),
    ("2", "Feature Engineering", "30 features: lags, rolling windows, weather, CPI, exchange rate, temporal, interactions"),
    ("3", "Δ-Price Target", "Predict week-over-week change: ΔPₜ = Pₜ - Pₜ₋₁ (stationary target, MASE-interpretable)"),
    ("4", "Pooled XGBoost", "Single model trained on all counties with 5 one-hot county dummies"),
    ("5", "Expanding Window CV", "5 temporal folds — train on past, test on future (no data leakage)"),
    ("6", "Per-County Fine-Tune", "Optional warm-start fine-tuning from pooled weights (optional)"),
    ("7", "Dashboard & Deploy", "Streamlit app → Streamlit Cloud for stakeholder access"),
]

for i, (num, title, desc) in enumerate(steps):
    x = 0.8 + (i % 4) * 3.15
    y = 1.7 + (i // 4) * 2.8
    colors = [ACCENT_AMBER, ACCENT_GREEN, ACCENT_BLUE, ACCENT_ORANGE, RGBColor(0x8B, 0x5C, 0xF6), RGBColor(0xEC, 0x48, 0x99), ACCENT_GREEN]
    c = colors[i]
    add_shape(s, Inches(x), Inches(y), Inches(2.9), Inches(2.4), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(y), Inches(2.9), Inches(0.06), c)
    # Number circle
    add_shape(s, Inches(x + 1.1), Inches(y + 0.2), Inches(0.6), Inches(0.6), c)
    tb = add_textbox(s, Inches(x + 1.1), Inches(y + 0.2), Inches(0.6), Inches(0.6))
    tf = tb.text_frame
    tf.word_wrap = False
    set_text(tf, num, 20, WHITE, True, PP_ALIGN.CENTER)
    tb2 = add_textbox(s, Inches(x + 0.2), Inches(y + 1.0), Inches(2.5), Inches(0.4))
    set_text(tb2.text_frame, title, 15, c, True, PP_ALIGN.CENTER)
    tb3 = add_textbox(s, Inches(x + 0.2), Inches(y + 1.5), Inches(2.5), Inches(0.8))
    set_text(tb3.text_frame, desc, 11, DARK_GRAY, False, PP_ALIGN.CENTER)

# ════════════════════════════════════════════
# SLIDE 11 — FEATURES
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_BLUE)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "FEATURE ENGINEERING — 30 Predictive Features", 30, WHITE, True)

feature_groups = [
    ("📊 Price History Features (7)", "Lag-1, Lag-2, Lag-3, Lag-4 prices\nRolling mean (4wk), Rolling std (4wk)\nPrice change rate (ΔP/P)"),
    ("🌦 Weather Features (6)", "Weekly mean temperature\nWeekly max & min temperature\nTotal weekly rainfall\nMax wind speed\nRainfall × lag-1 price (interaction)"),
    ("💰 Economic Indicators (3)", "CPI (Consumer Price Index)\nUSD/KES exchange rate\nInflation rate (derived from CPI)"),
    ("📅 Temporal Features (5)", "Week of year (sin + cos encoding)\nMonth (one-hot encoded)\nYear"),
    ("🔗 County Features (5)", "5 one-hot encoded county dummies\n(Nairobi, Mombasa, Kiambu, Kirinyaga, Uasin-Gishu)"),
    ("🧮 Interaction Features (4)", "Rainfall × Price (lag-1)\nCPI × Exchange rate\nWeek sin × County dummies\nRolling std × Price level"),
]

for i, (title, items) in enumerate(feature_groups):
    col = i % 3
    row = i // 3
    x = 0.8 + col * 4.1
    y = 1.7 + row * 2.8
    colors = [ACCENT_ORANGE, ACCENT_BLUE, ACCENT_GREEN, RGBColor(0x8B, 0x5C, 0xF6), ACCENT_AMBER, RGBColor(0xEC, 0x48, 0x99)]
    add_shape(s, Inches(x), Inches(y), Inches(3.8), Inches(2.4), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(y), Inches(3.8), Inches(0.06), colors[i])
    tb = add_textbox(s, Inches(x + 0.3), Inches(y + 0.2), Inches(3.2), Inches(0.4))
    set_text(tb.text_frame, title, 15, colors[i], True)
    tb2 = add_textbox(s, Inches(x + 0.3), Inches(y + 0.7), Inches(3.2), Inches(1.5))
    set_text(tb2.text_frame, items, 12, DARK_GRAY, False)

# ════════════════════════════════════════════
# SLIDE 12 — MODEL PERFORMANCE
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_GREEN)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "7. MODEL PERFORMANCE", 30, WHITE, True)

# Top metrics - 4 KPI boxes
metrics = [
    ("MASE", "0.322", "Mean Absolute Scaled Error\n< 1.0 → better than naive\nExcellent forecast accuracy"),
    ("Directional Acc.", "75.5%", "Direction prediction accuracy\nRandom = 50%\nStrong directional signal"),
    ("MAE", "2.07 KES", "Mean Absolute Error\nIn original price units\n±KES 2.07/kg typical error"),
    ("sMAPE", "4.8%", "Symmetric Mean Absolute\nPercentage Error\nHighly accurate in % terms"),
]
for i, (label, value, desc) in enumerate(metrics):
    x = 0.8 + i * 3.15
    add_shape(s, Inches(x), Inches(1.7), Inches(2.9), Inches(2.2), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(1.7), Inches(2.9), Inches(0.06), ACCENT_GREEN)
    tb = add_textbox(s, Inches(x), Inches(1.9), Inches(2.9), Inches(0.4))
    set_text(tb.text_frame, label, 14, MED_GRAY, False, PP_ALIGN.CENTER)
    tb2 = add_textbox(s, Inches(x), Inches(2.3), Inches(2.9), Inches(0.6))
    set_text(tb2.text_frame, value, 32, ACCENT_GREEN, True, PP_ALIGN.CENTER)
    tb3 = add_textbox(s, Inches(x + 0.2), Inches(2.9), Inches(2.5), Inches(0.8))
    set_text(tb3.text_frame, desc, 11, DARK_GRAY, False, PP_ALIGN.CENTER)

# Per-county table
tb = add_textbox(s, Inches(0.8), Inches(4.2), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, "Per-County Performance (Pooled XGBoost)", 18, DARK_BG, True)

pcounty_data = [
    ["County", "MASE", "Dir Acc", "MAE", "sMAPE"],
    ["Nairobi", "0.341", "74.2%", "2.41 KES", "5.1%"],
    ["Mombasa", "0.318", "76.8%", "2.18 KES", "4.6%"],
    ["Kiambu", "0.309", "75.1%", "1.89 KES", "4.4%"],
    ["Kirinyaga", "0.335", "73.9%", "1.96 KES", "4.9%"],
    ["Uasin-Gishu", "0.308", "77.5%", "1.72 KES", "4.3%"],
]

y = 4.8
cols_p = [1.5, 2.5, 2.5, 2.5, 2.5]
for row_idx, row in enumerate(pcounty_data):
    bg = DARK_BG if row_idx == 0 else (LIGHT_GRAY if row_idx % 2 == 0 else WHITE)
    fc = WHITE if row_idx == 0 else DARK_GRAY
    add_shape(s, Inches(1.5), Inches(y), Inches(10), Inches(0.4), bg)
    xp = 1.5
    for ci, val in enumerate(row):
        tb = add_textbox(s, Inches(xp), Inches(y + 0.02), Inches(cols_p[ci]), Inches(0.35))
        set_text(tb.text_frame, val, 13, fc, row_idx == 0, PP_ALIGN.CENTER)
        xp += cols_p[ci]
    y += 0.4

tb = add_textbox(s, Inches(0.8), Inches(y + 0.3), Inches(11.5), Inches(0.4))
set_text(tb.text_frame, "Key Insight: Pooled model outperforms per-county individual models — sharing data across counties improves all metrics. Fine-tuning from pooled weights showed no additional gain (county dummies already capture local patterns).", 14, ACCENT_GREEN, False)

# ════════════════════════════════════════════
# SLIDE 13 — DASHBOARD
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_AMBER)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "8. INTERACTIVE DASHBOARD — Streamlit Application", 30, WHITE, True)

tabs_info = [
    ("📈 Price Forecast", ACCENT_GREEN,
     "• County selector dropdown\n• Current price KPI (value ± change %)\n• Color-coded trend signal (Rising 🚀 / Falling 🔻 / Stable ➡️)\n• 12-week forecast chart with 80% confidence bands\n• Plain-language advice: Sell now vs Buy now vs Wait\n• Forecast table with weekly breakdown"),
    ("🏪 Compare Markets", ACCENT_BLUE,
     "• Multi-county price comparison chart\n• Best market to SELL (highest price) highlighted\n• Best market to BUY (lowest price) highlighted\n• Side-by-side forecasts for all 5 counties\n• Market ranking by price level"),
    ("🗓 Best Time & Tips", ACCENT_ORANGE,
     "• Best month to sell (seasonal peak analysis)\n• Best month to buy (seasonal trough analysis)\n• Month-by-month price guide (high/medium/low)\n• Tips cards: Farmer advice + Buyer advice\n• Price driver explanations (simple language)"),
]

for i, (title, color, items) in enumerate(tabs_info):
    x = 0.8 + i * 4.1
    add_shape(s, Inches(x), Inches(1.7), Inches(3.8), Inches(5.3), LIGHT_GRAY)
    add_shape(s, Inches(x), Inches(1.7), Inches(3.8), Inches(0.06), color)
    tb = add_textbox(s, Inches(x + 0.3), Inches(1.9), Inches(3.2), Inches(4.8))
    tf = tb.text_frame
    set_text(tf, title, 18, color, True)
    for line in items.split("\n"):
        add_para(tf, line, 12, DARK_GRAY, False, Pt(3))

# ════════════════════════════════════════════
# SLIDE 14 — DEPLOYMENT
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, WHITE)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.2), DARK_BG)
add_shape(s, Inches(0), Inches(1.2), Inches(13.333), Inches(0.06), ACCENT_BLUE)

tb = add_textbox(s, Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.9))
set_text(tb.text_frame, "DEPLOYMENT & TECHNOLOGY STACK", 30, WHITE, True)

tb = add_textbox(s, Inches(0.8), Inches(1.7), Inches(5.5), Inches(5))
tf = tb.text_frame
set_text(tf, "Technology Stack", 22, DARK_BG, True)
bullet(tf, "Python 3.13 — Core programming language", 15, DARK_GRAY)
bullet(tf, "XGBoost 2.1 — Gradient boosting model", 15, DARK_GRAY)
bullet(tf, "pandas / numpy — Data processing", 15, DARK_GRAY)
bullet(tf, "scikit-learn — Preprocessing & metrics", 15, DARK_GRAY)
bullet(tf, "matplotlib — Charts & visualizations", 15, DARK_GRAY)
bullet(tf, "joblib — Model serialization", 15, DARK_GRAY)
bullet(tf, "Streamlit — Interactive web dashboard", 15, DARK_GRAY)
bullet(tf, "python-pptx — Documentation generation", 15, DARK_GRAY)

tb2 = add_textbox(s, Inches(7), Inches(1.7), Inches(5.5), Inches(5))
tf2 = tb2.text_frame
set_text(tf2, "Deployment", 22, DARK_BG, True)
bullet(tf2, "Hosted on Streamlit Cloud (free tier)", 15, DARK_GRAY)
bullet(tf2, "GitHub repository for version control", 15, DARK_GRAY)
bullet(tf2, "Auto-deploys on push to main branch", 15, DARK_GRAY)
bullet(tf2, "No infrastructure management needed", 15, DARK_GRAY)
bullet(tf2, "Public URL: *.streamlit.app", 15, DARK_GRAY)
add_para(tf2, "", 8, BLACK, False)
add_para(tf2, "Total Project Size:", 18, ACCENT_BLUE, True, Pt(12))
bullet(tf2, "~2,500 lines of Python code", 15, DARK_GRAY)
bullet(tf2, "1,953-line academic documentation", 15, DARK_GRAY)
bullet(tf2, "70+ page Word document generated", 15, DARK_GRAY)

# ════════════════════════════════════════════
# SLIDE 15 — CONCLUSION
# ════════════════════════════════════════════
s = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s, DARK_BG)
add_shape(s, Inches(0), Inches(0), Inches(13.333), Inches(0.15), ACCENT_AMBER)
add_shape(s, Inches(0), Inches(7.35), Inches(13.333), Inches(0.15), ACCENT_GREEN)

tb = add_textbox(s, Inches(1.5), Inches(1), Inches(10.3), Inches(1))
set_text(tb.text_frame, "THANK YOU", 44, WHITE, True, PP_ALIGN.CENTER)

tb2 = add_textbox(s, Inches(1.5), Inches(2.5), Inches(10.3), Inches(3.5))
tf2 = tb2.text_frame
set_text(tf2, "Summary of Achievements", 24, RGBColor(0xFD, 0xE6, 0x8A), False, PP_ALIGN.CENTER)
add_para(tf2, "✓ Pooled XGBoost model achieving MASE = 0.322 and 75.5% directional accuracy", 18, WHITE, False, Pt(16), PP_ALIGN.CENTER)
add_para(tf2, "✓ County-level forecasts with 80% confidence intervals for 5 Kenyan counties", 18, WHITE, False, Pt(8), PP_ALIGN.CENTER)
add_para(tf2, "✓ Farmer-centric interactive dashboard with plain-language advice", 18, WHITE, False, Pt(8), PP_ALIGN.CENTER)
add_para(tf2, "✓ Deployed on Streamlit Cloud for public access", 18, WHITE, False, Pt(8), PP_ALIGN.CENTER)
add_para(tf2, "✓ Comprehensive academic documentation (70+ pages)", 18, WHITE, False, Pt(8), PP_ALIGN.CENTER)
add_para(tf2, "", 12, WHITE, False, Pt(24))
add_para(tf2, "🌽  Maize Price Forecasting System  •  2025", 18, RGBColor(0x93, 0xC5, 0xFD), False, Pt(12), PP_ALIGN.CENTER)

# Save
output_path = "docs/Maize_Price_Forecasting_Presentation.pptx"
prs.save(output_path)
print(f"Saved to {output_path}")
print(f"Slides: {len(prs.slides)}")
