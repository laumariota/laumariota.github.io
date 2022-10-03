function validaCampos(){
    var formulario;
    formulario=document.formuser;
    //valida el campo de usuario
    if (formulario.user.value==""){
        //valida si el campo esta vacio
        document.getElementById("validauser").innerHTML="por favor escribir el usuario" 
        //se posiciona en el campo user
        formulario.user.focus();
        return false;
        
    }else{
        document.getElementById("validauser").innerHTML="";
    }

    //valida el campo email
    if (formulario.email.value==""){
        //valida si el campo esta vacio
        document.getElementById("validaemail").innerHTML="por favor escribir el email" 
        //se posiciona en el campo email
        formulario.email.focus();
        return false;

    }else{
    document.getElementById("validaemail").innerHTML="";
    }

    //valida el campo de password
    if (formulario.password.value==""){
     //valida si el campo esta vacio
     document.getElementById("validapassword").innerHTML="por favor escribir su password" 
     //se pocisiona en el campo password
     formulario.password.focus();
     return false;
    
    }else{
        document.getElementById("validapassword").innerHTML="";
    }

    //valida el campo de passwordC
    if (formulario.passwordC.value==""){
     //valida si el campo esta vacio
     document.getElementById("validapasswordC").innerHTML="por favor confirme su password" 
     //se pocisiona en el campo passwordC
     formulario.passwordC.focus();
     return false;
        
    }else{
        document.getElementById("validapasswordC").innerHTML="";
    }

    formulario.submit();

}