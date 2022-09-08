import React, {useEffect, useState} from "react";
import style from "./Menu.module.scss"
import {getAuth} from "../../data/auth"
import {Link} from "react-router-dom";
import {PATH_MAIN_CONTENT} from "../../data/settings";
import {getLanguage} from "../../services/languageService";
import {getLanguages} from "../../data/menu";

function Menu(props){
  const {currentLanguage, setCurrentLanguage} = props
  const [languages, setLanguages] = useState([])
  const [auth, setAuth] = useState([])

  const changeLanguage = (e) => {
    document.cookie = `language=${e.target.value}`
    setCurrentLanguage(e.target.value)
  }
  useEffect(() => {
    const configure = async () => {
      // Languages
      setLanguages(await getLanguages())
      setCurrentLanguage(getLanguage())
    }
    configure()
  }, [])
  useEffect(() => {
    const configureAuth = async () => {
      // Languages
      setAuth(await getAuth(getLanguage()))
    }
    configureAuth()
    // auth fields

  }, [currentLanguage])
  const menu = props.menu
  return (
    <div className={style.content}>
      <div className={style.menu}>
        <div className={style.divLogo}>
          <Link className={style.logo} to={PATH_MAIN_CONTENT}>PORT.IT</Link>
        </div>
        <nav className={style.navigation}>
          <ul className={style.navigationList}>
            {menu.map((element, id) => {
              return <li key={id}>
                <Link to={element.path} className={style.navigationElement}>{element.title}</Link>
              </li>
            })}
          </ul>

        </nav>
        <div className={style.auth}>
          <ul className={style.authList}>
            {auth.map((element, id) => {
              return <li key={`auth-key-${id}`}>
                <Link to={element.path} className={style.authElement}>{element.title}</Link>
              </li>
              })
            }
          </ul>
        </div>
        <div className={style.language}>
          <select name="language" id="language" value={currentLanguage} onChange={(e) => changeLanguage(e)}>
            {
                (languages.includes(currentLanguage)) ? <option value={currentLanguage}>{currentLanguage}</option> : undefined
            }

            {languages.map((el, key) => {
              if (el !== currentLanguage){
                return <option value={el} key={key}>{el}</option>
              }
              return undefined
            })}
          </select>
        </div>
      </div>
      </div>

  )
}

export default Menu;
