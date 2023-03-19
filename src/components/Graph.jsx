// you must import this in order for chart.js to work
import { Chart as ChartJS } from "chart.js/auto";
import { Line } from "react-chartjs-2";

const Graph = ({ data }) => {
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Solar Irradiance",
      },
    },
    scales: {
      y: {
        title: {
          display: true,
          text: "w/m²",
          font: {
            size: 14,
          },
        },
      },
    },
  };

  return (
    <div style={{ width: "800px" }}>
      <Line options={options} data={data} />
    </div>
  );
};

export default Graph;
