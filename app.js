const express = require('express');
const http = require('http');
const bodyParser = require('body-parser');
const path = require('path');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit'); 

const body = 'public/index.html';

const app = express();

const server = http.createServer(app);
server.listen(80);

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

app.post('/', function(req, res){
    let sex = req.body.sex;
    let age = req.body.age;
    let mood = req.body.mood;

    function generateParam(sex, age, mood){
        return{
            sex,
            age,
            mood,
        }
    }

    const predParam = generateParam(sex, age, mood);
    JSON.stringify(predParam);
});