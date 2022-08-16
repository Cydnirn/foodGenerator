let headers = new Headers();
headers.append("key","value");
const RENDER_EVENT = "render-predict";

function makePred(pred){
    //const foodDesc = JSON.parse(__dirname+'desc/food.json');
    //const drinkDesc = JSON.parse(__dirname+'desc/drink.json');
    
    let food = document.createElement('h2');
    food.innerText = pred.food; 

    let drink = document.createElement('h2');
    drink.innerText = pred.drink;

    /*
    let foodPDesc = document.createElement('p');
    */

    const containerPred = document.createElement("div");
    containerPred.classList.add("pred-cont");
    containerPred.append(food, drink);

    return containerPred;
}

$(document).ready(() => {
    console.log("DOM READY");
    $('form').submit((e) => {
        e.preventDefault();
        let sexData, moodData, ageData;
        sexData = $('#sex').val();
        moodData = $("input[name='mood']:checked").val();
        ageData = $('#age').val();
        
        console.log(sexData, moodData, ageData);
        
        $.ajax({
            url: "/getpred",
            data: {"sex": sexData, "mood": moodData, "age": ageData},
            method: "POST",
            contentType : "application/x-www-form-urlencoded",
            success : (res) =>{
                console.log("Success");
                console.log(res);
                res = JSON.parse(res);
                console.log(res.food);
                console.log(res.drink);

                const contPred = document.getElementById("contPred");
                contPred.innerHTML = "";

                const elementPred = makePred(res);

                contPred.append(elementPred);

                /*
                document.dispatchEvent(new Event(RENDER_EVENT));

                document.addEventListener(RENDER_EVENT, () =>{
                    const contPred = document.getElementById("contPred");
                    contPred.innerHTML = "";

                    const elementPred = makePred(res);

                    contPred.append(elementPred);
                });
                */
            },
            error: (err) =>{
                console.log(err);
            }
        });
        
        /*
        let optPred = {
            method: "POST",
            headers: headers,
            contentType: "application/x-www-form-urlencoded"
        }
        */

        console.log("Submit button pressed");

        /*
        fetch("/getpred")
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log("Data FETCH Success!", data);
        })
        .catch(error => console.log("Error!", error))
        */
    });
});