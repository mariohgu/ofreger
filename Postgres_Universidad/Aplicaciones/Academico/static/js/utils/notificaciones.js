
const notificacionSwal = (titleText, text, icon,confirmButtonText)=> {
    Swal.fire({
        title: titleText,
        text: text,
        icon: icon,     //warnining, error, success,info
        confirmButtonText: confirmButtonText
    })
}