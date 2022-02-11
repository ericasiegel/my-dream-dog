async function singleDogFormHandler(event) {
  event.preventDefault();

  const breed_id = document.querySelector('input[id="form-id"]').value;
  const name = document.querySelector('input[id="form-name"]').value;

    const response = await fetch('/api/breeds', {
      method: 'post',
      body: JSON.stringify({
        breed_id,
        name
      }),
      headers: { 'Content-Type': 'application/json' }
    });
    if (response.ok) {
      document.getElementById('not-saved').style.display='none';
      document.getElementById('saved').style.display='block';
    } else {
      alert(response.statusText);
    }
  
}

document.querySelector('.norefresh').addEventListener('submit', singleDogFormHandler);

