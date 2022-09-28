import React from 'react';
import { Link } from 'react-router-dom';
import './navbar.css'
function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar_logo">
        <i className="fa-regular fa-copy"></i>
        <Link className="link" to='/'> Python elegance measure</Link>
      </div>
      <ul className="navbar_menu">

      </ul>
    </nav>
  )
}

export default NavBar
