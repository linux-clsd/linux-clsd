var modelo = new brain.NeutralNetwork();

document.getElementById("botonEntrenamiento").addEventListener("click",function(){
    modelo.train(generarListaEntrenamiento());
    document.getElementById("entrenamientoListo").style.display = "block";
    document.getElementById("preguntar").style.display = "block";
});
function generarListaEntrenamiento(){
    var lista = [];

    lista[0] = {input:[255/255,255/255,255/255],output:{claro:1}};

    lista[1] = {input:[0,0,0],output:{oscuro:1}};

    lista[2] = {input:[192/255,192/255,192/255],output:{claro:1}};

    lista[3] = {input:[64/255,64/255,64/255],output:{oscuro:1}};

    lista[4] = {input:[153/255,128/255,128/255],output:{oscuro:1}};
    console.log(JSON.stringify(lista));
    return lista;
}
document.getElementById("botonResultado").addEventListener("click",function(){
    var entrada = document.getElementById("colorSeleccionado").value;
    const r= parseInt(entrada.substr(1,2),16);
    const g= parseInt(entrada.substr(3,2),16);
    const b= parseInt(entrada.substr(5,2),16);
    var salida = modelo.run([r/255,g/255,b/255]);
    console.log(JSON.stringify(salida));
    var resultado = esOscuro(salida.oscuro);
    document.getElementById("resultadoFinal").innerHTML = "Este color es " + resultado;
});

function esOscuro(salida){
    if(salida> 0.5){
        return "oscuro";
    }else{
        return "claro";
    }
}