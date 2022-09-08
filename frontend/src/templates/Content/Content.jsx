import React from "react";
import Header from "./Header/Header";
import Main from "./Main/Main";
import style from "./Content.module.scss"

export default function Content() {
  return (
    <div className={style.content}>
      <Header />
      <Main />
    </div>
  )
}
