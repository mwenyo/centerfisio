var dataFormaPagamento;
var dataTipo;
var oTable;


function modalForm(dataDescricao, dataNatureza, formas_pgto, dataValor) {
    return `
    <form id="id_form_editar" class="need-validation" novalidate>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_descricao">
                        Descrição
                    </label>
                    <textarea id="id_descricao" cols="30" rows="2" class="form-control" required>${dataDescricao}</textarea>
                    <div class="invalid-feedback">Dê uma descrição para movimentação</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_natureza">Natureza da Operação</label>
                    <input type="text" class="form-control input" value="${dataNatureza}" id="id_natureza" placeholder="Ex: Compra de Materiais" required>
                    <div class="invalid-feedback">Informe a natureza da opeação</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col-6">
                <div class="form-group">
                    <label class="form-label">Tipo de Operação</label>
                    <select id="id_tipo" class="select2 form-control input-md" required>
                        <option value="0">ENTRADA</option>
                        <option value="1">SAÍDA</option>
                    </select>
                    <div class="invalid-feedback">Digite o Horário de Atendimento</div>
                </div>
            </div>
            <div class="col-6">
                <div class="form-group">
                    <label class="form-label text-center">Forma de Pagamento</label>
                        <select class="select2 form-control input-md" id="id_forma_pagamento" required>
                        </select>
                        <div class="invalid-feedback">Selecione uma forma de pagamento</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_valor">Valor</label>
                    <input type="number" class="form-control input" min="0.01" step="0.01" value="${dataValor}" id="id_valor" required>
                    <div class="invalid-feedback">Digite um valor válido</div>
                </div>
            </div>
        </div>
    </form>`;

}

