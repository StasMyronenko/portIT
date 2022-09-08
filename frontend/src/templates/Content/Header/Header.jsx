import React, {useEffect, useState} from "react";
import style from "./Header.module.scss";
import {getHeader} from "../../../data/header";
import {useOutletContext} from "react-router-dom";

function Header(){
  const currentLanguage = useOutletContext()
  const [data, setData] = useState({})
  useEffect(() => {
    const getData = async () => {
      setData(await getHeader(currentLanguage))
    }
    getData()
  }, [currentLanguage])
  return (
    <header>
      <div className={style.content}>
        <div className={style.backgroundLogoDiv}>
          <p className={style.backgroundLogoText}>
            PORT.IT
          </p>
        </div>
        <div className={style.blocks}>
          <div className={style.firstBlock}>
            <p>{data.firstBlock}</p>
          </div>
          <div className={style.secondBlock}>
            <p>
              {data.secondBlock}
            </p>
          </div>
        </div>

      </div>

    </header>
  )
}

export default Header
