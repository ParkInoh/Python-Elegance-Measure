import React, { useState } from 'react';
import axios from 'axios';
import {toast} from 'react-toastify'
import './selectOptions.css';
const SelectOptions = () => {
  const [option1, setOption1] = useState("loops");
  const [option2, setOption2] = useState("loops");
  const good = () => {
    console.log(option1);
    console.log(option2);
  }
  const onSubmit = (e) => {
    axios.get('//localhost:5000/runPy')
    .then((e)=>{
      toast.success('Upload Success', e);
    })
  }
  return (
    <>
    <form className="options">
      <p className='options_cmd'>Select 2 options</p>
      <hr/>
      <select onChange={e => setOption1(e.target.value)}>
        <option value="loops">Loops</option>
        <option value="loops_for">Loops for</option>
        <option value="loops_while">Loops while</option>
        <option value="functions">Functions</option>
        <option value="functions_recursion">Functions recursion</option>
        <option value="max_depth">Max depth</option>
        <option value="avg_depth">Average depth</option>
        <option value="sum_depth">Sum depth</option>
      </select>
      <select onChange={e => setOption2(e.target.value)}>
      <option value="loops">Loops</option>
        <option value="loops_for">Loops for</option>
        <option value="loops_while">Loops while</option>
        <option value="functions">Functions</option>
        <option value="functions_recursion">Functions recursion</option>
        <option value="max_depth">Max depth</option>
        <option value="avg_depth">Average depth</option>
        <option value="sum_depth">Sum depth</option>
      </select>
      <hr/><br/> 
      <button onClick={onSubmit} className="snip">Check Elegance</button>
    </form>
    <button onClick={good}>good</button>
    </>
  )
};

export default SelectOptions;
