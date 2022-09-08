import {HEADER_DATA_URL} from "./api_config";
import {hasDataLanguage} from "../services/languageService";

export const firstBlock = "It's my site portfolio where I post my projects"
export const secondBlock = "This site also my project..."


export const getHeader = async (language) => {
  const res = await fetch(HEADER_DATA_URL + `/${language}`)
  const json = await res.json()
  if (hasDataLanguage(json) || language === "en") {
  }
  return json
}
