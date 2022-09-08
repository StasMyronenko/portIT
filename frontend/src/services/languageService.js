const includesLanguage = () => {
  return document.cookie.includes("language")
}

export const hasDataLanguage = (data) => {
  return !(JSON.stringify(data) === JSON.stringify({}))
}

export const setUpLanguage = () =>
{
  if (!includesLanguage()) {
    document.cookie = "language=en"
  }
}

export const getLanguage = () => {
  if (includesLanguage) {
    const res = document.cookie.slice(document.cookie.lastIndexOf("language") + "language=".length,
      (document.cookie.indexOf(";", document.cookie.lastIndexOf("language")) > -1) ? document.cookie.indexOf(";", document.cookie.lastIndexOf("language")) : undefined)
    return res
  } else {
    return  "en"
  }
}
