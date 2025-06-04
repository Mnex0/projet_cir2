

document.getElementById('form_recherche').addEventListener('submit', get_form);



async function get_form(event) {
    /* Faire la requette pour appeler la fonction affiche_recherche avec les bon parametres   */
    event.preventDefault();
    let marque_onduleur = document.getElementById('marque_onduleur').value;
    let marque_panneaux = document.getElementById('marque_panneaux').value;
    let departement = document.getElementById('departement').value;
    document.getElementById('marque_onduleur').value = '';
    document.getElementById('marque_panneaux').value = '';
    document.getElementById('departement').value = '';
    
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
    
}


function affiche_recherche(mois_annee,nb_panneaux,surface,puissance,loc){
    /* affiche les paramètres dans la page html*/
    document.getElementById('mois_annee').innerHTML=mois_annee;
    document.getElementById('nb_panneaux').innerHTML=nb_panneaux;
    document.getElementById('surface').innerHTML=surface;
    document.getElementById('puissance_crete').innerHTML=puissance;
    document.getElementById('location').innerHTML=loc;    


}