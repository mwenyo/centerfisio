// variáveis globais
var id;
var nome;
var telefone;
var procedimentos;
var promocionais;
var profissional;
var dia;
var horario;
var observacoes;
var situacao;
var caixa_id;
var valor_diferenciado;

function modalForm() {
    return `
    <form id="id_form_editar" class="need-validation" novalidate>
        <div id="id_carregamento">
        <div class="row">
            <h3 class="text-primary"><div class="spinner-border text-primary"></div> Carregando formulário...</h3>
        </div>
        <div class="row">&nbsp;</div>
        </div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label">Situação</label>
                    <select name="status" id="id_buscar_status" class="select2 form-control" required>
                        <option value="0" class="fa-calendar-edit">A CONFIRMAR</option>
                        <option value="1" class="fa-check-square">CONFIRMADO</option>
                        <option value="2" class="fa-hourglass-start">EM ESPERA</option>
                        <option value="3" class="fa-transporter">EM ATENDIMENTO</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <a href="javascript:void(0);" class="btn btn-success" id="id_novo_paciente"><i class="fas fa-plus"></i> Novo Paciente</a>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_buscar_paciente">Buscar Paciente</label>
                    <select id="id_buscar_paciente" class="select2 form-control input-md border border-info" required>
                        <option value=""></option>
                    </select>
                    <div class="invalid-feedback">Selecione um paciente</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_buscar_profissionais">
                        Profissional
                    </label>
                    <select name="profissional" id="id_buscar_profissionais" class="select2 form-control" required>
                        <option value=""></option>
                    </select>
                    <div class="invalid-feedback">Selecione um profissional</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col-6">
                <div class="form-group">
                    <label class="form-label" for="id_data">Data</label>
                    <input type="text" class="form-control input" id="id_data" required>
                    <div class="invalid-feedback">Selecione uma data</div>
                </div>
            </div>
            <div class="col-6">
                <div class="form-group">
                    <label class="form-label">Horário</label>
                    <input type="time" class="form-control input" id="id_horario" required>
                    <div class="invalid-feedback">Digite o Horário de Atendimento</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col-12">
                <div class="form-group">
                    <label class="form-label" id="id_agendamentos_profissional"></label>
                    <!-- Carregar os dados ao selecionar o dia -->
                    <div id="id_carrega_agendamentos"></div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_buscar_promocionais">Procedimentos em Promoção</label>
                    <select name="procedimentos_promo[]" id="id_buscar_promocionais" class="select2 form-control input-md border border-info"
                        multiple="multiple" required>
                        <option value=""></option>
                    </select>
                    <div class="invalid-feedback">Selecione um procedimento</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label" for="id_buscar_procedimentos">Procedimentos</label>
                    <select name="procedimentos[]" id="id_buscar_procedimentos" class="select2 form-control" multiple="multiple"
                    required>
                        <option value=""></option>
                    </select>
                    <div class="invalid-feedback">Selecione um procedimento</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <div class="custom-control custom-switch">
                        <input type="checkbox" class="custom-control-input" id="id_valor_diferenciado">
                        <label class="custom-control-label" for="id_valor_diferenciado">Valor Diferenciado</label>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        
        <div class="row" id="id_linha_valor" style="display: none">
            <div class="col">
                <div class="form-group">
                    <label class="form-label">Valor</label>
                    <input type="number" class="form-control input none" min="0.00" step="0.01" value="0.00" id="id_input_valor_diferenciado" required>
                    <div class="invalid-feedback">Digite um valor válido</div>
                </div>
            </div>
        </div>
        <div class="row">&nbsp;</div>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <label class="form-label">Observações</label>
                    <textarea id="id_observacoes" cols="30" rows="5" class="form-control"></textarea>
                </div>
            </div>
        </div>
    </form>`;
}

