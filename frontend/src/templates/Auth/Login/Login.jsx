import React from "react";
import style from './Login.module.scss'
import generalStyle from '../../../General.module.css'
import {LOGIN_URL} from "../../../data/api_config";

export default function Login() {
  const login_user = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('username', e.target.username.value)
    formData.append('password', e.target.password.value)
    const res = await fetch(LOGIN_URL, {
      method: 'POST',
      body: formData
    })
    const json = await res.json()
    document.cookie = `jwt_token=${json.access_token}`
    alert(JSON.stringify(json))
  }

  return (
    <div className={generalStyle.content}>
      <div className={style.content}>
        <div className={style.loginDiv}>
          <div className={generalStyle.titleDiv}>
          <h2 className={generalStyle.title}>Login</h2>
        </div>
          <form className={style.loginForm} onSubmit={login_user}>
            <input type="email" name={'username'} id={'email'} placeholder={'Email'}/>
            <input type="password" name={'password'} id={'password'} placeholder={'Password'}/>
            <input type="submit" value={'Login'} id={style.submit}/>
          </form>
        </div>
      </div>

    </div>
  )
}
