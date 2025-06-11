document.getElementById('saisie').addEventListener('click', ajout_valeur);


async function ajout_valeur(event) {
    event.preventDefault();
    let Nombre_panneaux = document.getElementById('Nombre_panneaux').value;
    



    
    const response = await fetch('php/request.php/tweets/', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: 'login=' + login + '&text=' + value});
    if (!response.ok)
        displayErrors(response.status);
    else
    {

        }
    }