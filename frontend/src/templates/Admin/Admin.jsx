import React, {useEffect} from "react";

//It works, but i need to write token every time + i don't know can fastapi set_cookies on this page or no

import {ADMIN_URL} from "../../data/admin";
import {getJWTToken} from "../../data/api_config";


export default function Admin() {

  useEffect(() => {
    const DBfetch = async () => {
      const res = await fetch(ADMIN_URL, {
        headers: {
          'Content-Type': 'text/html',
          Authorization: getJWTToken(),
        },
        credentials: 'include'  // add cookies in request
      })
      const text = await res.text()
      const head = text.slice(text.indexOf('<head>') + 6, text.indexOf('</head>'))
      const body = text.slice(text.indexOf('<body>') + 6, text.indexOf('</body>'))
      document.head.innerHTML = head
      document.body.innerHTML = body
    }
    DBfetch()
  })

  return (<div/>)
}
