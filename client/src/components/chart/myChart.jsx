import React, { useEffect, useState } from 'react'
import ScatterChart from '../scatterChart';
import { useLocation } from 'react-router';
import { useSelector } from 'react-redux';
import './myChart.css';
import SelectOptions from '../selectOptions/selectOptions';
import { Scatter } from 'react-chartjs-2';
let chartList = [];

const init = (eOptions, fileList, elegantData) => {
  chartList.splice(0, fileList.length);
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
  const fileList = location.fileList;
  const elegantData = JSON.parse(location.data);

  useEffect(() => {
    init(eOptions, fileList, elegantData)
  }, [eOptions]);
  
  console.log(chartList);
  const [myData, setMyData] = useState({
    datasets:[{
      label: "Elegance",
      data: chartList,
      backgroundColor: ["red"],
      borderColor: "black",
      borderWidth: 1,
    }],
  })

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
            family: "'Noto Sans KR', 'serif'",
            lineHeight: 1,
          },
        }
      },
      tooltip: {
        backgroundColor: 'rgba(124, 35, 35, 0.5)',
      // 툴팁 색상을 지정할 수 있습니다.
        padding: 10,
      // 툴팁 패딩을 지정할 수 있습니다.
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
          color: '#911',
          font: {
            family: 'Comic Sans MS',
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
          color: '#191',
          font: {
            family: 'Comic Sans MS',
            size: 20,
            style: 'normal',
            lineHeight: 1.2
          },
          padding: {top: 30, left: 0, right: 0, bottom: 0}
        }
      }
    },
  }
  return (
    <div style={{width: 800}}>
      <Scatter data={myData} options={options}/>
      <SelectOptions where="elegant" myData={myData} setMyData={setMyData}/>
    </div>
  )
};

export default MyChart;