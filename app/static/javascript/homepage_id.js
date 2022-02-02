function replace (hide, show) {
  document.getElementById(hide).style.display='none';
  document.getElementById(show).style.display='block';
  // document.getElementById('cardform').classList.remove('norefresh')
}

async function formHandler(event) {
  event.preventDefault();

  let name = document.querySelector('input[name="name"]').value
  let breed_id = document.querySelector('button[name="id"]').value

  const response = await fetch(`/api/breeds`, {
    method: 'POST',
    body: JSON.stringify({
      breed_id,
      name
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    replace(hide, show)
    
  } else {
    alert(response.statusText);
  }
}


async function id1formHandler(event) {
  event.preventDefault();
  let name = document.querySelector('input[name="name"]').value
  let breed_id = document.querySelector('button[name="id"]').value
  const response = await fetch(`/api/breeds`, {
    method: 'POST',
    body: JSON.stringify({
      breed_id,
      name
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    replace(hide, show)
  } else {
    alert(response.statusText);
  }
}


// async function id2formHandler(event) {
//   event.preventDefault();

//   let name = document.querySelector('input[name="name"]').value
//   let breed_id = document.querySelector('button[name="id"]').value

//   const response = await fetch(`/api/breeds`, {
//     method: 'POST',
//     body: JSON.stringify({
//       breed_id,
//       name
//     }),
//     headers: {
//       'Content-Type': 'application/json'
//     }
//   });
//   if (response.ok) {
//     replace(hide, show)
    
//   } else {
//     alert(response.statusText);
//   }
// }
// async function id3formHandler(event) {
//   event.preventDefault();

//   let name = document.querySelector('input[name="name"]').value
//   let breed_id = document.querySelector('button[name="id"]').value

//   const response = await fetch(`/api/breeds`, {
//     method: 'POST',
//     body: JSON.stringify({
//       breed_id,
//       name
//     }),
//     headers: {
//       'Content-Type': 'application/json'
//     }
//   });
//   if (response.ok) {
//     replace(hide, show)
    
//   } else {
//     alert(response.statusText);
//   }
// }
// async function id4formHandler(event) {
//   event.preventDefault();

//   let name = document.querySelector('input[name="name"]').value
//   let breed_id = document.querySelector('button[name="id"]').value

//   const response = await fetch(`/api/breeds`, {
//     method: 'POST',
//     body: JSON.stringify({
//       breed_id,
//       name
//     }),
//     headers: {
//       'Content-Type': 'application/json'
//     }
//   });
//   if (response.ok) {
//     replace(hide, show)
    
//   } else {
//     alert(response.statusText);
//   }
// }
// async function id5formHandler(event) {
//   event.preventDefault();

//   let name = document.querySelector('input[name="name"]').value
//   let breed_id = document.querySelector('button[name="id"]').value

//   const response = await fetch(`/api/breeds`, {
//     method: 'POST',
//     body: JSON.stringify({
//       breed_id,
//       name
//     }),
//     headers: {
//       'Content-Type': 'application/json'
//     }
//   });
//   if (response.ok) {
//     replace(hide, show)
    
//   } else {
//     alert(response.statusText);
//   }
// }




document.querySelector('.norefresh').addEventListener('submit', formHandler)
document.querySelector('.id1').addEventListener('submit', id1formHandler)
// document.querySelector('.id2').addEventListener('submit', id2formHandler)
// document.querySelector('.id3').addEventListener('submit', id3formHandler)
// document.querySelector('.id4').addEventListener('submit', id4formHandler)
// document.querySelector('.id5').addEventListener('submit', id5formHandler)

