document.getElementById('modification').addEventListener('click', modification_valeur);

async function modification_valeur(event) {

    let value = event.target.closest('.mod').getAttribute('value');


    const response = await fetch('php/request.php/modifier/' + value, {
      method: 'PUT',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: 'login=' + login + '&text=' + prompt('Nouveau tweet :')});
    if (!response.ok)
      displayErrors(response.status);
    else
      requestTweets();
  }