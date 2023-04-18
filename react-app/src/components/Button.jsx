import React from "react";
import './Button.css';

export const Button = ({location}) => {
   return (
      <div className="container">
         <div className="Button"></div>
         <div className="text">
            <h1> {location} </h1>
         </div>
      </div>
   )
}
