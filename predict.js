//const fs = require('fs');

function generateParam(inSex, inMood, inAge){
    return{
        'sex':inSex,
        'mood':inMood,
        'age':inAge
    }
}

function getpred(sex, mood, age){
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