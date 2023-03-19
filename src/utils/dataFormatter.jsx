import { round } from "lodash";

// format numerical series data into an array of <li> elements
export const formatSeriesData = (seriesArray, valueUnit) => {
  const listContent = [];
  for (let i = 0; i < seriesArray.length; i++) {
    // rounding values to 2 decimal points
    listContent.push(
      <li>
        {i + 1}: {round(seriesArray[i], 2)} {valueUnit}
      </li>
    );
  }
  return listContent;
};
