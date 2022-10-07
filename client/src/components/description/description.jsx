import React from 'react'
import './description.css'
function Description() {
  return (
    <div className='desBox'>Description
    <ol>
      <li>
        Python 코드를 첨부합니다(다중 첨부 가능).
      </li>
      <li>
        우아함 옵션을 선택하고 'SUBMIT CODE' 버튼을 클릭합니다.
      </li>
      <li>
        2가지 옵션을 선택하고 'CHECK ELEGANCE' 버튼을 클릭합니다.
      </li>
      <li>
        만들어진 척도에 따라 코드의 우아함 점수를 매깁니다.
      </li>
      <li>
        점수를 차트와 테이블로 보여줍니다.
      </li>
      <div>
      (※ Score는 높을수록 그 외에는 낮은수록 우아한 코드입니다.)
      </div>
    </ol>

    </div>
    
  )
}

export default Description