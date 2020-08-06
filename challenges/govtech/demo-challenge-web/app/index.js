const express = require('express')
const path = require('path');
const app = express()
const port = 3000
const { expressCspHeader, SELF} = require('express-csp-header');

dataStore = {
  "max": "S1332603G",
  "chris": "S5729338A",
  "tim": "S7993655C",
  "peter": "S6572061B"
};

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(expressCspHeader({
  directives: {
      'default-src': [SELF]
  }
}));

app.use(express.static(__dirname + '/public'));
app.get('/',function(req,res){
    var query = req.query.q;
    res.render('index', {query:query});
  });

app.get('/query',function(req,res){
  if(req.query.hasOwnProperty("name") && req.query.name.length > 0) {
    if(dataStore.hasOwnProperty(req.query.name.toLowerCase())) {
      res.send(req.query.name.toLowerCase() + ":" + dataStore[req.query.name.toLowerCase()]);
    } else {
      res.send(req.query.name.toLowerCase() + " not found!");
    }
  } else {
    res.send("Invalid request! Query parameter(name) not found!");
  }
  
});

app.listen(port, () => console.log(`Vulnerable application listening at http://localhost:${port}`))