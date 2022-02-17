function modalForm(){
    return `
        <div class="row">
            <div class="col-md-12"> 
                <form id="modal_caixa" class="form-horizontal need-validation" novalidate> 
                    <div class="form-group"> 
                        <label class="form-label" for="id_saldo_inicial">Saldo Inicial</label> 
                        <input id="id_saldo_inicial" name="saldo_inicial" type="number" max="99999,99" min="0.00" step="0.01" required class="form-control input-md border border-info">
                        <div class="invalid-feedback">Digite um valor válido</div> 
                    </div> 
                </form>
            </div>
        </div>
      `;
}


$(document).ready(function () {

    csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    // tabela de exibição de dados
    var oTable = $('#dt-basic-example').DataTable(
        {
            responsive: true,
            order: [[1, "desc"], [0, "asc"], [2, 'desc']]
        });

    $("#caixa_abrir").click(function () {
        var dataUrl = $(this).data('url');
        var box = bootbox.dialog(
            {
                title: `Abrir Caixa`,
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
                            var saldo_inicial = $('#id_saldo_inicial').val();

                            var form = document.getElementById('modal_caixa');

                            if (form.checkValidity() === true) {
                                // envia requisição ao servidor
                                $.ajax({
                                    url: dataUrl,
                                    data: {
                                        csrfmiddlewaretoken: csrfToken,
                                        saldo_inicial: saldo_inicial,
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

        // coloca o foco no input "saldo_inicial"
        box.on('shown.bs.modal', function () {
            $("#id_saldo_inicial").focus();
            $('#id_saldo_inicial').keydown(OnKeyDown);
        });

    });
});


function OnKeyDown(e) {
    var code = (e.keyCode ? e.keyCode : e.which); //to support both methods
    if (code == 13) { //the Enter keycode

        //my actions
        return false;
    }
}
