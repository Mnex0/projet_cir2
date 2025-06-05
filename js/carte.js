



/* affiche la carte  */
var map =L.map('map').setView([48.11,-1.67] , 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19,attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);


document.getElementById('form_carte').addEventListener('submit', get_elt_carte);


async function get_elt_carte(event) {
    /* Recupere l'annee et le dep qui sont dans le select  */
    event.preventDefault();
    let annee = document.getElementById('annee_select').value;
    let departement = document.getElementById('departement_select').value;
    console.log(annee,departement);


    /*const response = await fetch('php/request.php/carte');
    
    if (!response.ok)
        displayErrors(response.status);
    else
     {
        $res=await response.json();
       affiche_ping(lat,long);
  }*/
    affiche_ping(43.51,1.51);

    
}

function affiche_ping(lat,long){
    /* affiche un marqueur a une lat et long donnée */
    map.setView([lat,long] , 10);
    var marker = L.marker([lat, long]).addTo(map);
    marker.bindPopup("<b>Hello world!</b><br>I am a popup.");
}