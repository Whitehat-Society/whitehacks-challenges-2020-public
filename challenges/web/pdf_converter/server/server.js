'use strict';

const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const multer = require('multer')
const uuid = require('uuid').v4
const fs = require('fs')
const ocr = require('node-ts-ocr').Ocr
const cookieSession = require('cookie-session')


// Constants
const PORT = 8080;
const HOST = '0.0.0.0';
const OUTPUT_DIR = "output";

// App
const app = express();

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

app.use(cookieSession({
  name: 'session',
  keys: ['🎌💩💩💩💩🎌']
}))

const storage = multer.diskStorage({
  destination: function(req, file, cb) {
      cb(null, 'uploads/');
  },

  // By default, multer removes file extensions so let's add them back
  filename: function(req, file, cb) {
      cb(null, uuid() + '-' + Date.now() + path.extname(file.originalname));
  }
});

async function getPdfText(filePath, options) {
  // Extract the text and return the result
  return await ocr.extractText(filePath, options);
}

app.use(express.static('static'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/static/index.html'));
});


app.post('/pdf_ocr', (req, res) => {
  try {
      var upload = multer({ storage : storage, limits: { fileSize: 1024 * 1024 * 4 } }).single('pdf');
      upload(req, res, function(err) {
        // req.file contains information of uploaded file
        // req.body contains information of text fields, if there were any

        if (!req.file) {
            return res.send('Please select a PDF to upload');
        }
        else if (err instanceof multer.MulterError) {
            return res.send(err);
        }
        else if (err) {
            return res.send(err);
        }
        
        // get options
        let options = req.body;

        // OCR the pdf
        getPdfText(req.file.path, options).then((txt) => {
          // return the text
          return res.send(txt);
        }).catch((e) => {
          return res.send('Something went wrong!');
        }).finally(() => {
          // delete the file
          fs.unlinkSync(req.file.path);
        });
      });
  } catch (e) {
    return res.send('Something went wrong!');
  }
});


app.options('/admin', (req, res) => {
  let body = req.body
  if (body && body.admin && body.admin === 'WhiteHacksAdmin') {
    let flag = fs.readFileSync('flag1.txt').toString('utf8')
    flag = `<h1>${flag}</h1>`
    flag += '<br/> but you are still not a real admin :>'
    res.send(flag)
  } else {
    res.send('<h1 style="color:red;">swiper no swiping!</h1>')
  }
})

app.get('/real_admin', (req, res) => {
  if (req.session && req.session.admin === true) {
    let flag = fs.readFileSync('flag2.txt').toString('utf8')
    flag = `<h1>${flag}</h1>`
    flag += '<br/> but you are still not a real admin :>, the real admin can run shell commands :)'
    res.send(flag)
  } else {
    res.send('<h1 style="color:red;">your cookies taste awful!</h1>')
  }
})

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);