import React, { useState } from "react";
import getGraphData from "./utils.js";

export const GraphCard = () => {
  const [solarData, setSolarData] = useState(null);

  function handleClick() {
    console.log("ENTERED handleClick()");
    const data = getGraphData();
    setSolarData(data);
    console.log("leaving handleClick with the following data");
    console.log(data);
    console.log("leaving handleClick with the following solarData");
    console.log(solarData);
  }

  if (solarData !== null && typeof myVariable !== "undefined") {
    console.log("logging solarData...");
    console.log(solarData);
    return <div>{solarData}</div>;
  } else {
    return (
      <div>
        <div>The graph itself would go here</div>
        <div>some text below it or something would go here</div>
        <div>
          <button onClick={handleClick}>Generate</button>
        </div>
      </div>
    );
  }
};
