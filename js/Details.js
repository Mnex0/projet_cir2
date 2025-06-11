'use strict'

async function get_details() {
    let id = (location.href).split("=")[1]; // Permet d'obtenir l'id stocké dans l'URL actuelle
    console.log(id);
    const response = await fetch('php/request.php/details?id='+id);
    if (!response.ok) {
        displayErrors(response.status);
        return false;
    }
    let res = await response.json();
    res = res[0];
    console.log(res);
    // Informations de base
    document.getElementById('id').innerHTML = res['id'];
    document.getElementById('mois_installation').innerHTML = res['mois_installation'];
    document.getElementById('annee_installation').innerHTML = res['an_installation'];
    
    // Informations sur les panneaux
    document.getElementById('nb_panneaux').innerHTML = res['nb_panneau'];
    document.getElementById('marque_panneaux').innerHTML = res['marque_pan'];
    document.getElementById('modele_panneaux').innerHTML = res['modele_pan'];
    
    // Informations sur les onduleurs
    document.getElementById('nb_onduleur').innerHTML = res['nb_onduleur'];
    document.getElementById('marque_ondu').innerHTML = res['marque'];
    document.getElementById('modele_ondu').innerHTML = res['modele_onduleur'];
    
    // Caractéristiques techniques
    document.getElementById('puissance_crete').innerHTML = res['puissance_crete'];
    document.getElementById('surface').innerHTML = res['surface'];
    document.getElementById('pente').innerHTML = res['pente'];
    document.getElementById('pente_optimum').innerHTML = res['pente_optimum'];
    document.getElementById('orientation').innerHTML = res['orientation'];
    document.getElementById('orientation_optimum').innerHTML = res['orientation_optimum'];
    
    // Informations sur l'installateur et la production
    document.getElementById('installateur').innerHTML = res['installatur'];
    document.getElementById('production_pvgis').innerHTML = res['production_pvgis'];
    
    // Coordonnées géographiques
    document.getElementById('lat').innerHTML = res['lat'];
    document.getElementById('lon').innerHTML = res['lon'];
    
    // Informations de localisation
    document.getElementById('code_INSEE').innerHTML = res['code_INSEE'];
    document.getElementById('localite').innerHTML = res['localite'];
    document.getElementById('num_dep').innerHTML = res['numero'];
    document.getElementById('departement').innerHTML = res['nom_departement'];
    document.getElementById('region').innerHTML = res['nom_region'];
}

get_details();