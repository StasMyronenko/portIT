export const BASE_URL = "http://192.168.1.34:8000"

export const LOGIN_URL = BASE_URL + '/auth/login'

export const REGISTER_URL = BASE_URL + '/auth/register'

export const BASE_SITE_DATA_URL = BASE_URL + "/site_app"
export const MENU_DATA_URL = BASE_SITE_DATA_URL + '/menu'
export const AUTH_DATA_URL = BASE_SITE_DATA_URL + '/auth'
export const LANGUAGES_URL = BASE_SITE_DATA_URL + '/languages'
export const HEADER_DATA_URL = BASE_SITE_DATA_URL + '/header'

export const getJWTToken = () => {
  if (document.cookie.includes('jwt_token')) {
    const res = document.cookie.slice(document.cookie.lastIndexOf("jwt_token=") + "jwt_token=".length,
      (document.cookie.indexOf(';', document.cookie.lastIndexOf("jwt_token=") + "jwt_token=".length) > -1) ?
        document.cookie.indexOf(';', document.cookie.lastIndexOf("jwt_token=") + "jwt_token=".length) : undefined
    )
    return res
  }
  return undefined
}
