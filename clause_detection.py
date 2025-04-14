import joblib

# Load pre-trained SVM model
model = joblib.load("models/svm_clause_risk_detector.pkl")

def detect_risky_clauses(text):
    clauses = text.split('\n')  # Assume clauses are separated by new lines
    risky_clauses = []

    for clause in clauses:
        prediction = model.predict([clause])
        if prediction[0] == 1:  # 1 indicates risk
            risky_clauses.append(clause)
    
    return risky_clauses
