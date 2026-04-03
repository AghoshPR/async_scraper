import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [url, setUrl] = useState([]);

  const handleScrape = () => {
    if (!url) return;

    setLoading(true);

    axios
      .post("http://127.0.0.1:8000/scrape", { url })
      .then((res) => {
        const responseData = res.data || [];
        setData(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
      });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Scraped Data</h1>

      <input
        type="text"
        placeholder="Enter Website URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "300px", marginRight: "10px" }}
      />

      <button onClick={handleScrape}>Click</button>

      {loading ? (
        <p>Loading...</p>
      ) : !data || data.length === 0 ? (
        <p>No data available</p>
      ) : (
        <table border="1" cellPadding="10">
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>{item.id}</td>
                <td>{item.title}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default App;
