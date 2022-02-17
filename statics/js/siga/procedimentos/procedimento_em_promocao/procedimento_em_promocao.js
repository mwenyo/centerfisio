function troca_virgula(x) {
    if (x != null || x != undefined || x != "") {
        x = x.split(",");
        if (x[1] != undefined)
            x = `${x[0]}.${x[1]}`;
        else
            x = `${x[0]}.00`;
        return x;
    }
    return "0.00";
}

function troca_ponto(x) {
    if (x != null || x != undefined || x != "") {
        x = x.split(".");
        if (x[1] != undefined)
            x = `${x[0]},${x[1]}`;
        else
            x = `${x[0]},00`;
        return x;
    }
    return "0,00";
}

function modalForm2() {   
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_procedimento" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="name">Procedimento</label> 
                        <select class="select2 form-control" id="id_procedimento" required>
                        </select>
                        <div class="invalid-feedback">Digite um valor válido</div>
                    </div> 
                    <div class="form-group">
                        <label class="form-label" for="name">Valor Original</label>
                        <input id="id_valor_original" name="valor_original" type="text" class="form-control input-md border border-info" value="" readonly> 
                    </div> 
                    <div class="form-group">
                        <label class="form-label" for="name">Valor Promocional</label>
                        <input id="id_valor_promocional" name="valor_promocional" type="number" min="0" step="0.01" required class="form-control input-md border border-info"> 
                        <div class="invalid-feedback">Digite um valor válido</div>
                    </div>
                </form>
            </div>
        </div>
      `;
}

function modalForm(dataValorOriginal, dataValorPromocional) {
    var max = parseFloat(dataValorOriginal) - 0.01;
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_procedimento" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="name">Valor Original</label> 
                        <input id="id_valor_original" name="valor_original" type="text" required class="form-control input-md border border-info" value="${troca_ponto(dataValorOriginal)}" readonly> 
                    </div> 
                    <div class="form-group"> 
                        <label class="form-label" for="name">Valor Promocional</label> 
                        <input id="id_valor_promocional" name="valor_promocional" type="number" max="${max}" min="0" step="0.01" required class="form-control input-md border border-info" value="${dataValorPromocional}"> 
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
    
    // execução do comando de criar procedimento
    $('#cadastrar_procedimento').click(function () {
        dataUrl = $(this).data('url');
        var dataId = $(this).data('id');

        // cria a modal com o formulário
        var box = bootbox.dialog(
            {
                title: `Adicionar Procedimento à Promoção`,
                message:

                    // cria o formulário de cadastro
                    modalForm2(),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            // cria e prepara os dados para serem enviados ao servidor
                            var valor_promocional = $('#id_valor_promocional').val();
                            var procedimento = $('#id_procedimento').val();
                            var dataUrl = `/estetica/procedimentos_promocoes/adicionar/`;

                            var form = document.getElementById('modal_procedimento');

                            if (form.checkValidity() === true) {
                                // envia requisição ao servidor
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        procedimento: procedimento,
                                        promocao: dataId,
                                        valor_promocional: valor_promocional
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {

                                        // cria uma variável temporária para armazenar os dados na nova linha
                                        var temp = [
                                            response.procedimento.nome,
                                            response.procedimento.descricao,
                                            `${troca_ponto(response.procedimento.valor)}`,
                                            `${troca_ponto(response.procedimento_promocao.valor_promocional)}`,
                                            `<div class="text-center">
                                            <a href="javascript:void(0);" id="edit_${response.procedimento_promocao.id}" class="btn btn-sm btn-primary mr-2 edit_procedimento" title="Editar"
                                            data-nome="${response.procedimento.nome}" data-id="${response.procedimento_promocao.id}" data-url="/estetica/procedimentos_promocoes/${response.procedimento_promocao.id}/editar/">
                                            <i class="fas fa-edit "></i>
                                            </a>
                                            <a href="javascript:void(0);" class="btn btn-sm btn-danger mr-2" title="Excluir" id="del_procedimento" data-id="${response.procedimento_promocao.id}" data-nome="${response.procedimento.nome}" data-url="/estetica/procedimentos_promocoes/${response.procedimento_promocao.id}/excluir/">
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
                                        $('td', rowNode).eq(2).addClass("text-center");
                                        $('td', rowNode).eq(3).addClass("text-center");

                                        // exibe mensagem de sucesso
                                        toastr["success"](`Procedimento <strong>${response.nome}</strong> adicionada.`, "SIGA");
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

        // carrega os procedimentos disponíveis
        $.ajax({
            url: dataUrl,
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: 'post',
            dataType: 'html',
            success: function (response) {
                $('#id_procedimento').append(response);
            },
            error: function (params) {
                console.log("deu ruim");
            }
        });

        $('#id_procedimento').on('change', function(e){
            var valor = $(this).find(':selected').data('valor');
            $('#id_valor_original').val(valor);
            $('#id_valor_promocional').attr('max', parseFloat(valor) - 0.01);
        });

        box.on('shown.bs.modal', function () {
            box.removeAttr('tabindex');
            $('#id_procedimento').select2({
                dropdownParent: $(".bootbox")
            });
            $("#id_procedimento").focus();
        });
    });

    // OK - execução do comando editar de cada linha da tabela 
    oTable.on('click', 'tbody td a.edit_procedimento, tbody span.dtr-data a.edit_procedimento', function () {
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
        var dataValorOriginal = troca_virgula(temp1[2]);
        var dataValorPromocional = troca_virgula(temp1[3]);
        var dataUrl = $(this).data('url');

        var box = bootbox.dialog(
            {
                title: `Alterar Valor Promocional do Procedimento <strong>${dataNome}</strong>`,
                message:
                    modalForm(dataValorOriginal, dataValorPromocional),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            var valor_promocional = $('#id_valor_promocional').val();

                            var form = document.getElementById('modal_procedimento');

                            if (form.checkValidity() === true) {
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        id: dataId,
                                        valor_promocional: valor_promocional,
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {
                                        
                                        // cria uma variável temporária para alterar os dados da linha
                                        var temp = oTable.row(row).data();
                                        temp[3] = `${troca_ponto(response.valor_promocional)}`

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

                                        toastr["success"]("Procedimento <strong>" + dataNome + "</strong> alterada.", "SIGA");
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
            $("#id_valor_promocional").focus();
        });
    });

    // OK - execução do comando excluir de cada linha da tabela
    oTable.on('click', 'tbody td a#del_procedimento, tbody span.dtr-data a#del_procedimento', function () {
        var dataId = $(this).data('id');
        var dataNome = $(this).data('nome');
        var $this = $(this);
        bootbox.confirm({
            message: `Deseja excluir a procedimento <span class="text-danger">${dataNome}</span>?`,
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
                        url: `/estetica/procedimentos_promocoes/${dataId}/excluir/`,
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
                            toastr["success"]("Procedimento excluído da promoção", "SIGA");
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
