import React, { useState, useEffect } from "react";
import getGraphData from "./utils.js";

export const GraphCard = () => {
  const [solarData, setSolarData] = useState(null);

  function handleClick() {
    const data = getGraphData();
    data.then((result) => setSolarData(result));
  }

  useEffect(() => {
    console.log("useEffect()");
  }, [solarData]);

  if (solarData !== null && typeof solarData !== "undefined") {
    console.log("solarData type");
    console.log(typeof solarData);
    console.log("solarData value");
    console.log(solarData);

    let li_elements = [];

    for (const key in solarData) {
      let rowData = `${key}: ${solarData[key]}`;
      let rowElement = <li key={key}>{rowData}</li>;
      li_elements.push(rowElement);
    }

    return (
      <div>
        <div>The graph itself would go here</div>
        <div>some text below it or something would go here</div>
        <div>solar data would go here below:</div>
        <div>
          <ul>{li_elements}</ul>
        </div>
      </div>
    );
  }

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
