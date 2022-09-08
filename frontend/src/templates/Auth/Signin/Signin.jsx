import React from "react";
import style from './Signin.module.scss'
import generalStyle from '../../../General.module.css'
import {REGISTER_URL} from '../../../data/api_config'

// TODO. LOGIC

export default function Signin() {
  const register_user = async (e) => {
    e.preventDefault();
    const res = await fetch(REGISTER_URL, {
      method: 'POST',
      headers: {
        'Content-Type': "application/json"
      },
      body: JSON.stringify({
        login: e.target.login.value,
        name: e.target.name.value,
        password: e.target.password.value,
        repeat_password: e.target.repeat_password.value
      })
    })
    console.log({
        login: e.target.login.value,
        name: e.target.name.value,
        password: e.target.password.value,
        repeat_password: e.target.repeat_password.value
      })
    const json = await res.json()
    console.log(json)
  }
  return (
    <div className={generalStyle.content}>
      <div className={style.content}>
        <div className={style.signinDiv}>
          <div className={generalStyle.titleDiv}>
          <h2 className={generalStyle.title}>Register</h2>
        </div>
          <form className={style.signinForm} onSubmit={register_user}>
            <input type="email" name={'login'} id={'login'} placeholder={'Email'}/>
            <input type="text" name={'name'} id={'name'} placeholder={'Name'}/>
            <input type="password" name={'password'} id={'password'} placeholder={'Password'}/>
            <input type="password" name={'repeat_password'} id={'repeat_password'} placeholder={'Repeat Password'}/>
            <input type="submit" value={'Register'} id={style.submit}/>
          </form>
        </div>
      </div>
    </div>
  )
}
