(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de que quiere eliminar?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();

aceptar = document.getElementById("aceptar");

data = document.getElementById("data");

campos = document.getElementsByClassName("formulario");
form = document.getElementById("form");

for (item of campos)
    {
        elimina_campo(item);
    }
if(data.name=="tabla"){
    current =  document.getElementsByClassName(data.value);
    for(item of current){
        item.style.display='block';
    } 
    }
    
hidden= document.getElementById("hidden");
hidden.style.display='none';

guardar= document.getElementById("guardar");
guardar.style.display='none';

listado= document.getElementById("listado");
listado.style.display='none';

editar = document.getElementById("editar");
aceptar.addEventListener("click",function(){
            actualizar(data);
})
function actualizar(data){
    hidden.value=data.value;
    for (item of campos)
       { console.log(item.id);
        elimina_campo(item);
    }
    current =  document.getElementsByClassName(data.value);
    for(item of current){
       agrega_campo(item);
    }
    guardar.style.display='block';
    listado.style.display='block';
}
function elimina_campo(campo){
    campo.removeAttribute("required");
    campo.style.display='none';
}
function agrega_campo(campo){
    campo.setAttribute("required",true);
    campo.style.display='block';
}
listado.addEventListener("click",function(){
    tabla.value=data.value;
})
