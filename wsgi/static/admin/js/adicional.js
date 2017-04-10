function busca_atributos(){

    if( $( "#id_codigo_ifes option:selected" ).val() == ""){
        if($('#tabela tr').length == 2){
            $('#tabela tr:last').remove();
        }
    }else{
                $.ajax({
                    url : "", // the endpoint
                    type : "GET", // http 
                    data : { csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').value, codigo : $( "#id_codigo_ifes option:selected" ).text()  }, // data sent with the post request
                    // handle a successful response
                    success : function(json) {
                        var table = document.getElementById("tabela");
                        if($('#tabela tr').length == 2){
                            $('#tabela tr:last').remove();
                        }
                        var row = table.insertRow(-1);
                        var cell1 = row.insertCell(0);
                        var cell2 = row.insertCell(1);
                        var cell3 = row.insertCell(2);
                        var cell4 = row.insertCell(3);
                        var cell5 = row.insertCell(4);
                        var cell6 = row.insertCell(5);
                        var cell7 = row.insertCell(6);
                        var cell8 = row.insertCell(7);
                        cell1.innerHTML = json.classe;
                        cell2.innerHTML = json.nome_classe;
                        cell3.innerHTML = json.subclasse;
                        cell4.innerHTML = json.assunto;
                        cell5.innerHTML = json.fase_corrente;
                        cell6.innerHTML = json.fase_intermediaria;
                        cell7.innerHTML = json.destinacao_final;
                        cell8.innerHTML = json.observacoes;
                    },

                    // handle a non-successful response
                    error : function(xhr,errmsg,err) {
                        $('#loader').hide();
                        $('#results').html("<div class='alert-box alert radius' data-alert>Opss! Nós encontramos um erro!: "+errmsg+
                            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    }
                });
            }
        }

