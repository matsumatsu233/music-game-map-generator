import React from 'react';
import {render} from 'react-dom';
import App from './App.jsx'
import About from './About.jsx'
import MapReader from './MapReader.jsx'
import { Router, Route, hashHistory } from 'react-router'

class MainRouter extends React.Component {
  render() {
    return (
      <Router history={hashHistory}>
        <Route path="/" component={App}/>
        <Route path="/about" component={About}/>
        <Route path="/mapreader" component={MapReader}/>
      </Router>
    )
  }
}

render(<MainRouter/>, document.getElementById('app'));