export async function getGraphData() {
  const url = "http://127.0.0.1:8000/pvlib/pvsystem";
  await fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log("this is what GET `pvlib/pvsystem` returns");
      console.log(data);
      return data;
    });
}

export default getGraphData;
