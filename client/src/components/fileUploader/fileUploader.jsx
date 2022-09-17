import React, { useState } from 'react';
import axios from 'axios';
import {toast} from 'react-toastify'
import './fileUploader.css';
function FileUploader() {
  const [files, setFiles] = useState([]);
  const [fileInputText, setFileInputText] = useState("form-control noShow");
  const onInputChange = (e) => {
    console.log(e.target.files);
    setFiles(e.target.files);
    setFileInputText("form-control");
  }
  const onSubmit = (e) => {
    e.preventDefault();
    const data = new FormData();
    for(let i = 0; i < files.length; i++){
      data.append('file', files[i]);
    }
    data.append('file', files);
    axios.post('//localhost:5000/upload', data)
    .then((e)=>{
      toast.success('Upload Success');
    })
    .catch((e)=>{
      toast.error('Upload Error');
    })
  }
  return (
    <form method="post" action="#" id="#" onSubmit={onSubmit}> 
      <div className="form-group files">
        <input
          type="file"
          onChange={onInputChange}
          className={fileInputText}
          multiple/>
      </div>
      <button className="snip1535">Code submit</button>
    </form>
  )
}

export default FileUploader