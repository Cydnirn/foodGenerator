const express = require('express');
const app = express();
const http = require('http');
const bodyParser = require('body-parser');

const server = http.createServer(app);
server.listen(80);

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());
app.use(express.static(__dirname + "/public"));

