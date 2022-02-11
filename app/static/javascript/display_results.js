async function oneDogFormHandler(event) {
    event.preventDefault();
  
    const breed_id = document.querySelector('input[id="form-id1"]').value;
    const name = document.querySelector('input[id="form-name1"]').value;
  
  
      const response = await fetch('/api/breeds', {
        method: 'post',
        body: JSON.stringify({
          breed_id,
          name
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.getElementById('not-saved1').style.display='none';
        document.getElementById('saved1').style.display='block';
      } else {
        alert(response.statusText);
      }
  }

  async function twoDogFormHandler(event) {
    event.preventDefault();
  
    const breed_id = document.querySelector('input[id="form-id2"]').value;
    const name = document.querySelector('input[id="form-name2"]').value;
  
  
      const response = await fetch('/api/breeds', {
        method: 'post',
        body: JSON.stringify({
          breed_id,
          name
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.getElementById('not-saved2').style.display='none';
        document.getElementById('saved2').style.display='block';
      } else {
        alert(response.statusText);
      }
  }

  async function threeDogFormHandler(event) {
    event.preventDefault();
  
    const breed_id = document.querySelector('input[id="form-id3"]').value;
    const name = document.querySelector('input[id="form-name3"]').value;
  
  
      const response = await fetch('/api/breeds', {
        method: 'post',
        body: JSON.stringify({
          breed_id,
          name
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.getElementById('not-saved3').style.display='none';
        document.getElementById('saved3').style.display='block';
      } else {
        alert(response.statusText);
      }
  }

  async function fourDogFormHandler(event) {
    event.preventDefault();
  
    const breed_id = document.querySelector('input[id="form-id4"]').value;
    const name = document.querySelector('input[id="form-name4"]').value;
  
  
      const response = await fetch('/api/breeds', {
        method: 'post',
        body: JSON.stringify({
          breed_id,
          name
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.getElementById('not-saved4').style.display='none';
        document.getElementById('saved4').style.display='block';
      } else {
        alert(response.statusText);
      }
  }

  async function fiveDogFormHandler(event) {
    event.preventDefault();
  
    const breed_id = document.querySelector('input[id="form-id5"]').value;
    const name = document.querySelector('input[id="form-name5"]').value;
  
  
      const response = await fetch('/api/breeds', {
        method: 'post',
        body: JSON.stringify({
          breed_id,
          name
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.getElementById('not-saved5').style.display='none';
        document.getElementById('saved5').style.display='block';
      } else {
        alert(response.statusText);
      }
  }

  document.querySelector('.norefresh1').addEventListener('submit', oneDogFormHandler);
  document.querySelector('.norefresh2').addEventListener('submit', twoDogFormHandler);
  document.querySelector('.norefresh3').addEventListener('submit', threeDogFormHandler);
  document.querySelector('.norefresh4').addEventListener('submit', fourDogFormHandler);
  document.querySelector('.norefresh5').addEventListener('submit', fiveDogFormHandler);