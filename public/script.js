document.addEventListener("DOMContentLoaded", function(){
    const submit = document.getElementById("mood-form");

    submit.addEventListener("submit", function(event){
        event.preventDefault();
    });
});