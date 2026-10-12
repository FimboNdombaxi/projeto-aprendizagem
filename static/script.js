// Exemplo: alerta quando o usuário envia um formulário
document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function() {
            alert("Formulário enviado com sucesso!");
        });
    });
});
