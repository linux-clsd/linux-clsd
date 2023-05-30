var modelo = new brain.NeutralNetwork();

document.getElementById("botonEntrenamiento").addEventListener("click",function(){
    modelo.train(generarListaEntrenamiento());
    document.getElementById("entrenamientoListo").style.display = "block";
    document.getElementById("preguntar").style.display = "block";
});
function generarListaEntrenamiento(){
    var lista = [];
    //Blanco (255,255,255)
    lista[0] = {input:[255/255,255/255,255/255],output:{claro:1}};
    //Negro (0,0,0)
}