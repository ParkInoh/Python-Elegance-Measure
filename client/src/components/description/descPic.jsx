import React from 'react';
import './descPic.css'
const DescPic = () => {
  return (
    <ul className='desc'>
      <li className='first_img'>
        <img src="file.png" alt="file"/>
      </li>
      <li>
        <img src="submit.png" alt="file"/>
      </li>
      <li>
        <img src="processing.png" alt="file"/>
      </li>
      <li>
        <img src="scatter.png" alt="file"/>
      </li>
    </ul>
  )
};

export default DescPic;