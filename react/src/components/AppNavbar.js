import 'bootstrap/dist/css/bootstrap.css';
import React, { useState } from 'react';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap';
const axios = require('axios')

const AppNavbar = (props) => {
  const [collapsed, setCollapsed] = useState(true);
  const [ontology, setOntology] = useState(true)
  const toggleNavbar = () => setCollapsed(!collapsed);

  axios.get("http://0.0.0.0:5000/api/ontology")
  .then(resp => {
      console.log(resp.data.res)
      setOntology(resp.data.res)
      
  })
  .catch(error => {
      console.log(error);
  })

  return (
    <div>
      <Navbar color="faded" light>
        <NavbarBrand href="/" className="mr-auto" id="font">umwelt</NavbarBrand>
        <NavbarToggler style={{border : "none"}} onClick={toggleNavbar} className="mr-2" />
        <Collapse isOpen={!collapsed} navbar>
          <Nav navbar>
            <NavItem>
              <NavLink href="/upload">upload</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href={`https://ipfs.io/ipfs/${ontology}`}>ontology</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="https://github.com/hicetnunc2000/umwelt">github</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default AppNavbar;
