'use strict'

document.getElementById('form_recherche').addEventListener('submit', call_form);
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

function call_form(event) {
    event.preventDefault();
    let marque_onduleur = document.getElementById('marque_ondu_select').value;
    let marque_panneaux = document.getElementById('marque_pan_select').value;
    let departement = document.getElementById('departement_select').value;
    if (marque_onduleur == "--Marque de l'onduleur--" && marque_panneaux == "--Marque des panneaux--" && departement == "--Département--") {
        get_form_none();
    }
    else if (marque_panneaux == "--Marque des panneaux--" && departement == "--Département--") {
        get_form_no_pan_dep(marque_onduleur);
    }
    else if (marque_onduleur == "--Marque de l'onduleur--" && departement == "--Département--") {
        get_form_no_ondu_dep(marque_panneaux);
    }
    else if (marque_onduleur == "--Marque de l'onduleur--" && marque_panneaux == "--Marque des panneaux--") {
        get_form_no_ondu_pan(departement);
    }
    else if (marque_onduleur == "--Marque de l'onduleur--") {
        get_form_no_ondu(marque_panneaux, departement);
    }
    else if (marque_panneaux == "--Marque des panneaux--") {
        get_form_no_pan(marque_onduleur, departement);
    }
    else if (departement == "--Département--") {
        get_form_no_dep(marque_onduleur, marque_panneaux);
    }
    else {
        get_form_all(marque_onduleur, marque_panneaux, departement);
    }
}

async function get_form_all(marque_onduleur, marque_panneaux, departement) {
    // Récupère les valeurs des selects et 
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
                    <a href='Details.html?id=${res[i]['id']}' >Détails id ${res[i]['id']}</a>
                </div>
            </div>`
        }
    }
}

async function get_form_none() {
    let a;
}

async function get_form_no_pan_dep(marque_ondu) {
    let a;
}

async function get_form_no_ondu_dep(marque_pan) {
    let a;
}

async function get_form_no_ondu_pan(departement) {
    let a;
}

async function get_form_no_ondu(marque_pan, departement) {
    let a;
}

async function get_form_no_pan(marque_ondu, departement) {
    let a;
}

async function get_form_no_dep(marque_ondu, marque_pan) {
    let a;
}

select_recherche();