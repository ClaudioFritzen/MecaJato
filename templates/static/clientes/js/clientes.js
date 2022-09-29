function add_carro(){

    container = document.getElementById("form-carro")

    html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='Carro' class='form-control' name='carro'></div> <div class='col-md'> <input type='text' placeholder='Placa' class='form-control' name='placa'> </div> <div class='col-md'> <input type='number' placeholder='Ano' class='form-control' name='ano'> </div></div>"

    container.innerHTML += html


} 

function exibir_form(tipo){

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if (tipo == '1'){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
        
    }
    else if (tipo == '2'){
        add_cliente.style.display = "none"
        att_client.style.display = "block"
    }

}

function dados_cliente() {
    cliente = document.getElementById('cliente-select')
    
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    // simulação de formulario
    data = new FormData()
    data.append('id_cliente', id_cliente)
    
    
    fetch("/clientes/atualiza_cliente/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function(result) {
        return result.json()
        
    }).then(function(data){
               
        document.getElementById('form-att cliente').style.display = 'block'

        nome = document.getElementById('nome')
        nome.value = data['clientes']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['clientes']['sobrenome']

        email = document.getElementById('email')
        email.value = data['clientes']['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['clientes']['cpf']

        // trazendo os carros pro frontend
        div_carros = document.getElementById('carros')
        div_carros.innerHTML = " "
        for(i=0; i<data['carros'].length; i++){
            console.log(data['carros'][i]['fields']['carros'])

            div_carros.innerHTML+="<form action='' method=''>\
                <div class='row'>\
                    <div='col-md'>\
                        <input class='form-control' type='text' name='carro'>\
                    </div>\
                    <div='col-md'>\
                        <input class='form-control' type='text' name='placa'>\
                    </div>\
                    <div='col-md'>\
                        <input class='form-control' type='text' name='ano' placaholder='leu ate aqui'>\
                    </div>\
                </div>\
            </form><br>"
        }
        
    
    })
    
}