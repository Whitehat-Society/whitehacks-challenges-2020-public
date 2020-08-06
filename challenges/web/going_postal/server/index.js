const express = require('express')
const app = express()
const port = 3000
const fs = require('fs')
const BACKDOOR = '/admin_s3kr1t_backd0Or'

app.use(express.static('public'))

app.get(BACKDOOR, function (req, res, next) {
    res.status(405).send('GET method not supported')
})

app.all(BACKDOOR, function (req, res, next) {
    let flag = fs.readFileSync('flag.txt')
    res.end(flag)
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))