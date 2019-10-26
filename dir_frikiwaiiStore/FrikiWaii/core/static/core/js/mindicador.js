$(document).ready(function(){
    
    $.get("https://mindicador.cl/api", function(respuesta){    

        var dolar =  respuesta.dolar.valor;

        var valordolar1 = ""+11990/dolar;
        var valordolar2 = ""+9990/dolar;
        var valordolar3 = ""+5990/dolar;
        var valordolar4 = ""+5990/dolar;
        var valordolar5 = ""+6990/dolar;
        var valordolar6 = ""+990/dolar;

        var valordolar11 = "Precio $ "+valordolar1.substring(0 ,valordolar1.indexOf("."),0)+" USD";
        var valordolar22 = "Precio $ "+valordolar2.substring(0 ,valordolar2.indexOf("."),0)+" USD";
        var valordolar33 = "Precio $ "+valordolar3.substring(0 ,valordolar3.indexOf("."),0)+" USD";
        var valordolar44 = "Precio $ "+valordolar4.substring(0 ,valordolar4.indexOf("."),0)+" USD";
        var valordolar55 = "Precio $ "+valordolar5.substring(0 ,valordolar5.indexOf("."),0)+" USD";
        var valordolar66 = "Precio $ "+valordolar6.substring(0 ,valordolar6.indexOf("."),0)+" USD";

        $("#valorDolar1").html(valordolar11);
        $("#ValorDolar2").html(valordolar22);
        $("#ValorDolar3").html(valordolar33);
        $("#ValorDolar4").html(valordolar44);
        $("#ValorDolar5").html(valordolar55);
        $("#ValorDolar6").html(valordolar66);

    });
});