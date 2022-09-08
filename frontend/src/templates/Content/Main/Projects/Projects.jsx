import React from "react";
import style from "./Projects.module.scss";
import generalStyle from "../../../../General.module.css";
import {title, projectsDescription} from "../../../../data/projects"
import {Link} from "react-router-dom";

// TODO. Rewrite logic about project, I'll take it from api db

export default function Projects() {
  return (
    <div className={generalStyle.content}>

      <div className={style.projects}>
        <div className={generalStyle.titleDiv}>
          <h1 className={generalStyle.title}>{title}</h1>
        </div>
        <main>
          {
            projectsDescription.map((element, id) => {
              console.log(element.imageUrl)
              return <Link to={{pathname: element.link}} key={`project ${id}`} target="_blank">
                <img src={element.imageUrl}  alt={element.title}/>
                <p>12</p>
              </Link>
            })
          }
        </main>
      </div>
    </div>
  )
}
