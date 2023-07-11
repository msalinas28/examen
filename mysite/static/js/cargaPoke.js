$('#submit-form').click(function(event) {
    event.preventDefault();
    var POKEMON = $("#pokemon").val();

    // Convertir a minúsculas y eliminar espacios en blanco
    pokemon = POKEMON.trim().toLowerCase();
    pokemon = pokemon.replace(/\s/g, '-');

    if (pokemon === '') {
        // Si el campo de entrada está vacío, buscar un Pokémon al azar
        var randomPokemonId = Math.floor(Math.random() * 898);
        pokemon = randomPokemonId.toString();
    }

    $.ajax({
        url: 'https://pokeapi.co/api/v2/pokemon/'+pokemon,
        data: {
            format: 'json'
        },
        error: function() {
            $('#info').html('<p>Un error ha ocurrido!!!!</p>');
        },

        dataType: 'json',
        success: function(data) {
            console.log(data);
            var $nombre_pokemon = $('<h1 class="card-title" id="nombrePokemon"></h1>').text(data.name)
            var $foto_pokemon = $("<img id='imgPokemon'src='"+data.sprites.front_default+"'>")
            var $id_pokemon = $('<h2 class="card-subtitle" id="idPokemon"></h2>').text(data.id)
            var $tipo1_pokemon =$('<span>').text(data.types[0].type.name)
            var $altura_pokemon= $('<span>').text((data.height)*10)
            var $peso_pokemon=$('<span>').text((data.weight)/10);
            // este if es para los pokemos de solo u tipo, si no esta el api manda error
            if (data.types.length > 1) {
                var $tipo2_pokemon =$('<span>').text(data.types[1].type.name);
               }

             //esto limpia cada carta
             $("#nombrePokemon").empty()
             $("#imgPokemon").empty()
             $("#idPokemon").empty()
             $("#tipoPokemon").empty()
             $("#alturaPokemon").empty()
             $("#pesoPokemon").empty()

             
            // muestra la data en la caja info card 
            $('#nombrePokemon')
                .append($nombre_pokemon)
                .append($id_pokemon);
            $('#imgPokemon')
                .append($foto_pokemon);
            $('#tipoPokemon')
                .append($tipo1_pokemon)
            $('#alturaPokemon')
                .append($altura_pokemon)
                .append("cm")
            $('#pesoPokemon')
                .append($peso_pokemon)
                .append("kg")
               // este if es para los pokemos de solo u tipo, si no esta el api manda error
             if (data.types.length > 1) {
             $('#tipoPokemon')
             .append(" ")
             .append($tipo2_pokemon);
            }
                

        },
        type: 'GET'
    });
});