'use strict'

/* affiche la carte  */
var map = L.map('map').setView([47.01, 1.87], 6);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' }).addTo(map);

document.getElementById('form_carte').addEventListener('submit', get_elt_carte);

async function select_carte() {
    const response = await fetch("php/request.php/selectCarte");
    if (!response.ok)
        displayErrors(response.status);
    else {
        let res = await response.json();
        for (let i = 0; i < res[0].length; i++) {
            document.getElementById("annee_select").innerHTML += "<option id='" + i + "' value='" + res[0][i]['num_annee'] + "'>" + res[0][i]['num_annee'] + "</option>";
        }
        for (let j = 0; j < res[1].length; j++) {
            document.getElementById("departement_select").innerHTML += "<option id='" + j + "' value='" + res[1][j]['numero'] + "'>" + res[1][j]['numero'] + " - " + res[1][j]['nom_departement'] + "</option>";//Le 0 est a changé par le numero du departement
        }
    }
}

async function get_elt_carte(event) {
    /* Recupère l'annee et le dep qui sont dans le select et appèle l'affichage des pings répondant aux arguments passés */
    event.preventDefault();
    let annee = document.getElementById('annee_select').value;
    let departement = document.getElementById('departement_select').value;
    const response = await fetch("php/request.php/carte?annee=" + annee + "&dep=" + departement + "");

    if (!response.ok) {
        displayErrors(response.status);
        return false;
    }
    let res = await response.json();
    for (let i = 0; i < res.length; i++) {
        affiche_ping(res[i]['id'], res[i]['lat'], res[i]['lon'], res[i]['puissance'], res[i]['localite'])
    }
}

async function affiche_ping(id, lat, lon, puissance, localite) {
    /* affiche un marqueur a une lat et lon donnée */
    map.setView([lat, lon], 10);
    var marker = L.marker([lat, lon]).addTo(map);
    marker.bindPopup("<p>Localité : " + localite + "</p><p>Puissance : " + puissance + `</p><a href='Details.html?id=${id}'>Détails de l'installation</a>`);//A modifier
}

select_carte();