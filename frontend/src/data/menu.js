import About from "../templates/Content/Main/About/About";
import Contacts from "../templates/Content/Main/Contacts/Contacts";
import Projects from "../templates/Content/Main/Projects/Projects";
import {PATH_MAIN_CONTENT} from "./settings";
import {LANGUAGES_URL, MENU_DATA_URL} from "./api_config"
import {hasDataLanguage} from "../services/languageService";

export const menu = {
  projects: {
    // title: "My projects",
    path: PATH_MAIN_CONTENT,
    component: Projects
  },
  about: {
    // title: "About",
    path: PATH_MAIN_CONTENT + "/about",
    component: About
  },
  contacts: {
    // title: "Contacts",
    path: PATH_MAIN_CONTENT + "/contacts",
    component: Contacts
  }
}


export const getMenu = async (language) => {
  const res = await fetch(MENU_DATA_URL + `/${language}`, {
    method: 'GET'
  })
  const json = await res.json()
  if (hasDataLanguage(json) || language === "en"){
    menu.projects.title = json.projects
    menu.about.title = json.about
    menu.contacts.title = json.contacts
    return [menu.projects, menu.about, menu.contacts]
  } else {
    return await getMenu("en")
  }
}

export const getMenuWithoutTitle = () => {
  return [menu.projects, menu.about, menu.contacts]
}

export const getLanguages = async () => {
  const res = await fetch(LANGUAGES_URL)
  const json = await res.json()
  return json
}
