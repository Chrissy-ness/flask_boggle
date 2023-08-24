$('#submit').on('click', submitBtn);

async function submitBtn(evt) {
    evt.preventDefault();

    const response = await axios.get('/check-answer');
    console.log(response)
    console.log("####", response.data);
    console.log("you clicked the submit btn");
}




