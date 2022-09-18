import React, { useState } from 'react'
import Footer from '../footer/footer';
import NavBar from '../navbar/navbar'
import styles from './elegance.module.css';
import ScatterChart from '../scatterChart';
import {MyData} from '../../data2';
function Elegance() {
  const [myData, setMyData] = useState({
    labels: MyData.map((data) => data.x),
    datasets:[{
      label: "Elegancy",
      data: MyData.map((data) => data.y),
      backgroundColor: ["red"],
      borderColor: "black",
      borderWidth: 1,
    }],
  })
  const MyId = MyData.map((data) => data);
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
          padding: 10,
          // 범례 간 가로 간격을 조정할 수 있습니다. 범례의 상하 padding을 지정하는 기능은 따로 지원되지 않아요. ㅠㅠ
          font: { // 범례의 폰트 스타일도 지정할 수 있습니다.
            family: "'Noto Sans KR', 'serif'",
            lineHeight: 1,
          },
        }
      },
      tooltip: {
        backgroundColor: 'rgba(124, 35, 35, 0.4)',
      // 툴팁 색상을 지정할 수 있습니다.
      padding: 10,
      // 툴팁 패딩을 지정할 수 있습니다.
      bodySpacing: 5,
      filter: (item) => item.parsed.id !== null,
        callbacks: {
          beforeTitle: function(con){
            // console.log(MyData.length);
            // console.log(this);
            console.log(con);
            // for(let i = 0; i < MyData.length; i++){
            //   if(MyData[i].x === con[i].parsed.x && MyData[i].y === con[i].parsed.y){
            //     return MyData[i].id;
            //   }
            // }
          }
        }
      }
    },
    scales: {
      x: {
        display: true,
        title: {
          display: true,
          text: '지표1',
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
          text: '지표2',
          color: '#191',
          font: {
            family: 'Times',
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
    <section className={styles.body}>
      <NavBar/>
      <div className={styles.container}>
      <h1>우아함</h1>
      <div style={{margin:100} }>표위치</div>
      <div style={{width: 700}}>
        <ScatterChart chartData={myData} options={options}/>
      </div>
      </div>
      <Footer/>

    </section>

  )
}

export default Elegance