/*
const $formularioCurso = document.getElementById("formularioCurso");
const $txtNombre = document.getElementById("txtNombre");
const $numsinpad = document.getElementById("numsinpad");
*/


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




})();