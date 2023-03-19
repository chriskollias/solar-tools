import { formatSeriesData } from "../utils/dataFormatter";
import Graph from "./Graph";

const ResultSummary = ({ solarData }) => {
  const labels = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const graphData = {
    labels,
    datasets: [
      {
        label: "GHI",
        data: labels.map((label, idx) => solarData["monthly_ghi"][idx]),
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
      {
        label: "DNI",
        data: labels.map((label, idx) => solarData["monthly_dni"][idx]),
        borderColor: "rgb(53, 162, 235)",
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
      {
        label: "DHI",
        data: labels.map((label, idx) => solarData["monthly_dhi"][idx]),
        borderColor: "rgb(36, 252, 3)",
        backgroundColor: "rgba(149, 252, 158, 0.5)",
      },
    ],
  };

  return (
    <div>
      {/*
      Monthly GHI
      <div>
        <ul>{formatSeriesData(solarData["monthly_ghi"], "w/m²")}</ul>
      </div>
      Monthly DNI
      <div>
        <ul>{formatSeriesData(solarData["monthly_dni"], "w/m²")}</ul>
      </div>
      Monthly DHI
      <div>
        <ul>{formatSeriesData(solarData["monthly_dhi"], "w/m²")}</ul>
      </div>
      */}
      <Graph data={graphData} />
    </div>
  );
};

export default ResultSummary;
