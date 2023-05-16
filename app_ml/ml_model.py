
"""
import joblib
import numpy as np


def predict_disease(patient):
    # importe as bibliotecas necessárias para o modelo de machine learning
    
    
    # carregue o modelo treinado
    ml_model = joblib.load('./model/random_forest_cardio.pkl')
    
    # crie uma matriz de recursos com os dados do paciente
    
    
    features = np.array([[
        patient.age,
        patient.gender,
        patient.weight,
        patient.height,
        patient.systolic_pressure,
        patient.diastolic_pressure,
        patient.glucose,
    ]])
    # execute a previsão do modelo
    prediction = ml_model.predict(features)
    
    # retorne o resultado da previsão
    return 'doença cardíaca' if prediction == 1 else 'sem doença cardíaca'

"""