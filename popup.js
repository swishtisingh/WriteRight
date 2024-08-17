document.addEventListener('DOMContentLoaded', function () {
  const userInput = document.getElementById('myForm');
  const submitButton = document.getElementById('submitButton');
  const resultContainer = document.getElementById('summary');

  submitButton.addEventListener('click', function (e) {
    //const userText = userInput['Input Text'].value;
    // Do something with userText, e.g., alert it
    //alert(`You entered: ${userText}`);
    // Make an asynchronous POST request to the Flask server
    submitButton.disabled = true;
    submitButton.innerHTML = "Summarising..";
    e.preventDefault();
    const formData = new FormData(userInput);

    // Convert FormData to JSON
    const formDataJSON = {};
    formData.forEach((value, key) => {
      formDataJSON[key] = value;
    });

    alert(JSON.stringify(formDataJSON));

    fetch('http://127.0.0.1:5000/Summarise', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formDataJSON)
    })
      .then(response => 
        //alert('hi');
        //console.log(response,response.json());
        response.json()
  )
      .then(data => {
        // Display the returned text in the result container
        console.log(data);
        //alert(data);
        resultContainer.textContent = `${data.summary_text}`;
        submitButton.disabled = false;
        submitButton.innerHTML = "Summarise";
      })
      .catch(error => {
        console.log('Error:', error);
      });

  });
});