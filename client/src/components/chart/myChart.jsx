import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router';
import { useSelector } from 'react-redux';
import './myChart.css';
import SelectOptions from '../selectOptions/selectOptions';
import { Scatter } from 'react-chartjs-2';
import {Chart} from 'chart.js/auto'
import styled from 'styled-components';
let chartList = [];
const chartLabel = "Elegance(The lower the better except score)";
const init = (eOptions, fileList, elegantData) => {
  chartList = [];
  for(let i = 0; i < fileList.length; i++){
    let tmp = {}
    tmp['x'] = elegantData[fileList[i]][eOptions[0]];
    tmp['y'] = elegantData[fileList[i]][eOptions[1]];
    tmp['file'] = fileList[i];
    chartList.push(tmp);
  }
}

const MyChart = () => {
  const eOptions = useSelector(state => state.options.options);
  const location = useLocation().state.data;
  const elegantData = JSON.parse(location.data);
  const fileList = Object.keys(elegantData);
  useEffect(() => {
    init(eOptions, fileList, elegantData);
    setMyData({
      datasets:[{
        label: chartLabel,
        data: chartList,
        backgroundColor: ["red"],
        borderColor: "black",
        borderWidth: 1,
      }],
    })
  }, [eOptions]);
  const [myData, setMyData] = useState(
    {
      datasets:[{
        label: chartLabel,
        data: chartList,
        backgroundColor: ["red"],
        borderColor: "black",
        borderWidth: 1,
      }],
    }
  )
  const options = {
    spanGaps: true,
    interaction: {
      mode: 'index',
    },
    plugins: {
      legend: { // 범례 스타일링
        labels: {
          usePointStyle: true,
          // 범례 도형 모양과 관련된 속성으로, false일 경우엔 기본 직사각형 도형으로 표시됩니다.
          padding: 15,
          // 범례 간 가로 간격을 조정할 수 있습니다. 범례의 상하 padding을 지정하는 기능은 따로 지원되지 않아요. ㅠㅠ
          font: { // 범례의 폰트 스타일도 지정할 수 있습니다.
            family: "sans-serif",
            lineHeight: 1,
          },
        }
      },
      tooltip: {
        backgroundColor: 'rgba(124, 35, 35, 0.5)',
        padding: 10,
        bodySpacing: 5,
        callbacks: {
          label: (ct) => {
            return `${ct.raw.file}:(${ct.raw.x}, ${ct.raw.y})`
          }
        },
      }
    },
    scales: {
      x: {
        display: true,
        title: {
          display: true,
          text: "x: "+eOptions[0],
          color: 'black',
          font: {
            family: 'sans serif',
            size: 20,
            weight: 'bold',
            lineHeight: 1.2,
          },
          padding: {top: 20, left: 0, right: 0, bottom: 0}
        }
      },
      y: {
        display: true,
        title: {
          display: true,
          text: "y: " + eOptions[1],
          color: 'black',
          font: {
            family: 'sans serif',
            size: 20,
            style: 'normal',
            weight: 'bold',
            lineHeight: 1.2
          },
          padding: {top: 30, left: 0, right: 0, bottom: 0}
        }
      }
    },
  }
  return (
    <Container>
      <Scatter data={myData} options={options}/>
      <SelectOptions
        where="elegant"/>
    </Container>
  )
};

export default MyChart;

const Container = styled.div`
  width: 100vw;
  max-width: 99%;
`