document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos o campo de quantidade dentro dos formulários de atualização
    const quant = document.querySelector('#id_quant');
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        quant.addEventListener('change', function() {
            const form = this.closest('form');
            const formData = new FormData(form);
            const url = form.getAttribute('action');

            fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Identifica como requisição AJAX
                    'X-CSRFToken': csrftoken,
                },
            })
            .then(response => {
                if (response.ok) {
                    console.log("atualizado com sucesso")
                } else {
                    console.error('Erro ao atualizar carrinho');
                }
            })
            .catch(error => {
                console.error('Erro na requisição:', error);
            });
        });
    });