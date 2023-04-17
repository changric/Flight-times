import React from "react";
import Button_img from './Button.png';

export const Button = ({location}) => {
   return (
      <button>
         <img src={Button_img} />
         {location}
      </button>
   )
}
