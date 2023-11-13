/*
const $formularioCurso = document.getElementById("formularioCurso");
const $txtNombre = document.getElementById("txtNombre");
const $numsinpad = document.getElementById("numsinpad");
*/

const btnsEliminacion = document.querySelectorAll(".btnEliminacion");

(function () {
    //notificacionSwal(document.title, "Cursos listados con éxito", "success", "Ok");
    formularioPeligro.addEventListener("submit", function (e) {
        let sinpad = parseInt(txtsinpad.value);
            if (sinpad < 10) {
                notificacionSwal(document.title, "El numero de sinpad debe ser mayor a 10", "warning", "Ok");
                e.preventDefault();
            }
    });

    /*
    btnsEliminacion.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            let confirmacion = confirm("¿Confirma la eliminación del curso?");
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    */

    btnsEliminacion.forEach((btn) => {
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
})();