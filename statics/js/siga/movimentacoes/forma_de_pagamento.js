function troca_virgula(x) {
    if (x != null || x != undefined || x != "") {
        x = x.split(",");
        if (x[1] != undefined)
            x = `${x[0]}.${x[1]}`;
        else
            x = `${x[0]}.0000`;
        return x;
    }
    return "0.0000";
}

function troca_ponto(x) {
    if (x != null || x != undefined || x != "") {
        x = x.split(".");
        if(x[1] != undefined)
            x = `${x[0]},${x[1]}`;
        else
            x = `${x[0]},0000`;
        return x;
    }
    return "0,0000";
}

function modalForm(dataNome, dataAcrescimo, dataDesconto){
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_forma_de_pagamento" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="name">Nome</label> 
                        <input id="id_nome" name="nome" type="text" required class="form-control input-md border border-info" value="${dataNome}">
                        <div class="invalid-feedback">Digite um nome</div> 
                    </div> 
                    <div class="form-group"> 
                        <label class="form-label" for="acrescimo">Acrescimo</label> 
                        <input id="id_acrescimo" name="acrescimo" type="number" max="99.9999" min="0" step="0.0001" class="form-control input-md border border-info" required placeholder="Exemplo: 1,2345" value="${dataAcrescimo}">
                        <div class="invalid-feedback">Digite um valor válido</div> 
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="desconto">Desconto</label> 
                        <input id="id_desconto" name="desconto" class="form-control input-md border border-info" required placeholder="Exemplo: 5,4321"  type="number" max="99.9999" min="0" step="0.0001" value="${dataDesconto}">
                        <div class="invalid-feedback">Digite um valor válido</div> 
                    </div>
                </form>
            </div>
        </div>
      `;
}
$(document).ready(function () {
    // variável para envio de formulários
    csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    // tabela de exibição de dados
    var oTable = $('#dt-basic-example').DataTable(
        {
            responsive: true,
            columnDefs: [
                {
                    type: 'alt-string', targets: 2
                }
            ]
        });

    $('#dt-basic-example').on('page.dt', function () {
        // var info = oTable.page.info();
        // $('#pageInfo').html('Showing page: ' + info.page + ' of ' + info.pages);
        oTable.responsive.rebuild();
        oTable.responsive.recalc();
    });

    // execução do comando de criar forma de pagamento
    $('#cadastrar_forma_de_pagamento').click(function(){
        console.log('Cadastrar Forma de Pagamento');
        var dataUrl = $(this).data('url');

        // cria a modal com o formulário
        var box = bootbox.dialog(
        {
            title: `Adicionar Forma de Pagamento`,
            message:

                // cria o formulário de cadastro
                modalForm("", "", ""),
            buttons:
            {
                success:
                {
                    label: "Salvar",
                    className: "btn-success",
                    callback: function () {

                        // cria e prepara os dados para serem enviados ao servidor
                        var nome = $('#id_nome').val();
                        var acrescimo = $('#id_acrescimo').val();
                        var desconto = $('#id_desconto').val();

                        var form = document.getElementById('modal_forma_de_pagamento');

                        if (form.checkValidity() === true) {
                            // envia requisição ao servidor
                            $.ajax({
                                url: dataUrl,
                                data: {
                                    csrfmiddlewaretoken: csrfToken,
                                    nome: nome,
                                    acrescimo: acrescimo,
                                    desconto: desconto
                                },
                                type: 'post',
                                dataType: 'json',
                                success: function (response) {

                                    // cria uma variável temporária para armazenar os dados na nova linha
                                    var temp = [
                                        response.nome,
                                        `${troca_ponto(response.acrescimo)}%`,
                                        `${troca_ponto(response.desconto)}%`,
                                        `<div class="text-center">
                                            <a href="javascript:void(0);" id="edit_${response.id}" class="btn btn-sm btn-primary mr-2 edit_fpgto" title="Detalhes" data-nome="${response.nome}" data-acrescimo="${response.acrescimo}" data-desconto="${response.desconto}" data-id="${response.id}" data-url="/financeiro/forma_pgto/${response.id}/editar/">
                                                <i class="fas fa-edit "></i>
                                            </a>
                                            <a href="javascript:void(0);" class="btn btn-sm btn-danger mr-2" title="Detalhes" id="del_fpgto" data-id="${response.id}" data-url="/financeiro/forma_pgto/${response.id}/excluir/" data-nome="${response.nome}">
                                                <i class="fas fa-times "></i>
                                            </a>
                                        </div>`
                                    ]
                                    
                                    // inserir linha na tabela
                                    var rowNode = oTable
                                        .row.add(temp)
                                        .draw()
                                        .node();

                                    // Ajusta a tabela para exibir as colunas ocultas e o botão de expandir 
                                    oTable.columns.adjust().draw();

                                    // Adiciona a classe text-center às células novas 
                                    $('td', rowNode).eq(1).addClass("text-center");
                                    $('td', rowNode).eq(2).addClass("text-center");

                                    // exibe mensagem de sucesso
                                    toastr["success"](`Forma de pagamento <strong>${response.nome}</strong> adicionada.`, "SIGA");
                                    toastr.options = {
                                        "closeButton": false,
                                        "debug": false,
                                        "newestOnTop": true,
                                        "progressBar": true,
                                        "positionClass": "toast-top-right",
                                        "preventDuplicates": true,
                                        "showDuration": 300,
                                        "hideDuration": 100,
                                        "timeOut": 3000,
                                        "extendedTimeOut": 1000,
                                        "showEasing": "swing",
                                        "hideEasing": "linear",
                                        "showMethod": "fadeIn",
                                        "hideMethod": "fadeOut"
                                    }
                                    box.modal('hide');
                                },
                                error: function(response) {
                                    if (response.status == 403) {
                                        toastr["error"](`Erro ${response.status}: <b>Usuário não autorizado.</b>`, "SIGA");
                                    } else {
                                        console.log(response)
                                        toastr["error"](`Erro ${response.status}: <b>Erro no servidor.</b>`, "SIGA");
                                    }
                                    toastr.options = {
                                        "closeButton": false,
                                        "debug": false,
                                        "newestOnTop": true,
                                        "progressBar": true,
                                        "positionClass": "toast-top-right",
                                        "preventDuplicates": true,
                                        "showDuration": 300,
                                        "hideDuration": 100,
                                        "timeOut": 3000,
                                        "extendedTimeOut": 1000,
                                        "showEasing": "swing",
                                        "hideEasing": "linear",
                                        "showMethod": "fadeIn",
                                        "hideMethod": "fadeOut"
                                    }
                                }
                            });
                        } else {
                            form.classList.add('was-validated');
                        }
                        return false;
                    }
                },
                cancel: {
                    label: "Cancelar",
                    className: "btn-default"
                }
            }
        });

        // coloca o foco no input "nome"
        box.on('shown.bs.modal', function () {
            $("#id_nome").focus();
        });
    });
    
    // execução do comando editar de cada linha da tabela
    oTable.on('click', 'tbody td a.edit_fpgto, tbody span.dtr-data a.edit_fpgto', function () {
        var row;
        if ($(this).closest('table').hasClass("collapsed")) {
            var child = $(this).parents("tr.child");
            row = $(child).prevAll(".parent");
        } else {
            row = $(this).parents('tr');
        }
        var temp1 = oTable.row(row).data();
        var dataId = $(this).data('id');
        var dataNome = temp1[0];
        var dataAcrescimo = troca_virgula(temp1[1].split("%")[0]); 
        var dataDesconto = troca_virgula(temp1[2].split("%")[0]); 
        var dataUrl = $(this).data('url');
        var $this = $(this);
        var box = bootbox.dialog(
        {
            title: `Alterar dados de ${dataNome}`,
            message: 
               modalForm(dataNome, dataAcrescimo, dataDesconto),
            buttons:
            {
                success:
                {
                    label: "Salvar",
                    className: "btn-success",
                    callback: function () {

                        var nome = $('#id_nome').val();
                        var acrescimo = $('#id_acrescimo').val();
                        var desconto = $('#id_desconto').val();
                        
                        var form = document.getElementById('modal_forma_de_pagamento');
                        
                        if (form.checkValidity() === true){
                            $.ajax({
                                url: dataUrl,
                                data: {
                                    csrfmiddlewaretoken: csrfToken,
                                    id: dataId,
                                    nome: nome, 
                                    acrescimo: acrescimo,
                                    desconto: desconto
                                },
                                type: 'post',
                                dataType: 'json',
                                success: function (response) {
                                    // cria uma variável temporária para alterar os dados da linha
                                    var temp = oTable.row(row).data();
                                    temp[0] = response.nome
                                    temp[1] = `${troca_ponto(response.acrescimo)}%`
                                    temp[2] = `${troca_ponto(response.desconto)}%`

                                    // atualiza a linha
                                    $('#dt-basic-example')
                                        .dataTable()
                                        .fnUpdate(temp, row, undefined, false);

                                    $this = $(`tbody td a#edit_${dataId}.edit_fpgto, tbody span.dtr-data a.a#edit_${dataId}.edit_fpgto`);
                                    $this.attr('data-nome', response.nome);
                                    $this.attr('data-acrescimo', response.acrescimo);
                                    $this.attr('data-desconto', response.desconto);

                                    toastr["success"]("Forma de pagamento <strong>" + dataNome + "</strong> alterada.", "SIGA");
                                    toastr.options = {
                                        "closeButton": false,
                                        "debug": false,
                                        "newestOnTop": true,
                                        "progressBar": true,
                                        "positionClass": "toast-top-right",
                                        "preventDuplicates": true,
                                        "showDuration": 300,
                                        "hideDuration": 100,
                                        "timeOut": 3000,
                                        "extendedTimeOut": 1000,
                                        "showEasing": "swing",
                                        "hideEasing": "linear",
                                        "showMethod": "fadeIn",
                                        "hideMethod": "fadeOut"
                                    }
                                    box.modal('hide');
                                },
                                error: function (response) {

                                    toastr["error"](`Algo de errado não está certo: \n${response.result}`, "SIGA");
                                    toastr.options = {
                                        "closeButton": false,
                                        "debug": false,
                                        "newestOnTop": true,
                                        "progressBar": true,
                                        "positionClass": "toast-top-right",
                                        "preventDuplicates": true,
                                        "showDuration": 300,
                                        "hideDuration": 100,
                                        "timeOut": 3000,
                                        "extendedTimeOut": 1000,
                                        "showEasing": "swing",
                                        "hideEasing": "linear",
                                        "showMethod": "fadeIn",
                                        "hideMethod": "fadeOut"
                                    }
                                }
                            });
                        } else {
                            form.classList.add('was-validated');
                        }
                        return false;
                    }
                },
                cancel: {
                    label: "Cancelar",
                    className: "btn-default"
                }
            }
        });
        box.on('shown.bs.modal', function () {
            $("#id_nome").focus();
        });
    });

    // execução do comando excluir de cada linha da tabela
    oTable.on('click','tbody td a#del_fpgto, tbody span.dtr-data a#del_fpgto', function () {
        var dataId = $(this).data('id');
        var dataNome = $(this).data('nome');
        var $this = $(this);
        bootbox.confirm({
            message: `Deseja excluir a forma de pagamento <span class="text-danger">${dataNome}</span>?`,
            buttons: {
                confirm: {
                    label: "Sim",
                    className: "btn-primary"
                },
                cancel: {
                    label: "Não",
                    className: "btn-danger"
                }
            },
            callback: function (result) {
                if (result) {
                    $.ajax({
                        url: `/financeiro/forma_pgto/${dataId}/excluir/`,
                        data: {
                            csrfmiddlewaretoken: csrfToken,
                            id: dataId
                        },
                        type: 'post',
                        dataType: 'json',
                        success: function () {
                            var row;
                            if ($this.closest('table').hasClass("collapsed")) {
                                var child = $this.parents("tr.child");
                                row = $(child).prevAll(".parent");
                            } else {
                                row = $this.parents('tr');
                            }
                            oTable.row(row).remove().draw();
                            if (response.status == 403) {
                                toastr["error"](`Erro ${response.status}: <b>Usuário não autorizado.</b>`, "SIGA");
                            } else {
                                console.log(response)
                                toastr["error"](`Erro ${response.status}: <b>Erro no servidor.</b>`, "SIGA");
                            }
                            toastr.options = {
                                "closeButton": false,
                                "debug": false,
                                "newestOnTop": true,
                                "progressBar": true,
                                "positionClass": "toast-top-right",
                                "preventDuplicates": true,
                                "showDuration": 300,
                                "hideDuration": 100,
                                "timeOut": 3000,
                                "extendedTimeOut": 1000,
                                "showEasing": "swing",
                                "hideEasing": "linear",
                                "showMethod": "fadeIn",
                                "hideMethod": "fadeOut"
                            }
                        }
                    });
                }
            }
        });
    });
});
