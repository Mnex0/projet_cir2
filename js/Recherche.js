'use strict'

document.getElementById('form_recherche').addEventListener('submit', get_form);
document.getElementById("res").style.display = "none";

async function select_recherche() {
    const response = await fetch("php/request.php/selectRecherche");
    if (!response.ok)
        displayErrors(response.status);
    else {
        let res = await response.json();
        for (let i = 0; i < res.length; i++) {
            document.getElementById("marque_ondu_select").innerHTML += "<option id='m_ondu" + i + "' value='" + res[i]['marque_ondu'] + "'>" + res[i]['marque_ondu'] + "</option>";
            document.getElementById("marque_pan_select").innerHTML += "<option id='m_pan" + i + "' value='" + res[i]['marque_pan'] + "'>" + res[i]['marque_pan'] + "</option>";
            document.getElementById("departement_select").innerHTML += "<option id='dep" + i + "' value='" + res[i]['numero'] + "'>" + res[i]['numero'] + " - " + res[i]['nom_departement'] + "</option>";
        }
    }
}

async function get_form_no_ondu(event) {
    
}

async function get_form_no_pan(event) {
    
}

async function get_form_no_dep(event) {
    
}

async function get_form_all(event) {
    // Récupère les valeurs des selects et 
    event.preventDefault();
    let marque_onduleur = document.getElementById('marque_ondu_select').value;
    let marque_panneaux = document.getElementById('marque_pan_select').value;
    let departement = document.getElementById('departement_select').value;
    const response = await fetch("php/request.php/recherche?mondu=" + marque_onduleur + "&mpan=" + marque_panneaux + "&dep=" + departement + "")

    let res = await response.json();
    if (res.length == 0 || !response.ok) {
        document.getElementById("res").style.display = "none";
        document.getElementById("no_res").innerHTML = '<h3>Pas de résultats correspondant</h3>';
        return false;
    }
    else {
        document.getElementById("res").style.display = "block";
        document.getElementById("no_res").innerHTML = '';
        document.getElementById("res_recherche").innerHTML = '';
        for (let i = 0; i < res.length; i++) {
            let mois_annee = res[i]['mois'] + '/' + res[i]['annee'];
            let nb_panneau = res[i]['nb_panneau'];
            let surface = res[i]['surface'];
            let puissance = res[i]['puissance'];
            let loc = res[i]['localite'];
            document.getElementById("res_recherche").innerHTML += `
            <div class='row row-cols-6'>
                <div class='col' id='mois_annee'>${mois_annee}</div>
                <div class='col' id='nb_panneaux'>${nb_panneau}</div>
                <div class='col' id='surface'>${surface}</div>
                <div class='col' id='puissance_crete'>${puissance}</div>
                <div class='col' id='localisation'>${loc}</div>
                <div class='col' id='details'>
                    <a href='Details.html' >Détails id ${res[i]['id']}</a>
                </div>
            </div>`
        }
    }
}

select_recherche();