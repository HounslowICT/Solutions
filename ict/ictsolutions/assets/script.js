
const form_boton = document.querySelector(".btn-form");
const form = document.querySelector('.fact-form');
// const option_boton = document.querySelector('.btn-categories');

//const option_action = document.querySelectorAll(".action-button");

form_boton.addEventListener('click', function() {
    if (form.classList.contains('hidden')) {
        form.classList.remove('hidden');
        form_boton.textContent = "Close";
    }else {
        form.classList.add('hidden');
        form_boton.textContent = "Share a Solution";
    }
})


function handleButtonOptionClick(buttonText) {
    console.log("Button Clicked: "+buttonText);
}

document.querySelectorAll('.action-button').forEach(button => {
    button.addEventListener('click', function(){
        handleButtonOptionClick(this.textContent);
    })
})

// option_boton.MTHLButtonElement.onclick('click', function navigateTo(parameter) { 
//     window.location.href = parameter; 
// })

function navigateTo(urls){
    const url = `http://127.0.0.1:8000/filtered_solutions/${encodeURIComponent(urls)}/`;
    window.location.href = url;
}