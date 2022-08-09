//const fs = require('fs');

function generateParam(sex, mood, age){
    return{
        'sex':sex,
        'mood':mood,
        'age':age
    }
}

async function getpred(sex, mood, age){
    let param = generateParam(sex, mood, age);
    param = JSON.stringify(param);

    return param;
    /*
    fs.writeFileSync('./pred.json', json, (err) => {
        if(!err){
            console.log('JSON file created');
        }
    }); */
}

module.exports = {
    getpred,
}