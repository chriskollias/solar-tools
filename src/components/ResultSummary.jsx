import { formatSeriesData } from "../utils/dataFormatter";

const ResultSummary = ({ solarData }) => {
  return (
    <div>
      Monthly GHI
      <div>
        <ul>{formatSeriesData(solarData["monthly_ghi"], "w/m²")}</ul>
      </div>
      Monthly DHI
      <div>
        <ul>{formatSeriesData(solarData["monthly_dhi"], "w/m²")}</ul>
      </div>
      Monthly DNI
      <div>
        <ul>{formatSeriesData(solarData["monthly_dni"], "w/m²")}</ul>
      </div>
    </div>
  );
};

export default ResultSummary;
