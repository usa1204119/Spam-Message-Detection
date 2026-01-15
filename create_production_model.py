import pickle

# Load trained model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Save as production model
with open("rf_model_production.pkl", "wb") as f:
    pickle.dump(model, f)

print("Production model created successfully")
