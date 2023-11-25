let dataTable;
let dataTableIsInitialized = false;


const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [0, 3, 4] },
        { searchable: false, targets: [0, 2] }
    ],
    pageLength: 4,
    destroy: true,
    language: {
        url: "//cdn.datatables.net/plug-ins/1.11.5/i18n/es-ES.json"
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listPeligros();

    dataTable = $("#datatable-peligros").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listPeligros = async () => {
    try {
        const response = await fetch("/generacionTablas/");
        const data = await response.json();

        let content = ``;
        data.peligros.forEach((peligros, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${escapeHtml(peligros.sinpad)}</td>
                    <td>${escapeHtml(peligros.distrito)}</td>
                    <td style="font-size:x-small;" width="40%">${escapeHtml(peligros.descripcion)}</td>
                    <td><a href="../media/${escapeHtml(peligros.url_pdf)}" target="_blank" class="btn btn-sm btn-block btn-info"><i class="fas fa-file-pdf"></i></a></td>
                    <td>
                    <a href="../editarPeligro/${peligros.id}" class="btn btn-sm btn-block btn-info"><i class="fas fa-pencil-alt"></i></a>
                    <a href="../eliminarPeligro/${peligros.id}" class="btn btn-sm btn-block btn-danger btnEliminacion"><i class="far fa-trash-alt"></i></a>
                    </td>
                </tr>`;
        });
        tableBody_peligros.innerHTML = content;

        // Configura los event listeners para los botones después de cargar los datos
        setupDeleteButtons();

    } catch (ex) {
        alert(ex);
    }
};

// Función para escapar HTML y prevenir XSS
function escapeHtml(unsafe) {
    if (unsafe === null || unsafe === undefined) {
        return ""; // o puedes devolver un valor por defecto como "N/A"
    }

    // Convierte el valor a una cadena si no lo es
    const safeString = unsafe.toString();

    return safeString
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}






window.addEventListener("load", async () => {
    await initDataTable();

});

// Configura los event listeners para los botones de eliminación
const setupDeleteButtons = () => {
    document.querySelectorAll(".btnEliminacion").forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            Swal.fire({
                title: "¿Confirma la eliminación del Peligro?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });
};