function modalFormNovoPaciente() {
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_paciente" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="id_nome">Nome</label> 
                        <input id="id_nome" name="nome" type="text" required class="form-control input-md border border-info value="">
                        <div class="invalid-feedback">Digite o nome do paciente</div> 
                    </div> 
                    <div class="form-group"> 
                        <label class="form-label" for="id_telefone">Telefone</label> 
                        <input type="text" name="telefone" class="form-control border-info" data-inputmask="'mask': '(99) 99999-9999'" im-insert="true" maxlength="20" required id="id_telefone">
                        <div class="invalid-feedback">Digite o telefone do paciente</div> 
                    </div> 
                </form>
            </div>
        </div>
      `;
}

function init_load(dataId) {

    // POPULAR SELECT PROCEDIMENTOS EM PROMOÇÕES
    $.ajax({
        url: '/estetica/procedimentos_promocoes/buscar_procedimentos/',
        type: 'get',
        dataType: 'html',
        async: false,
        success: function (response) {
            $('#id_buscar_promocionais').append(response);

        }, error: function () {
            console.log("Não foi possível carregar os dados");
        }
    });

    // POPULAR SELECT PROFISSIONAIS
    $.ajax({
        url: '/financeiro/usuarios/buscar_profissionais/',
        type: 'get',
        dataType: 'html',
        async: false,
        success: function (response) {
            $('#id_buscar_profissionais').append(response);
        }, error: function () {
            console.log("Não foi possível carregar os dados de profissionais");
        }
    });

    // INICIALIZAÇÃO DO SELECT2
    $("#id_buscar_paciente").select2({
        placeholder: 'Digite o nome ou telefone do paciente',
        dropdownParent: $(".bootbox")
    });

    $("#id_buscar_profissionais").select2({
        placeholder: 'Digite o nome do profissional',
        dropdownParent: $(".bootbox-body")
    });

    $("#id_buscar_promocionais").select2({
        placeholder: 'Digite o nome do procedimento em promocao',
        dropdownParent: $(".bootbox-body")
    });

    $("#id_buscar_procedimentos").select2({
        placeholder: 'Digite o nome do procedimento',
        dropdownParent: $(".bootbox-body")
    });

    function formatState(state) {
        if (!state.id) {
            return state.text;
        }
        var $state = $(
            '<span><i class="fal ' + state.element.className + '"></i> ' + state.text + '</span>'
            );
        console.table({
            'text: ': state.text,
            'id': state.id,
            'rel': state.element
        });
        return $state;
    };
    $("#id_buscar_status").select2({
        templateResult: formatState,
        placeholder: 'Selecione a situação do agendamento',
        dropdownParent: $(".bootbox-body")
    });

    jQuery.fn.extend({
        disable: function (state) {
            return this.each(function () {
                var $this = $(this);
                $this.toggleClass('disabled', state);
            });
        }
    });

    $('#id_valor_diferenciado').change(function () {
        $('#id_linha_valor').toggle(this.checked);
        $('#id_input_valor_diferenciado').disable(!this.checked).focus().select();
    }).change();

    // POPULAR SELECT PACIENTES
    $.ajax({
        url: '/pacientes/buscar_pacientes/',
        type: 'get',
        dataType: 'json',
        async: false,
        success: function (response) {
            for (i = 0; i < response.length; i++) {
                var data = {
                    id: response[i].pk,
                    text: `${response[i].fields['nome']} - ${response[i].fields['telefone']}`
                }
                var newOption = new Option(data.text, data.id, false, false);
                $('#id_buscar_paciente').append(newOption).trigger('change');
            }
        }, error: function () {
            console.log("Não foi possível carregar os dados dos pacientes");
        }
    });

    // POPULAR SELECT PROCEDIMENTOS
    $.ajax({
        url: '/estetica/procedimentos/buscar_procedimentos/',
        type: 'get',
        dataType: 'json',
        async: false,
        success: function (response) {
            for (i = 0; i < response.length; i++) {
                var data = {
                    id: response[i].pk,
                    text: `${response[i].fields['nome']} - R$ ${response[i].fields['valor']}`
                }
                var newOption = new Option(data.text, data.id, false, false);
                $('#id_buscar_procedimentos').append(newOption).trigger('change');
            }
        }, error: function () {
            console.log("Não foi possível carregar os dados dos procedimentos");
        }
    });

    // SELECÇÃO DE DATA
    var controls = {
        leftArrow: '<i class="fal fa-angle-left" style="font-size: 1.25rem"></i>',
        rightArrow: '<i class="fal fa-angle-right" style="font-size: 1.25rem"></i>'
    }
    var hoje = moment().format('DD/MM/YYYY');

    // DATEPICKER
    $('#id_data').datepicker({
        todayHighlight: true,
        templates: controls,
        //startDate: todaysDate,
        startDate: hoje,
        format: "dd/mm/yyyy"
    }).on('change', function () {
        profissional = $("#id_buscar_profissionais").select2('data');
        profissional_id = profissional[0].id;
        profissional_nome = profissional[0].text;
        $.ajax({
            url: '/financeiro/agendamentos/lista_ajax/',
            type: 'post',
            dataType: 'html',
            async: true,
            data: {
                csrfmiddlewaretoken: csrfToken,
                dia: $(this).val().split('/').reverse().join('-')
            },
            success: function (response) {
                $("#id_agendamentos_profissional").html(`Agendamentos para o dia <b>${$('#id_data').val()}</b>.`);
                $("#id_carrega_agendamentos").html(response);
                toastr["info"](`Cuidado para ão agendar dois paciente no mesmo dia/horário com o mesmo profissional!`, "SIGA");
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
                if (response == "Não há agendamentos marcados para esse dia") {
                    $("#id_carrega_agendamentos").style("color", "#FF0");
                }
                p = document.getElementsByClassName('procedimentos_agendados');
                if (p[0].textContent != "Não há agendamentos marcados para esse dia") {
                    s = p[0].textContent;
                    p[0].textContent = `${s.substring(0, s.length - 2)}.`;
                }
            }
        });
    });

    // ADICIONAR PACIENTE
    $('#id_novo_paciente').click(function () {
        var dataUrl = $(this).data('url');

        // cria a modal com o formulário
        var box = bootbox.dialog(
            {
                title: `Adicionar Paciente`,
                message:

                    // cria o formulário de cadastro
                    modalFormNovoPaciente(),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            // cria e prepara os dados para serem enviados ao servidor
                            var nome = $('#id_nome').val();
                            var telefone = $('#id_telefone').val();

                            var form = document.getElementById('modal_paciente');

                            if (form.checkValidity() === true) {
                                // envia requisição ao servidor
                                $.ajax({
                                    url: dataUrl,
                                    async: false,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        nome: nome,
                                        telefone: telefone,
                                    },
                                    type: 'post',
                                    dataType: 'json',
                                    success: function (response) {

                                        var data = {
                                            id: response.id,
                                            text: `${response.nome} - ${response.telefone}`
                                        };

                                        var newOption = new Option(data.text, data.id, false, true);
                                        $('#id_buscar_paciente').append(newOption).trigger('change');

                                        // exibe mensagem de sucesso
                                        toastr["success"](`Paciente <strong>${response.nome}</strong> adicionado(a).`, "SIGA");
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

        // coloca o foco no input "nome"
        box.on('shown.bs.modal', function () {
            $("#id_nome").focus();
            $("#id_telefone").inputmask();
        });
    });

    // CARREGAR OS DADOS DO AGENDAMENTO E COLOCAR NO FORMULÁRIO
    $.ajax({
        url: `/financeiro/agendamentos/detalhe_ajax/${dataId}/`,
        data: {
            csrfmiddlewaretoken: csrfToken,
            id: dataId
        },
        type: 'post',
        dataType: 'json',
        async: false,
        success: function (response) {
            procedimentos_array = [];
            procedimentos_promo_array = [];

            for (i = 0; i < response[1].procedimentos[0].length; i++) {

                procedimentos_array.push(response[1].procedimentos[0][i].id)
            }

            for (i = 0; i < response[2].procedimentos_promo[0].length; i++) {

                procedimentos_promo_array.push(response[2].procedimentos_promo[0][i].id)
            }

            $("#id_buscar_paciente").val(response[0].agendamento[0][0].paciente_id);
            $("#id_buscar_paciente").trigger('change');
            $("#id_buscar_profissionais").val(response[0].agendamento[0][0].profissional_id);
            $("#id_buscar_profissionais").trigger('change');
            $("#id_buscar_status").val(response[0].agendamento[0][0].status);
            $("#id_buscar_status").trigger('change');
            $("#id_data").val(response[0].agendamento[0][0].data.split("-").reverse().join("/"));
            $("#id_horario").val(response[0].agendamento[0][0].horario);
            $("#id_buscar_procedimentos").val(procedimentos_array)
            $("#id_buscar_procedimentos").trigger('change');
            $("#id_buscar_promocionais").val(procedimentos_promo_array)
            $("#id_buscar_promocionais").trigger('change');
            
            if (response[0].agendamento[0][0].valor_diferenciado){
                $("#id_valor_diferenciado").prop("checked", true).trigger('change');
                $("#id_input_valor_diferenciado").val(response[0].agendamento[0][0].valor);
            }

            $("#id_observacoes").val(response[0].agendamento[0][0].observacoes);
        },
        error: function (response) {
            console.error("Os dados não poderam ser carregados");
        }
    });
}

function situacaoFormatacao(tipo) {
    x = "";
    switch (tipo) {
        case 0:
            x = '<span class="badge border border-secondary text-secondary">A CONFIRMAR</span>';
            break;

        case 1:
            x = '<span class="badge border border-info text-info">CONFIRMADO</span>';
            break;

        case 2:
            x = '<span class="badge border border-warning text-black">EM ESPERA</span>';
            break;

        case 3:
            x = '<span class="badge border border-success text-success">EM ATENDIMENTO</span>';
            break;

        case 4:
            x = '<span class="badge border border-danger text-danger">ENCERRADO</span>';
            break;

        default:
            break;
    }
    return x;
}

function modalFormPagar(formas_pgto, paciente, profissional, horario, valor, desconto, total) {
    str_valor = valor.toString().replace('.', ',');
    str_desconto = desconto.toString().replace('.', ',');
    options = "";
    for (i=0;i < formas_pgto.length; i++){
        options += `<option value="${formas_pgto[i].id}">${formas_pgto[i].nome}</option>`;
    }
    return `
    <form id="id_form_pay" class="need-validation" novalidate>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <h4 class="text-primary"><b>${paciente}</b></h4>
                    <h5>${horario}, ${profissional}</h5>
                    <hr>
                </div>
                <div class="form-group">
                    <dl class="row fs-md">
                        <dt class="col-sm-2">Valor</dt>
                        <dl class="col-sm-10 text-info" id="id_total"><b>R$ ${str_valor}</b></dl>
                        <dt class="col-sm-2">Desconto</dt>
                        <dl class="col-sm-10 text-danger" id="id_desconto"><b>R$ ${str_desconto}</b></dl>
                        <dt class="col-sm-2">À Pagar</dt>
                        <dl class="col-sm-10 text-success" id="id_pago"><b>R$ ${total.toString().replace('.', ',')}</b></dl>
                    </dl>
                </div>
            </div>
        </div>
        <div id="forma_pgto">
            <div class="row">&nbsp;</div>
            <hr>
            <div class="row">
                <div class="col-6">
                    <div class="form-group">
                        <label class="form-label text-center">Forma de Pagamento</label>
                        <select class="select2 form-control input-md opt-forma-pagamento" required>
                            ${options}
                        </select>
                        <div class="invalid-feedback">Selecione uma forma de pagamento</div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="form-group">
                        <label class="form-label " for="id_valor">Valor</label>
                        <input type="number" class="form-control input-valor" min="0.00" max="${total}" step="0.01" required value="${total}">
                        <div class="invalid-feedback">Digite o valor pago</div>
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <div class="row">
            <div class="col">
                <div class="form-group">
                    <button type="button" id="id_adicionar_forma_pagamento" class="btn btn-primary btn-sm"><i class="fas fa-plus"></i> Adicionar Forma de Pagamento</button>
                </div>
            </div>
        </div>
    </form>`;
}

$(document).ready(function () {

    $(document).ajaxStart(function () {
        $("#id_carregamento").show();
    });

    $(document).ajaxStop(function () {
        $("#id_carregamento").hide();
    });

    // variável para envio de formulários
    csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    // tabela de exibição de dados
    var oTable = $('#dt-basic-example').DataTable(
        {
            responsive: true,
            alEditor: true,
            columnDefs: [
                {
                    type: 'date-euro', targets: 0
                }
            ],
            order: [[0, 'desc'], [4, 'asc'], [1, 'asc']]
        });

    $('#dt-basic-example').on('page.dt', function () {
        // var info = oTable.page.info();
        // $('#pageInfo').html('Showing page: ' + info.page + ' of ' + info.pages);
        oTable.responsive.rebuild();
        oTable.responsive.recalc();
    });

    // execução do comando editar de cada linha da tabela
    oTable.on('click', 'tbody td a.edit_agendamento, tbody span.dtr-data a.edit_agendamento', function () {
        var dataId = $(this).data('id');
        var row;
        if ($(this).closest('table').hasClass("collapsed")) {
            var child = $(this).parents("tr.child");
            row = $(child).prevAll(".parent");
        } else {
            row = $(this).parents('tr');
        }

        var box = bootbox.dialog(
            {
                title: `Alterar dados do Agendamento`,
                size: 'large',
                onEscape: true,
                backdrop: true,
                message:
                    modalForm(),
                buttons:
                {
                    success:
                    {
                        label: "Salvar",
                        className: "btn-success",
                        callback: function () {

                            var form = document.getElementById('id_form_editar');

                            var $selects = $('#id_buscar_procedimentos, #id_buscar_promocionais');
                            $selects.on('change', function () {
                                $selects.not(this).prop('required', !$(this).val().length);
                            });

                            a = $('#id_buscar_procedimentos');
                            b = $('#id_buscar_promocionais');

                            if (a.val().length != 0 || b.val().length != 0) {

                                a.prop('required', false);
                                b.prop('required', false);

                            } else {

                                a.prop('required', true);
                                b.prop('required', true);

                            }

                            if (form.checkValidity() === true) {

                                // Inicialização das variáveis
                                paciente = $("#id_buscar_paciente").select2('data')[0].id;
                                profissional = $("#id_buscar_profissionais").select2('data')[0].id;
                                dia = $("#id_data").val().split('/').reverse().join('-');
                                horario = $("#id_horario").val();
                                procedimentos = $("#id_buscar_procedimentos").val();
                                promocionais = $("#id_buscar_promocionais").val();
                                observacoes = $("#id_observacoes").val();
                                situacao = $("#id_buscar_status").select2('data')[0].id;

                                if ($("#id_valor_diferenciado").prop("checked")) {
                                    valor_diferenciado = $("#id_input_valor_diferenciado").val();
                                } else {
                                    valor_diferenciado = '';
                                }

                                $.ajax({
                                    url: `/financeiro/agendamentos/editar_ajax/${dataId}/`,
                                    type: 'post',
                                    dataType: 'json',
                                    //async: false,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        paciente: paciente,
                                        profissional: profissional,
                                        dia: dia.split('/').reverse().join('-'),
                                        horario: horario,
                                        procedimentos: procedimentos,
                                        procedimentos_promo: promocionais,
                                        valor_diferenciado: valor_diferenciado,
                                        observacoes: observacoes,
                                        status: situacao
                                    },
                                    success: function (response) {

                                        // preparacao dos dados
                                        tProcedimentos = ""

                                        for (i = 0; i < response[1].procedimentos[0].length; i++) {

                                            tProcedimentos += `${response[1].procedimentos[0][i].nome}, `;
                                        }

                                        for (i = 0; i < response[2].procedimentos_promo[0].length; i++) {

                                            tProcedimentos += `<span class="badge border border-danger text-danger">${response[2].procedimentos_promo[0][i]._nome}</span>, `;
                                        }

                                        paciente = response[0].agendamento[0][0]._paciente;
                                        profissional = response[0].agendamento[0][0]._profissional;
                                        data = response[0].agendamento[0][0]._data.split("-").reverse().join("/");
                                        horario = response[0].agendamento[0][0]._horario.split(':');

                                        horario = horario[0] + ":" + horario[1];

                                        observacoes = response[0].agendamento[0][0]._observacoes;
                                        valor = response[0].agendamento[0][0]._valor;
                                        situacao = situacaoFormatacao(response[0].agendamento[0][0]._situacao);

                                        if (row.length == 0) {
                                            $this = $(`tbody td a#edit_${dataId}.edit_agendamento, tbody span.dtr-data a.a#edit_${dataId}.edit_agendamento`);
                                            row = $this.parents('tr');
                                        }

                                        // pega a linha que foi clicada
                                        var temp1 = oTable.row(row).data();
                                        var temp2 = oTable.row(row).node();
                                        temp1[0] = data;
                                        temp1[1] = horario;
                                        temp1[2] = paciente;
                                        temp1[3] = profissional;
                                        temp1[4] = situacao;
                                        temp1[5] = `${tProcedimentos.substring(0, tProcedimentos.length - 2)}.`;
                                        temp1[6] = observacoes;
                                        temp1[7] = `R$ ${valor.split('.').join(',')}`;

                                        if (response[0].agendamento[0][0]._situacao == 4 || response[0].agendamento[0][0]._situacao == 3) {
                                            temp1[8] = `
                                                <a href="javascript:void(0);" id="pay_${dataId}" data-id="${dataId}" class="btn btn-sm btn-warning mr-2 pay_agendamento" title="Realizar Pagamento">
                                                    <i class="fas fa-badge-dollar "></i>
                                                </a>
                                                `;
                                        } else {
                                            temp1[8] = `
                                                <a href="javascript:void(0);" id="edit_${dataId}" class="btn btn-sm btn-primary mr-2 edit_agendamento" title="Editar Agendamento"data-id="${dataId}">
                                                    <i class="fas fa-edit "></i>
                                                </a>
                                                <a href="javascript:void(0);" id="delete_${dataId}" class="btn btn-sm btn-danger mr-2 delete_agendamento" title="Excluir Agendamento"data-id="${dataId}">
                                                    <i class="fas fa-times "></i>
                                                </a>
                                                `;
                                        }
                                        $('td', temp2).eq(8).addClass("text-center");

                                        // atualiza a linha
                                        $('#dt-basic-example')
                                            .dataTable()
                                            .fnUpdate(temp1, row, undefined, false);

                                        oTable.order([0, 'desc'], [4, 'asc'], [1, 'asc']).draw();

                                        // Esconde a linha
                                        $("tr").each(function () {
                                            var tr = $(this).closest('tr');
                                            var row = oTable.row(tr);
                                            if (row.child.isShown()) {
                                                row.child.hide();
                                                tr.removeClass('parent');

                                            };
                                        });

                                        toastr["success"]("Dados alterados com sucesso");
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
                                        toastr["error"](`Não foi possível salvar o agendamento. <br> ${response.responseJSON[0].valor}`, "SIGA");
                                        toastr.options = {
                                            "closeButton": false,
                                            "debug": false,
                                            "newestOnTop": true,
                                            "progressBar": true,
                                            "positionClass": "toast-top-right",
                                            "preventDuplicates": true,
                                            "showDuration": 300,
                                            "hideDuration": 100,
                                            "timeOut": 4000,
                                            "extendedTimeOut": 1000,
                                            "showEasing": "swing",
                                            "hideEasing": "linear",
                                            "showMethod": "fadeIn",
                                            "hideMethod": "fadeOut"
                                        };
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
            box.removeAttr('tabindex');
            init_load(dataId);
        });
    });

    // execução do comando excluir de cada linha da tabela
    oTable.on('click', 'tbody td a.delete_agendamento, tbody span.dtr-data a.delete_agendamento', function () {

        var dataId = $(this).data('id');
        var row;
        if ($(this).closest('table').hasClass("collapsed")) {
            var child = $(this).parents("tr.child");
            row = $(child).prevAll(".parent");
        } else {
            row = $(this).parents('tr');
        }
        if (row.length == 0) {
            $this = $(`tbody td a#delete_${dataId}.delete_agendamento, tbody span.dtr-data a.a#delete_${dataId}.delete_agendamento`);
            row = $this.parents('tr');
        }

        var temp2 = oTable.row(row).node();
        var dataPaciente = $('td', temp2).eq(2).text();
        var dataDia = $('td', temp2).eq(0).text();
        var dataHorario = $('td', temp2).eq(1).text();

        bootbox.confirm({
            message: `Deseja excluir o agendamento? <span class="text-danger">${dataPaciente} - ${dataDia} às ${dataHorario}</span>?`,
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
                        url: `/financeiro/agendamentos/excluir_ajax/${dataId}/`,
                        data: {
                            csrfmiddlewaretoken: csrfToken,
                            id: dataId
                        },
                        type: 'post',
                        dataType: 'json',
                        success: function () {

                            oTable.row(row).remove().order([0, 'desc'], [4, 'asc'], [1, 'asc']).draw();
                            toastr["success"]("Agendamento excluído.", "SIGA");
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
                        },
                        error: function (response) {
                            if (response.status == 403){
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

    // execução do comando efetuar pagamento
    oTable.on('click', 'tbody td a.pay_agendamento, tbody span.dtr-data a.pay_agendamento', function () {

        // verificar se há um caixa aberto
        var caixa;
        var formas_pgto = [];
        var dataId = $(this).data('id');

        // buscar o caixa e as formas de pagamento
        $.ajax({
            url: '/financeiro/caixa/aberto_ajax/',
            data: {
                csrfmiddlewaretoken: csrfToken
            },
            type: 'post',
            dataType: 'json',
            async: false,
            success: function (response) {
                if (response.result == "fechado") {
                    //location.href = "/financeiro/caixas/";
                    caixa = false;
                    return false;
                } else {
                    caixa = response;

                    // busca as formas de pagamento
                    $.ajax({
                        url: '/financeiro/formas_de_pagamento_ajax/',
                        data: {
                            csrfmiddlewaretoken: csrfToken
                        },
                        type: 'post',
                        dataType: 'json',
                        async: false,
                        success: function (response) {
                            formas_pgto = response;
                        },
                        error: function (response) {
                            console.log(response);
                            toastr["error"](`Algo de errado não está certo: \n${response.responseJSON.result}`, "SIGA");
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
            error: function (response) {
                console.log(response);
                toastr["error"](`Algo de errado não está certo: \n${response.responseJSON.result}`, "SIGA");
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

        // verifica se o caixa está fechado ou se as formas de pagamento estão cadastradas
        if (!caixa && formas_pgto.length == 0) {
            toastr["error"](`Caixa fechado ou Formas de Pagamento não cadastradas!`, "SIGA");
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
            return false;
        }

        var desconto;
        var prosseguir = false;
        var total;

        // Perguntar se tem desconto antes de abrir a tela principal
        var box1 = bootbox.prompt(
            {
                title: `Este agendamento possui <span class="text-danger">Desconto?</span>`,
                inputType: 'text',
                buttons:
                {
                    confirm:
                    {
                        label: "Continuar",
                        className: "btn-primary",
                    },
                    cancel:
                    {
                        label: "Cancelar",
                        className: "btn-secondary",
                        callback: function(){
                            box1.modal('hide');
                        }
                    },
                },
                callback: function (result) {
                    if (result != null) {
                        result = result.trim().replace(",", ".");
                        desconto = Math.abs(parseFloat(result));
                        if (isNaN(desconto)){
                            desconto = 0;
                        }
                        var row2;
                        if ($(this).closest('table').hasClass("collapsed")) {
                            var child = $(this).parents("tr.child");
                            row2 = $(child).prevAll(".parent");
                        } else {
                            row2 = $(this).parents('tr');
                        }
                        if (row2.length == 0) {
                            $this = $(`tbody td a#pay_${dataId}.pay_agendamento, tbody span.dtr-data a.a#pay_${dataId}.pay_agendamento`);
                            row2 = $this.parents('tr');
                        }

                        var temp2 = oTable.row(row2).node();
                        paciente = $('td', temp2).eq(2).text();
                        profissional = $('td', temp2).eq(3).text();
                        valor = parseFloat($('td', temp2).eq(7).text().trim().split(" ")[1].replace(",", "."));
                        horario = `${$('td', temp2).eq(0).text()} às ${$('td', temp2).eq(1).text()}`;

                        desconto = (Math.round(desconto * 100) / 100).toFixed(2);
                        valor = (Math.round(valor * 100) / 100).toFixed(2);
                        total = (Math.round((valor - desconto) * 100) / 100).toFixed(2);
                        prosseguir = true;
                    }
                }
            });
        box1.on('shown.bs.modal', function () {
            var input = $('input.bootbox-input');
            input.attr('placeholder', 'Exemplo: 12,34');
            input.val(0);
            input.trigger('focus');
            input.select();
        }).on('hide.bs.modal', function(){
            if(prosseguir){
                var box = bootbox.dialog({
                    title: "Efetuar Pagamento do Agendamento",
                    message: modalFormPagar(formas_pgto, paciente, profissional, horario, valor, desconto, total),
                    size: 'large',
                    onEscape: true,
                    buttons: {
                        success: {
                            label: "Concluir",
                            className: "btn-primary",
                            callback: function (result) {
                                if (result) {
                                    console.log("Valida o(s) campo(s) e envia os dados.");
                                    var form = document.getElementById('id_form_pay');
                                    if (form.checkValidity() === true) { 
                                        console.log('validado!');

                                        // preparação dos dados
                                        var f_pagamentos = []
                                        $('.opt-forma-pagamento').each(function(){
                                            f_pagamentos.push($(this).val());
                                        });

                                        var valores_pagos = []
                                        $('.input-valor').each(function () {
                                            valores_pagos.push($(this).val());
                                        });

                                        $.ajax({
                                            url: `/financeiro/caixa/receber/${dataId}/`,
                                            data: {
                                                csrfmiddlewaretoken: csrfToken,
                                                caixa: caixa.id,
                                                formas_de_pagamento: f_pagamentos,
                                                valores: valores_pagos,
                                                desconto: desconto
                                            },
                                            type: 'post',
                                            dataType: 'json',
                                            async: false,
                                            success: function (response) {
                                                console.log(response);
                                                if(response.result == "ok"){
                                                    var row;
                                                    if ($(this).closest('table').hasClass("collapsed")) {
                                                        var child = $(this).parents("tr.child");
                                                        row = $(child).prevAll(".parent");
                                                    } else {
                                                        row = $(this).parents('tr');
                                                    }

                                                    if (row.length == 0) {
                                                        $this = $(`tbody td a#pay_${dataId}.pay_agendamento, tbody span.dtr-data a.a#edit_${dataId}.pay_agendamento`);
                                                        row = $this.parents('tr');
                                                    }

                                                    // altera os dados da linha
                                                    var temp1 = oTable.row(row).data();
                                                    temp1[4] = situacaoFormatacao(4);
                                                    temp1[8] = '';

                                                    // atualiza a linha
                                                    $('#dt-basic-example')
                                                        .dataTable()
                                                        .fnUpdate(temp1, row, undefined, false);

                                                    // Esconde a linha
                                                    $("tr").each(function () {
                                                        var tr = $(this).closest('tr');
                                                        var row = oTable.row(tr);
                                                        if (row.child.isShown()) {
                                                            row.child.hide();
                                                            tr.removeClass('parent');

                                                        };
                                                    });

                                                    toastr["success"](`Pagamento realizado com sucesso`, "SIGA");
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
                                                } else {
                                                    console.log(response)
                                                }
                                            },
                                            error: function (response) {
                                                console.log(response);
                                                toastr["error"](`Algo de errado não está certo: \n${response.responseJSON.result}`, "SIGA");
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
                            }
                        },
                        cancel: {
                            label: "Cancelar",
                            className: "btn-secondary"
                        }
                    }
                });
                box.on('shown.bs.modal', function () {
                    $('.modal:visible').length && $(document.body).addClass('modal-open');
                    box.removeAttr('tabindex');
                    $('.input-valor').trigger('focus');
                    $('.input-valor').select();
                    $(this).on('click', '#id_adicionar_forma_pagamento', function (e) {
                        var valor_pago = 0;
                        prosseguir = false;
                        $('.input-valor').each(function(){
                            x = parseFloat($(this).val());

                            // verifica se é um valor válido
                            if(isNaN(x) || x <= 0){
                                x = 0;
                                $(this).val(0);
                                prosseguir = false;
                                $(this).trigger('focus').select();
                                return false;

                            } else {

                                // verifica se esse valor não vai superar o valor total
                                if (valor_pago + x <= total){

                                    // caso seja diferente realiza os cálculos e libera a flag para criar o novo campo
                                    if (x != total){
                                        var formatar = $(this).val();
                                        $(this).val((Math.round(formatar * 100) / 100).toFixed(2));
                                        valor_pago += x;
                                        prosseguir = true;
                                    } else {
                                        prosseguir = false;
                                    }
                                } else {
                                    x = total - valor_pago;
                                    $(this).val((Math.round(x * 100) / 100).toFixed(2));
                                    prosseguir = false;
                                    $(this).trigger('focus').select();
                                }
                            }
                        });
                        if (prosseguir){
                            var valor_restante = total - valor_pago;

                            // verificação para evitar o valor R$ 0,00
                            if (valor_restante == 0) {
                                $('.input-valor').last().trigger('focus').select();
                                return false;
                            }
                            valor_restante = (Math.round(valor_restante * 100) / 100).toFixed(2);
                            options = "";
                            for (i = 0; i < formas_pgto.length; i++) {
                                options += `<option value="${formas_pgto[i].id}">${formas_pgto[i].nome}</option>`;
                            }
                            var n_form = `
                                        <hr>
                                        <div class="row">
                                            <div class="col-6">
                                                <div class="form-group">
                                                    <select class="select2 form-control input-md opt-forma-pagamento" required>
                                                        ${options}
                                                    </select>
                                                    <div class="invalid-feedback">Selecione uma forma de pagamento</div>
                                                </div>
                                            </div>
                                            <div class="col-6">
                                                <div class="form-group">
                                                    <input type="number" class="form-control input-valor" value="${valor_restante}" min="0.00" max="${total}" step="0.01" required>
                                                    <div class="invalid-feedback">Digite o valor pago</div>
                                                </div>
                                            </div>
                                        </div>`;
                            $('#forma_pgto').append(n_form);
                            $(".opt-forma-pagamento").select2({
                                dropdownParent: $(".bootbox-body")
                            });
                        }
                    });
                    $(".opt-forma-pagamento").select2({
                        dropdownParent: $(".bootbox-body")
                    });
                });
            }
        });
        
    });
});