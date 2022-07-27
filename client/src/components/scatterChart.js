import React from 'react';
import {Scatter} from 'react-chartjs-2';
import {Chart} from 'chart.js/auto'
const ScatterChart = ({chartData, options}) => {
  return (
    <Scatter data={chartData} options={options}/>
  )
};

export default ScatterChart;