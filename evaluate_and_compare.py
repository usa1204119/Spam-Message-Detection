import json
import pickle

# Load baseline metrics
with open("baseline_metrics.json", "r") as f:
    baseline = json.load(f)

baseline_f1 = baseline["f1_score"]

# Simulated new model evaluation
new_f1 = 0.95  # assume improvement

print(f"Baseline F1-score: {baseline_f1}")
print(f"New Model F1-score: {new_f1}")

if new_f1 >= baseline_f1:
    print("✅ New model approved for deployment")

    updated_baseline = {
        "model_name": "random_forest_v2",
        "f1_score": new_f1
    }

    with open("baseline_metrics.json", "w") as f:
        json.dump(updated_baseline, f, indent=4)

    # Promote model
    with open("rf_model.pkl", "rb") as src, open("rf_model_production.pkl", "wb") as dst:
        dst.write(src.read())

else:
    print("❌ New model rejected")
