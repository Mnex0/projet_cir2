

async function chart1() {
    /* Demande et affiche un graphique avec le  nombre d’installations par années  */
    const response = await fetch("php/request.php/chart1");
      if (!response.ok)
    displayErrors(response.status);
  else
    {
        res=await response.json();
        const ctx1 = document.getElementById('myChart1');
        new Chart(ctx1, {
        type: 'bar',
        data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],//a changer
        datasets: [{
        label: 'Nombre d’installations',
        data: [12, 19, 3, 5, 2, 3],//a changer
        borderWidth: 1
        }]
        },
       options: {
        scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
        
    }
}


async function stat1() {

    /* Demande et affiche nombre d’enregistrement en base  */
    
    document.getElementById('stat1').innerHTML+= 26432;
    
    
    /*const response = await fetch("php/request.php/stat1");
      if (!response.ok)
    displayErrors(response.status);
  else{
    document.getElementById('stat1').innerHTML+=stat1;
}*/
}

async function stat2() {
    
    /* Demande et affiche Nombre d’installateurs   */
    
    document.getElementById('stat2').innerHTML+= 4736;
    
    
    /*const response = await fetch("php/request.php/stat2");
      if (!response.ok)
    displayErrors(response.status);
  else{
    document.getElementById('stat2').innerHTML+=stat2;
}*/
}

async function stat3() {

    /* Demande et affiche Nombre de marques d’onduleurs  */
    
    document.getElementById('stat3').innerHTML+= 864;


    /*const response = await fetch("php/request.php/stat3");
      if (!response.ok)
    displayErrors(response.status);
  else{
    document.getElementById('stat1').innerHTML+=stat3;
}*/
}

async function stat4() {
    
    /* Demande et affiche Nombre de marques de panneaux solaires   */
    
    document.getElementById('stat4').innerHTML+= 875;


    /*const response = await fetch("php/request.php/stat4");
      if (!response.ok)
    displayErrors(response.status);
  else{
    document.getElementById('stat1').innerHTML+=stat4;
}*/
}






function displayErrors(errorCode)
{
  let messages = {
    400: 'Requête incorrecte',
    401: 'Authentifiez-vous',
    403: 'Accès refusé',
    404: 'Page non trouvée',
    500: 'Erreur interne du serveur',
    503: 'Service indisponible'
  };

  // Display error.
  if (errorCode in messages)
  {
    document.getElementById('errors').innerHTML = '<i class="fa-solid ' +
      'fa-circle-exclamation"></i> <strong>' + messages[errorCode] +
      '</strong>';
    document.getElementById('errors').style.display = 'block';
  }
}


const ctx1 = document.getElementById('myChart1');
  new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'Nombre d’installations',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

 const ctx2 = document.getElementById('myChart2');

    new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'Nombre d’installations',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });


  stat1();
  stat2();
  stat3();
  stat4();

