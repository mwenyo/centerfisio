function modalForm(dataDescricao, dataInicio, dataTermino) {
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_promocao" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="id_descricao"    >Descricao</label> 
                        <input id="id_descricao" name="descricao" type="text" required class="form-control input-md border border-info" value="${dataDescricao}">
                        <div class="invalid-feedback">Digite um descricao</div> 
                    </div> 
                    <div class="form-group"> 
                        <label class="form-label" for="id_inicio">Inicio</label> 
                        <input id="id_inicio" name="inicio" type="date" class="form-control input-md border border-info" required value="${dataInicio}">
                        <div class="invalid-feedback">Digite um valor válido</div> 
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="id_termino">Termino</label> 
                        <input id="id_termino" name="termino" type="date" class="form-control input-md border border-info" value="${dataTermino}">
                        <div class="invalid-feedback">Digite um valor válido</div> 
                    </div>
                </form>
            </div>
        </div>
      `;
}

function formartar_data(data, lang) {
    if (data) {
        if(lang == 0){
            x = data.split("/");
            return `${x[2]}-${x[1]}-${x[0]}`;
        } else {
            x = data.split("-");
            return `${x[2]}/${x[1]}/${x[0]}`;
        }
    } else {
        return "";
    }
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
    $('#cadastrar_promocao').click(function () {
        var dataUrl = $(this).data('url');

        // cria a modal com o formulário
        var box = bootbox.dialog(
            {
                title: `Adicionar Promoção`,
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
                            var descricao = $('#id_descricao').val();
                            var inicio = $('#id_inicio').val();
                            var termino = $('#id_termino').val();

                            var form = document.getElementById('modal_promocao');

                            if (form.checkValidity() === true) {
                                // envia requisição ao servidor
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        descricao: descricao,
                                        inicio: inicio,
                                        termino: termino
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {

                                        // cria uma variável temporária para armazenar os dados na nova linha
                                        var temp = [
                                            response.descricao,
                                            response.inicio,
                                            response.termino,
                                            `<div class="text-center">
                                            <a href="/estetica/promocoes/${response.id}/detalhes/" class="btn btn-sm btn-success mr-2" title="Detalhes">
                                                <i class="fas fa-eye "></i>
                                            </a>
                                            <a href="javascript:void(0);" id="edit_${response.id}" class="btn btn-sm btn-primary mr-2 edit_promocao" title="Editar" data-descricao="${response.descricao}" data-id="${response.id}" data-url="/estetica/promocoes/${response.id}/editar/">
                                                <i class="fas fa-edit "></i>
                                            </a>
                                            <a href="javascript:void(0);" class="btn btn-sm btn-danger mr-2" title="Excluir" id="del_promocao" data-id="${response.id}" data-url="/estetica/promocoes/${response.id}/excluir/" data-descricao="${response.descricao}">
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

                                        // Adiciona as datas no padrão às células novas 
                                        $('td', rowNode).eq(1).data('padrao', formartar_data(inicio, 1));
                                        $('td', rowNode).eq(2).data('padrao', formartar_data(termino, 1));

                                        // exibe mensagem de sucesso
                                        toastr["success"](`Promoção <strong>${response.descricao}</strong> adicionada.`, "SIGA");
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

        // coloca o foco no input "descricao"
        box.on('shown.bs.modal', function () {
            $("#id_descricao").focus();
        });
    });

    // execução do comando editar de cada linha da tabela
    oTable.on('click', 'tbody td a.edit_promocao, tbody span.dtr-data a.edit_promocao', function () {
        var row;
        if ($(this).closest('table').hasClass("collapsed")) {
            var child = $(this).parents("tr.child");
            row = $(child).prevAll(".parent");
        } else {
            row = $(this).parents('tr');
        }
        var temp1 = oTable.row(row).data();
        var linha = oTable.row(row).node();
        var dataId = $(this).data('id');
        var dataDescricao = temp1[0];
        var dataInicio = formartar_data($('td', linha).eq(1).data('padrao'), 0);
        var dataTermino = formartar_data($('td', linha).eq(2).data('padrao'), 0);
        var dataUrl = $(this).data('url');
        var $this = $(this);
        var box = bootbox.dialog(
            {
                title: `Alterar dados de ${dataDescricao}`,
                message:
                    modalForm(dataDescricao, dataInicio, dataTermino),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            var descricao = $('#id_descricao').val();
                            var inicio = formartar_data($('#id_inicio').val(), 1);
                            var termino = formartar_data($('#id_termino').val(), 1);

                            var form = document.getElementById('modal_promocao');

                            if (form.checkValidity() === true) {
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        id: dataId,
                                        descricao: descricao,
                                        inicio: inicio,
                                        termino: termino
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {
                                        // cria uma variável temporária para alterar os dados da linha
                                        var temp = oTable.row(row).data();

                                        temp[0] = response.descricao;
                                        temp[1] = response.inicio;
                                        temp[2] = response.termino;

                                        $('td', linha).eq(1).data('padrao', inicio);
                                        $('td', linha).eq(2).data('padrao', termino);

                                        // atualiza a linha
                                        $('#dt-basic-example')
                                            .dataTable()
                                            .fnUpdate(temp, row, undefined, false);

                                        $this = $(`tbody td a#edit_${dataId}.edit_promocao, tbody span.dtr-data a.a#edit_${dataId}.edit_promocao`);
                                        $this.attr('data-descricao', response.descricao);

                                        toastr["success"]("Promoção <strong>" + dataDescricao + "</strong> alterada.", "SIGA");
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
            $("#id_descricao").focus();
        });
    });

    // execução do comando excluir de cada linha da tabela
    oTable.on('click', 'tbody td a#del_promocao, tbody span.dtr-data a#del_promocao', function () {
        var dataId = $(this).data('id');
        var dataDescricao = $(this).data('descricao');
        var $this = $(this);
        bootbox.confirm({
            message: `Deseja excluir a promoção <span class="text-danger">${dataDescricao}</span>?`,
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
                        url: `/estetica/promocoes/${dataId}/excluir/`,
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
                            toastr["success"]("Promoção excluída.", "SIGA");
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
