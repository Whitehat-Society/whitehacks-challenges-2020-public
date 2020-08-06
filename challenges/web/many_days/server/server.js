'use strict';

const express = require('express');
let path = require('path');
let bodyParser = require('body-parser');
let yaml = require('js-yaml');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

app.use(express.static('static'))

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/static/index.html'));
});


app.post('/yaml_to_json', (req, res) => {
  if (req.body && req.body.yaml){
    res.end(JSON.stringify(yaml.load(req.body.yaml), null, 2));
  }
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);