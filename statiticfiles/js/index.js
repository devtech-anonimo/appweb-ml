document.getElementById('submit-form').addEventListener('click', function(event) {
    event.preventDefault(); // Previne o envio do formulário
    
    // Obtém os valores dos campos do formulário
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var age = parseInt(document.getElementById('age').value);
    var gender = document.getElementById('gender').value;
    var weight = parseFloat(document.getElementById('weight').value);
    var height = parseFloat(document.getElementById('height').value);
    var systolicPressure = parseInt(document.getElementById('systolic-pressure').value);
    var diastolicPressure = parseInt(document.getElementById('diastolic-pressure').value);
    var glucose = parseInt(document.getElementById('glucose').value);
    
    // Cria objeto com os dados do formulário
    var formData = {
        'name': name,
        'email': email,
        'age': age,
        'gender': gender,
        'weight': weight,
        'height': height,
        'systolic_pressure': systolicPressure,
        'diastolic_pressure': diastolicPressure,
        'glucose': glucose
    };
    
    // Envia requisição POST para a view em Django
    fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Atualiza o resultado na página
        var result = document.getElementById('result');
        if (data.result === 'positive') {
            result.innerHTML = '<p>Você possui uma doença cardíaca. Consulte um médico o quanto antes.</p>';
            result.classList.add('positive-result');
        } else {
            result.innerHTML = '<p>Você não possui uma doença cardíaca. Continue cuidando da sua saúde.</p>';
            result.classList.add('negative-result');
        }
    })
    .catch(error => {
        console.error('Erro ao enviar dados do formulário:', error);
    });
});
