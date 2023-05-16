from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

from .forms import CardioForm
import pandas as pd
import numpy as np

import joblib

def form(request):
    return render(request, 'form.html')

def result(request):
    return render(request, 'result.html')

def predict(request):
    return render(request, 'predict.html')

def index(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        age = float(request.POST['age'])
        gender = float(request.POST['gender'])
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        systolic_pressure = float(request.POST['systolic_pressure'])
        diastolic_pressure = float(request.POST['diastolic_pressure'])
        glucose = float(request.POST['glucose'])
        smoker = float(request.POST['smoker'])
        cholesterol = float(request.POST['cholesterol'])
        alcohol_intake = float(request.POST['alcohol_intake'])
        physical_activity = float(request.POST['physical_activity'])

        imc= int(weight /(height/100)**2)
        # Carrega o modelo treinado
        model = joblib.load('./model/random_forest_cardio.pkl')
        
        # Realiza as previsões usando o modelo treinado
        
        X = np.array([age, gender, weight, height, systolic_pressure, diastolic_pressure, glucose, smoker, cholesterol, alcohol_intake, physical_activity])
        X = X.reshape(1, -1)
        X = X.astype(np.float32)
        y_pred = model.predict(X)
        # Transforma a previsão em uma mensagem para enviar por e-mail
        if y_pred[0] == 0:
            resultado = 'sem sintomas de doença cardíaca'
        else:
            resultado = 'com possivel doença cardíaca'
        
        
        # Envia o resultado por e-mail para o usuário
         # Envia o resultado por e-mail para o usuário
        html_content = render_to_string('result.html', {'name': name, 'lastname': lastname, 'resultado': resultado, 'imc':imc})
        text_content = strip_tags(html_content)

        subject = 'Resultado da previsão de doença cardíaca'
        message = "Olá {} {}! Gostaríamos de informar que o resultado da sua análise preditiva é: {}".format(name, lastname, resultado)

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        e_mail = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            recipient_list,
        )
        e_mail.attach_alternative(html_content, 'text/html')
        e_mail.send()

        return HttpResponseRedirect('/predict/')
    else:
        resultado = 'Verifique se preencheu corretamente o formulário'
        
    # Renderiza a página de resultado
    return render(request, 'index.html', {'resultado': resultado})

####################

"""def cardiology_prediction(request):
    if request.method == 'POST':
        form = CardioForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            systolic_pressure = form.cleaned_data['systolic_pressure']
            diastolic_pressure = form.cleaned_data['diastolic_pressure']
            cholesterol = form.cleaned_data['cholesterol']
            glucose = form.cleaned_data['glucose']
            smoker = form.cleaned_data['smoker']
            alcohol_intake = form.cleaned_data['alcohol_intake']
            physical_activity = form.cleaned_data['physical_activity']

            # Load the saved model
            model = joblib.load('./model/random_forest_cardio.pkl')

            # Make a prediction using the loaded model
            prediction = model.predict(pd.DataFrame({
                'age': [age],
                'gender': [gender],
                'height': [height],
                'weight': [weight],
                'systolic_pressure': [systolic_pressure],
                'diastolic_pressure': [diastolic_pressure],
                'cholesterol': [cholesterol],
                'glucose': [glucose],
                'smoker': [smoker],
                'alcohol_intake': [alcohol_intake],
                'physical_activity': [physical_activity]
            }))

            # Render the result page
            resultado = prediction[0]
            context = {'resultado': resultado}
            if resultado == 0:
                resultado = 'sem doença cardíaca'
            else:
                resultado = 'com doença cardíaca'

            # Send the result by email to the user
            subject = 'Resultado da previsão de doença cardíaca'
            message = "Olá {} {}! Gostaríamos de informar que o resultado da sua análise preditiva é: ".format(nome, sobrenome)
                                    
            #message = render_to_string('index.html', {'nome': nome, 'sobrenome': sobrenome, 'resultado': resultado})
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email] 
            #send_mail(subject, message, from_email, recipient_list, html_message=message)
            send_mail(
            'Obrigado por entrar em contato',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
            return HttpResponseRedirect('/sucesso/')
    else:
        form = CardioForm()
    return render(request, 'form.html', {'form': form})"""

"""
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
import joblib
from app_ml.ml_model import predict_disease

def predict(request):
    return render(request, 'predict.html')

def index(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        age = float(request.POST['age'])
        gender = int(request.POST['gender'])
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        systolic_pressure = float(request.POST['systolic_pressure'])
        diastolic_pressure = float(request.POST['diastolic_pressure'])
        glucose = float(request.POST['glucose'])
        
        # Carrega o modelo treinado
        model = joblib.load('./model/random_forest_cardio.pkl')
        
        # Realiza as previsões usando o modelo treinado
        
        X = [[age, gender, weight, height, systolic_pressure, diastolic_pressure, glucose]]
        y_pred = predict_disease(X[0])
        
        # Transforma a previsão em uma mensagem para enviar por e-mail
        if y_pred[0] == 0:
            resultado = 'sem doença cardíaca'
        else:
            resultado = 'com doença cardíaca'
        
        
        # Envia o resultado por e-mail para o usuário
        subject = 'Resultado da previsão de doença cardíaca'
        message = "Olá {} {}! Gostaríamos de informar que o resultado da sua análise preditiva é: ".format(nome, sobrenome)
                                   
        #message = render_to_string('index.html', {'nome': nome, 'sobrenome': sobrenome, 'resultado': resultado})
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email] 
        #send_mail(subject, message, from_email, recipient_list, html_message=message)
        send_mail(
            'Obrigado por entrar em contato',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return HttpResponseRedirect('/sucesso/')
    else:
        resultado = 'Verifique se preencheu corretamente o formulário'
        
    # Renderiza a página de resultado
    return render(request, 'predict.html', {'resultado': resultado})
"""