import React from 'react';
import logo from './logo.svg';
import './App.css';
import Upload from './components/Upload';
import Login from './components/Login';
import Feed from './components/Feed';
import Search from './components/Search';

function App() {
  return (
    <div className="App">
      <Upload />
      <Login />
      <Feed />
      <Search />
    </div>
  );
}

export default App;
