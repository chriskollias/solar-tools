const promise = new Promise((resolve, reject) => {
  if (true) {
    resolve("stuff worked");
  } else {
    reject("stuff bad");
  }
});

export async function getGraphData() {
  const url = "http://127.0.0.1:8000/pvlib/pvsystem";

  const promise = new Promise((resolve, reject) => {
    fetch(url)
      .then((response) => response.json())
      .then((data) => resolve(data))
      .catch((err) => reject(err));
  });

  return promise;

  /*
  promise
    .then((result) => {
      console.log("The promise has been resolved!");
      return result;
    })
    .catch((err) => console.log("error:", err));
  */
  /*
  try {
    const res = await Promise;
    await fetch(url)
      .then((response) => response.json())
      .then((data) => {
        //console.log("this is what GET `pvlib/pvsystem` returns");
        //console.log(data);
        return data;
      });
  } catch (err) {
    console.log("ERROR:", err);
  }
  */
}

export default getGraphData;
