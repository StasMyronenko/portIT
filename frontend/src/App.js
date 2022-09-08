import style from './App.scss';

import Menu from "./templates/Menu/Menu";
import React, {useEffect, useState} from "react";
import {Outlet} from "react-router-dom";
import Footer from "./templates/Footer/Footer";
import {getMenu} from "./data/menu";
import {getLanguage} from "./services/languageService";


function App() {
  const [menu, setMenu] = useState([])
  const [currentLanguage, setCurrentLanguage] = useState('')
  useEffect( () => {
    const getMenuData = async () =>  {
      const data = await getMenu(getLanguage())
      setMenu(data)
    }
    getMenuData()
  }, [currentLanguage]) // make button and turn on it here
  return (
    <div className={style.App}>
      <Menu menu={menu} currentLanguage={currentLanguage} setCurrentLanguage={setCurrentLanguage}/>
      <Outlet context={currentLanguage}/>
      <Footer menu={menu}/>
    </div>

  );
}

export default App;
