export function getGraphData() {
  const url = "http://127.0.0.1:8000/pvlib/pvsystem";
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log(`We love our data ${data}`);
      console.log(data);
    });
}

export default getGraphData;
