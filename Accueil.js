'use strict'

let ctx = document.getElementById('myChart3');

const stackedBar = new Chart(ctx, {
    type: 'bar',
    data: {
    labels: [1,2,3,4,5],//annee
      datasets: [ {
            label: 'Dataset 1',//nom region 
            data: [10],//valeur pour les annees
            backgroundColor: 'rgba(255, 99, 132, 0.7)',
          }, {
            label: 'Dataset 2',
            data: [15, 25, 35, 45, 55],
            backgroundColor: 'rgba(54, 162, 235, 0.7)',
          }, {
            label: 'Dataset 3',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 192, 192, 0.7)',
          },{
            label: 'Dataset 4',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(210, 224, 80, 0.7)',
          },{
            label: 'Dataset 5',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 192, 124, 0.7)',
          },{
            label: 'Dataset 6',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(173, 75, 192, 0.7)',
          },{
            label: 'Dataset 7',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 75, 124, 0.7)',
          },{
            label: 'Dataset 8',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 132, 75, 0.7)',
          },{
            label: 'Dataset 9',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 75, 130, 0.7)',
          },{
            label: 'Dataset 10',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 75, 104, 0.7)',
          },{
            label: 'Dataset 11',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 174, 75, 0.7)',
          },{
            label: 'Dataset 12',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 192, 163, 0.7)',
          },{
            label: 'Dataset 13',
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 87, 192, 0.7)',
          }
      ]},
    options: {
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true
            }
        }
    }
});


async function chart1() {

  /* Demande et affiche un graphique avec le  nombre d'installations par années  */

  const response = await fetch("php/request.php/chart1");
  if (!response.ok) {
    displayErrors(response.status)
    return false;
  }
  const res = await response.json();
  let label = [];
  let valeur = [];

  for (let i = 0; i < res.length; i++) {
    label.push(res[i]['num_annee']);
    valeur.push(res[i]['count']);
  }

  let ctx1 = document.getElementById('myChart1');

  new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: label,
      datasets: [{
        label: "Nombre d'installations",
        data: valeur,
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

  /* Demande et affiche un graphique avec le  nombre d'installation par région  */

  const response = await fetch("php/request.php/chart2");

  if (!response.ok) {
    displayErrors(response.status)
    return false;
  }
  const res = await response.json();
  let label = [];
  let valeur = [];
  for (let i = 0; i < res.length; i++) {
    label.push(res[i]['nom_region']);
    valeur.push(res[i]['count']);
  }

  let ctx2 = document.getElementById('myChart2');

  new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: label,
      datasets: [{
        label: "Nombre d'installations",
        data: valeur,
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

async function chart3() {
  const response = await fetch("php/request.php/chart3");

    if (!response.ok) {
      displayErrors(response.status)
    return false;
    }
    const res = await response.json();
    let annee = [];
    let region =[];
    let valeur = [];
    for (let i = 0; i < res.length; i++) {
      region.push(res[i]['nom_region']);
      valeur.push(res[i]['count']);
      annee.push(res[i]['nom_annee']);
  }



    let ctx = document.getElementById('myChart3');

    const stackedBar = new Chart(ctx, {
    type: 'bar',
    data: {
    labels: annee,
      datasets: [ {
            label: region[0],
            data: [10, 20, 30, 40, 50],
            backgroundColor: 'rgba(255, 99, 132, 0.7)',
          }, {
            label: region[1],
            data: [15, 25, 35, 45, 55],
            backgroundColor: 'rgba(54, 162, 235, 0.7)',
          }, {
            label: region[2],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 192, 192, 0.7)',
          },{
            label: region[3],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(210, 224, 80, 0.7)',
          },{
            label: region[4],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 192, 124, 0.7)',
          },{
            label: region[5],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(173, 75, 192, 0.7)',
          },{
            label: region[6],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 75, 124, 0.7)',
          },{
            label: region[7],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 132, 75, 0.7)',
          },{
            label: region[8],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 75, 130, 0.7)',
          },{
            label: region[9],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 75, 104, 0.7)',
          },{
            label: region[10],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(192, 174, 75, 0.7)',
          },{
            label: region[11],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 192, 163, 0.7)',
          },{
            label: region[12],
            data: [20, 30, 40, 50, 60],
            backgroundColor: 'rgba(75, 87, 192, 0.7)',
          }
      ]},
    options: {
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true
            }
        }
    }
});
}

async function statEnr() {

  /* Demande et affiche nombre d'enregistrement en base  */

  const response = await fetch("php/request.php/statEnr");
  if (!response.ok)
    displayErrors(response.status);
  else {
    const res = await response.json();
    document.getElementById('stat1').innerHTML += res[0]['count'];
  }
}

async function stat2() {

  /* Demande et affiche Nombre d'installateurs   */

  const response = await fetch("php/request.php/stat2");
  if (!response.ok)
    displayErrors(response.status);
  else {
    const res = await response.json();
    document.getElementById('stat2').innerHTML += res[0]['count'];
  }
}

async function stat3() {

  /* Demande et affiche Nombre de marques d'onduleurs  */


  const response = await fetch("php/request.php/stat3");
  if (!response.ok)
    displayErrors(response.status);
  else {
    const res = await response.json();
    document.getElementById('stat3').innerHTML += res[0]['count'];
  }
}

async function stat4() {

  /*  Demande et affiche Nombre de marques de panneaux solaires   */

  const response = await fetch("php/request.php/stat4");
  if (!response.ok)
    displayErrors(response.status);
  else {
    const res = await response.json();
    document.getElementById('stat4').innerHTML += res[0]['count'];
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
function main()
{
  statEnr();
  stat2();
  stat3();
  stat4();
  chart1();
  chart2();
}

main();