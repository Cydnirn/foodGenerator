const express = require('express');
const http = require('http');
const bodyParser = require('body-parser');
const path = require('path');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit'); 

const body = 'public/index.html';

const app = express();

const server = http.createServer(app);
server.listen(80, function(){
    let datetime = new Date();
    let message = "Server running on port 80, Started at: " +datetime;
    console.log(message); 
});

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());
app.use(express.static(__dirname + "/public"));

//Limiter
const limiter = rateLimit({
    windowMS: 15 * 60 * 1000, //15 min
    max: 100
})

//GET Request
app.get("/", function(req, res){
    res.sendFile(path.join(__dirname, body))
});

//READ
app.use(helmet());
app.use(limiter);

//Import
let predLib = require('./predict');

let getPred = predLib.getpred;

app.post('/getpred', function(req, res){
    let sex = req.body.sex;
    let age = req.body.age;
    let mood = req.body.mood;

    console.log(sex, mood, age);
    predjson = getPred(sex, mood, age);
    console.log(predjson);

    const spawn = require('child_process').spawn;
    const pypred = spawn('python', [__dirname+'/public/magic/predict.py', predjson]);

    pydata = '';

    pypred.stdout.on('data', (stdData) => {
        pydata += stdData.toString();
        console.log(pydata);
    });

    pypred.stderr.on('data', (data) =>{
        console.error('stderr:', data);
    });

    pypred.on('exit', (code) =>{
        console.log("Child process exit with code", code, pydata);

        let resultPred = JSON.parse(pydata);

        let foodPred = resultPred['food'];
        let drinkPred = resultPred['drink'];
        console.log(foodPred, drinkPred);
        res.send(pydata);
    });
});