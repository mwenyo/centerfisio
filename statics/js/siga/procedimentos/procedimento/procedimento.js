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

function modalForm(dataNome, dataDescricao, dataDuracao, dataValor) {
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_procedimento" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="name">Nome</label> 
                        <input id="id_nome" name="nome" type="text" required class="form-control input-md border border-info" value="${dataNome}">
                        <div class="invalid-feedback">Digite um nome</div> 
                    </div> 
                    <div class="form-group"> 
                        <label class="form-label" for="descricao">Descrição</label> 
                        <textarea id="id_descricao" name="descricao" class="form-control input-md border border-info">${dataDescricao}</textarea>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="duracao">Duração</label> 
                        <input id="id_duracao" name="duracao" class="form-control input-md border border-info" placeholder="Exemplo: 00:30" type="time" max="04:00" min="00:00" value="${dataDuracao}">
                        <div class="invalid-feedback">Digite um valor válido</div>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="valor">Valor</label> 
                        <input id="id_valor" name="valor" class="form-control input-md border border-info" placeholder="Exemplo: 150,50" type="number" max="999.99" min="0" step="0.01" value="${dataValor}" required>
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
        var dataUrl = $(this).data('url');

        // cria a modal com o formulário
        var box = bootbox.dialog(
            {
                title: `Adicionar Procedimento`,
                message:

                    // cria o formulário de cadastro
                    modalForm("", "", "", ""),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            // cria e prepara os dados para serem enviados ao servidor
                            var nome = $('#id_nome').val();
                            var descricao = $('#id_descricao').val();
                            var duracao = $('#id_duracao').val();
                            var valor = $('#id_valor').val();

                            var form = document.getElementById('modal_procedimento');

                            if (form.checkValidity() === true) {
                                // envia requisição ao servidor
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        nome: nome,
                                        descricao: descricao,
                                        duracao: duracao,
                                        valor: valor
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {
                                        if (duracao){
                                            duracao = response.duracao.split(':');
                                            duracao = `${duracao[0]}:${duracao[1]}`;
                                        }
                                        // cria uma variável temporária para armazenar os dados na nova linha
                                        var temp = [
                                            response.nome,
                                            response.descricao,
                                            duracao,
                                            `${troca_ponto(response.valor)}`,
                                            `<div class="text-center">
                                            <a href="javascript:void(0);" id="edit_${response.id}" class="btn btn-sm btn-primary mr-2 edit_procedimento" title="Editar" data-nome="${response.nome}" data-descricao="${response.descricao}" data-duracao="${response.duracao}" data-valor="${response.valor}" data-id="${response.id}" data-url="/estetica/procedimentos/${response.id}/editar/">
                                                <i class="fas fa-edit "></i>
                                            </a>
                                            <a href="javascript:void(0);" class="btn btn-sm btn-danger mr-2" title="Excluir" id="del_procedimento" data-id="${response.id}" data-delete-url="/estetica/procedimentos/${response.id}/excluir/" data-nome="${response.nome}">
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

        // coloca o foco no input "nome"
        box.on('shown.bs.modal', function () {
            $("#id_nome").focus();
        });
    });

    // execução do comando editar de cada linha da tabela
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
        var dataDescricao = temp1[1];
        var dataDuracao = temp1[2];
        var dataValor = troca_virgula(temp1[3]);
        var dataUrl = $(this).data('url');
        var $this = $(this);
        var box = bootbox.dialog(
            {
                title: `Alterar dados de ${dataNome}`,
                message:
                    modalForm(dataNome, dataDescricao, dataDuracao, dataValor),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            var nome = $('#id_nome').val();
                            var descricao = $('#id_descricao').val();
                            var duracao = $('#id_duracao').val();
                            var valor = $('#id_valor').val();

                            var form = document.getElementById('modal_procedimento');

                            if (form.checkValidity() === true) {
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        id: dataId,
                                        nome: nome,
                                        descricao: descricao,
                                        duracao: duracao,
                                        valor: valor,
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {
                                        // cria uma variável temporária para alterar os dados da linha
                                        var temp = oTable.row(row).data();
                                        temp[0] = response.nome
                                        temp[1] = response.descricao
                                        temp[2] = `${response.duracao.split(':')[0]}:${response.duracao.split(':')[1]}`
                                        temp[3] = `${troca_ponto(response.valor)}`

                                        // oTable.row(row).child.hide();
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

                                        $this = $(`tbody td a#edit_${dataId}.edit_procedimento, tbody span.dtr-data a.a#edit_${dataId}.edit_procedimento`);
                                        $this.attr('data-nome', response.nome);
                                        $this.attr('data-descricao', response.descricao);
                                        $this.attr('data-duracao', response.duracao);
                                        $this.attr('data-valor', response.valor);
                                        
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
            $("#id_nome").focus();
        });
    });

    // execução do comando excluir de cada linha da tabela
    oTable.on('click', 'tbody td a#del_procedimento, tbody span.dtr-data a#del_procedimento', function () {
        var dataId = $(this).data('id');
        var dataNome = $(this).data('nome');
        var dataUrl = $(this).data('delete-url');
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
                        url: dataUrl,
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
                            toastr["success"]("Procedimento excluído.", "SIGA");
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
