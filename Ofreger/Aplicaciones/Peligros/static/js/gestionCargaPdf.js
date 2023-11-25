

let sinpadValues = [];

// Función para cargar los valores de sinpad desde el servidor
async function loadSinpadValues() {
    try {
        const response = await fetch("/listasinpad/");
        const data = await response.json();
        sinpadValues = data.sinpad;
    } catch (error) {
        console.error("Error al cargar valores de sinpad:", error);
    }
}

// Función para verificar si el sinpad ya existe
function sinpadExists(sinpad) {
    return sinpadValues.includes(sinpad);
}

// Evento de envío del formulario
formularioPeligro.addEventListener("submit", function (e) {
    let sinpad = parseInt(txtsinpad.value);

    if (sinpad < 10) {
        notificacionSwal(document.title, "El número de SINPAD debe ser mayor a 10", "warning", "Ok");
        e.preventDefault();
        return;
    }

    if (sinpadExists(sinpad)) {
        notificacionSwal(document.title, "El número de SINPAD ya existe, buscarlo en la tabla", "warning", "Ok");
        e.preventDefault();
        return;
    }
});

// Cargar los valores de sinpad cuando se carga la página
window.addEventListener("load", async () => {
    await loadSinpadValues();
});
