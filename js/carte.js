




var map =L.map('map').setView([48.11,-1.67] , 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19,attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
document.getElementById('form_carte').addEventListener('submit', get_elt_carte);


async function get_elt_carte(event) {
    event.preventDefault();
    let annee = document.getElementById('annee_select').value;
    let departement = document.getElementById('departement_select').value;
    //console.log(annee,departement);
    /*


    REQUETE A FAIRE 

    const response = await fetch('php/request.php/tweets/', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: 'login=' + login + '&text=' + value});
    */
    /*if (!response.ok)
        displayErrors(response.status);
    else
     {
       affiche_recherche(mois_annee,nb_panneaux,surface,puissance,loc); 
  }*/
    affiche_ping(43.51,1.51)

    
}

function affiche_ping(lat,long){
    map.setView([lat,long] , 10);
    var marker = L.marker([lat, long]).addTo(map);
    marker.bindPopup("<b>Hello world!</b><br>I am a popup.");
}