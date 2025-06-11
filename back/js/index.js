




function affiche_recherche(mois_annee,nb_panneaux,surface,puissance,loc){
    /* affiche les paramètres dans la page html*/
    document.getElementById("res_recherche").innerHTML+="<div class='row row-cols-6'> <div class='col' id='mois_annee'>"+mois_annee+"</div><div class='col' id='nb_panneaux'>"+nb_panneaux+"</div><div class='col' id='surface'>"+surface+"</div><div class='col' id='puissance_crete'>"+puissance+"</div><div class='col' id='location'>"+loc+"</div><div class='col' id='details'><a href='Details.html' >Clique ici pour avoir les détails</a></div></div>"
}