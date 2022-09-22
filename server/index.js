const express = require("express");
const multer = require("multer");
const cors = require("cors");
const file = require('fs');
const {PythonShell} = require('python-shell');
const app = express();

require("dotenv").config();
app.use(cors());
app.use(express.json());

const server = app.listen(process.env.PORT, ()=>{
  console.log(`Server Started on Port ${process.env.PORT}`)
});

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'public');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
  }
})

const upload = multer({storage}).array('file');

app.post('/upload', (req, res) => {
  upload(req, res, (err) => {
    if(err){
      return res.status(500).json(err)
    }
    return res.status(200).send(req.file);
  })
})

app.get('/runPy', (req, res) => {
  const fn = file.readdirSync('public');
  console.log(fn);
  //PythonShell.run("")
})