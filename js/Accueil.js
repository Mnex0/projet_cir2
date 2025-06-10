'use strict'

async function chart1() {

  /* Demande et affiche un graphique avec le  nombre d’installations par années  */

  const response = await fetch("php/request.php/chart1");

  if (!response.ok)
    displayErrors(response.status);
  else {
    res = await response.json();
  }

  const label=[];
  const valeur=[];

  for (let index = 0; index < res.length; index++) {
    label.push(res[index]['count']);
    valeur.push(res[index]['num_annee']);
  }

  const ctx1 = document.getElementById('myChart1');
  
  new Chart(ctx1, {
      type: 'bar',
      data: {
        labels: label,//
        datasets: [{
          label: "Nombre d'installations",
          data: valeur, //
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

async function chart2() {

  /* Demande et affiche un graphique avec le  nombre d’installation par région  */
  
  const response = await fetch("php/request.php/chart2");
  
  if (!response.ok)
    displayErrors(response.status);
  else {
    res = await response.json();
  }
    
  const label=[];
  const valeur=[];
  for (let index = 0; index < res.length; index++) {
    label.push(res[index]['count']);
    valeur.push(res[index]['nom_region']);
    }
    
    const ctx2 = document.getElementById('myChart2');
    
    new Chart(ctx2, {
      type: 'bar',
      data: {
        labels: label,//
        datasets: [{
          label: 'Nombre d’installations',
          data: valeur,//
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

async function statEnr() {

  /* Demande et affiche nombre d’enregistrement en base  */

  const response = await fetch("php/request.php/statEnr");
  if (!response.ok)
    displayErrors(response.status);
  else{
    const res=await response.json();
    document.getElementById('stat1').innerHTML+=res[0]['COUNT(*)'];
  }
}

async function stat2() {

  /* Demande et affiche Nombre d’installateurs   */

  const response = await fetch("php/request.php/stat2");
  if (!response.ok)
    displayErrors(response.status);
  else{
    const res=await response.json();
    document.getElementById('stat2').innerHTML+=res[0]['COUNT(*)'];
  }
}

async function stat3() {

  /* Demande et affiche Nombre de marques d’onduleurs  */


  const response = await fetch("php/request.php/stat3");
  if (!response.ok)
    displayErrors(response.status);
  else{
    const res=await response.json();
    document.getElementById('stat3').innerHTML+=res[0]['COUNT(*)'];
  }
}

async function stat4() {

  /*  Demande et affiche Nombre de marques de panneaux solaires   */

  const response = await fetch("php/request.php/stat4");
  if (!response.ok)
    displayErrors(response.status);
  else{
    const res=await response.json();
    document.getElementById('stat4').innerHTML+=res[0]['COUNT(*)'];
  }
}






function displayErrors(errorCode) {
  let messages = {
    400: 'Requête incorrecte',
    401: 'Authentifiez-vous',
    403: 'Accès refusé',
    404: 'Page non trouvée',
    500: 'Erreur interne du serveur',
    503: 'Service indisponible'
  };

  // Display error.
  if (errorCode in messages) {
    document.getElementById('errors').innerHTML = '<i class="fa-solid ' +
      'fa-circle-exclamation"></i> <strong>' + messages[errorCode] +
      '</strong>';
    document.getElementById('errors').style.display = 'block';
  }
}




statEnr();
stat2();
stat3();
stat4();
chart1();
chart2();

