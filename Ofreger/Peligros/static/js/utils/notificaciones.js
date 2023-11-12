// const $formulario = document.getElementById('formularioCurso');
// const $txtNombre = document.getElementById('txtNombre');
const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

(function () {
    notificacionSwal(document.title, 'CArga de Fichas de peligos', 'success', 'ok')
    formularioCurso.addEventListener('submit', (event) => {        
        let nombre = String(txtNombre.value).trim();
        if (nombre.length===0){
            notificacionSwal(document.title, 'Por favor, ingrese un nombre', 'error', 'ok')
            txtNombre.focus();
            event.preventDefault();
        }
        let creditos = parseInt(numCreditos.value);
        if (creditos<1 || creditos>10){
            notificacionSwal(document.title, 'Por favor, ingrese un credito entre 1 y 10', 'error', 'ok')
            numCreditos.focus();
            event.preventDefault();
        }
       

        // const creditos = document.getElementById('numCreditos').value;
    });

    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', (event) => {
            // if (!confirm('¿Desea eliminar el registro?')) {
            //     
            // }
            event.preventDefault();
            Swal.fire({
                title: 'Desea eliminar el reigistro?',
                showCancelButton: true,
                confirmButtonText: 'Si',
                cancelButtonText: 'No',
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm:() => {
                    location.href = event.target.href;
                },
                allowoutsideclick: () => false,
                allowScapeKey: () => false,
            })
        })
    })

})();
