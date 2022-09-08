import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import reportWebVitals from './reportWebVitals';
import {getMenuWithoutTitle} from "./data/menu";
import {getAuthWithoutTitle} from "./data/auth"

import Content from "./templates/Content/Content";
import Admin from "./templates/Admin/Admin";
import {PATH_MAIN_CONTENT} from "./data/settings"
import {setUpLanguage} from "./services/languageService";

setUpLanguage()
const menu = getMenuWithoutTitle()
const auth = getAuthWithoutTitle()

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(

  <React.StrictMode>
    <BrowserRouter>

      <Routes>
        <Route path={"/"} element={<App />}>
          <Route path={PATH_MAIN_CONTENT} element={<Content />} >
            {menu.map((element, key) => {
            return (
                <Route path={element.path} key={key} element={<element.component />} />
            )
          })}
          </Route>

          {auth.map((element, key) => {
            return (
              <Route path={element.path} key={key} element={<element.component />} />
            )
          })}
        </Route>
        <Route path={'/admin'} element={<Admin />}/>

      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