$(document).ready(function () {

    csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    // tabela de exibição de dados
    oTable = $('#dt-basic-example').DataTable(
        {
            responsive: true,
            alEditor: true,
            columnDefs: [
                {
                    type: 'date-euro', targets: 0
                }
            ],
            order: [[0, 'desc'], [1, 'asc']]
        });

    // Fechar o caixa
    $("#fechar_caixa").click(function () {
        var dataUrl = $(this).data('url');
        var box = bootbox.dialog(
            {
                title: `Fechamento do Caixa`,
                message: `
                    <div class="row">
                        <div class="col">
                            <div class="text-center">
                                <span class="fs-xl badge badge-warning">
                                    <i class="fas fa-exclamation-triangle"></i>  Cuidado!
                                </span>
                            </div>
                        </div>
                    </div>
                    <hr>
                    <div class="row">
                        <div class="col">
                            <span class="fs-xl">
                                Confira todas as transações para que não haja nenhuma surpresa!
                            </span>
                        </div>
                    </div>`,
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            // envia requisição ao servidor
                            $.ajax({
                                url: dataUrl,
                                data: {
                                    csrfmiddlewaretoken: csrfToken,
                                },
                                type: 'post',
                                dataType: 'json',
                                success: function (response) {
                                    location.href = `/financeiro/caixa/${response.id}/detalhes/`;
                                    box.modal('hide');
                                },
                                error: function (response) {
                                    if (response.status == 403) {
                                        toastr["error"](`Erro ${response.status}: <b>Usuário não autorizado.</b>`, "SIGA");
                                    } else {
                                        console.log(response)
                                        toastr["error"](`Erro ${response.status}: <b>Erro ao fechar o caixa.</b>`, "SIGA");
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
                    },
                    cancel: {
                        label: "Cancelar",
                        className: "btn-default"
                    }
                }
            });

        // coloca o foco no input "saldo_inicial"
        box.on('shown.bs.modal', function () {
            $("#id_saldo_inicial").focus();
        });
    });

    // Registrar movimentação
    $("#movimentar_caixa").on('click', function () {
        var dataCaixa = $(this).data('id');
        var dataDescricao = "";
        var dataNatureza = "";
        var dataValor = "0.00";
        var dataUrl = $(this).data('url');
        var formas_pgto = [];

        // busca as formas de pagamento
        var box = bootbox.dialog(
            {
                title: `Registrar Movimentação do Caixa`,
                message: modalForm(dataDescricao, dataNatureza, formas_pgto, dataValor),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            var descricao = $('#id_descricao').val();
                            var natureza = $('#id_natureza').val();
                            var tipo = $("#id_tipo").select2('data')[0].id
                            var forma_pagamento_id = $("#id_forma_pagamento").select2('data')[0].id
                            var forma_pagamento_nome = $("#id_forma_pagamento").select2('data')[0].text
                            var valor = parseFloat($('#id_valor').val());

                            valor = (Math.round(valor * 100) / 100).toFixed(2);

                            var form = document.getElementById('id_form_editar');

                            if (form.checkValidity() === true) {
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        descricao: descricao,
                                        natureza: natureza,
                                        tipo: tipo,
                                        forma_pagamento: forma_pagamento_id,
                                        valor: valor,
                                        caixa: dataCaixa
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {
                                        data_horario = response['horario'].split('T');
                                        d = data_horario[0].split("-").reverse().join("/");
                                        t = data_horario[1].split(":");
                                        t = `${t[0]}:${t[1]}`;

                                        // cria uma variável temporária para alterar os dados da linha
                                        var temp = [];

                                        // 2020-09-24T17:39:15.346
                                        temp.push(`${d} ${t}`);

                                        temp.push(response['descricao']);
                                        temp.push(response['natureza']);

                                        saldo = parseFloat($('#card_saldo').text().replace(',', '.'));

                                        if (response['tipo'] == 0) {
                                            temp.push(`<span class="badge border border-success text-success">Entrada</span>`);
                                            saldo += parseFloat(response['valor']);
                                        } else {
                                            temp.push(`<span class="badge border border-danger text-danger">Saída</span>`);
                                            saldo -= parseFloat(response['valor']);
                                        }

                                        saldo = (Math.round(saldo * 100) / 100).toFixed(2);

                                        $('#card_saldo').text(saldo.toString().replace(".", ","));

                                        temp.push(forma_pagamento_nome);
                                        
                                        temp.push(`R$ ${response['valor'].replace(".", ',')}`);
                                        temp.push(`
                                            <a href="javascript:void(0);" id="edit_${response['id']}" class="btn btn-sm btn-primary mr-2 edit_mov" title="Editar Movimentação" data-id="${response['id']}" data-url="/financeiro/movimentacao/${response['id']}/editar/">
                                                <i class="fas fa-edit "></i>
                                            </a>
                                            <a href="javascript:void(0);" id="delete_${response.id}" class="btn btn-sm btn-danger mr-2 delete_mov" title="Excluir Movimentação"data-id="${response['id']}" data-url="/financeiro/movimentacao/${response['id']}/excluir/">
                                                <i class="fas fa-times "></i>
                                            </a>
                                            `);

                                        // Esconde a linha
                                        $("tr").each(function () {
                                            var tr = $(this).closest('tr');
                                            var row = oTable.row(tr);
                                            if (row.child.isShown()) {
                                                row.child.hide();
                                                tr.removeClass('parent');

                                            };
                                        });

                                        // inserir linha na tabela
                                        var rowNode = oTable
                                            .row.add(temp)
                                            .draw()
                                            .node();

                                        // atualiza a linha
                                        oTable.columns.adjust().draw();
                                        $('td', rowNode).eq(0).addClass("text-center");
                                        $('td', rowNode).eq(3).addClass("text-center");
                                        $('td', rowNode).eq(6).addClass("text-center");
                                        if(response['tipo'] == 0){
                                            $('td', rowNode).eq(3).data('id', 0);
                                        } else{ 
                                            $('td', rowNode).eq(3).data('id', 1);
                                        }
                                        $('td', rowNode).eq(4).data('id', forma_pagamento_id);
                                        box.modal('hide');

                                        toastr["success"]("Movimentação Registrada.", "SIGA");
                                        toastr.options = {
                                            "closeButton": false,
                                            "debug": false,
                                            "newestOnTop": true,
                                            "progressBar": true,
                                            "positionClass": "toast-top-right",
                                            "preventDuplicates": true,
                                            "showDuration": 300,
                                            "hideDuration": 100,
                                            "timeOut": 2000,
                                            "extendedTimeOut": 1000,
                                            "showEasing": "swing",
                                            "hideEasing": "linear",
                                            "showMethod": "fadeIn",
                                            "hideMethod": "fadeOut"
                                        }
                                    },
                                    error: function (response) {
                                        if (response.status == 403) {
                                            toastr["error"](`Erro ${response.status}: <b>Usuário não autorizado.</b>`, "SIGA");
                                        } else {
                                            console.log(response)
                                            toastr["error"](`Erro ${response.status}: <b>Erro ao movimentar o caixa.</b>`, "SIGA");
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
                                            "timeOut": 2000,
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
            $("#id_descricao").focus();

            $("#id_tipo").select2({
                placeholder: 'Selecione o Tipo',
                dropdownParent: $(".bootbox-body")
            });

            $("#id_forma_pagamento").select2({
                placeholder: 'Selecione uma Forma de Pagamento',
                dropdownParent: $(".bootbox-body")
            });

            $.ajax({
                url: '/financeiro/formas_de_pagamento_ajax/',
                data: {
                    csrfmiddlewaretoken: csrfToken
                },
                type: 'post',
                dataType: 'json',
                async: false,
                success: function (response) {
                    for (i = 0; i < response.length; i++) {
                        var data = {
                            id: response[i].id,
                            text: `${response[i].nome}`
                        }
                        var newOption = new Option(data.text, data.id, false, false);
                        $('#id_forma_pagamento').append(newOption).trigger('change');
                    }
                },
                error: function (response) {
                    console.log(response);
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
        });
    });

    // execução do comando editar de cada linha da tabela 
    oTable.on('click', 'tbody td a.edit_mov, tbody span.dtr-data a.edit_mov', function () {
        var row;
        if ($(this).closest('table').hasClass("collapsed")) {
            var child = $(this).parents("tr.child");
            row = $(child).prevAll(".parent");
        } else {
            row = $(this).parents('tr');
        }
        var temp1 = oTable.row(row).data();
        var temp2 = oTable.row(row).node();
        //var dataId = $(this).data('id');
        var dataDescricao = temp1[1];
        var dataNatureza = temp1[2];
        var dataValor = temp1[5].trim().split(" ")[1].replace(",", ".");
        //dataTipo = parseInt($('td', temp2).eq(3).data('id'));
        var dataUrl = $(this).data('url');
        var formas_pgto = [];
        
        dataTipo = parseInt($('td', temp2).eq(3).data('id'));
        dataFormaPagamento = $('td', temp2).eq(4).data('id');

        // busca as formas de pagamento
        var box = bootbox.dialog(
            {
                title: `Editar Dados da Movimentação`,
                message: modalForm(dataDescricao, dataNatureza, formas_pgto, dataValor),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            var descricao = $('#id_descricao').val();
                            var natureza = $('#id_natureza').val();
                            var tipo = $("#id_tipo").select2('data')[0].id
                            var forma_pagamento_id = $("#id_forma_pagamento").select2('data')[0].id
                            var forma_pagamento_nome = $("#id_forma_pagamento").select2('data')[0].text
                            var valor = parseFloat($('#id_valor').val());

                            valor = (Math.round(valor * 100) / 100).toFixed(2);
                            // console.table({
                            //     'descrição': descricao,
                            //     'natureza': natureza,
                            //     'tipo': tipo,
                            //     'forma_pagamento': forma_pagamento_id + "-" + forma_pagamento_nome,
                            //     'valor': valor
                            // });

                            var form = document.getElementById('id_form_editar');

                            if (form.checkValidity() === true) {
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        descricao: descricao,
                                        natureza: natureza,
                                        tipo: tipo,
                                        forma_pagamento: forma_pagamento_id,
                                        valor: valor
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {

                                        console.log(response);
                                        // cria uma variável temporária para alterar os dados da linha
                                        var temp = oTable.row(row).data();
                                        temp[1] = response['descricao'];
                                        temp[2] = response['natureza'];

                                        var saldo = parseFloat($('#card_saldo').text().replace(',', '.'));
                                        dataValor = parseFloat(dataValor);
                                        var valor_response = parseFloat(response['valor']);
                                        
                                        if(response['tipo'] == 0 && dataTipo == 0){
                                            temp[3] = `<span class="badge border border-success text-success">Entrada</span>`;
                                            $('td', temp2).eq(3).data('id', response['tipo']);
                                            saldo -= dataValor;
                                            saldo += valor_response;
                                        } else if (response['tipo'] == 1 && dataTipo == 1) {
                                            temp[3] = `<span class="badge border border-danger text-danger">Saída</span>`;
                                            $('td', temp2).eq(3).data('id', response['tipo']);

                                            saldo += dataValor;
                                            saldo -= valor_response;
                                        } else if (response['tipo'] == 0 && dataTipo == 1) {
                                            temp[3] = `<span class="badge border border-success text-success">Entrada</span>`;
                                            $('td', temp2).eq(3).data('id', response['tipo']);
                                            saldo += dataValor;
                                            saldo += valor_response;
                                        } else {
                                            temp[3] = `<span class="badge border border-danger text-danger">Saída</span>`;
                                            $('td', temp2).eq(3).data('id', response['tipo']);
                                            saldo -= dataValor;
                                            saldo -= valor_response;
                                        }

                                        saldo = (Math.round(saldo * 100) / 100).toFixed(2);

                                        $('#card_saldo').text(saldo.toString().replace(".", ","));

                                        temp[4] = forma_pagamento_nome;
                                        $('td', temp2).eq(4).data('id', forma_pagamento_id);
                                        temp[5] = `R$ ${response['valor'].replace(".", ',')}`;

                                        // Esconde a linha
                                        $("tr").each(function () {
                                            var tr = $(this).closest('tr');
                                            var row = oTable.row(tr);
                                            if (row.child.isShown()) {
                                                row.child.hide();
                                                tr.removeClass('parent');

                                            };
                                        });

                                        // atualiza a linha
                                        $('#dt-basic-example')
                                            .dataTable()
                                            .fnUpdate(temp, row, undefined, false);

                                        box.modal('hide');

                                        toastr["success"]("Movimentação alterada.", "SIGA");
                                        toastr.options = {
                                            "closeButton": false,
                                            "debug": false,
                                            "newestOnTop": true,
                                            "progressBar": true,
                                            "positionClass": "toast-top-right",
                                            "preventDuplicates": true,
                                            "showDuration": 300,
                                            "hideDuration": 100,
                                            "timeOut": 2000,
                                            "extendedTimeOut": 1000,
                                            "showEasing": "swing",
                                            "hideEasing": "linear",
                                            "showMethod": "fadeIn",
                                            "hideMethod": "fadeOut"
                                        }
                                    },
                                    error: function (response) {

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
                                            "timeOut": 2000,
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
            $("#id_descricao").focus();

            $("#id_tipo").select2({
                placeholder: 'Selecione o Tipo',
                dropdownParent: $(".bootbox-body")
            });

            $("#id_forma_pagamento").select2({
                placeholder: 'Selecione uma Forma de Pagamento',
                dropdownParent: $(".bootbox-body")
            });

            $.ajax({
                url: '/financeiro/formas_de_pagamento_ajax/',
                data: {
                    csrfmiddlewaretoken: csrfToken
                },
                type: 'post',
                dataType: 'json',
                async: false,
                success: function (response) {
                    for (i = 0; i < response.length; i++) {
                        var data = {
                            id: response[i].id,
                            text: `${response[i].nome}`
                        }
                        var newOption = new Option(data.text, data.id, false, false);
                        $('#id_forma_pagamento').append(newOption).trigger('change');
                    }
                },
                error: function (response) {
                    console.log(response);
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
            $("#id_tipo").val(dataTipo);
            $("#id_tipo").trigger('change');

            $("#id_forma_pagamento").val(dataFormaPagamento);
            $("#id_forma_pagamento").trigger('change');
        });
    });

    // execução do comando excluir de cada linha da tabela
    oTable.on('click', 'tbody td a.delete_mov, tbody span.dtr-data a.delete_mov', function () {
        console.log("passou");
        var row;
        if ($(this).closest('table').hasClass("collapsed")) {
            var child = $(this).parents("tr.child");
            row = $(child).prevAll(".parent");
        } else {
            row = $(this).parents('tr');
        }
        var temp1 = oTable.row(row).data();
        var temp2 = oTable.row(row).node();
        var dataDescricao = temp1[1];
        var dataValor = parseFloat(temp1[5].trim().split(" ")[1].replace(",", "."));
        dataTipo = parseInt($('td', temp2).eq(3).data('id'));
        var dataUrl = $(this).data('url');

        var tipo = dataTipo == 0 ? "<b>Entrada</b>" : "<b>Saída</b>";

        bootbox.confirm({
            message: `Deseja excluir a ${tipo} <span class="text-danger">${dataDescricao}</span>?`,
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
                        url: dataUrl,
                        data: {
                            csrfmiddlewaretoken: csrfToken,
                        },
                        type: 'post',
                        dataType: 'json',
                        success: function () {

                            // excui a linha
                            oTable.row(row).remove().draw();

                            // pega o saldo
                            var saldo = parseFloat($('#card_saldo').text().replace(',', '.'));
                            
                            // remove o valor da movimentação
                            saldo += dataTipo == 0 ? -dataValor : dataValor;
                            
                            // formata o número
                            saldo = (Math.round(saldo * 100) / 100).toFixed(2);
                            
                            // escreve de volta
                            $('#card_saldo').text(saldo.toString().replace(".", ","));

                            toastr["success"]("Movimentação excluída", "SIGA");
                            toastr.options = {
                                "closeButton": false,
                                "debug": false,
                                "newestOnTop": true,
                                "progressBar": true,
                                "positionClass": "toast-top-right",
                                "preventDuplicates": true,
                                "showDuration": 300,
                                "hideDuration": 100,
                                "timeOut": 2000,
                                "extendedTimeOut": 1000,
                                "showEasing": "swing",
                                "hideEasing": "linear",
                                "showMethod": "fadeIn",
                                "hideMethod": "fadeOut"
                            }
                        }, error: function(response){
                            if (response.status == 403) {
                                toastr["error"](`Erro ${response.status}: <b>Usuário não autorizado.</b>`, "SIGA");
                            } else {
                                console.log(response)
                                toastr["error"](`Erro ${response.status}: <b>Erro ao excluir.</b>`, "SIGA");
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
                                "timeOut": 2000,
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