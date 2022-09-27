import React from 'react'
import Description from '../description/description';
import FileUploader from '../fileUploader/fileUploader';
import NavBar from '../navbar/navbar';
import {ToastContainer} from 'react-toastify';
import Footer from '../footer/footer';
import styles from './home.module.css';
function Home() {
  return (
    <section className={styles.body}>
      <NavBar/>
      <div className={styles.container}>
        <Description/>
        <FileUploader/>
        <ToastContainer/>
      </div>
      <Footer/>
    </section>)
}

export default Home