import React from "react";
import style from "./Footer.module.scss";
import {Link} from "react-router-dom";

export default function Footer(props) {
  const menu = props.menu
  return (
    <footer >
      <nav className={style.navigation}>
          <ul className={style.navigationList}>
            {menu.map((element, id) => {
              return <li key={id}>
                <Link to={element.path} key={id} className={style.navigationElement}>{element.title}</Link>
              </li>
            })}
          </ul>
        </nav>
    </footer>
  )
}
