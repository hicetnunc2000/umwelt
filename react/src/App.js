import React from 'react';
import logo from './logo.svg';
import './App.css';
import Upload from './components/Upload';
import Login from './components/Login';
import Feed from './components/Feed';
import Search from './components/Search';
import AppNavbar from './components/AppNavbar';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Home from './components/Home';
import SearchResults from './components/SearchResults';

function App() {
  return (
    <Router>
      <AppNavbar />
      <Switch>
        <Route path="/upload">
          <Upload />
        </Route>
        <Route path="/search/:search">
          <SearchResults />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
