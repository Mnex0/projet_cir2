'use strict'

/* affiche la carte  */
var map = L.map('map').setView([48.11, -1.67], 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' }).addTo(map);

document.getElementById('form_carte').addEventListener('submit', get_elt_carte);

async function select_carte() {
    const response = await fetch("php/request.php/selectCarte");
    if (!response.ok)
        displayErrors(response.status);
    else {
        res = await response.json();
        for (let index = 0; index < res.length; index++) {
            document.getElementById("annee_select").innerHTML += "<option value='" + index + "'>" + res[index][0] + "</option>";
            document.getElementById("departement_select").innerHTML += "<option value='" + index + "'>" + res[index][1] + "</option>";//Le 0 est a changé par le numero du departement

        }
    }
}

async function get_elt_carte(event) {
    /* Recupere l'annee et le dep qui sont dans le select  */
    event.preventDefault();
    let annee = document.getElementById('annee_select').value;
    let departement = document.getElementById('departement_select').value;
    console.log(annee, departement);


    /*const response = await fetch('php/request.php/carte');
    
    if (!response.ok)
        displayErrors(response.status);
    else
     {
        res=await response.json();
       affiche_ping(lat,long);
  }*/
    affiche_ping(43.51, 1.51);


}

async function affiche_ping(lat, long) {
    /* affiche un marqueur a une lat et long donnée */
    map.setView([lat, long], 10);
    var marker = L.marker([lat, long]).addTo(map);
    res = ["Rennes", 1500,]
    marker.bindPopup("<p>Localité : " + res[0] + "</p><p>Puissance : " + res[1] + "</p><a href='Details.html'>Détails de l'installation</a>");//A modifier

    /*const response = await fetch('php/request.php/ping');
    if (!response.ok)
        displayErrors(response.status);
    else
     {
       res=await response.json();
       marker.bindPopup("<div class='container text-center'><div class='row row-cols-3'><div class='col' id='loc'>"+res[0]+"</div><div class='col' id='puissance'>"+res[1]+"</div><div class='col' id='details'><a href='Details.html' >Clique ici pour avoir les détails</a></div></div></div>");//A modifier
  }*/

}