var id;
var nome;
var telefone;
var procedimentos;
var promocionais;
var profissional;
var dia;
var horario;
var observacoes;
var valor_diferenciado;

function modalForm() {
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

function init_load(){

    // POPULAR SELECT PROCEDIMENTOS EM PROMOÇÕES
    $.ajax({
        url: '/estetica/procedimentos_promocoes/buscar_procedimentos/',
        type: 'get',
        dataType: 'html',
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
        success: function (response) {
            $('#id_buscar_profissionais').append(response);
        }, error: function () {
            console.log("Não foi possível carregar os dados de profissionais");
        }
    });

    // INICIALIZAÇÃO DO WIZARD
    $('#smartwizard').smartWizard({
        selected: 0,
        justified: true,
        autoAdjustHeight: true,
        lang: {
            next: 'Próximo',
            previous: 'Anterior'
        }
    });

    // INICIALIZAÇÃO DO SELECT2
    $("#id_buscar_paciente").select2({
        placeholder: 'Digite o nome ou telefone do paciente',
    });

    $("#id_buscar_promocionais").select2({
        placeholder: 'Digite o nome do procedimento em promocao',
    });

    $("#id_buscar_procedimentos").select2({
        placeholder: 'Digite o nome do procedimento',
    });

    $("#id_buscar_profissionais").select2({
        placeholder: 'Digite o nome do profissional',
    });


    // POPULAR SELECT PACIENTES
    $.ajax({
        url: '/pacientes/buscar_pacientes/',
        type: 'get',
        dataType: 'json',
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
            console.log("Não foi possível carregar os dados");
        }
    });

    // POPULAR SELECT PROCEDIMENTOS
    $.ajax({
        url: '/estetica/procedimentos/buscar_procedimentos/',
        type: 'get',
        dataType: 'json',
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
            console.log("Não foi possível carregar os dados");
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
        autoclose: true,
        format: "dd/mm/yyyy"
    }).on('change', function () {
        profissional = $("#id_buscar_profissionais").select2('data');
        profissional_id = profissional[0].id;
        profissional_nome = profissional[0].text;
        $.ajax({
            url: '/financeiro/agendamentos/lista_ajax/',
            type: 'post',
            dataType: 'html',
            data: {
                csrfmiddlewaretoken: csrfToken,
                dia: $(this).val().split('/').reverse().join('-')
            },
            success: function (response) {
                $("#id_agendamentos_profissional").html(`Agendamentos para o dia <b>${$('#id_data').val()}</b>.`);
                $("#id_carrega_agendamentos").html(response);
                console.log(response)
                if (response.trim() != `<span class="procedimentos_agendados">Não há agendamentos marcados para esse dia</span>`){
                    toastr["warning"](`Cuidado para não agendar dois paciente no mesmo dia/horário com o mesmo profissional!`, "SIGA");
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
                document.getElementById('id_horario').focus();
                p = document.getElementsByClassName('procedimentos_agendados');
                s = p.textContent;
                //p.textContent = `${s.substring(0, s.length - 2)}.`;
            }
        });
    });

    // SALVAR AGENDAMENTO
    $("#id_salvar").click(function () {
        $.ajax({
            url: '/financeiro/agendamentos/adicionar/',
            type: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrfToken,
                paciente: id,
                profissional: profissional[0].id,
                dia: dia.split('/').reverse().join('-'),
                horario: horario,
                procedimentos: procedimentos,
                procedimentos_promo: promocionais,
                valor_diferenciado: valor_diferenciado,
                observacoes: observacoes
            },
            success: function (response) {
                if (response.result === "ok") {
                    toastr["success"]("<b>Agendamento realizado.</b><br>Redirecionando...", "SIGA");
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
                    };
                    toastr.options.onHidden = function () {
                        location.href = '/financeiro/agendamentos/';
                    };
                    location.href = '/financeiro/agendamentos/';
                }
            },
            error: function (response) {
                //console.log(response.responseJSON[0]);
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
                    modalForm(),
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
}

$(document).ready(function () {

    // variável para envio de formulários
    csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    moment.locale('pt-br');
    

    // carrega todos plugins e popula os selects
    init_load();

    if (document.getElementById('id_buscar_paciente').value === "") {
        $('#smartwizard').smartWizard("reset");
        $('#smartwizard').smartWizard("goToStep", 0);
    }

    // CONFIGURAÇÃO DOS PASSOS
    $("#smartwizard").on("showStep", function(e, anchorObject, stepNumber, stepDirection){
        if (stepNumber === 3) {
            var data_paciente = $("#id_buscar_paciente").select2('data');
            var data_procedimentos = $("#id_buscar_procedimentos").select2('data');
            var data_promocao = $("#id_buscar_promocionais").select2('data');
            profissional = $("#id_buscar_profissionais").select2('data');
            var now = moment($("#id_data").val(), "DD/MM/YYYY");
            now = now.add(parseInt($("#id_horario").val().split(':')[0]), 'h');
            now = now.add(parseInt($("#id_horario").val().split(':')[1]), 'm');
            
            var text = "";

            for (i = 0; i < data_procedimentos.length; i++){
                text += `${data_procedimentos[i].text}, `;
            }
            for (i = 0; i < data_promocao.length; i++){
                text += `${data_promocao[i].text}, `;
            }

            text = text.substring(0, text.length-2);

            id = data_paciente[0].id;
            nome = data_paciente[0].text.split(" - ")[0];
            telefone = data_paciente[0].text.split(" - ")[1];
            dia = $("#id_data").val();
            horario = $("#id_horario").val();
            procedimentos = $("#id_buscar_procedimentos").val();
            promocionais = $("#id_buscar_promocionais").val();
            observacoes = $("#id_observacoes").val();
            valor_diferenciado = $("#id_input_valor_diferenciado").val();
            valor_diferenciado = (Math.round(valor_diferenciado * 100) / 100).toFixed(2);

            $("#id_conclusao_paciente").text(nome);
            $("#id_conclusao_telefone").text(telefone);
            $("#id_conclusao_profissional").text(profissional[0].text);
            $("#id_conclusao_dia_horario").text(`${dia} às ${horario}, (${now.fromNow()})`);
            $("#id_conclusao_procedimentos").text(text);
            $("#id_conclusao_observacoes").text(observacoes);
            if(!$('#id_valor_diferenciado').prop('checked')){
                $('.valor-diferenciado').toggle($('#id_valor_diferenciado').prop('checked'));
                valor_diferenciado = '';
            } else {
                $('.valor-diferenciado').toggle($('#id_valor_diferenciado').prop('checked'));
                $("#id_conclusao_valor").text('R$ ' + valor_diferenciado.toString().replace('.', ','));
            }
        }
        if (stepNumber === 1) {
            var $selects = $('#id_buscar_procedimentos, #id_buscar_promocionais');
            $selects.on('change', function () {
                $selects.not(this).prop('required', !$(this).val().length);
            });
        } else if (stepNumber === 2) {
            $("#id_observacoes").focus();
        }
    });

    // VALIDAÇÃO DOS FORMULÁRIOS
    $("#smartwizard").on("leaveStep", function(e, anchorObject, stepNumber, stepDirection){
        var elmForm = document.getElementById(`form-step-${stepNumber}`);
        if (stepDirection === 'forward' && elmForm) {
            if (elmForm.checkValidity() === false) {
                elmForm.classList.add('was-validated');
                return false;
            } else {
                return true;
            }
        }
        return true;
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
});