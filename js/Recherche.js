'use strict'

document.getElementById('form_recherche').addEventListener('submit', get_form);
document.getElementById("res").style.display = "none";

async function select_recherche() {
    const response = await fetch("php/request.php/selectRecherche");
    if (!response.ok)
       displayErrors(response.status);
    else{
        let res = await response.json();
        for (let i = 0; i < res.length; i++) {
           document.getElementById("marque_ondu_select").innerHTML+= "<option value='"+i+"'>"+res[i]['marque_ondu']+"</option>";
           document.getElementById("marque_pan_select").innerHTML+= "<option value='"+i+"'>"+res[i]['marque_pan']+"</option>";
           document.getElementById("departement_select").innerHTML+= "<option value='"+i+"'>"+res[i]['numero']+" - "+res[i]['nom_departement']+"</option>";
           
        }
}
}

async function get_form(event) {
    /*    */
    event.preventDefault();
    document.getElementById("res").style.display = "block";
    let marque_onduleur = document.getElementById('marque_onduleur').value;
    let marque_panneaux = document.getElementById('marque_panneaux').value;
    let departement = document.getElementById('departement').value;
    document.getElementById('marque_onduleur').value = '';
    document.getElementById('marque_panneaux').value = '';
    document.getElementById('departement').value = '';
    
    /*


    const response = await fetch('php/request.php/tweets/')
    */
    if (!response.ok)
        displayErrors(response.status);
    else
     {
       res=await response.json();
    for (let index = 0; index < res.length; index++) {
        affiche_recherche(mois_annee,nb_panneaux,surface,puissance,loc);
        
    } 
  }
    
}

function affiche_recherche(mois_annee,nb_panneaux,surface,puissance,loc){
    /* affiche les paramètres dans la page html*/
    document.getElementById("res_recherche").innerHTML+="<div class='row row-cols-6'> <div class='col' id='mois_annee'>"+mois_annee+"</div><div class='col' id='nb_panneaux'>"+nb_panneaux+"</div><div class='col' id='surface'>"+surface+"</div><div class='col' id='puissance_crete'>"+puissance+"</div><div class='col' id='location'>"+loc+"</div><div class='col' id='details'><a href='Details.html' >Clique ici pour avoir les détails</a></div></div>"
}

select_recherche();