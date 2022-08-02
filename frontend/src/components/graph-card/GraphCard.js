import React from "react";
import getGraphData from "./utils.js";

export const GraphCard = () => {
  const handleClick = () => {
    console.log("hi");
    getGraphData();
  };

  return (
    <div>
      <div>The graph itself would go here</div>
      <div>some text below it or something would go here</div>
      <div>
        <button onClick={handleClick}>Generate</button>
      </div>
    </div>
  );
};
