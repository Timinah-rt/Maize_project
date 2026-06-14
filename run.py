"""
Maize Price Forecasting Pipeline Runner
Run the full pipeline: clean -> features -> train -> dashboard
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def main():
    print("="*60)
    print("MAIZE PRICE FORECASTING PIPELINE")
    print("="*60)
    
    # Step 1: Clean data
    print("\n[1/4] Cleaning datasets...")
    from data.clean import main as clean_data
    clean_data()
    
    # Step 2: Create features
    print("\n[2/4] Creating features...")
    from data.features import create_features
    panel = create_features()
    
    # Step 3: Train models
    print("\n[3/4] Training models (this may take a while)...")
    from models.train import MaizePriceForecaster
    forecaster = MaizePriceForecaster()
    results = forecaster.train_and_evaluate()
    
    # Step 4: Launch dashboard option
    print("\n[4/4] Pipeline complete!")
    print("\nTo launch the dashboard, run:")
    print("  streamlit run src/dashboard/app.py")
    print("\nModel evaluation results saved to models/model_evaluation.csv")

if __name__ == "__main__":
    main()
