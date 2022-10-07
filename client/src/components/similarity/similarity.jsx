import React from 'react'
import NavBar from '../navbar/navbar'
import styles from './similarity.module.css';
function Similarity() {
  return (
    <>
    <NavBar/>
    <h1>유사도</h1>
    <div className={styles.table}>표위치</div>
    <div className={styles.code}>
      <div className={styles.code1}>
        코드1
      </div>
      <div>
        코드2
      </div>
    </div>
    </>
  )
}
export default Similarity