let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [
    { nombre: "Administrador", correo: "admin@pa.cl", pass: "Admin123!", rol: "admin" }
];

document.getElementById("formLogin")?.addEventListener("submit", e => {
    e.preventDefault();

    let email = loginEmail.value;
    let pass = loginPass.value;

    let u = usuarios.find(x => x.correo === email && x.pass === pass);
    if (!u) return alert("Credenciales incorrectas");

    localStorage.setItem("sesion", JSON.stringify(u));

    // ✅ Redirección correcta en Django
    if (u.rol === "admin") {
        window.location.href = "/admin-panel/";
    } else {
        window.location.href = "/";
    }
});

document.getElementById("formRegistro")?.addEventListener("submit", e => {
    e.preventDefault();

    usuarios.push({
        nombre: nombre.value,
        correo: correo.value,
        pass: pass.value,
        rol: "usuario"
    });

    localStorage.setItem("usuarios", JSON.stringify(usuarios));
    alert("¡Registro exitoso!");

    // ✅ Volver al Home (ruta Django)
    window.location.href = "/";
});

let sesion = JSON.parse(localStorage.getItem("sesion"));
if (sesion && sesion.rol === "admin") {
    document.getElementById("adminLink")?.classList.remove("d-none");
}

function logout() {
    localStorage.removeItem("sesion");
    window.location.href = "/";
}
