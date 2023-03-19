import { useState } from "react";

const InputForm = ({ initialLat, initialLon, submitForm }) => {
  const [lat, setLat] = useState(initialLat);
  const [lon, setLon] = useState(initialLon);

  const handleSubmit = (e) => {
    // prevent browser from reloading page
    e.preventDefault();

    const submittedLat = e.target[0].value;
    const submittedLon = e.target[1].value;
    submitForm(submittedLat, submittedLon);
  };

  return (
    <form method="post" onSubmit={handleSubmit}>
      <div>
        <label>
          Latitude
          <input
            type="text"
            value={lat}
            onChange={(e) => setLat(e.target.value)}
          />
        </label>
      </div>
      <div>
        <label>
          Longitude
          <input
            type="text"
            value={lon}
            onChange={(e) => setLon(e.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
      </div>
    </form>
  );
};

export default InputForm;
