$(function(){
    $("#Formulario").validate({
        rules : {
            txtNombre : {
                required : true,
                lettersonly : true
            },
            txtApellido : {
                required : true,
                lettersonly : true
            },
            txtCorreo : {
                required : true,
                email : true
            },
            txtPassword1 : {
                required : true
            },
            txtPassword2 : {
                required : true,
                equalTo : "#pw1"
            }
        },
        messages : {
            txtNombre : {
                required : "¡¡Campo Obligatorio!!",
                lettersonly : "¡¡Ingrese Un Nombre Real Sin Numeros!!"
            },
            txtApellido : {
                required : "¡¡Campo Obligatorio!!",
                lettersonly : "¡¡Ingrese Un Apellido Real Sin Numeros!!"
            },
            txtCorreo : {
                required : "¡¡Campo Obligatorio!!",
                email : "¡¡Ingrese Un Email Valido!!"
            },
            txtPassword1 : {
                required : "¡¡Campo Obligatorio!!"
            },
            txtPassword2 : {
                required : "¡¡Campo Obligatorio!!",
                equalTo : "¡¡Las Contraseñas Deben Ser Iguales!!"
            }
        }
    });
});