import React from 'react'
import Footer from '../footer/footer';
import NavBar from '../navbar/navbar'
import styles from './elegance.module.css';
import { ToastContainer } from 'react-toastify';
import Table from '../table/table';
import MyChart from '../chart/myChart';
function Elegance() {
  return (
    <section className={styles.body}>
      <NavBar/>
      <Table/>
      <div className={styles.container}>
        <MyChart/>
      </div>
      <ToastContainer/>
      <Footer/>
    </section>
  )
}

export default Elegance