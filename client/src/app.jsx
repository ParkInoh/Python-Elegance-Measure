import './app.css';
import 'react-toastify/dist/ReactToastify.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './components/home/home';
import Similarity from './components/similarity/similarity';
import Elegance from './components/elegance/elegance';
function App() {
  return (
    <div className='app'>
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<Home/>}/>
        <Route path="/similar" element={<Similarity/>}/>
        <Route path="/elegant" element={<Elegance/>}/>
      </Routes>
    </BrowserRouter> 
    </div> 
  )

}

export default App;
