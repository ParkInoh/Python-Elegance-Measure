const express = require("express");
const multer = require("multer");
const cors = require("cors");
const fs = require('fs');
const {PythonShell} = require('python-shell');
const app = express();
const path = require("path");

require("dotenv").config();
app.use(cors());
app.use(express.json());

app.listen(process.env.PORT, ()=>{
  console.log(`Server Started on Port ${process.env.PORT}`);
});

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'public');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
})

const upload = multer({storage}).array('file');

app.post('/upload', (req, res) => {
  try{
    fs.unlinkSync('./output.json');
  } catch(err) {
    if(err.code === 'ENOENT'){
      console.log('No such file');
    }
  } finally{
    fs.rmSync('./public', {recursive:true});
    fs.mkdirSync('./public');
    upload(req, res, (err) => {
      if(err){
        return res.status(500).json(err)
      }
      return res.status(200).send(req.file);
    })
    PythonShell.run("main.py", null, (err) => {
      if(err) return err;
      console.log("finished");
    })
  }
})

app.post('/runPy', (req, res) => {
  // PythonShell.run("main.py", null, (err) => {
  //   if(err) return err;
  //   console.log("finished");
  //   fs.readFile('output.json', 'utf-8', (err, data) => {
  //     if(err) return console.log(err);
  //     res.send({data});
  //   })
  // })
  fs.readFile('output.json', 'utf-8', (err, data) => {
    if(err) return console.log(err);
    res.send({data});
  })
})

app.post('/download', (req, res) => {
  res.download('./output.json');
})