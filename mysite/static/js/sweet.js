$(document).ready(function () {
  $("#click").click(function(event) {
    event.preventDefault();
 
    Swal.fire(
      '¡Muy bien!',
      '¡Usted ha sido registrado!',
      'success'
    );
  });
});


  $('#borrar').click(function(event) {
    event.preventDefault();
     var postId = this.getAttribute('data-post-id')
      Swal.fire({
        title: '¿Estás seguro?',
        text: 'Esta acción no se puede deshacer',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.replace('/Post/' + postId + '/borrar');
        }
      });
    });




