import Login from "../templates/Auth/Login/Login"
import Signin from "../templates/Auth/Signin/Signin"
import {AUTH_DATA_URL} from "./api_config";

const auth = {
  login: {
    // title: "Log in",
    path: "/login",
    component: Login
  },
  signin: {
    // title: "Sign in",
    path: "/signin",
    component: Signin
  }
}

export const getAuth = async (language) => {
  const res = await fetch(AUTH_DATA_URL + `/${language}`)
  const json = await res.json()
  auth.login.title = json.login
  auth.signin.title = json.signin
  return [auth.login, auth.signin]
}

export const getAuthWithoutTitle = () => {
  return [auth.login, auth.signin]
}
