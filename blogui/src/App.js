import React  from 'react';
import logo from './logo.svg';
import'./App.css';

import {
  BrowserRouter as Router, Route, Link
}

function Article({article}){
  return<div style={{display: "inline-block", width: '50%', verticalAlign:"top", border:"2px solid black"}}>
  <h1>{article.titel}</h1>
     <p>{article.body.substr(0,100).replace(/\s\w*$/)+'...'}</p>
    <a href="#">Read more ... </a>
  </div>
}



function App({articles}){

  return <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to The Blog</h2>
        </div>
     <div>
       <div style={{textAlign : 'left', padding: 10}}>
         {articles.map(article => <Article Key={article.id} article={article}/>)}
       </div>
     </div>
  </div>
}

export default App;
