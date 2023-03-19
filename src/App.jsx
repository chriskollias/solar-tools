import { useState } from "react";
import { getNRELDataRequest } from "./requests/requests";
import InputForm from "./components/ui/InputForm";
import ResultSummary from "./components/ResultSummary";
import { Oval } from "react-loader-spinner";

function App() {
  const [requestPending, setRequestPending] = useState(false);
  const [solarData, setSolarData] = useState(null);

  const submitForm = (lat, lon) => {
    setRequestPending(true);
    const response = getNRELDataRequest({
      lat: lat,
      lon: lon,
    })
      .then((response) => {
        console.log("printing response");
        console.log(response);
        setRequestPending(false);
        setSolarData(response.data);
      })
      .catch((error) => {
        console.log("AN ERROR HAS OCCURRED");
        console.log(error);
      });
  };

  const initialLat = 40.5137;
  const initialLon = -108.5449;

  return (
    <div>
      <div>
        <InputForm
          initialLat={initialLat}
          initialLon={initialLon}
          submitForm={submitForm}
        />
      </div>
      {requestPending && (
        <Oval
          height={80}
          width={80}
          color="#4fa94d"
          wrapperStyle={{}}
          wrapperClass=""
          visible={true}
          ariaLabel="oval-loading"
          secondaryColor="#4fa94d"
          strokeWidth={2}
          strokeWidthSecondary={2}
        />
      )}
      {solarData && <ResultSummary solarData={solarData} />}
    </div>
  );
}

export default App;
