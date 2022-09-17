import React from 'react'
import './description.css'
import ReactImageTooltip from 'react-image-tooltip';
import file from './file.png';
import submit from './submit.png';
function Description() {
  return (
    <div className='desBox'>Description
    <ol>
      <li> 
      <ReactImageTooltip image={file}>
        코드를 첨부합니다(다중 첨부 가능).
      </ReactImageTooltip>
      </li>
      <li>
        <ReactImageTooltip image={submit}>
        우아함 옵션을 선택하고 제출 버튼을 클릭합니다.
        </ReactImageTooltip>
      </li>
      <li>
        만들어진 척도에 따라 코드에 우아함 점수를 매깁니다.
      </li>
      <li>
        점수를 차트와 테이블로 보여줍니다.
      </li>
    </ol>
    </div>
    
  )
}

export default Description