const comentariosDiv = document.getElementById("listaComentarios");
const formComentario = document.getElementById("formComentario");
const comentarioTexto = document.getElementById("comentarioTexto");

let comentarios = JSON.parse(localStorage.getItem("comentariosFeria")) || [];

function cargarComentarios() {
    if (!comentariosDiv) return;

    comentariosDiv.innerHTML = "";

    comentarios.forEach(c => {
        comentariosDiv.innerHTML += `
            <div class="mb-2">
                <strong>${c.usuario}:</strong>
                <p>${c.texto}</p>
            </div>
        `;
    });
}

if (formComentario) {
    formComentario.addEventListener("submit", e => {
        e.preventDefault();

        let sesion = JSON.parse(localStorage.getItem("sesion"));

        if (!sesion) {
            alert("Debes iniciar sesión para comentar");
            return;
        }

        let nuevoComentario = {
            usuario: sesion.nombre,
            texto: comentarioTexto.value
        };

        comentarios.push(nuevoComentario);
        localStorage.setItem("comentariosFeria", JSON.stringify(comentarios));

        comentarioTexto.value = "";
        cargarComentarios();
    });
}

cargarComentarios();